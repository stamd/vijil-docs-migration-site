#!/usr/bin/env python3
"""Generate a standalone static migration handbook. Preserve published progress."""
from pathlib import Path
from html import escape
import csv
import hashlib
import json
import re
import shutil
import unicodedata

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / 'content' / 'reports'
PUBLIC = ROOT / 'public'
PROJECT = 'vijil-docs-diataxis'
SNAPSHOT = '2026-10-28'
TYPE_NAMES = {'E': 'Explanation', 'H': 'How-to', 'T': 'Tutorial', 'R': 'Reference', '—': 'Retiring'}
STATUSES = {'not-started': 'Not started', 'in-progress': 'In progress', 'in-review': 'In review', 'blocked': 'Blocked', 'done': 'Done'}


def read_json(name):
    return json.loads((CONTENT / name).read_text())


def sections(name):
    """Split numbered H2 sections, ignoring headings inside code fences."""
    result, current, fence = {}, None, False
    for line in (CONTENT / name).read_text().splitlines():
        if line.startswith('```'):
            fence = not fence
        match = re.match(r'^## (\d+)\. ', line) if not fence else None
        if match:
            current = int(match[1])
            result[current] = []
        if current is not None:
            result[current].append(line)
    return {key: '\n'.join(value) for key, value in result.items()}


def slug(text):
    value = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')


def relative(current, target):
    import posixpath
    return posixpath.relpath(target, str(Path(current).parent))


old_pages = read_json('migration-map.json')
with (CONTENT / 'new-pages.csv').open() as handle:
    new_pages = list(csv.DictReader(handle))
targets = read_json('target-pages.json')
target_by_id = {page['id']: page for page in targets}
tasks = []
for page in old_pages:
    tasks.append({**page, 'kind': 'existing', 'name': page['title'], 'type': page['target_type'],
                  'tab': page['navigation'][0], 'gate': '', 'href': 'pages/' + page['id'].lower() + '.html'})
for page in new_pages:
    tasks.append({**page, 'kind': 'new', 'name': page['title'], 'action': 'add', 'target_slug': page['slug'],
                  'tab': "Concepts" if page['slug'].startswith('concepts/') else "Agent Owner's Guide" if page['slug'].startswith('owner-guide/') else "Agent Developer's Guide",
                  'target_title': page['title'], 'goal': page['content'], 'finding': '', 'change': page['content'],
                  'href': 'pages/' + page['id'].lower() + '.html'})
task_by_id = {page['id']: page for page in tasks}
assert len(tasks) == 126 and len(task_by_id) == 126

architecture = sections('architecture.md')
migration = sections('migration-and-standard.md')
evidence = sections('evidence-and-dejan.md')

NAV = [
    ('Getting started', [('Overview', 'index.html'), ('Start here', 'meeting.html'), ('Using this handbook', 'using.html')]),
    ('Understand the approach', [('Diátaxis explained', 'guide/diataxis.html'), ('Architecture', 'architecture/index.html'), ('Content relationships', 'architecture/content.html'), ('Writing for agents', 'architecture/agents.html'), ('Proposed documentation tree', 'architecture/toc.html')]),
    ('Plan and delivery', [('Rollout and Diamond pilot', 'plan/roadmap.html'), ('Page-by-page plan', 'plan/pages.html'), ('Progress tracker', 'plan/progress.html')]),
    ('Working standards', [('Page templates and links', 'standards/writing.html'), ('Checks and evaluation', 'standards/validation.html'), ('Ownership and reviews', 'standards/ownership.html')]),
    ('Audit evidence', [('Findings and monitoring', 'evidence/findings.html'), ('API reference audit', 'evidence/api.html'), ('CLI removal · PR #251', 'evidence/cli.html'), ('Dejan’s proposal and decisions', 'evidence/dejan.html')]),
    ('Reference library', [('Audit baseline', 'resources/baseline.html'), ('All references and downloads', 'resources/index.html'), ('Sharing progress', 'resources/tracking.html')]),
]
ROUTES = {
    'README.md': 'resources/baseline.html', 'meeting-brief.md': 'meeting.html',
    'architecture.md': 'architecture/index.html', 'proposed-toc.md': 'architecture/toc.html',
    'page-by-page.md': 'plan/pages.html', 'migration-and-standard.md': 'plan/roadmap.html',
    'evidence-and-dejan.md': 'evidence/findings.html',
}
DOCS = []
SEARCH = []


def render_markdown(text, current):
    parser = MarkdownIt('commonmark', {'html': False}).enable('table')
    html = parser.render(text.replace('<!-- pagebreak -->', ''))
    soup = BeautifulSoup(html, 'html.parser')
    seen = {}
    for heading in soup.find_all(re.compile(r'^h[1-6]$')):
        key = slug(heading.get_text(' ', strip=True))
        count = seen.get(key, 0)
        seen[key] = count + 1
        heading['id'] = key + (f'-{count + 1}' if count else '')
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('../../docs/'):
            href = 'https://docs.vijil.ai/' + href[len('../../docs/'):].removesuffix('.mdx')
        elif not re.match(r'^(?:https?:|mailto:|#)', href):
            filename, separator, fragment = href.partition('#')
            destination = ROUTES.get(filename, 'downloads/' + filename)
            href = relative(current, destination) + (separator + fragment if separator else '')
        link['href'] = href
        if href.startswith('https://'):
            link['rel'] = 'noopener'
    for node in list(soup.find_all(string=True)):
        if node.find_parent(['a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4']):
            continue
        if not re.search(r'\b[PN]\d{3}\b', str(node)):
            continue
        parts = re.split(r'(\b[PN]\d{3}\b)', str(node))
        for part in parts:
            if part in task_by_id:
                link = soup.new_tag('a', href=relative(current, task_by_id[part]['href']))
                link['class'] = 'task-link'
                link['title'] = task_by_id[part]['name']
                link.string = part
                node.insert_before(link)
            else:
                node.insert_before(part)
        node.extract()
    for table in soup.find_all('table'):
        wrapper = soup.new_tag('div', attrs={'class': 'table-scroll', 'tabindex': '0', 'aria-label': 'Scrollable reference table'})
        table.wrap(wrapper)
    for code in soup.select('pre > code.language-mermaid'):
        # Keep all original relationships readable, without a runtime CDN dependency.
        details = soup.new_tag('details', attrs={'class': 'diagram-source'})
        summary = soup.new_tag('summary')
        summary.string = 'Read the navigation graph · Mermaid source'
        details.append(summary)
        pre = code.parent
        pre.replace_with(details)
        details.append(pre)
    return str(soup)


def badge(text, kind='neutral'):
    return f'<span class="badge {escape(kind)}">{escape(text)}</span>'


def panel_link(current, title, href, description):
    return f'<a class="route-card" href="{relative(current, href)}"><strong>{escape(title)} <span aria-hidden="true">→</span></strong><span>{escape(description)}</span></a>'


def add_page(path, title, description, body, *, section='', wide=False, extra=''):
    DOCS.append({'path': path, 'title': title, 'description': description, 'body': body, 'section': section, 'wide': wide, 'extra': extra})


def md_page(path, title, description, text, section):
    add_page(path, title, description, render_markdown(text, path), section=section)


def task_table(current, progress=False):
    rows = []
    for page in tasks:
        title = page['target_title'] if page['kind'] == 'new' else page['title']
        owner = '<td class="owner-cell" data-owner-cell>—</td>' if progress else ''
        gate = ' <span class="conditional-mark" title="Publication requires confirmation">Conditional</span>' if page.get('gate') else ''
        rows.append(f'''<tr data-task-row data-task-id="{page['id']}">
          <td><a href="{relative(current, page['href'])}"><span class="row-id">{page['id']}</span><strong>{escape(title)}</strong></a><span class="row-subtitle">{escape(page['tab'])}{gate}</span></td>
          <td>{escape(page['action'].replace('retire-by-251', 'Retire via PR #251'))}<span class="row-subtitle">{TYPE_NAMES.get(page['type'], page['type'])}</span></td>
          <td>{page['priority']}</td><td data-status-cell>{badge('Not started', 'status-not-started')}</td>{owner}
        </tr>''')
    return f'''<section class="inventory" data-inventory data-default-status="all">
      <div class="filter-grid">
        <label class="filter-search">Find a page<input type="search" data-filter="query" placeholder="Title, page ID, topic, or owner…" aria-label="Filter migration pages"></label>
        <label>Scope<select data-filter="kind"><option value="all">All 126 tasks</option><option value="existing">Existing pages · 92</option><option value="new">New pages · 34</option></select></label>
        <label>Area<select data-filter="tab"><option value="all">All three tabs</option><option>Concepts</option><option>Agent Owner's Guide</option><option>Agent Developer's Guide</option></select></label>
        <label>Status<select data-filter="status"><option value="all">All statuses</option>{''.join(f'<option value="{k}">{v}</option>' for k,v in STATUSES.items())}</select></label>
        <label>Action<select data-filter="action"><option value="all">All actions</option><option value="keep">Keep</option><option value="refactor">Refactor</option><option value="split">Split</option><option value="rewrite">Rewrite</option><option value="move">Move</option><option value="move+split">Move and split</option><option value="add">Add</option><option value="retire-by-251">Retire via PR #251</option></select></label>
        <label>Priority<select data-filter="priority"><option value="all">All priorities</option><option>P0</option><option>P1</option><option>P2</option></select></label>
      </div>
      <div class="result-line"><p data-result-count aria-live="polite">126 tasks</p><button class="text-button" type="button" data-clear-filters>Clear filters</button></div>
      <div class="table-scroll"><table class="task-table"><thead><tr><th>Page</th><th>Decision / type</th><th>Priority</th><th>Status</th>{'<th>Owner</th>' if progress else ''}</tr></thead><tbody>{''.join(rows)}</tbody></table></div>
      <p class="empty-state" data-empty-state hidden>No pages match these filters. Try a broader search or clear the filters.</p>
      <div class="pagination" data-pagination hidden><button type="button" data-page-prev>Previous</button><span data-page-label></span><button type="button" data-page-next>Next</button></div>
    </section>'''


def progress_summary():
    return '''<section class="progress-summary" aria-label="Migration progress"><div class="progress-overview"><strong data-completion>0 of 126 tasks complete</strong><span data-completion-percent>0%</span></div><progress max="126" value="0" data-progress-bar aria-label="Completed migration tasks"></progress><div class="status-counts" data-status-counts></div></section>'''


home = '''<p class="lead">Keep the three existing documentation tabs. Give every page one clear job, connect related content, and migrate in small, verifiable batches.</p>
<p>This handbook brings together the proposal, architecture, evidence, page decisions, and delivery progress. Start with the approach, then explore the implementation detail when you need it.</p>
<h2 id="recommended-reading-order">Recommended reading order</h2><div class="route-grid">'''
for title, href, desc in [
    ('1. Start here', 'meeting.html', 'Why the documentation needs to change, the approach, and how to begin.'),
    ('2. Understand Diátaxis', 'guide/diataxis.html', 'Tutorials, how-to guides, reference, and explanations.'),
    ('3. Review the architecture', 'architecture/index.html', 'How the three tabs work together and where information belongs.'),
    ('4. Explore individual pages', 'plan/pages.html', 'Every existing-page decision and every proposed new page.'),
    ('5. Plan the rollout', 'plan/roadmap.html', 'The Diamond pilot, migration batches, and prerequisites.'),
    ('6. Track delivery', 'plan/progress.html', 'Status, ownership, notes, and implementation links in one place.'),
]:
    home += panel_link('index.html', title, href, desc)
home += '''</div><h2 id="proposal-at-a-glance">The proposal at a glance</h2><div class="table-scroll"><table><thead><tr><th>Area</th><th>Primary responsibility</th></tr></thead><tbody><tr><td>Concepts</td><td>Shared explanations and terminology.</td></tr><tr><td>Agent Owner’s Guide</td><td>A first tutorial and focused Console workflows.</td></tr><tr><td>Agent Developer’s Guide</td><td>SDK/MCP/plugin workflows, integrations, self-hosting, and technical reference.</td></tr></tbody></table></div>
<p>Align with the planned CLI removal in PR #251. REST remains reference material and a secondary path. Begin with a Diamond evaluation pilot before expanding.</p>
<h2 id="scope-and-progress">Scope and progress</h2><p>The audit covers 92 existing pages, including 8 planned CLI retirements, plus 34 proposed new pages. The target documentation contains 118 pages. The tracker includes all <strong>126 migration tasks</strong>, so retirement work remains visible.</p>'''
home += progress_summary()
home += '<p class="muted">Progress starts at “Not started.” A proposed change is not evidence that implementation is complete.</p><p>Need a specific source? Open the <a href="resources/index.html">reference library</a> or use search. Audit figures and PR observations reflect the inspected documentation baseline.</p>'
add_page('index.html', 'Documentation migration', 'A clear path from the proposal to the work.', home, section='Getting started')
# Preserve the existing URL while presenting an introduction written for the site.
md_page('meeting.html', 'Start here', 'Understand the proposal before exploring the architecture and individual pages.', (ROOT / 'content' / 'start-here.md').read_text(), 'Getting started')
md_page('using.html', 'Using this handbook', 'Start broad, then move from decisions to tasks.', '''## Read at the level you need

Begin with Start here and the Diátaxis explanation. Architecture pages describe responsibilities and relationships. The proposed tree shows the target structure. The page plan provides a dedicated page for every existing-page decision and proposed addition.

## Find a decision

Search titles, page IDs such as P024 or N014, method names, and full document text. The page plan can be filtered by area, status, action, priority, or existing/new scope. Every page has a permanent URL for sharing in a meeting or issue.

## Read the labels

### Page and scenario IDs

| Label | Meaning |
| --- | --- |
| `P001`–`P092` | The 92 audited existing pages. |
| `N001`–`N034` | The 34 proposed new pages. |
| `D01`–`D12` | The 12 proposed documentation evaluation scenarios. |

### Page types

| Label | Page type | Purpose |
| --- | --- | --- |
| `E` | Explanation | Understand how and why something works. |
| `H` | How-to | Complete a specific task. |
| `T` | Tutorial | Learn through a guided example. |
| `R` | Reference | Look up exact options, parameters, and behavior. |

### Priorities

| Label | Meaning |
| --- | --- |
| `P0` | Accuracy or contract work, or an already-decided retirement. |
| `P1` | Main migration work. |
| `P2` | Later improvements. |

- **Conditional:** a publication prerequisite must be confirmed before the page can be published.
- **Retire via PR #251:** a planned retirement action, not a completed status.

## Track real implementation

Open a page decision to set its status, owner, notes, and implementation link. The tracker summarizes the same records. Browser edits are drafts. Export the shared progress file and commit it to publish updates for the team. The Sharing progress guide explains the workflow.

## Keep the evidence in view

The audit reflects the recorded snapshot, not a live check of product releases or GitHub PR state. All supporting files remain available in the reference library. The proposed navigation is a design; new documentation content has not been authored by this site.
''', 'Getting started')

for path, title, desc, chunks, group in [
    ('guide/diataxis.html', 'Diátaxis explained', 'Four reader needs. One primary purpose per page.', [architecture[1]], 'Understand the approach'),
    ('architecture/index.html', 'Architecture', 'Keep the audience structure and clarify each area’s responsibility.', [architecture[2], architecture[3]], 'Understand the approach'),
    ('architecture/content.html', 'Content relationships', 'Canonical sources, interface-specific tasks, and useful links.', [architecture[4], architecture[5]], 'Understand the approach'),
    ('architecture/agents.html', 'Writing for agents', 'Precise context, readable content, and verifiable workflows.', [architecture[6], architecture[7]], 'Understand the approach'),
    ('plan/roadmap.html', 'Rollout and Diamond pilot', 'Start with a small, complete journey and expand in batches.', [migration[1], migration[2], migration[3], migration[4]], 'Plan and delivery'),
    ('standards/writing.html', 'Page templates and links', 'The authoring standard for new and migrated pages.', [migration[5], migration[6]], 'Working standards'),
    ('standards/validation.html', 'Checks and evaluation', 'Build checks, task success, and meaningful evidence of improvement.', [migration[7], migration[8]], 'Working standards'),
    ('standards/ownership.html', 'Ownership and reviews', 'Separate documentation quality from product-contract approval.', [migration[9], migration[10]], 'Working standards'),
    ('evidence/findings.html', 'Findings and monitoring', 'What the audit found and why it affects the migration.', [evidence[1], evidence[2], evidence[3]], 'Audit evidence'),
    ('evidence/api.html', 'API reference audit', 'Coverage, aliases, and every operation in the inspected specification.', [evidence[4]], 'Audit evidence'),
    ('evidence/cli.html', 'CLI removal · PR #251', 'The inspected change and the dependencies that remain.', [evidence[5]], 'Audit evidence'),
    ('evidence/dejan.html', 'Dejan’s proposal and decisions', 'Where the recommendations align and what still needs confirmation.', [evidence[6], evidence[7]], 'Audit evidence'),
]:
    md_page(path, title, desc, '\n\n'.join(chunks), group)

evaluation_html = '<h2 id="evaluation-scenarios">The 12 proposed evaluation scenarios</h2><p>These are evaluation specifications, not executed tests or evidence of product availability.</p>'
for case in read_json('agent-evaluation-tasks.json')['tasks']:
    text = f"### {case['id']}\n\n{case['prompt']}\n\n**Expected pages:** {', '.join(case['expected_pages'])}\n\n**Pass:** {case['pass']}\n\n**Fail:** {case['fail']}"
    evaluation_html += render_markdown(text, 'standards/validation.html')
next(p for p in DOCS if p['path'] == 'standards/validation.html')['body'] += evaluation_html

tree_html = '<p>The target contains 118 documentation pages, plus generated REST reference. Open any entry for its migration decision. Conditional entries need their stated prerequisite confirmed before publication.</p>'
navigation = read_json('proposed-navigation.json')['navigation']
by_target_slug = {p['slug']: p for p in targets}
def render_tree(items):
    result = '<ul class="doc-tree">'
    for item in items:
        if isinstance(item, str):
            page = by_target_slug[item]
            result += f'<li><a href="{relative("architecture/toc.html", task_by_id[page["id"]]["href"])}">{escape(page["title"])}</a> <span class="muted small">{page["id"]} · {TYPE_NAMES[page["type"]]}</span>' + (' ' + badge('Conditional') if page['gate'] else '') + '</li>'
        elif 'openapi' in item:
            result += '<li><a href="../evidence/api.html">REST API Reference</a> <span class="muted small">149 source operations · generated</span></li>'
        else:
            result += '<li><strong>' + escape(item['group']) + '</strong>' + render_tree(item['pages']) + '</li>'
    return result + '</ul>'
for tab in navigation['tabs']:
    tree_html += f'<h2 id="{slug(tab["tab"])}">{escape(tab["tab"])}</h2>' + render_tree(tab['groups'])
tree_html += '<p><a href="../downloads/proposed-toc.md">Download the complete TOC</a> · <a href="../downloads/proposed-navigation.json">Download the navigation design</a></p>'
add_page('architecture/toc.html', 'Proposed documentation tree', 'The complete target structure, with a decision behind every page.', tree_html, section='Understand the approach')

intro = '<p>Every audited page and proposed addition has a dedicated decision page. Open a row for the finding, recommended change, destination, related pages, and tracking fields.</p><p class="muted">Keep includes specified corrections and links. Split means content moves into named destinations. CLI retirements remain visible as tasks until confirmed complete.</p>'
add_page('plan/pages.html', 'Page-by-page plan', '92 existing pages, 34 proposed additions, and their exact next steps.', intro + task_table('plan/pages.html'), section='Plan and delivery', wide=True)
progress_tools = '''<section class="tracking-tools" aria-label="Shared progress controls"><div><strong>Shared file, local drafts</strong><p class="muted">Publish team updates by committing the exported <code>progress.json</code> to <code>public/</code>.</p></div><div class="button-row"><button type="button" data-export-progress>Export progress.json</button><button type="button" data-import-progress>Import progress</button><button type="button" class="text-button" data-refresh-progress>Refresh published</button></div><p class="draft-summary" data-draft-summary aria-live="polite"></p><p data-conflict-summary class="notice" hidden></p><p><a href="../resources/tracking.html">How sharing works</a> · <button class="text-button danger" type="button" data-discard-drafts>Discard local drafts</button></p></section>'''
add_page('plan/progress.html', 'Progress tracker', 'Track implementation, ownership, and review across the migration.', progress_summary() + progress_tools + task_table('plan/progress.html', True), section='Plan and delivery', wide=True)

api_rows = []
with (CONTENT / 'api-operation-inventory.csv').open() as handle:
    api_operations = list(csv.DictReader(handle))
for index, operation in enumerate(api_operations, 1):
    anchor = f'operation-{index:03}'
    api_rows.append(f'''<tr data-api-row id="{anchor}"><td><span class="method">{operation['method']}</span><code>{escape(operation['path'])}</code></td><td><strong>{escape(operation['summary'])}</strong><span class="row-subtitle">{escape(operation['operation_id'])}</span><span class="row-subtitle">{escape(operation['target_group'].split(' / ')[-1])}</span></td><td>{escape(operation['action'])}</td></tr>''')
    SEARCH.append({'title': operation['method'] + ' ' + operation['path'], 'section': 'API reference audit', 'href': 'evidence/api.html#' + anchor, 'text': ' '.join(operation.values()), 'kind': 'API operation'})
api_page = next(p for p in DOCS if p['path'] == 'evidence/api.html')
api_page['wide'] = True
api_page['body'] += '''<h2 id="operation-inventory">All 149 source operations</h2><p>Each operation is retained as Reference or flagged for alias review. These are structural decisions, not backend execution results.</p><label class="standalone-search">Find an operation<input type="search" id="api-search" placeholder="Method, path, resource, or operation ID…"></label><p class="muted" id="api-count" aria-live="polite">149 operations</p><div class="table-scroll"><table class="api-table"><thead><tr><th>Method and route</th><th>Operation</th><th>Recommended action</th></tr></thead><tbody>''' + ''.join(api_rows) + '</tbody></table></div><p id="api-empty" hidden>No operations match this search.</p><p><a href="../downloads/api-operation-inventory.csv">Download the complete operation inventory</a></p>'

residuals_html = '<h2 id="remaining-cli-evidence">Remaining CLI evidence at the inspected PR head</h2><p>Verbatim source lines are retained below for review. The migration does not reintroduce CLI reference.</p>'
for row in read_json('pr251-cli-residuals.json'):
    page = next(p for p in tasks if p.get('slug') == row['page'])
    residuals_html += f'<h3 id="remaining-{page["id"].lower()}"><a href="../{page["href"]}">{page["id"]} · {escape(page["name"])}</a></h3><pre><code>' + escape('\n'.join(f"L{line['line']}: {line['text']}" for line in row['candidates'])) + '</code></pre>'
next(p for p in DOCS if p['path'] == 'evidence/cli.html')['body'] += residuals_html

def tracking_editor(page):
    options = ''.join(f'<option value="{k}">{v}</option>' for k,v in STATUSES.items())
    condition = f'<label class="check-label"><input type="checkbox" name="gate_confirmed"> Publication prerequisite confirmed</label><p class="muted small">{escape(page["gate"])}</p>' if page.get('gate') else ''
    return f'''<section id="progress" class="task-editor" data-editor="{page['id']}"><h2>Implementation progress</h2><p class="muted">Edits are drafts in this browser. <a href="../resources/tracking.html">Export and commit</a> to share them with the team.</p><div data-task-conflict hidden class="notice"></div><form>
    <div class="editor-grid"><label>Status<select name="status">{options}</select></label><label>Owner<input name="owner" maxlength="120" placeholder="Person or team"></label></div>
    <label>Issue or pull request<input name="link" type="url" maxlength="2000" placeholder="https://github.com/…"></label>
    <label>Notes<textarea name="notes" rows="4" maxlength="4000" placeholder="Implementation, review, or blockers…"></textarea></label>{condition}
    <div class="button-row"><button type="submit">Save draft</button><button type="button" data-revert-task="{page['id']}" class="text-button">Use published version</button><a href="../plan/progress.html">Open tracker</a></div><p data-editor-message role="status"></p></form></section>'''

for page in tasks:
    path = page['href']
    typ = TYPE_NAMES.get(page['type'], page['type'])
    body = f'<div class="page-facts">{badge(page["id"])}{badge("Existing page" if page["kind"] == "existing" else "New page")}{badge(page["priority"])}{badge(typ)}<span data-task-status="{page["id"]}">{badge("Not started", "status-not-started")}</span></div>'
    if page['kind'] == 'existing':
        text = f"## Finding\n\n{page['finding']}\n\n## Recommended change\n\n{page['change']}\n\n## Single page goal\n\n{page['goal']}\n\n## Destination\n\n"
        if page['target_slug'] == '—':
            text += 'Removed from the public TOC through PR #251, without a replacement CLI reference. Map legacy URLs to semantically appropriate supported tasks or an explicit retirement notice. Retirement is planned until implementation is confirmed.'
        else:
            target = target_by_id[page['id']]
            text += f"**{page['target_title']}** · {typ}\n\n{target['group'].replace('/', ' → ')}\n\nTarget path: `/{page['target_slug']}`"
        text += f"\n\n## Audited source\n\nOriginal title: **{page['title']}**\n\nOriginal location: {' → '.join(page['navigation'])}\n\nCurrent type: {page['current_type']} · Action: {page['action']}\n\n[Open the audited documentation URL](https://docs.vijil.ai/{page['slug']}). The published version can differ from the recorded working-tree snapshot.\n\nSource length: {page['lines']} lines; approximately {page['words_approx']} words including code and MDX."
        if page['extracts']:
            text += '\n\n## Related content destinations\n\n' + ', '.join(page['extracts'].split(','))
        description = page['change']
    else:
        text = f"## Proposed content\n\n{page['content']}\n\n## Acceptance criteria\n\n{page['acceptance']}\n\n## Placement\n\n{page['tab']} → {page['group'].replace('/', ' → ')}\n\nTarget path: `/{page['slug']}`\n\n## Content origins\n\n{', '.join(page['origin'].split(','))}"
        if page['gate']:
            text += '\n\n## Publication prerequisite\n\n' + page['gate']
        description = page['content']
    body += render_markdown(text, path) + tracking_editor(page)
    add_page(path, page['target_title'] if page['kind'] == 'new' else page['title'], f'{page["id"]} · {page["action"].replace("retire-by-251", "Retire via PR #251")} · {page["tab"]}', body, section='Page-by-page plan')

baseline_md = (CONTENT / 'README.md').read_text()
baseline_md = re.sub(r'^# .+\n', '', baseline_md, count=1)
md_page('resources/baseline.html', 'Audit baseline', 'The complete source overview, scope, decisions, and verification limits.', baseline_md, 'Reference library')

RESOURCE_INFO = {
 'meeting-brief.md': ('Original meeting brief · source', 'The original presentation artifact, retained for reference.', ''),
 'meeting-brief.pdf': ('Original meeting brief · PDF', 'The original two-page presentation artifact.', ''),
 'README.md': ('Full proposal overview', 'Audit scope, constraints, counts, and reading order.', 'resources/baseline.html'),
 'architecture.md': ('Architecture source', 'Complete Diátaxis and architecture rationale.', 'architecture/index.html'),
 'proposed-toc.md': ('Proposed TOC', 'Every target page and its primary purpose.', 'architecture/toc.html'),
 'page-by-page.md': ('Complete page-by-page report', 'All original decisions and new-page specifications in one source document.', 'plan/pages.html'),
 'migration-and-standard.md': ('Migration and authoring standard', 'Sequencing, templates, checks, and ownership.', 'plan/roadmap.html'),
 'evidence-and-dejan.md': ('Evidence and Dejan comparison', 'Findings, API issues, PR #251, and unresolved contracts.', 'evidence/findings.html'),
 'migration-map.csv': ('Migration decision table · CSV', 'All 92 existing-page decisions for spreadsheet planning.', ''),
 'migration-map.json': ('Migration decision data · JSON', 'The structured existing-page decision records.', ''),
 'new-pages.csv': ('New-page specifications · CSV', '34 additions with origins, acceptance criteria, and publication conditions.', ''),
 'new-pages.tsv': ('New-page editorial source · TSV', 'Editable input to the original audit generator.', ''),
 'page-decisions.tsv': ('Existing-page editorial source · TSV', 'Editable source decisions for the original audit generator.', ''),
 'target-pages.json': ('Target-page registry', '118 proposed documentation destinations and types.', ''),
 'proposed-navigation.json': ('Mintlify navigation design', 'Proposed navigation; new page bodies are not included.', 'architecture/toc.html'),
 'api-operation-inventory.csv': ('API operation inventory', 'All 149 operations, aliases, and recommended handling.', 'evidence/api.html'),
 'agent-evaluation-tasks.json': ('Documentation evaluation scenarios', '12 proposed tasks and pass/fail criteria; not executed results.', 'standards/validation.html#evaluation-scenarios'),
 'evidence.json': ('Structural audit evidence', 'Counts, links, diagrams, redirects, aliases, and coverage gaps.', ''),
 'pr251-cli-residuals.json': ('Remaining CLI evidence', 'Exact lines retained at the inspected PR head.', 'evidence/cli.html#remaining-cli-evidence'),
 'source-inventory.json': ('Source-page inventory', 'Titles, navigation, sizes, and hashes of all 92 audited pages.', ''),
 'source-snapshot.json': ('Source snapshot', 'Working-tree and PR-head identifiers and audit scope.', ''),
 'validation-results.json': ('Artifact validation results', 'Checks performed on the audit package and English translation.', ''),
 'build_audit.py': ('Original audit generator', 'Requires the original docs checkout; separate from this website’s build script.', ''),
}
resource_rows = []
for file in sorted(CONTENT.iterdir()):
    if not file.is_file():
        continue
    title, desc, view = RESOURCE_INFO.get(file.name, (file.name, 'Supporting audit artifact.', ''))
    view_link = f'<a href="{relative("resources/index.html", view)}">Read on site</a> · ' if view else ''
    resource_rows.append(f'<tr data-resource-row><td><strong>{escape(title)}</strong><span class="row-subtitle">{escape(desc)}</span><code class="small">{escape(file.name)}</code></td><td>{view_link}<a href="../downloads/{file.name}" download>Download</a><span class="row-subtitle">{file.stat().st_size / 1024:.0f} KB</span></td></tr>')
resources_body = '<p>All 23 supporting report artifacts are included in this standalone site. Read the curated sections first or download the source files when you need the full detail.</p><label class="standalone-search">Find a reference<input type="search" id="resource-search" placeholder="Report, CSV, source snapshot, API…"></label><div class="table-scroll"><table><thead><tr><th>Reference</th><th>Open</th></tr></thead><tbody>' + ''.join(resource_rows) + '</tbody></table></div><p id="resource-empty" hidden>No references match this search.</p>'
add_page('resources/index.html', 'All references and downloads', 'One place for every report, source table, and evidence file.', resources_body, section='Reference library')

tracking_md = '''## The shared progress file

The published team record is `public/progress.json` in this website repository. GitHub reviews and Netlify deployments distribute that file to everyone. There is no account or backend in this site.

## Make and publish an update

1. Open a page decision and edit its status, owner, notes, and issue/PR link. Select Save draft.
2. Review your changes in the Progress tracker. Drafts are saved in this browser and are not yet visible to other people.
3. Select Export progress.json. Replace `public/progress.json` in your checkout with the downloaded file.
4. Review the diff against the latest repository version, commit it, and push. Netlify publishes the updated file with the site.
5. Refresh published progress. Drafts that match the new published record are cleared automatically.

You can import a progress file as a local draft to review it before publishing. Imports are validated and show the number of changes before they are applied. Keep the newest repository version when multiple people contribute.

## Resolve a conflicting draft

If someone publishes a change to the same task while you have a different draft, the site flags a conflict and blocks export. Open the task to compare the two versions. Keep your draft against the new baseline, or use the published version. Then export again.

## What statuses mean

| Status | Meaning |
| --- | --- |
| Not started | Proposed work has not been recorded as underway. |
| In progress | Implementation is being worked on. |
| In review | Implementation is ready for review or validation. |
| Blocked | A prerequisite or decision prevents progress. Record it in notes. |
| Done | The task’s implementation and review criteria are satisfied. |

All 126 tasks begin Not started; the site does not infer completion from a proposal or open PR. Conditional new pages require their publication prerequisite to be confirmed before they can be marked Done.

## Keep data portable

Browser drafts belong to that browser and site address. Export them before moving between devices, preview addresses, or deployments. Discard local drafts restores the published baseline, not an earlier repository version. Git history preserves published changes.

When opened directly from disk, the site uses its bundled baseline. Use the local HTTP preview or Netlify to read the committed progress file. Refresh published progress after a deployment to see other contributors’ updates.
'''
md_page('resources/tracking.html', 'Sharing progress', 'A GitHub-backed team record, with reviewable browser drafts.', tracking_md, 'Reference library')


def shell(page, position):
    path = page['path']
    prefix = relative(path, 'index.html').removesuffix('index.html')
    links = []
    for heading, entries in NAV:
        links.append(f'<div class="nav-group"><p>{escape(heading)}</p><ul>')
        for title, href in entries:
            active = href == path or (path.startswith('pages/') and href == 'plan/pages.html')
            links.append(f'<li><a href="{relative(path, href)}"' + (' aria-current="page"' if active else '') + f'>{escape(title)}</a></li>')
        links.append('</ul></div>')
    soup = BeautifulSoup(page['body'], 'html.parser')
    toc = []
    for heading in soup.find_all('h2', id=True):
        toc.append(f'<li><a href="#{heading["id"]}">{escape(heading.get_text(" ", strip=True))}</a></li>')
    toc_html = f'<aside class="page-toc" aria-label="On this page"><p>On this page</p><ul>{"".join(toc)}</ul><a class="back-top" href="#main">Back to top ↑</a></aside>' if toc else ''
    ordered = [href for _, entries in NAV for _, href in entries]
    related = ''
    if path in ordered:
        i = ordered.index(path)
        nav = []
        for target, label in ([(ordered[i - 1], 'Previous')] if i else []) + ([(ordered[i + 1], 'Next')] if i + 1 < len(ordered) else []):
            name = next(t for _, entries in NAV for t, h in entries if h == target)
            nav.append(f'<a href="{relative(path, target)}"><span>{label}</span><strong>{escape(name)}</strong></a>')
        related = '<nav class="reading-nav" aria-label="Reading order">' + ''.join(nav) + '</nav>'
    description = escape(page['description'], quote=True)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(page['title'])} · Vijil migration</title><meta name="description" content="{description}"><meta name="theme-color" content="#ffffff"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/styles.css"><script src="{prefix}assets/data.js" defer></script><script src="{prefix}assets/progress-core.js" defer></script><script src="{prefix}assets/app.js" defer></script></head>
<body data-root="{prefix}" data-page="{path}"><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><button class="menu-toggle" id="menu-toggle" type="button" aria-label="Open navigation" aria-controls="site-sidebar" aria-expanded="false">☰</button><a class="brand" href="{prefix}index.html"><strong>Vijil</strong><span>Documentation migration</span></a><div class="header-actions"><button class="search-trigger" data-search-open type="button"><span>Search the handbook</span><kbd>/</kbd></button><a class="progress-shortcut" href="{prefix}plan/progress.html">Progress <span data-draft-count class="draft-count" hidden>0</span></a></div></header>
<div class="site-layout"><nav class="sidebar" id="site-sidebar" aria-label="Handbook">{''.join(links)}</nav><div class="sidebar-overlay" data-close-menu hidden></div><main id="main" class="main {'wide' if page['wide'] else ''}" tabindex="-1"><div class="article-layout"><article><div class="breadcrumb">{escape(page['section'])}</div><h1>{escape(page['title'])}</h1><p class="page-description">{description}</p>{page['extra']}{page['body']}{related}<footer class="article-footer">Migration proposal · Implementation status is maintained in the <a href="{prefix}plan/progress.html">progress tracker</a>.</footer></article>{toc_html}</div></main></div>
<dialog class="search-dialog" id="search-dialog" aria-labelledby="search-title"><div class="dialog-heading"><h2 id="search-title">Search the handbook</h2><button type="button" data-search-close aria-label="Close search">✕</button></div><label class="sr-only" for="global-search">Search pages, decisions, and API operations</label><input id="global-search" type="search" placeholder="Try Trust Score, P024, or deployment…" autocomplete="off"><p class="search-meta" id="search-meta" aria-live="polite">Search full text, page IDs, and reference material.</p><div id="search-results" class="search-results"></div></dialog>
<dialog id="import-dialog" class="import-dialog" aria-labelledby="import-title"><h2 id="import-title">Review imported progress</h2><p data-import-summary></p><p>Import creates local drafts. Export and commit the file to publish updates for the team.</p><div class="button-row"><button type="button" data-import-confirm>Import as drafts</button><button type="button" data-import-cancel>Cancel</button></div></dialog><input type="file" id="progress-file" accept="application/json,.json" hidden><div class="toast" id="toast" role="status" aria-live="polite" hidden></div><noscript><p class="noscript-note">Reading works without JavaScript. Enable JavaScript for search, filters, and progress tracking.</p></noscript></body></html>'''


def build():
    PUBLIC.mkdir(exist_ok=True)
    (PUBLIC / 'downloads').mkdir(exist_ok=True)
    for source in CONTENT.iterdir():
        if source.is_file():
            shutil.copy2(source, PUBLIC / 'downloads' / source.name)
    progress_path = PUBLIC / 'progress.json'
    if progress_path.exists():
        progress = json.loads(progress_path.read_text())
        assert progress['schema_version'] == 1 and progress['project'] == PROJECT and progress['snapshot'] == SNAPSHOT
        assert set(progress['items']) == set(task_by_id), 'Review progress migration before changing task IDs.'
    else:
        progress = {'schema_version': 1, 'project': PROJECT, 'snapshot': SNAPSHOT, 'revision': 'initial', 'items': {page['id']: {'status': 'not-started', 'owner': '', 'notes': '', 'link': '', 'gate_confirmed': False, 'updated_at': None} for page in tasks}}
        progress_path.write_text(json.dumps(progress, indent=2) + '\n')
    for position, page in enumerate(DOCS):
        destination = PUBLIC / page['path']
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(shell(page, position))
        soup = BeautifulSoup(page['body'], 'html.parser')
        for hidden in soup.select('.task-editor, .inventory, .api-table'):
            hidden.decompose()
        SEARCH.append({'title': page['title'], 'section': page['section'], 'href': page['path'], 'text': page['description'] + ' ' + soup.get_text(' ', strip=True), 'kind': 'Page decision' if page['path'].startswith('pages/') else 'Handbook'})
    payload = {'project': PROJECT, 'snapshot': SNAPSHOT, 'tasks': tasks, 'search': SEARCH, 'baseline': progress, 'statuses': STATUSES}
    (PUBLIC / 'assets' / 'data.js').write_text('window.MIGRATION_DATA = ' + json.dumps(payload, ensure_ascii=False).replace('</', '<\\/') + ';\n')
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in CONTENT.iterdir() if p.is_file()}
    (PUBLIC / 'assets' / 'content-manifest.json').write_text(json.dumps({'snapshot': SNAPSHOT, 'source_artifacts': manifest, 'handbook_pages': len(DOCS) - len(tasks), 'decision_pages': len(tasks), 'api_operations': len(api_operations)}, indent=2) + '\n')
    print(f'Built {len(DOCS)} HTML pages, {len(tasks)} tracked decisions, {len(api_operations)} API operations, and {len(manifest)} source artifacts. Published progress preserved.')


if __name__ == '__main__':
    build()
