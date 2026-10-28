# Vijil documentation migration handbook

A standalone, static website for reviewing the migration proposal and tracking its implementation. All content is in English. This folder can be pushed to its own GitHub repository; it does not depend on the original documentation checkout.

## Preview locally

From this folder, run:

```sh
python3 -m http.server 8080 --directory public
```

Open **http://localhost:8080**. The generated `public/` directory is ready to serve; no install or build is required. An HTTP preview reads the current shared progress file. Opening `public/index.html` directly uses the baseline bundled at the last build.

## What is included

- Overview and a short Start here guide, followed by Diátaxis, architecture, and the proposed documentation tree.
- A page-by-page plan and 122 individual decision pages: 92 audited pages and 30 additions. The 8 planned CLI retirements remain tracked.
- Rollout, authoring standards, ownership, evaluation scenarios, and audit evidence.
- All 149 API operations and all 23 original source artifacts, available to search or download.
- A progress tracker with status, owner, notes, issue/PR links, filters, and import/export.

The target documentation has 114 pages; the tracker has 122 tasks because it also includes retirements. Audit observations refer to the inspected documentation baseline, rather than live product or PR status.

## Share progress through GitHub

The canonical team record is **`public/progress.json`**. No backend or account is required.

1. Open a decision page, edit its progress fields, and **Save draft**.
2. Review the Progress tracker, then choose **Export progress.json**. Export refreshes published progress first and blocks if the same task has conflicting changes.
3. Replace `public/progress.json` in your checkout with the download.
4. Pull the latest repository changes, review the diff, resolve any Git conflicts, and commit/push the file.
5. After deployment, choose **Refresh published**. Drafts matching the published version clear automatically.

Browser drafts are specific to that browser and site address. They are not team updates until committed and deployed. Import previews a file before staging it as drafts. Conditional new pages require their publication prerequisite to be confirmed before they can be marked Done. Completion is never inferred from a proposed change or an open PR.

The site cannot check for GitHub changes that have not yet reached the deployment. Always review against the latest repository file before committing. Notes and owners in the shared file are visible to anyone who can access the deployed site; choose your hosting access accordingly.

## Deploy to Netlify later

Push the **contents of this folder** to a GitHub repository and connect that repository to Netlify. The included `netlify.toml` sets the publish directory to **`public`**; leave the build command empty. Alternatively, upload `public/` for a manual deployment.

If you keep this folder inside a larger repository, set Netlify’s base directory to `vijil-docs-migration-site`. Nothing has been deployed or connected by this project.

## Update the handbook

The prebuilt website is checked in. `build.py` generates its pages from the included English reports and structured audit files in `content/reports/`. The website introduction is maintained separately in `content/start-here.md`; its existing `meeting.html` URL is retained for shared links. The CSS and JavaScript in `public/assets/` are authored source files and remain in place during a rebuild.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 build.py
```

Rebuilding preserves `public/progress.json` and refreshes the bundled fallback. Commit generated output with source changes. If task IDs or the audit snapshot change, plan an explicit progress-data migration first; the generator will reject a mismatched shared file. `content/reports/build_audit.py` is the **original audit generator** and requires the original docs checkout; it is included as evidence and is not this website’s build script.

## Verify changes

```sh
node --test tests/progress.test.cjs
python3 tests/check_site.py
```

The checks cover progress validation, prerequisites, imports, draft reconciliation and conflicts, source-file integrity, task coverage, API coverage, and every local link/anchor. The Python check uses the same packages as the optional generator. No Node dependencies are needed. The website uses no external fonts, scripts, or CDN assets.

## Folder layout

```text
public/                  Ready-to-serve website
  progress.json          Shared implementation record
  assets/                Styles, browser code, search index, manifest
  pages/                 Individual migration decisions
  downloads/             Exact copies of all original artifacts
content/reports/         Self-contained audit source package
content/start-here.md     Website introduction
build.py                 Optional website generator
tests/                   Progress and site-integrity checks
netlify.toml             Static hosting configuration
```
