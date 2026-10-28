"""Check the prebuilt standalone site, without regenerating or altering progress."""
from pathlib import Path
from urllib.parse import urlparse, unquote
import hashlib
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / 'public'
manifest = json.loads((PUBLIC / 'assets/content-manifest.json').read_text())
documents = {p.resolve(): BeautifulSoup(p.read_text(), 'html.parser') for p in PUBLIC.rglob('*.html')}
errors = []
for path, soup in documents.items():
    assert soup.html['lang'] == 'en', path
    assert len(soup.find_all('h1')) == 1, path
    ids = [node['id'] for node in soup.find_all(id=True)]
    assert len(ids) == len(set(ids)), f'Duplicate IDs in {path}'
    for node in soup.select('[href], [src]'):
        href = node.get('href', node.get('src', ''))
        url = urlparse(href)
        if url.scheme or url.netloc:
            continue
        destination = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not destination.is_relative_to(PUBLIC.resolve()) or not destination.exists():
            errors.append((str(path.relative_to(PUBLIC)), href, 'Missing or nonportable file'))
        elif url.fragment and destination.suffix == '.html' and not documents[destination].find(id=unquote(url.fragment)):
            errors.append((str(path.relative_to(PUBLIC)), href, 'Missing anchor'))
assert not errors, errors

assert len(documents) == manifest['handbook_pages'] + manifest['decision_pages'] == 146
assert manifest['decision_pages'] == 125 and manifest['api_operations'] == 149
progress = json.loads((PUBLIC / 'progress.json').read_text())
decisions = list((PUBLIC / 'pages').glob('*.html'))
assert len(decisions) == len(progress['items']) == 125
for path in decisions:
    task_id = path.stem.upper()
    assert task_id in progress['items']
    assert documents[path.resolve()].find(attrs={'data-editor': task_id})
assert 'N028' not in progress['items']
assert not (PUBLIC / 'pages/n028.html').exists()
tree = documents[(PUBLIC / 'architecture/toc.html').resolve()]
target_links = [a['href'] for a in tree.select('.doc-tree a') if '/pages/' in a['href']]
assert len(target_links) == len(set(target_links)) == 117
assert len(documents[(PUBLIC / 'evidence/api.html').resolve()].select('[data-api-row]')) == 149
assert len(documents[(PUBLIC / 'resources/index.html').resolve()].select('[data-resource-row]')) == 23
for name, expected_hash in manifest['source_artifacts'].items():
    original = ROOT / 'content/reports' / name
    download = PUBLIC / 'downloads' / name
    assert hashlib.sha256(original.read_bytes()).hexdigest() == expected_hash, name
    assert original.read_bytes() == download.read_bytes(), name

# Every numbered source section must appear in the reading website as well as downloads.
all_headings = {node.get_text(' ', strip=True) for soup in documents.values() for node in soup.find_all(['h2', 'h3'])}
for name in ['architecture.md', 'migration-and-standard.md', 'evidence-and-dejan.md']:
    for heading in re.findall(r'^## (\d+\. .+)$', (ROOT / 'content/reports' / name).read_text(), re.M):
        assert heading in all_headings, (name, heading)
print(f'Checked {len(documents)} pages, all local links/anchors, 125 tasks, 117 target links, 149 API operations, and 23 exact source copies.')
