const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const core = require('../public/assets/progress-core.js');
const root = path.resolve(__dirname, '..');
const context = {window: {}};
vm.runInNewContext(fs.readFileSync(path.join(root, 'public/assets/data.js'), 'utf8'), context);
const data = JSON.parse(JSON.stringify(context.window.MIGRATION_DATA));
const baseline = JSON.parse(fs.readFileSync(path.join(root, 'public/progress.json')));
const task = data.tasks[0];
const record = (values = {}) => ({...baseline.items[task.id], ...values});
const clone = value => JSON.parse(JSON.stringify(value));

test('published file has exactly 125 valid known tasks, including all 8 retirements', () => {
  assert.equal(Object.keys(core.validate(baseline, data).items).length, 125);
  assert.equal(data.tasks.filter(task => task.action === 'retire-by-251').length, 8);
  assert.equal(data.tasks.filter(task => task.kind === 'new').length, 33);
});
test('rejects incompatible projects, unknown tasks, missing tasks, and invalid records', () => {
  assert.throws(() => core.validate({...baseline, project: 'other'}, data), /project/);
  const unknown = clone(baseline); unknown.items.X001 = unknown.items.P001; delete unknown.items.P001;
  assert.throws(() => core.validate(unknown, data), /known task/);
  assert.throws(() => core.validate({...baseline, items: {}}, data), /known task/);
  for (const value of [{status: 'complete'}, {owner: 'x'.repeat(121)}, {notes: 'x'.repeat(4001)}, {link: 'javascript:alert(1)'}, {link: 'file:///tmp/x'}, {gate_confirmed: 'true'}, {updated_at: 'yesterday'}]) {
    assert.throws(() => core.validateRecord(record(value), task));
  }
});
test('all conditional pages require explicit confirmation before Done', () => {
  const conditional = data.tasks.filter(task => task.gate);
  assert.equal(conditional.length, 2);
  for (const gate of conditional) {
    assert.throws(() => core.validateRecord({...baseline.items[gate.id], status: 'done', gate_confirmed: false}, gate), /prerequisite/);
    assert.equal(core.validateRecord({...baseline.items[gate.id], status: 'done', gate_confirmed: true}, gate).status, 'done');
  }
});
test('drafts stay separate from published data; equivalent edits remove a draft', () => {
  const drafts = core.stage(baseline, {}, task, record({status: 'in-progress', owner: 'Docs'}));
  assert.equal(core.effective(baseline, drafts)[task.id].owner, 'Docs');
  assert.notEqual(baseline.items[task.id].owner, 'Docs');
  assert.deepEqual(core.stage(baseline, drafts, task, record()), {});
});
test('reconciliation clears published drafts and retains independent changes', () => {
  const drafts = core.stage(baseline, {}, task, record({status: 'in-progress'}));
  const published = clone(baseline); published.items[task.id] = drafts[task.id].value;
  assert.deepEqual(core.reconcile(published, drafts), {changes: {}, conflicts: []});
  const other = clone(baseline); other.items.P002.owner = 'Another owner';
  assert.deepEqual(core.reconcile(other, drafts).conflicts, []);
  const output = core.exportFile(other, drafts, data);
  assert.equal(output.items.P002.owner, 'Another owner');
  assert.equal(output.items[task.id].status, 'in-progress');
});
test('conflicts block export until explicitly rebased or removed', () => {
  const drafts = core.stage(baseline, {}, task, record({notes: 'My draft'}));
  const published = clone(baseline); published.items[task.id].notes = 'Published by a colleague';
  assert.deepEqual(core.reconcile(published, drafts).conflicts, [task.id]);
  assert.throws(() => core.exportFile(published, drafts, data), /Resolve/);
  const rebased = core.rebase(published, drafts, task.id);
  assert.deepEqual(core.reconcile(published, rebased).conflicts, []);
  assert.equal(core.exportFile(published, rebased, data).items[task.id].notes, 'My draft');
  assert.equal(core.exportFile(published, {}, data).items[task.id].notes, 'Published by a colleague');
});
test('saving a conflicting draft does not implicitly resolve the conflict', () => {
  const drafts = core.stage(baseline, {}, task, record({owner: 'Me'}));
  const published = clone(baseline); published.items[task.id].owner = 'Them';
  const edited = core.stage(published, drafts, task, record({owner: 'Us'}));
  assert.deepEqual(core.reconcile(published, edited).conflicts, [task.id]);
});
test('imports validate all records and stage a reviewable full-file update', () => {
  const imported = clone(baseline); imported.items.P002.notes = '<script>This stays plain text</script>';
  const drafts = core.importFile(baseline, {}, imported, data);
  assert.deepEqual(Object.keys(drafts), ['P002']);
  assert.equal(core.exportFile(baseline, drafts, data).items.P002.notes, imported.items.P002.notes);
  imported.items.P002.status = 'unknown';
  assert.throws(() => core.importFile(baseline, {}, imported, data), /unknown status/);
});
test('local draft envelopes are validated and timestamps do not create false conflicts', () => {
  const drafts = core.stage(baseline, {}, task, record({owner: 'Me'}));
  const envelope = {version: 1, project: data.project, snapshot: data.snapshot, changes: drafts};
  assert.deepEqual(core.validateDrafts(envelope, data), drafts);
  assert.throws(() => core.validateDrafts({...envelope, snapshot: 'old'}, data), /match/);
  const published = clone(baseline); published.items[task.id].updated_at = new Date().toISOString();
  assert.deepEqual(core.reconcile(published, drafts).conflicts, []);
});

test('older progress imports discard only the deleted proposal and preserve other records', () => {
  const legacy = clone(baseline);
  legacy.items.N028 = record({status: 'blocked', notes: 'Obsolete proposal'});
  legacy.items.P002.owner = 'Existing contributor';
  const validated = core.validate(legacy, data);
  assert.equal(Object.keys(validated.items).length, 125);
  assert.equal(validated.items.N028, undefined);
  assert.equal(validated.items.P002.owner, 'Existing contributor');
  const imported = core.importFile(baseline, {}, legacy, data);
  assert.deepEqual(Object.keys(imported), ['P002']);
  legacy.items.X001 = record();
  assert.throws(() => core.validate(legacy, data), /known task/);
});

test('saved browser drafts survive deletion of an unrelated proposal', () => {
  const changes = core.stage(baseline, {}, task, record({owner: 'Draft contributor'}));
  changes.N028 = {base: record(), value: record({notes: 'Obsolete draft'})};
  const envelope = {version: 1, project: data.project, snapshot: data.snapshot, changes};
  const restored = core.validateDrafts(envelope, data);
  assert.deepEqual(Object.keys(restored), [task.id]);
  assert.equal(restored[task.id].value.owner, 'Draft contributor');
});
