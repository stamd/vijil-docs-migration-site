(function () {
  'use strict';
  const data = window.MIGRATION_DATA, core = window.ProgressCore;
  if (!data || !core) return;
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => [...scope.querySelectorAll(selector)];
  const root = document.body.dataset.root || '';
  const storageKey = `${data.project}:${data.snapshot}:drafts:v1`;
  const taskById = Object.fromEntries(data.tasks.map(task => [task.id, task]));
  let baseline = core.validate(data.baseline, data), drafts = {}, conflicts = [], items = baseline.items;
  let publishedError = '', storageError = '', pendingImport = null, toastTimer;
  const inventories = [];

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function toast(message) {
    const node = $('#toast');
    node.textContent = message; node.hidden = false;
    clearTimeout(toastTimer); toastTimer = setTimeout(() => { node.hidden = true; }, 6500);
  }
  function badge(status) { return element('span', `badge status-${status}`, data.statuses[status]); }
  function persist() {
    try {
      if (Object.keys(drafts).length) localStorage.setItem(storageKey, JSON.stringify({version: 1, project: data.project, snapshot: data.snapshot, changes: drafts}));
      else localStorage.removeItem(storageKey);
      storageError = '';
    } catch (_) {
      storageError = 'Browser storage is unavailable. Keep this tab open and export your drafts before leaving.';
      toast(storageError);
    }
  }
  function reconcile() {
    const result = core.reconcile(baseline, drafts);
    drafts = result.changes; conflicts = result.conflicts; items = core.effective(baseline, drafts);
  }
  function readDrafts() {
    try {
      const saved = localStorage.getItem(storageKey);
      drafts = saved ? core.validateDrafts(JSON.parse(saved), data) : {};
    } catch (error) {
      storageError = 'Saved drafts could not be read. They have not been overwritten. ' + error.message;
      toast(storageError);
    }
    reconcile();
  }
  async function fetchPublished() {
    if (location.protocol === 'file:') {
      publishedError = 'Opened from disk: using the bundled baseline. Use an HTTP preview to read the committed progress file.';
      return;
    }
    try {
      const response = await fetch(root + 'progress.json', {cache: 'no-store'});
      if (!response.ok) throw new Error('HTTP ' + response.status);
      const next = core.validate(await response.json(), data);
      baseline = next; publishedError = '';
      reconcile();
    } catch (error) {
      publishedError = 'Published progress could not be loaded. Draft editing is available; export is paused until Refresh published succeeds. ' + error.message;
      throw new Error(publishedError);
    }
  }
  function conflictPanel(editor, id) {
    const panel = $('[data-task-conflict]', editor);
    panel.replaceChildren(); panel.hidden = !conflicts.includes(id);
    if (panel.hidden) return;
    panel.append(element('strong', '', 'This task has a conflicting published update.'));
    panel.append(element('p', '', 'Compare both versions, then choose which one to keep before exporting.'));
    const grid = element('div', 'conflict-comparison');
    for (const [title, value] of [['Published', baseline.items[id]], ['Your saved draft', drafts[id].value]]) {
      const column = element('div');
      column.append(element('strong', '', title), element('pre', '', `${data.statuses[value.status]}\nOwner: ${value.owner || '—'}\nLink: ${value.link || '—'}\nPrerequisite confirmed: ${value.gate_confirmed ? 'Yes' : 'No'}\nNotes: ${value.notes || '—'}`));
      grid.append(column);
    }
    const actions = element('div', 'button-row');
    const keep = element('button', '', 'Keep my saved draft'); keep.type = 'button';
    keep.addEventListener('click', () => { drafts = core.rebase(baseline, drafts, id); changed(true); toast('Draft kept against the latest published version.'); });
    const discard = element('button', '', 'Use published version'); discard.type = 'button';
    discard.addEventListener('click', () => revert(id));
    actions.append(keep, discard); panel.append(grid, actions);
  }
  function fillEditors() {
    $$('[data-editor]').forEach(editor => {
      const value = items[editor.dataset.editor], form = $('form', editor);
      ['status', 'owner', 'notes', 'link'].forEach(key => { form.elements[key].value = value[key]; });
      if (form.elements.gate_confirmed) form.elements.gate_confirmed.checked = value.gate_confirmed;
    });
  }
  function render() {
    reconcile();
    const draftCount = Object.keys(drafts).length;
    const counts = Object.fromEntries(Object.keys(data.statuses).map(status => [status, 0]));
    Object.values(items).forEach(record => counts[record.status]++);
    const completed = counts.done, percent = Math.round(completed / data.tasks.length * 100);
    $$('[data-completion]').forEach(node => { node.textContent = `${completed} of ${data.tasks.length} tasks complete`; });
    $$('[data-completion-percent]').forEach(node => { node.textContent = percent + '%'; });
    $$('[data-progress-bar]').forEach(node => { node.value = completed; });
    $$('[data-status-counts]').forEach(node => {
      node.replaceChildren(...Object.entries(counts).map(([key, count]) => element('span', '', `${data.statuses[key]} · ${count}`)));
    });
    $$('[data-draft-count]').forEach(node => { node.textContent = draftCount; node.hidden = !draftCount; });
    $$('[data-task-status]').forEach(node => { node.replaceChildren(badge(items[node.dataset.taskStatus].status)); });
    $$('[data-task-row]').forEach(row => {
      const id = row.dataset.taskId, cell = $('[data-status-cell]', row);
      cell.replaceChildren(badge(items[id].status));
      if (drafts[id]) cell.append(element('span', 'draft-marker', conflicts.includes(id) ? 'Conflicting draft' : 'Local draft'));
      const owner = $('[data-owner-cell]', row);
      if (owner) owner.textContent = items[id].owner || '—';
    });
    $$('[data-draft-summary]').forEach(node => {
      node.textContent = `${draftCount ? `${draftCount} local draft${draftCount === 1 ? '' : 's'} · Export and commit to share.` : 'No local drafts. Showing published progress.'}${publishedError ? ' ' + publishedError : ''}${storageError ? ' ' + storageError : ''}`;
    });
    $$('[data-conflict-summary]').forEach(node => {
      node.hidden = !conflicts.length;
      node.replaceChildren(element('strong', '', `${conflicts.length} conflicting draft${conflicts.length === 1 ? '' : 's'}. `));
      node.append(document.createTextNode('Open each task to resolve it before exporting: '));
      conflicts.forEach((id, i) => { const link = element('a', '', id); link.href = root + taskById[id].href + '#progress'; node.append(link, document.createTextNode(i < conflicts.length - 1 ? ', ' : '.')); });
    });
    $$('[data-export-progress]').forEach(node => { node.disabled = !!conflicts.length; });
    $$('[data-discard-drafts]').forEach(node => { node.disabled = !draftCount; });
    $$('[data-editor]').forEach(editor => conflictPanel(editor, editor.dataset.editor));
    inventories.forEach(inventory => inventory.update(false));
  }
  function changed(fill = false) { reconcile(); persist(); render(); if (fill) fillEditors(); }
  function revert(id) {
    delete drafts[id]; changed(true);
    const editor = $(`[data-editor="${id}"]`);
    if (editor) $('[data-editor-message]', editor).textContent = 'Using the published version. Local draft removed.';
  }

  // Responsive navigation and dialog controls.
  const menu = $('#menu-toggle'), overlay = $('[data-close-menu]'), sidebar = $('#site-sidebar');
  const desktop = matchMedia('(min-width: 721px)');
  function syncSidebar() {
    const concealed = !desktop.matches && !document.body.classList.contains('menu-open');
    sidebar.inert = concealed;
    if (concealed) sidebar.setAttribute('aria-hidden', 'true'); else sidebar.removeAttribute('aria-hidden');
  }
  function closeMenu() {
    const focused = sidebar.contains(document.activeElement);
    document.body.classList.remove('menu-open'); menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', 'Open navigation'); overlay.hidden = true; syncSidebar();
    if (focused && !desktop.matches) menu.focus();
  }
  menu.addEventListener('click', () => {
    const open = !document.body.classList.contains('menu-open');
    document.body.classList.toggle('menu-open', open); menu.setAttribute('aria-expanded', String(open)); overlay.hidden = !open;
    menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    syncSidebar();
  });
  overlay.addEventListener('click', closeMenu);
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  desktop.addEventListener('change', closeMenu);
  syncSidebar();

  const searchDialog = $('#search-dialog'), searchInput = $('#global-search');
  const index = data.search.map(entry => ({...entry, haystack: (entry.title + ' ' + entry.text).toLowerCase()}));
  function search() {
    const query = searchInput.value.trim().toLowerCase(), tokens = query.split(/\s+/).filter(Boolean), results = $('#search-results');
    results.replaceChildren();
    if (!tokens.length) { $('#search-meta').textContent = 'Search full text, page IDs, and reference material.'; return; }
    const matches = index.filter(entry => tokens.every(token => entry.haystack.includes(token)))
      .map(entry => ({entry, score: (entry.title.toLowerCase() === query ? 100 : 0) + tokens.reduce((score, token) => score + (entry.title.toLowerCase().includes(token) ? 15 : 0), 0) + (entry.kind === 'Page decision' && /\b[pn]\d{3}\b/i.test(query) ? 10 : 0)}))
      .sort((a, b) => b.score - a.score);
    $('#search-meta').textContent = matches.length ? `${matches.length} result${matches.length === 1 ? '' : 's'}${matches.length > 16 ? ' · Showing the first 16; narrow your search for more.' : ''}` : 'No results. Try a page ID, product name, or shorter phrase.';
    for (const {entry} of matches.slice(0, 16)) {
      const link = element('a', 'search-result'); link.href = root + entry.href;
      const position = Math.max(0, entry.text.toLowerCase().indexOf(tokens[0]) - 55);
      const snippet = (position ? '…' : '') + entry.text.slice(position, position + 210) + (position + 210 < entry.text.length ? '…' : '');
      link.append(element('small', '', entry.kind + ' · ' + entry.section), element('strong', '', entry.title), element('p', '', snippet));
      results.append(link);
    }
  }
  function openSearch() { closeMenu(); searchDialog.showModal(); searchInput.focus(); search(); }
  $$('[data-search-open]').forEach(button => button.addEventListener('click', openSearch));
  $('[data-search-close]').addEventListener('click', () => searchDialog.close());
  searchDialog.addEventListener('click', event => {
    const rect = searchDialog.getBoundingClientRect();
    if (event.target === searchDialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) searchDialog.close();
  });
  searchInput.addEventListener('input', search);
  searchInput.addEventListener('keydown', event => {
    if (event.key === 'ArrowDown') { event.preventDefault(); $('.search-result', searchDialog)?.focus(); }
    if (event.key === 'Enter') { const first = $('.search-result', searchDialog); if (first) location.href = first.href; }
  });
  document.addEventListener('keydown', event => {
    const editable = event.target.closest('input,textarea,select,[contenteditable]');
    if ((event.key === '/' && !editable) || ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k')) {
      event.preventDefault(); if (!searchDialog.open) openSearch();
    }
  });

  // Each table has one combined filter model, with shareable query parameters.
  $$('[data-inventory]').forEach(scope => {
    const controls = $$('[data-filter]', scope), rows = $$('[data-task-row]', scope), params = new URLSearchParams(location.search);
    let pageNumber = 1;
    controls.forEach(control => { if (params.has(control.dataset.filter)) { const value = params.get(control.dataset.filter); if (control.tagName === 'INPUT' || [...control.options].some(option => option.value === value)) control.value = value; } });
    function update(writeUrl = true) {
      const filters = Object.fromEntries(controls.map(control => [control.dataset.filter, control.value]));
      const tokens = filters.query.toLowerCase().trim().split(/\s+/).filter(Boolean);
      const matches = rows.filter(row => {
        const task = taskById[row.dataset.taskId], record = items[task.id];
        const text = [task.id, task.name, task.target_title, task.slug, task.target_slug, task.goal, task.finding, task.change, record.owner, record.notes].join(' ').toLowerCase();
        return tokens.every(token => text.includes(token)) && ['kind', 'tab', 'action', 'priority'].every(key => filters[key] === 'all' || filters[key] === task[key]) && (filters.status === 'all' || filters.status === record.status);
      });
      const pageCount = Math.max(1, Math.ceil(matches.length / 20));
      pageNumber = Math.min(pageNumber, pageCount);
      rows.forEach(row => { row.hidden = true; });
      matches.slice((pageNumber - 1) * 20, pageNumber * 20).forEach(row => { row.hidden = false; });
      $('[data-result-count]', scope).textContent = `${matches.length} of ${rows.length} tasks${matches.length ? ` · Showing ${(pageNumber - 1) * 20 + 1}–${Math.min(pageNumber * 20, matches.length)}` : ''}`;
      $('[data-empty-state]', scope).hidden = !!matches.length;
      $('[data-pagination]', scope).hidden = pageCount <= 1;
      $('[data-page-label]', scope).textContent = `Page ${pageNumber} of ${pageCount}`;
      $('[data-page-prev]', scope).disabled = pageNumber === 1;
      $('[data-page-next]', scope).disabled = pageNumber === pageCount;
      if (writeUrl) {
        const next = new URL(location.href);
        controls.forEach(control => { const value = control.value; if (value && value !== 'all') next.searchParams.set(control.dataset.filter, value); else next.searchParams.delete(control.dataset.filter); });
        try { history.replaceState(null, '', next); } catch (_) { /* file:// can restrict history */ }
      }
    }
    controls.forEach(control => control.addEventListener(control.tagName === 'INPUT' ? 'input' : 'change', () => { pageNumber = 1; update(); }));
    $('[data-clear-filters]', scope).addEventListener('click', () => { controls.forEach(control => { control.value = control.tagName === 'INPUT' ? '' : 'all'; }); pageNumber = 1; update(); });
    $('[data-page-prev]', scope).addEventListener('click', () => { pageNumber--; update(false); });
    $('[data-page-next]', scope).addEventListener('click', () => { pageNumber++; update(false); });
    inventories.push({update}); update(false);
  });
  function simpleFilter(inputSelector, rowSelector, emptySelector, countSelector, noun) {
    const input = $(inputSelector); if (!input) return;
    const rows = $$(rowSelector).map(row => ({row, text: row.textContent.toLowerCase()}));
    input.addEventListener('input', () => {
      const tokens = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      let count = 0;
      rows.forEach(({row, text}) => { row.hidden = !tokens.every(token => text.includes(token)); if (!row.hidden) count++; });
      $(emptySelector).hidden = !!count;
      if (countSelector) $(countSelector).textContent = `${count} of ${rows.length} ${noun}`;
    });
  }
  simpleFilter('#api-search', '[data-api-row]', '#api-empty', '#api-count', 'operations');
  simpleFilter('#resource-search', '[data-resource-row]', '#resource-empty');

  $$('[data-editor]').forEach(editor => {
    const id = editor.dataset.editor, form = $('form', editor), message = $('[data-editor-message]', editor);
    form.addEventListener('submit', event => {
      event.preventDefault();
      try {
        drafts = core.stage(baseline, drafts, taskById[id], {
          status: form.elements.status.value, owner: form.elements.owner.value.trim(),
          link: form.elements.link.value.trim(), notes: form.elements.notes.value,
          gate_confirmed: form.elements.gate_confirmed?.checked || false, updated_at: new Date().toISOString(),
        });
        changed(); message.textContent = storageError || 'Draft saved in this browser. Export and commit to share it with the team.';
      } catch (error) { message.textContent = error.message; }
    });
    $('[data-revert-task]', editor).addEventListener('click', () => revert(id));
  });
  $$('[data-export-progress]').forEach(button => button.addEventListener('click', async () => {
    button.disabled = true;
    try {
      await fetchPublished(); persist(); render();
      const file = core.exportFile(baseline, drafts, data);
      const blob = new Blob([JSON.stringify(file, null, 2) + '\n'], {type: 'application/json'});
      const url = URL.createObjectURL(blob), anchor = element('a');
      anchor.href = url; anchor.download = 'progress.json'; document.body.append(anchor); anchor.click(); anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 30000);
      toast('Downloaded progress.json. Replace public/progress.json, review the diff, and commit to share.');
    } catch (error) { toast(error.message); render(); }
    finally { button.disabled = !!conflicts.length; }
  }));
  $$('[data-refresh-progress]').forEach(button => button.addEventListener('click', async () => {
    button.disabled = true;
    try { await fetchPublished(); persist(); render(); fillEditors(); toast('Published progress refreshed. Matching drafts have been cleared.'); }
    catch (error) { render(); toast(error.message); }
    finally { button.disabled = false; }
  }));
  $$('[data-discard-drafts]').forEach(button => button.addEventListener('click', () => {
    if (!confirm('Discard all local drafts and return to published progress? Export first if you want to keep a copy.')) return;
    drafts = {}; changed(true); toast('Local drafts discarded. Showing published progress.');
  }));
  const importDialog = $('#import-dialog'), fileInput = $('#progress-file');
  $$('[data-import-progress]').forEach(button => button.addEventListener('click', () => fileInput.click()));
  fileInput.addEventListener('change', async () => {
    const file = fileInput.files[0]; if (!file) return;
    try {
      if (file.size > 2 * 1024 * 1024) throw new Error('Progress files must be smaller than 2 MB.');
      pendingImport = core.validate(JSON.parse(await file.text()), data);
      const changedIds = data.tasks.filter(task => !core.same(items[task.id], pendingImport.items[task.id])).map(task => task.id);
      const overwritten = changedIds.filter(id => drafts[id]).length;
      $('[data-import-summary]').textContent = `${changedIds.length} task${changedIds.length === 1 ? '' : 's'} differ from your current view.${overwritten ? ` This will replace ${overwritten} existing local draft${overwritten === 1 ? '' : 's'}.` : ''} ${changedIds.length ? 'Changed IDs: ' + changedIds.join(', ') + '.' : 'There are no changes to apply.'}`;
      $('[data-import-confirm]').disabled = !changedIds.length;
      importDialog.showModal();
    } catch (error) { pendingImport = null; toast('Import rejected. ' + error.message); }
    finally { fileInput.value = ''; }
  });
  $('[data-import-confirm]').addEventListener('click', () => {
    if (!pendingImport) return;
    drafts = core.importFile(baseline, drafts, pendingImport, data); changed(true); pendingImport = null;
    importDialog.close(); toast('Imported as local drafts. Review, export, and commit to share.');
  });
  $('[data-import-cancel]').addEventListener('click', () => { pendingImport = null; importDialog.close(); });
  window.addEventListener('storage', event => {
    if (event.key !== storageKey) return;
    readDrafts(); render(); toast('Drafts changed in another tab. Reload this page before editing the same task.');
  });

  async function init() {
    $$('form button[type=submit]').forEach(button => { button.disabled = true; });
    readDrafts(); render();
    try { await fetchPublished(); if (!storageError) persist(); }
    catch (error) { toast(error.message); }
    render(); fillEditors();
    $$('form button[type=submit]').forEach(button => { button.disabled = false; });
    if (publishedError) $$('[data-editor-message]').forEach(node => { node.textContent = publishedError; });
  }
  init();
})();
