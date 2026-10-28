# Migration, Editorial Standards, and Acceptance Criteria

## 1. Work Sequence

This is an incremental migration plan. The number of new pages in the full target TOC is not a publication checklist for one PR. Each batch completes content and links before introducing navigation. Do not publish empty categories or stubs merely to resemble Diátaxis.

| Batch | Concrete deliverable | Dependencies | Exit criteria |
| --- | --- | --- | --- |
| 0. Confirm the baseline | Compare merged PR #251 with other active documentation changes; regenerate inventory; record retired URLs and residual CLI steps | Documentation PR merge order | TOC count and content hashes match the actual migration baseline; CLI reference is not reintroduced |
| 1. Agree contracts and standards | Confirm relevant names, score/sampling/status/ID contracts, and interface scope; assign docs/engineering owners; approve templates | Product/engineering for disputed topics | N012/N018 foundations and terminology registry have owners and verified claims; unrelated editorial fixes can proceed |
| 2. Diamond pilot | Two first-evaluation tutorials; focused execution/results guides; shared evidence explanation and supporting references | Confirmed test Agent, credentials/setup, evaluation contracts | Humans and agents can complete both introductory paths; the pilot has no conflicting scales or duplicate Red Team procedure |
| 3. Concepts and catalogs | Split P008–P020; Agent/lifecycle/context explanations; cleaned Glossary | Confirmed taxonomy and versioned catalog source | Concepts pages explain; every transferred lookup row has a canonical destination and visible IDs |
| 4. AOG and programmatic tasks | Console-only procedures; separate SDK/MCP setup; registration; Red Team execution/investigation; Python CI gate | Contracts for the relevant interfaces | No copied full explanation or catalog table; every procedure has verification and a supported failure path |
| 5. Runtime protection | Concepts for Controls/Trust Runtime; canonical configuration/results reference; current how-to guides and five integrations | Confirmed `vijil-dome` release and framework compatibility | ScanResult, Controls results, and trust decisions are not conflated; safe/blocked/error cases are verified |
| 6. Discover and self-hosting | Collector installation in ADG; owner handoff; DLP path where supported; AWS/application/reference split | Artifact/chart access and supported bootstrap replacement | Each supported installation has enrollment/health evidence; missing alternatives are not concealed with invented SDK/MCP calls |
| 7. Conditional content and final consolidation | Darwin guides only for confirmed workflows; remove remaining duplicates, obsolete destination links, and stale generated entries | Availability and a complete navigation graph | Every public destination has a purpose; conditional backlog items have not become unverified guides |

OpenAPI synchronization and coverage work starts in batch 1 and can run alongside writing. Do not wait until the end to discover that a guide uses a public route missing from reference. The same applies to CI: enable basic checks early for new/changed pages and expand strict enforcement across migrated content batch by batch.

This is not a calendar commitment. The main schedule risks are contract confirmation, test-environment access, and product review rather than writing 33 files. After the pilot, measure the actual cost of one E/H/R/T migration before estimating the remainder. Split batches into small PRs by connected task graph rather than arbitrary file counts.

## 2. Exact Diamond Pilot Scope

The proposed pilot has 12 connected pages: nine existing and three new.

| Role in the experience | Pages |
| --- | --- |
| Controlled learning | P029 First Evaluation in the Console; P054 First Evaluation with the Python SDK |
| Explanation | P007 How the Trust Score Works; P017 Evaluation Harnesses; N003 Interpret Evaluation Evidence |
| Real Console work | P041 Configure a Baseline Evaluation; P044 Run and Monitor; P045 Review Results |
| Programmatic work | P058 Run and Monitor; P060 Retrieve and Investigate Results |
| Contract lookup | N006 Harness Reference; N012 Evaluation Contracts and Results |

The pilot need not migrate all Red Team content, every Probe catalog, or all deployment guidance. Remove their duplicates from pilot pages and link existing canonical guides. Apply minimal corrections to P089 where setup versions or credentials would block the tutorial; N019/N021 can follow in another small PR.

A practical sequence is three content PRs and one validation PR: contracts/explanations/reference; Console path; SDK path; then task demonstrations and corrections. Each PR introduces reciprocal links alongside the split.

## 3. How to Migrate One Page

1. Record one target task or need, its type, audience/interface, and supported version.
2. Mark existing sections as staying here, moving to an existing P-ID, being extracted into a new N-ID, or requiring factual verification.
3. Complete the destination, authoritative source, and verification criteria before extraction. Leave no dangling links.
4. Shorten the source page while retaining sufficient local context; add named links to the extracted content.
5. Change the TOC group once both ends work. Sidebar reorganization does not require changing the URL.
6. Check HTML and Markdown, internal links/anchors, any redirect, and the actual task path.

For example, P068 keeps the dict/TOML task and test in Configure Guardrails in Code; complete option/default tables move into N013. P068 links relevant N013 sections. N013 links back to P068 and P048, with the model explained in P024. P024 no longer maintains a competing configuration reference.

## 4. URL, Link, and Redirect Policy

**Preserve URLs when only the type or sidebar group changes.** P071 remains `/developer-guide/protect/detection-methods` even when placed in Reference. P054 remains `/developer-guide/agentic/quickstart` while its title becomes a concrete SDK tutorial. Folder tidiness alone does not justify changing a public URL.

| Source URL | Proposal | Reason |
| --- | --- | --- |
| `/owner-guide/register-agents/what-is-an-agent` | `/concepts/agents` | The explanation serves all interfaces; an actual move |
| `/tutorials/protect-agents/dome-containerized-deployment` | `/developer-guide/deploy-vijil/dome-service` | The deployment how-to moves into ADG |
| `/get-started/quickstart` | `/developer-guide/agentic/quickstart` | Its current destination, `/developer-guide/getting-started/quickstart`, does not exist in the checkout |
| `/get-started/welcome` | `/concepts/welcome` | Currently leads to a different non-TOC overview; align with the canonical public entry point |
| Eight retired `/developer-guide/cli/*` pages | Map individually by intent: authentication, registration, evaluation, monitoring… or provide a clear retirement notice | Do not redirect everything to Welcome or imply new SDK content still describes retired command syntax |

Review/fix two relative links: Welcome → `concepts/trust-score/introduction` and How Evaluation Works → `concepts/evaluation-components/scenario`. Prefer root-relative MDX source paths. Normalize P091’s `models-errors/#paget` link and verify its anchor; the static check does not classify it as definitively broken.

Five non-redirected links from TOC content lead to four non-TOC pages: old custom Harness/OWASP/custom Detector/risk pages. This does not automatically mean HTTP 404. The first three topics have newer TOC destinations or a new catalog; the risk guide cannot be declared replaced without review. If necessary, explicitly add and review that content in scope or transfer its required material into a canonical TOC destination. Do not silently expand the audit to the whole legacy folder.

A redirect does not automatically solve legacy fragments (`#anchor`) when one document is split into multiple destinations. Servers generally do not receive fragments. For important old anchors, retain a compatibility anchor and a short pointer section at the retained URL; update internal links to the actual new destination. Verify chains/cycles, final status, semantic destination, and the `.md` path.

Capture generated API routes from the published index before changing summary/tag taxonomy. Do not assume slugs remain stable when `List Presets` becomes `List Persona Presets` or an alias is removed. Build canonical documentation URLs and redirects only with that map available.

## 5. Standard for New or Migrated Pages

Every page has one primary E/H/R/T purpose, clear title/description, scope, and content owner. Types can be tracked in `content-registry.json` or another tooling sidecar; **do not assume Mintlify displays arbitrary `doc_type` frontmatter or includes it in its AI index**. Public rendering must itself communicate the goal and interface. Use confirmed native fields such as `title` and `description` in frontmatter.

Proposed editorial registry:

```json
{
  "developer-guide/evaluate/running-evaluations": {
    "type": "how-to",
    "audience": ["developer", "automation-agent"],
    "surface": ["python-sdk", "mcp"],
    "product": "diamond",
    "content_owner": "to-be-assigned",
    "contract_owner": "to-be-assigned",
    "verified_release": "to-be-confirmed",
    "last_verified": null,
    "concept": "concepts/evaluation-components/introduction",
    "reference": "developer-guide/reference/evaluation-contracts"
  }
}
```

This is a **proposed tooling structure**, not an existing registry. `last_verified` does not mean the latest grammar-edit timestamp. Update it when relevant behavior is checked against a particular release.

### Tutorial Template

```markdown
---
title: "Your First Evaluation with the Python SDK"
description: "Run one behavioral evaluation with the Python SDK and inspect its evidence."
---

One sentence stating what you will learn and what you will produce.

## Before You Begin
Exact supported environment, credentials, test Agent and access.

## Run Your First Evaluation
One chosen path; bounded steps and checkpoints; complete example.

## Check Your Results
Expected shape and how to distinguish success from failure.

## Clean Up
Only actions and retained state relevant to this exercise.

## Related
The next real task, the concept, and the exact reference.
```

A tutorial does not silently default to a production Agent, require beginners to write an adapter, or demand design decisions before their first success. State cost and variable completion time where they materially affect the user’s choices.

### How-to Template

```markdown
---
title: "Run and Monitor Evaluations"
description: "Start a behavioral evaluation with the Python SDK or MCP and retrieve its result."
---

Goal, supported interface and final artifact in one short paragraph.

## Before You Begin
Required state, IDs, permissions, versions, credentials and limits.

## Start the Evaluation
Only the steps needed for this task; name the returned identifier.

## Wait and Check the Result
Bounded polling, terminal statuses, saved/readiness conditions.

## Troubleshooting
Likely actionable failures; task-specific recovery.

## Related
Concept, full options reference, and the Console counterpart.
```

When one how-to has SDK and MCP variants, each block has an explicit heading and independently defined variables. Do not combine them in an unlabeled command or hide a necessary prerequisite in only one tab. REST examples are a secondary route to the contract; every task need not have a third complete copy.

### Reference Template

```markdown
---
title: "Dome Results and Telemetry Reference"
description: "Look up Dome payloads, results, telemetry fields and units for the supported release."
---

Scope, package/service and version.

## Result Types
Fields, types, defaults, units and conditional availability.

## Behavior
Guaranteed semantics, limits, errors and retries where applicable.

## Examples
Small examples of the described contract.

## Related
The concept and at least one task using this contract.
```

“Everything supported” can mean only what the authoritative versioned source actually covers. Runtime Detectors and evaluation Detectors have separate namespaces; API, SDK, and UI names are shown as a mapping rather than silently treated as synonyms.

### Explanation Template

```markdown
---
title: "How Trust Runtime Works"
description: "Understand identity, constraints and the enforcement boundaries of Trust Runtime."
---

The conceptual question and a concise answer.

## Mental Model
Definitions and a small example.

## How the Parts Relate
Mermaid plus a textual description of the same relationships.

## Tradeoffs and Boundaries
Important design choices and scope limits.

## Related
The Console task where it exists, the developer task, and reference.
```

Every topic need not use identical headings. Templates are content checklists. Public English pages should follow existing repository styles: Title Case, H2/H3, component names, inline code, and Vale rules. Do not rename a real API literal merely to satisfy prose linting or undermine stable IDs.

## 6. Linking Rules and Controlled Exceptions

| Type | Required links |
| --- | --- |
| T | Next H task; E explanation; R for what was used |
| H | Relevant E; full R contract; counterpart interface where one exists |
| E | Relevant AOG and ADG tasks when both are supported; concrete reference |
| R | The model explaining the concept; at least one how-to using the contract |

Every authored page ends with `Related`. Checks must not reward arbitrary links merely because the section exists. Products without a supported guide yet, such as Darwin, have a documented exception: link availability and the existing model instead of an empty how-to stub. The Glossary links relevant domains and guides rather than repeating every term as a separate footer link.

Generated API pages need a functional equivalent through the generator, API descriptions, or a linked resource landing and registry. Do not manually add the same footer to 149 artifacts that the next synchronization overwrites. CI must know which pages are generated and how to verify their links.

## 7. CI and Validation

| Check | What it catches | When |
| --- | --- | --- |
| TOC/source inventory | Every navigated MDX exists; no duplicate URLs; each has an E/H/R/T type and goal | Every documentation PR |
| Frontmatter and descriptions | Missing title/description, generic or duplicate candidates, registry scope/version | New/changed content; warnings for the unmigrated remainder |
| Content/link graph | Related exists and reaches valid, relevant destinations; type-specific links and exceptions | Migrated pages |
| Terminology lint | Confirmed names and prohibited obsolete prose aliases; explicit exceptions for code literals | Every documentation PR |
| Mintlify build and broken links | MDX/render/build failures and dead links; pin the appropriate CLI version in CI | Every documentation PR |
| Redirects and anchors | No chains/cycles/dead targets; expected legacy anchors and generated routes remain useful | Path and TOC changes |
| OpenAPI schema/coverage | Schema validation, unique IDs, public routes, alias decisions, examples, and stable documentation routes | Specification synchronization PRs and relevant service releases |
| Executable examples | Imports, complete minimal examples, retained supporting CLI steps, response shapes, statuses, and failure branches | Examples changed by the batch; relevant package releases |
| Rendered Markdown | IDs, prerequisites, necessary tab/accordion content, Mermaid, and Related appear in the agent view | Pilot, new components, and a representative regression set |
| Documentation task evaluation | Correct interface selection, task completion, valid API/tool calls, and respect for limits | Before/after the pilot and significant architectural changes |

`mint broken-links` does not verify semantic destination relevance, score units, or the existence of every SDK method. Vale cannot determine whether a page is a useful how-to. Automation and domain review therefore have different jobs.

Tie executable checks to releases and fixtures. Do not run live production write/deploy workflows for every prose edit. For consequential tasks such as CI gating or tool enforcement, verify failure, timeout, missing results, and shadow/enforce distinctions. For moving already-verified text without changing meaning, build/link/render checks and domain review are sufficient.

## 8. Measuring Whether Migration Works

Before changing content, save results for the same tasks, queries, and model/tool environment. Repeat them afterward. Traffic is not task success: a crawler fetching ten pages and an agent successfully running an evaluation are different session types.

| Measure | Proposed assessment |
| --- | --- |
| Finding the right destination | Short tree test with Console users and developers: first tab/group choice, retrieval success, time, and wrong turns |
| Agent retrieval | Whether relevant H/R destinations are found early; correct product/interface/version selection |
| Agent task success | Completed task with verifiable results, valid IDs, and bounded polling, without invented methods |
| Contract correctness | Correct scale/unit/status; no unverified interchange of evaluation and engagement IDs |
| Context cost | Pages read, tokens required, backtracking, and irrelevant interface content |
| Maintenance | Locations changed for one definition, drift findings per release, and ownership completeness |
| Human comprehension | Whether an owner can explain a finding and next action without reading the SDK catalog |

Proposed pilot exit criteria: all critical contract tasks pass without wrong interfaces, statuses, or units; most remaining tasks show shorter or equally short paths with better success. Agree numerical task-success and token-budget thresholds after measuring the baseline, rather than inventing them as evidence of improvement.

[agent-evaluation-tasks.json](agent-evaluation-tasks.json) defines 12 initial tasks with expected destinations in the target plan and disallowed incorrect conclusions. It is a documentation evaluation specification, not an executed benchmark or product-functionality test.

## 9. Ownership and Maintenance

| Responsibility | Role owner | Approval scope |
| --- | --- | --- |
| Architecture and standards | Docs lead | Type, goal, placement, link graph, and editorial consistency |
| Console | Console product/engineering owner + AOG editor | Actual UI names, role permissions, state, and verification |
| Diamond/Red Team | Domain engineering owner + ADG/Concepts editor | Score/sampling/taxonomy, IDs, statuses, and report contracts |
| Dome/Controls/Trust Runtime | Runtime engineering owner + ADG/Concepts editor | Enforcement, types/units, framework boundaries, telemetry, and version compatibility |
| Discover | Discover engineering owner + AOG/ADG editor | Collector artifacts, credentials, support scope, and DLP path |
| API/SDK generation | API/SDK maintainer | Authoritative release source, coverage, drift, and generated routes |

Assign individuals during implementation. One person can hold multiple roles, but responsibility for product behavior must be distinguished from responsibility for documentation quality.

Trigger review primarily through contract/release changes and task regressions. Periodic review catches neglected areas; it does not replace documentation updates alongside public behavior changes. For conditional Darwin guides, the decision owner confirms publication only when the actual workflow exists.

## 10. What Is Ready for Review

The architectural direction, exact content destinations, complete TOC, and pilot can be reviewed now. The next approval should concern this concrete pilot and standard. Public pages can then be authored/migrated in separate PRs. This package does not change public navigation or claim that unresolved product contracts have been settled.
