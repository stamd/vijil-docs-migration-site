/* Shared progress validation and draft reconciliation. No browser dependencies. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.ProgressCore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const statuses = ['not-started', 'in-progress', 'in-review', 'blocked', 'done'];
  const fields = ['status', 'owner', 'notes', 'link', 'gate_confirmed'];
  const copy = value => JSON.parse(JSON.stringify(value));
  function same(a, b) { return !!a && !!b && fields.every(key => a[key] === b[key]); }
  function validateRecord(record, task) {
    const fail = message => { throw new Error(`${task.id}: ${message}`); };
    if (!record || typeof record !== 'object' || Array.isArray(record)) fail('invalid task record.');
    if (!statuses.includes(record.status)) fail('unknown status.');
    for (const [key, limit] of [['owner', 120], ['notes', 4000], ['link', 2000]]) {
      if (typeof record[key] !== 'string' || record[key].length > limit) fail(`invalid ${key} (maximum ${limit} characters).`);
    }
    if (record.link) {
      let url;
      try { url = new URL(record.link); } catch (_) { fail('the issue/PR link must be a full HTTP or HTTPS URL.'); }
      if (!['https:', 'http:'].includes(url.protocol)) fail('the issue/PR link must use HTTP or HTTPS.');
    }
    if (typeof record.gate_confirmed !== 'boolean') fail('publication confirmation must be true or false.');
    if (record.updated_at !== null && (typeof record.updated_at !== 'string' || !/^\d{4}-\d\d-\d\dT/.test(record.updated_at) || !Number.isFinite(Date.parse(record.updated_at)))) fail('invalid update timestamp.');
    if (task.gate && record.status === 'done' && !record.gate_confirmed) fail('confirm the publication prerequisite before marking this task Done.');
    return Object.fromEntries([...fields, 'updated_at'].map(key => [key, record[key]]));
  }
  function validate(file, data) {
    if (!file || typeof file !== 'object' || file.schema_version !== 1 || file.project !== data.project || file.snapshot !== data.snapshot) throw new Error('This file does not match this migration project and snapshot.');
    if (typeof file.revision !== 'string' || file.revision.length > 120) throw new Error('Invalid progress revision.');
    const ids = data.tasks.map(task => task.id);
    if (!file.items || Array.isArray(file.items) || Object.keys(file.items).length !== ids.length || !ids.every(id => Object.hasOwn(file.items, id))) throw new Error(`Progress must contain exactly the ${ids.length} known task IDs.`);
    const items = {};
    for (const task of data.tasks) items[task.id] = validateRecord(file.items[task.id], task);
    return {schema_version: 1, project: data.project, snapshot: data.snapshot, revision: file.revision, items};
  }
  function validateDrafts(file, data) {
    if (!file || file.version !== 1 || file.project !== data.project || file.snapshot !== data.snapshot || !file.changes || Array.isArray(file.changes)) throw new Error('Saved drafts do not match this migration.');
    const tasks = Object.fromEntries(data.tasks.map(task => [task.id, task]));
    const changes = {};
    for (const [id, draft] of Object.entries(file.changes)) {
      if (!tasks[id] || !draft) throw new Error('Saved drafts contain an unknown task.');
      changes[id] = {base: validateRecord(draft.base, tasks[id]), value: validateRecord(draft.value, tasks[id])};
    }
    return changes;
  }
  function reconcile(baseline, drafts) {
    const changes = {}, conflicts = [];
    for (const [id, draft] of Object.entries(drafts)) {
      if (!baseline.items[id]) throw new Error('Unknown draft task.');
      if (same(draft.value, baseline.items[id])) continue;
      changes[id] = copy(draft);
      if (!same(draft.base, baseline.items[id])) conflicts.push(id);
    }
    return {changes, conflicts};
  }
  function effective(baseline, drafts) {
    const items = copy(baseline.items);
    for (const [id, draft] of Object.entries(drafts)) items[id] = copy(draft.value);
    return items;
  }
  function stage(baseline, drafts, task, record) {
    const value = validateRecord(record, task), changes = copy(drafts);
    if (same(value, baseline.items[task.id])) delete changes[task.id];
    else changes[task.id] = {base: copy(drafts[task.id]?.base || baseline.items[task.id]), value};
    return changes;
  }
  function rebase(baseline, drafts, id) {
    const changes = copy(drafts);
    if (changes[id]) changes[id].base = copy(baseline.items[id]);
    return reconcile(baseline, changes).changes;
  }
  function exportFile(baseline, drafts, data, time = new Date().toISOString()) {
    const result = reconcile(baseline, drafts);
    if (result.conflicts.length) throw new Error('Resolve conflicting drafts before exporting: ' + result.conflicts.join(', '));
    return validate({...baseline, revision: time, items: effective(baseline, result.changes)}, data);
  }
  function importFile(baseline, drafts, file, data) {
    const imported = validate(file, data);
    let changes = copy(drafts);
    for (const task of data.tasks) changes = stage(baseline, changes, task, imported.items[task.id]);
    return changes;
  }
  return {same, validateRecord, validate, validateDrafts, reconcile, effective, stage, rebase, exportFile, importFile};
});
