#!/usr/bin/env python3
"""Build review artifacts only. Never modifies the documentation repository."""
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parents[1] / "docs"
PR_HEAD = "c75df95b9291806368625203414abc77ba66ab69"
METHODS = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}


def git(*args):
    return subprocess.check_output(["git", "-C", str(DOCS), *args], text=True).strip()


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def write_csv(name, rows):
    with (HERE / name).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for row in rows:
            w.writerow({k: "; ".join(v) if isinstance(v, list) else v for k, v in row.items()})


def read_tsv(name):
    with (HERE / name).open() as f:
        return list(csv.DictReader(f, delimiter="\t"))


def walk(node, trail=()):
    if isinstance(node, str):
        yield node, trail
    elif isinstance(node, dict):
        label = node.get("tab") or node.get("group")
        trail = (*trail, label) if label else trail
        for key in ("tabs", "groups", "pages"):
            for item in node.get(key, []):
                yield from walk(item, trail)


def tab_for(slug):
    if slug.startswith("concepts/"):
        return "Concepts"
    if slug.startswith("owner-guide/"):
        return "Agent Owner's Guide"
    return "Agent Developer's Guide"


def api_group(path):
    if path.startswith(("/v1/auth/", "/v1/users", "/v1/teams")):
        return "Authentication and Teams"
    if path.startswith(("/v1/agent-configurations", "/v1/agents/")) and not any(x in path for x in ("/evolution", "/proposals")):
        return "Agents and Registration"
    if path.startswith(("/v1/personas", "/v1/demographics", "/v1/dimensions")):
        return "Personas and Demographics"
    if path.startswith(("/v1/policies", "/v1/rules")):
        return "Policies and Rules"
    if path.startswith(("/v1/evaluations", "/v1/evaluation-", "/v1/harnesses", "/v1/custom-harnesses")):
        return "Evaluations and Harnesses"
    if path.startswith(("/v1/dome", "/v1/default-dome", "/v1/detections", "/v1/webhooks")):
        return "Runtime Protection"
    if path.startswith(("/v1/telemetry", "/v1/dashboard")):
        return "Telemetry and Dashboard"
    if path.startswith(("/v1/campaigns", "/v1/tools")):
        return "Red Team"
    return "Evolution and Genomes"


def main():
    config = json.loads((DOCS / "docs.json").read_text())
    inventory = []
    texts = {}
    for index, (slug, trail) in enumerate(walk(config["navigation"]), 1):
        path = DOCS / (slug + ".mdx")
        text = path.read_text()
        texts[slug] = text
        title = re.search(r"^title:\s*(.+)", text, re.M)
        inventory.append({"id": f"P{index:03}", "slug": slug, "title": title[1].strip("\"'"),
                          "navigation": list(trail), "lines": len(text.splitlines()),
                          "words_approx": len(text.split()),
                          "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    decisions = read_tsv("page-decisions.tsv")
    additions = read_tsv("new-pages.tsv")
    assert len(inventory) == len(decisions) == 92
    assert [x["id"] for x in inventory] == [x["id"] for x in decisions]
    assert len(additions) == 30 and len({x["id"] for x in additions}) == 30
    ids = {x["id"] for x in decisions + additions}
    migration, targets = [], []
    for source, decision in zip(inventory, decisions):
        assert len(decision) == 12 and None not in decision, decision
        for destination in filter(None, decision["extracts"].split(",")):
            assert destination in ids, (source["id"], destination)
        target = source["slug"] if decision["target_slug"] == "=" else decision["target_slug"]
        migration.append({**source, **decision, "target_slug": target})
        if target != "—":
            targets.append({"id": source["id"], "slug": target, "title": decision["target_title"],
                            "type": decision["target_type"], "group": decision["group"],
                            "priority": decision["priority"], "gate": ""})
    for page in additions:
        assert len(page) == 10 and None not in page, page
        assert all(origin in ids for origin in page["origin"].split(",")), page
        targets.append({k: page[k] for k in ("id", "slug", "title", "type", "group", "priority", "gate")})
    assert len(targets) == len({x["slug"] for x in targets}) == 114
    assert all(x["type"] in {"E", "H", "T", "R"} for x in targets)
    assert not any("/cli/" in x["slug"] for x in targets)
    write_json("source-inventory.json", inventory)
    write_json("migration-map.json", migration)
    write_csv("migration-map.csv", migration)
    write_csv("new-pages.csv", additions)
    write_json("target-pages.json", targets)

    # A navigation design, not an installable change: new page bodies are not written.
    order = {
        "Concepts": ["Platform", "Trust and Evaluation", "Discovery", "Red Team", "Runtime Defense", "Glossary"],
        "Agent Owner's Guide": ["Get Started", "Teams and Agents", "Discover Agents", "Prepare Evaluations", "Evaluate Agents", "Red Team", "Protect and Monitor", "Improve Agents"],
        "Agent Developer's Guide": ["Get Started", "Teams and Agents", "Discover Agents", "Prepare Evaluations", "Evaluate Agents", "Red Team", "Protect Agents", "Release and Improve", "Self-Hosting", "Reference"],
    }
    tabs = []
    tree = ["# Complete Proposed TOC", "", "Target-state design; new page content has not been authored. E = explanation, H = how-to, T = tutorial, R = reference. ⚑ = conditional page: do not publish until the condition in the new-page registry is confirmed.", "", "```text"]
    for tab, groups in order.items():
        node = {"tab": tab, "groups": []}
        tree.append(tab)
        for group in groups:
            subset = [x for x in targets if tab_for(x["slug"]) == tab and x["group"].split("/")[0] == group]
            if not subset:
                continue
            g = {"group": group, "pages": []}
            tree.append("  " + group)
            for page in subset:
                if "/" in page["group"]:
                    sub = page["group"].split("/", 1)[1]
                    match = next((p for p in g["pages"] if isinstance(p, dict) and p["group"] == sub), None)
                    if match is None:
                        match = {"group": sub, "pages": []}
                        g["pages"].append(match)
                    match["pages"].append(page["slug"])
                else:
                    g["pages"].append(page["slug"])
                tree.append(f"    [{page['type']}] {page['title']} ({page['id']})" + (" ⚑" if page["gate"] else ""))
            if tab == "Agent Developer's Guide" and group == "Reference":
                g["pages"].append({"group": "REST API Reference", "openapi": "openapi/api.json"})
                tree.append("    [R] REST API Reference — generated from openapi/api.json (149 source operations)")
            node["groups"].append(g)
        tabs.append(node)
    # Render the assembled hierarchy, including nested reference/integration labels.
    by_slug = {p["slug"]: p for p in targets}
    tree = tree[:4]
    def render_pages(items, depth):
        for item in items:
            if isinstance(item, str):
                page = by_slug[item]
                tree.append("  " * depth + f"[{page['type']}] {page['title']} ({page['id']})" + (" ⚑" if page["gate"] else ""))
            elif "openapi" in item:
                tree.append("  " * depth + "[R] REST API Reference — generated from openapi/api.json (149 source operations)")
            else:
                tree.append("  " * depth + item["group"])
                render_pages(item["pages"], depth + 1)
    tree.append("```text")
    for tab in tabs:
        tree.append(tab["tab"])
        for group in tab["groups"]:
            tree.append("  " + group["group"])
            render_pages(group["pages"], 2)
    tree += ["```", "", "Exact URLs, content origins, and publication conditions are recorded in target-pages.json and new-pages.csv. A page's type does not depend on its folder; existing meaningful URLs are preserved."]
    (HERE / "proposed-toc.md").write_text("\n".join(tree) + "\n")
    nav = {"tabs": tabs, "global": config["navigation"].get("global", {})}
    assert len(list(walk(nav))) == 114
    write_json("proposed-navigation.json", {"navigation": nav})

    # Structural evidence, with conservative link findings (not a replacement for Mintlify).
    toc = set(texts)
    link_issues, off_toc, images, hover_pages, mermaid_pages = [], [], [], [], []
    for slug, text in texts.items():
        if re.search(r"hover|Hover|Tooltip", text):
            hover_pages.append(slug)
        if "```mermaid" in text:
            mermaid_pages.append(slug)
        for number, line in enumerate(text.splitlines(), 1):
            for target in re.findall(r'(?:\]\(|(?:href|src)=")([^\)"\s]+)', line):
                if target.startswith(("http:", "https:", "mailto:", "#")):
                    continue
                clean = target.split("#")[0].split("?")[0].strip("/")
                item = {"page": slug, "line": number, "target": target}
                if not target.startswith("/"):
                    link_issues.append({**item, "status": "relative path needs renderer check"})
                elif any(r["source"].strip("/") == clean for r in config.get("redirects", [])):
                    continue
                elif clean in toc or (DOCS / clean).is_file():
                    continue
                elif (DOCS / (clean + ".mdx")).is_file():
                    off_toc.append(item)
                elif not any(r["source"].strip("/") == clean for r in config.get("redirects", [])):
                    link_issues.append({**item, "status": "no local target found"})
        for match in re.finditer(r"<(?:img|Image)\b[^>]*>", text, re.S):
            images.append({"page": slug, "line": text[:match.start()].count("\n") + 1,
                           "src": re.findall(r'src="([^"]+)"', match[0])})
    redirects = [{**r, "destination_exists": (DOCS / (r["destination"].strip("/") + ".mdx")).is_file(),
                  "destination_in_toc": r["destination"].strip("/") in toc} for r in config["redirects"]]
    spec = json.loads((DOCS / "openapi/api.json").read_text())
    operations = []
    for path, methods in spec["paths"].items():
        for method, operation in methods.items():
            if method not in METHODS:
                continue
            alias = path.startswith(("/v1/demographics/", "/v1/dimensions/"))
            operations.append({"method": method.upper(), "path": path, "operation_id": operation.get("operationId"),
                               "summary": operation.get("summary"), "tags": operation.get("tags", []),
                               "target_group": "Agent Developer's Guide / Reference / REST API / " + api_group(path),
                               "canonical_identity": method.upper() + " " + path,
                               "target_url_policy": "preserve published URL via generated-route registry; alias choice requires product confirmation",
                               "target_type": "R", "action": "verify canonical alias and generated route" if alias else "retain; verify source sync and canonical generated route",
                               "priority": "P0" if alias else "P1",
                               "semantic_validation": "not executed against a backend"})
    duplicate_ids = {k: n for k, n in Counter(x["operation_id"] for x in operations).items() if n > 1}
    aliases = []
    for path, methods in spec["paths"].items():
        if not path.startswith("/v1/demographics/"):
            continue
        paired = path.replace("/v1/demographics", "/v1/dimensions", 1)
        for method, operation in methods.items():
            other = spec["paths"].get(paired, {}).get(method)
            if method in METHODS and other:
                a, b = dict(operation), dict(other)
                a.pop("operationId", None)
                b.pop("operationId", None)
                aliases.append({"method": method.upper(), "path_a": path, "path_b": paired,
                                "equal_except_operation_id": a == b})
    write_csv("api-operation-inventory.csv", operations)
    evidence = {"counts": {"toc_mdx": len(inventory), "source_lines": sum(x["lines"] for x in inventory),
                           "source_words_approx": sum(x["words_approx"] for x in inventory),
                           "tabs": dict(Counter(x["navigation"][0] for x in inventory)),
                           "openapi_paths": len(spec["paths"]), "openapi_operations": len(operations),
                           "proposed_existing": len(targets) - len(additions), "proposed_new": len(additions),
                           "proposed_total": len(targets), "conditional_new": sum(bool(p["gate"]) for p in additions)},
                "mermaid_pages": mermaid_pages, "images": images, "hover_pages": hover_pages,
                "link_candidates": link_issues, "links_to_non_toc_content": off_toc, "redirects": redirects,
                "openapi_duplicate_operation_ids": duplicate_ids, "openapi_alias_pairs": aliases,
                "openapi_missing_prefixes": [p for p in ("/v1/discover", "/v1/redteam", "/manifests", "/v1/manifests") if not any(x.startswith(p) for x in spec["paths"])],
                "openapi_operations_with_multiple_tags": sum(len(x["tags"]) > 1 for x in operations)}
    write_json("evidence.json", evidence)

    # The locally available branch exactly matches the connector-verified PR head.
    pr_config = json.loads(git("show", PR_HEAD + ":docs.json"))
    pr_slugs = [slug for slug, _ in walk(pr_config["navigation"])]
    residuals = []
    for slug in pr_slugs:
        body = git("show", PR_HEAD + ":" + slug + ".mdx")
        hits = [{"line": i, "text": line.strip()} for i, line in enumerate(body.splitlines(), 1)
                if re.search(r'(?<!/)\bvijil (?:auth|config|team|agent|discover|evaluate|evaluations|persona|policy|dome|manifest|harness|scores|reports)\b|<Tab title="CLI"|title="CLI"', line)]
        if hits:
            residuals.append({"page": slug, "candidates": hits})
    write_json("pr251-cli-residuals.json", residuals)
    assert len(pr_slugs) == 84
    removed = set(texts) - set(pr_slugs)
    retired = {x["slug"] for x in migration if x["action"] == "retire-by-251"}
    assert removed == retired, (removed, retired)
    write_json("source-snapshot.json", {"working_tree_head": git("rev-parse", "HEAD"), "working_tree_status_at_generation": git("status", "--short"),
               "docs_json_sha256": hashlib.sha256((DOCS / "docs.json").read_bytes()).hexdigest(),
               "pr251_url": "https://github.com/vijilAI/docs/pull/251", "pr251_head": PR_HEAD,
               "pr251_state_observed": "open, unmerged (GitHub connector)", "post_pr251_mdx": len(pr_slugs),
               "removed_toc_pages": sorted(removed), "residual_candidate_pages": len(residuals),
               "source_policy": "Working tree is audited as-is; PR head is a separately inspected future delta, not a merged snapshot."})

    lines = ["# Page-by-Page Plan", "", "Scope: all 92 MDX pages in the local TOC. Eight CLI pages are recorded as retired through PR #251. The target consists of 84 existing pages, each with one primary purpose, plus 30 proposed new pages (two conditional).", "",
             "E = explanation; H = how-to; T = tutorial; R = reference. Current type is an editorial assessment of the content, not existing frontmatter. P0 identifies a contract/accuracy issue or an already-decided retirement; P1 is the main transition work; P2 is a later improvement.", "",
             "Keep preserves the page, URL, and main structure with the specified corrections and standard links. Refactor changes focus without extracting separate pages; split specifies explicit destinations; retire-by-251 does not restore retired content.", ""]
    for row in migration:
        lines += [f"## {row['id']} — {row['title']}", "",
                  f"Source: [{row['slug']}](../../docs/{row['slug']}.mdx). Current type: **{row['current_type']}**. Action: **{row['action']}**, **{row['priority']}**.", "",
                  f"**Finding:** {row['finding']}", "", f"**Change:** {row['change']}", ""]
        if row["target_slug"] != "—":
            lines += [f"**Destination:** {tab_for(row['target_slug'])} → {row['group'].replace('/', ' → ')} → **{row['target_title']} [{row['target_type']}]**; URL `/{row['target_slug']}`.", "", f"**Single page goal:** {row['goal']}", ""]
        else:
            lines += ["**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.", ""]
        if row["extracts"]:
            lines += [f"**Related content destinations:** {row['extracts']}. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.", ""]
    lines += ["## Generated REST API Reference", "", "The TOC also includes an OpenAPI group, which is not a single MDX page. Each of the 149 operations across 112 paths has its own row in [api-operation-inventory.csv](api-operation-inventory.csv). The audit covers Reference classification, navigation, aliases, operation IDs, tags, and differences from guides; backend calls and every individual response field have not been verified through execution. Detailed diagnostics are in evidence-and-dejan.md.", "", "## Registry of All Proposed New Pages", ""]
    for row in additions:
        lines += [f"### {row['id']} — {row['title']} [{row['type']}]", "",
                  f"**Placement:** {tab_for(row['slug'])} → {row['group'].replace('/', ' → ')}. URL `/{row['slug']}`. Priority **{row['priority']}**. Sources: {row['origin']}.", "",
                  f"**Content:** {row['content']}", "", f"**Acceptance criteria:** {row['acceptance']}", ""]
        if row["gate"]:
            lines += [f"**Publication condition:** {row['gate']}", ""]
    (HERE / "page-by-page.md").write_text("\n".join(lines))
    print(json.dumps({"validated_source_pages": len(inventory), "post_251_existing_pages": len(pr_slugs),
                      "new_pages": len(additions), "target_pages": len(targets), "api_operations": len(operations),
                      "actions": dict(Counter(x["action"] for x in decisions)),
                      "target_types": dict(Counter(x["type"] for x in targets)),
                      "pr251_residual_candidate_pages": len(residuals)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
