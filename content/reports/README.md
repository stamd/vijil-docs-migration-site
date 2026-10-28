# Vijil Documentation: Hybrid Diátaxis Transition Proposal

This proposal and its supporting tables are in English.

**Recommendation: retain Concepts, Agent Owner’s Guide, and Agent Developer’s Guide, and use Diátaxis to govern each page’s purpose.** Concepts becomes the canonical home for explanations. AOG covers Console workflows. ADG covers SDK, MCP/plugin, and technical operator tasks; REST remains reference material and a secondary path. Technical Reference stays within ADG, without a fourth tab.

The largest expected gains come from separating mixed content, resolving conflicting definitions, and creating verifiable paths from a task to its relevant contract. Renaming navigation groups alone would not solve these problems.

## How to Read This Proposal

1. [Architecture and Diátaxis application](architecture.md): the model, content responsibilities, agent-oriented requirements, and navigation decisions.
2. [Complete proposed TOC](proposed-toc.md): every existing and new target page, with its Diátaxis type.
3. [Page-by-page plan](page-by-page.md): a separate finding and decision for all 92 existing MDX pages, followed by a detailed registry of 30 proposed new pages.
4. [Evidence and comparison with Dejan’s proposal](evidence-and-dejan.md): concrete inconsistencies, OpenAPI findings, PR #251, and verification limits.
5. [Migration, standards, and checks](migration-and-standard.md): PR sequencing, the pilot, redirect policy, templates, ownership, and success criteria.

For spreadsheet work, use [migration-map.csv](migration-map.csv), [new-pages.csv](new-pages.csv), and [api-operation-inventory.csv](api-operation-inventory.csv). [proposed-navigation.json](proposed-navigation.json) is a complete Mintlify navigation **design**, not a deployable change: new page bodies have not been written, and two new pages have explicit publication conditions.

## Baseline and Key Decisions

| Item | Status / decision |
| --- | --- |
| Audit source | Local `docs/docs.json` and all 92 included MDX pages: 28 Concepts, 23 AOG, 41 ADG |
| Source volume | Approximately 104,356 words and 18,668 lines; words include code and MDX and are not a readability measure |
| Generated reference | Additionally, 112 OpenAPI paths and 149 operations from the TOC’s OpenAPI group |
| PR #251 | Open and unmerged when checked; exact head `c75df95`. Removes eight TOC CLI pages, leaving an anticipated baseline of 84 MDX pages |
| CLI in the target plan | No new CLI group, CLI reference, or CLI tutorial. Supporting and remaining commands are treated as dependencies of specific setup tasks |
| Primary interfaces | Console for AOG; Python SDK and MCP/Claude Code plugin for ADG |
| REST | The user confirmed that it remains reference material and a secondary path, without a separate introductory tutorial |
| Products | All current products remain in scope; no planned retirement is known |
| Navigation flexibility | Groups and ordering may change; the existing three top-level tabs remain |
| Dejan’s document | The complete text pasted by the user was analyzed. Direct access to the Google document was unsuccessful |
| 77% AI traffic | User-provided Mintlify analytics figure, likely including crawlers and agents. It does not establish that 77% of sessions execute tasks |

The proposal covers 84 retained existing pages and 30 proposed new pages: **114 MDX pages in the full target model**, plus generated REST reference. Of the new pages, 28 have no special product-availability publication condition; two Darwin guides await confirmed supported workflows. This is neither a recommendation to publish 30 new pages immediately nor a page-count growth target. Most additions extract existing content. After the pilot, verify that each proposed split addresses a real need.

Of the current 92 pages, 17 retain their basic structure, 28 change focus without extracting separate pages, 35 are split, two are substantially rewritten, one is moved, one is moved and split, and eight are retired through PR #251. These are mutually exclusive primary decisions; “keep” includes the specified minor corrections and standard links.

## What to Do First

First resolve the contracts that currently yield different answers: Trust Score scale and threshold, Probe/sample_size units, evaluation/engagement/campaign ID relationships, actual capability availability, and monitoring names/scope. Align with PR #251 in parallel. There is no need to block the entire documentation set until every term is agreed; block publication only where content depends on an unresolved contract.

Then run a small Diamond pilot: one Console tutorial, one SDK tutorial, focused run/results guides, an explanation of evidence, and two supporting references. The pilot must demonstrate that a human and an agent can find the right interface, complete the task, and verify its result. Extend the standard to the remaining areas afterward.

## Verification and Limits

This is a content and architecture audit of all TOC MDX sources and a structural audit of the OpenAPI group. It does not verify every code example, API response, UI state, or published release through execution. The local working tree, public site, and PR head are not assumed to be identical; their roles are distinguished in [evidence-and-dejan.md](evidence-and-dejan.md).

Validation confirmed exactly 92 unique source-page records, eight retirement decisions matching the PR-head TOC, all 30 new-page records with type/placement/origin/acceptance criteria, 114 unique target URLs without a CLI group, and an inventory of all 149 OpenAPI operations. For the same source snapshot, regenerate artifacts with `python3 build_audit.py` from this directory; after TOC changes, update the editorial map as well. The script only reads `docs` and writes analytical artifacts here.

The documentation content and `docs/docs.json` were not modified. The pre-existing local change to `developer-guide/getting-started/introduction.mdx` was preserved and included in the working-tree review; source hashes and repository state are recorded in [source-snapshot.json](source-snapshot.json).
