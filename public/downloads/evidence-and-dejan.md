# Evidence, Dejan’s Document, and Unresolved Product Contracts

## 1. Review Scope and Confidence

The primary source is the local `docs` working tree, with its TOC defined by `docs.json`. The review covers the purpose, structure, instructions, catalogs, examples, and links of all 92 included MDX pages. The inventory records each page’s title, navigation, line count, and hash. Non-TOC files, drafts, and other repositories are not silently added as documentation pages in scope.

The generated OpenAPI group is an additional part of the TOC. All 149 operations were structurally inspected: method, route, operation ID, summary, tags, and potential alias relationships. [api-operation-inventory.csv](api-operation-inventory.csv) contains a separate record for each operation. Every request/response field has not been verified through backend contract execution.

The public [Vijil index](https://docs.vijil.ai/llms.txt), [Welcome](https://docs.vijil.ai/concepts/welcome), [Quickstart](https://docs.vijil.ai/developer-guide/agentic/quickstart), and [Protection Overview](https://docs.vijil.ai/developer-guide/protect/overview) were used to check public structure and representative rendering. Web results for some pages carry different crawl dates, and direct reads of some `.md` URLs failed. Therefore, **this report does not claim that all 92 live URLs were checked at their latest published version**. The local TOC remains the boundary of the content audit.

The local head is `2e3245d865ce3ffeb87ee734e7ea82b11efc0f15` on `docs-cleanup-v3`. A change to `developer-guide/getting-started/introduction.mdx` existed before this work; it was reviewed as found and was not modified. PR #251 was inspected as a separate future change, not as already merged into that working tree. [source-snapshot.json](source-snapshot.json) and [source-inventory.json](source-inventory.json) record this baseline.

Evidence is distinguished as follows:

- **Confirmed source finding:** directly observed text, table, route, or count.
- **Inconsistency requiring resolution:** sources describe different contracts; the audit does not arbitrarily choose which is correct in production.
- **Recommendation:** proposed content design, new page, or validation step; not an existing product capability.

## 2. Main Content and Structural Findings

| Finding | Concrete evidence | Consequence and recommendation |
| --- | --- | --- |
| Concepts contains multiple catalogs | P008–P010 are largely Probe tables; P017–P020 already describe themselves as reference tables | Turn existing URLs into genuine explanations and extract lookup data into N006–N010 |
| Evaluation Detector has the wrong introduction | P020 says components within Guards and links runtime Guard | Separate the Diamond scoring contract from the Dome runtime contract before copying definitions further |
| Two scales appear without consistent scope | P007/P045/P060: 0–100 and 70; P041/P042: 0–1 and 0.70; newer P052/P053 explain the UI/SDK difference | Canonically document scale per field/interface; verify report display and actual threshold rather than globally renaming numbers |
| Threshold is presented as a deployment decision | P007/P060 say meets deployment threshold; P053 says 0.70 is an example and release criteria belong to the team | Separate product score/verdict from organizational approval criteria; identify defaults versus recommendations |
| Probe and sample_size have inconsistent meanings | P019: a Probe is a group of prompts; P016 describes one prompt, then a group; P090 counts Probes per Harness; P059 counts prompts per Probe | The domain owner must confirm units and API/SDK/engine mappings. Otherwise, agents cannot estimate work reliably |
| Catalog completeness claims exceed the presented data | P017 discusses all Harnesses, benchmarks, and Audits but lists three dimension Harnesses; P018 uses different narrative/table taxonomies | State source version and catalog coverage; moving an old list into Reference does not make it complete |
| Behavioral and Red Team content is duplicated | P044 repeats P046 launch/settings; P045 repeats P047 results; P058/P063 describe multiple programmatic Red Team flows | One launch and one results task per interface context; shared semantics in Concepts/N012 |
| Report anatomy is copied | All six Trust Report sections are described in detail in P045/P060, with summaries in P002/P029/P041 | Shared explanation N003; AOG keeps UI drilldown, ADG keeps SDK retrieval/filter/report tasks |
| Runtime examples use different API models | P026 uses `from vijil.dome import Detector`, voting strategies, and a different result shape; P070 uses `DetectionMethod`, async detect, and `(hit, metadata)` | Older examples are at least inconsistent with newer public reference. Check the release and remove pseudo APIs or label them clearly as illustrations |
| The same measurement has two units | P024 describes `exec_time` in milliseconds; P064/P069 use seconds | P0 contract fix in N014 and all examples, including JSON/tables |
| Detector categories differ across examples | P068 lists `policy-gpt-oss-safeguard` under Policy, while P071 places it under Generic; P070 says a Guard accepts only its own category | Confirm the release registry category and derive configuration examples from it |
| Observability explanation uses another instrumentation API | P027 uses `vijil.dome.DomeClient`, `scan_input`, and `trace`; P072 uses `vijil_dome` and `instrument_dome` | P027 becomes the explanatory signal model; actual setup and verified metrics live in P072/N014 |
| The main architecture omits three distinct protection models | P066 distinguishes `VijilDome`/`Dome`/`TrustRuntime`; platform Dome and How Defense Works largely describe only content Guardrails | Add Controls Engine and Trust Runtime Concepts pages and explain their contract boundaries |
| Tutorials require too many early decisions | P029 progresses from business context to Red Team, Dome, and monitoring; P054 has four interface tabs across six steps | Two controlled first-evaluation tutorials; alternate interfaces lead to setup/how-to guides |
| Local denotes two workflows | P057 says local does not support Red Team; P059 explains that a public tunnel supports it, while no-tunnel local mode does not | Distinguish reachable tunneled endpoints from SDK local mode in the selector, without blanket statements |
| SDK existence does not establish availability | P006: Darwin in development/not GA; P090 includes adapt/evolve/deploy; P053 says the platform does not deploy applications; P091 has unimplemented monitoring reads | N018 release/deployment matrix; conditional Darwin guides. Distinguish corrective adaptation, generative evolution, and application deployment |
| Python requirements differ | P089: 3.12+; P054: 3.11–3.13; local `vijil-sdk/pyproject.toml`: >=3.11,<3.14 | The local manifest supports the inconsistency finding but does not establish the published package version. Confirm the public release and pin the example |
| Base Dome verification omits required dependencies | P065 distinguishes thin/base, local, and pii extras, but the opening scan uses default models | Select a verified minimal scan or explicitly install all extras required by the defaults |
| Owner deployment includes developer work | P050 contains Python integration; P033 contains root/PowerShell/Helm/AWS IAM procedures | P050 becomes a handoff; four Collector installation paths move into ADG |
| A large self-hosting runbook sits in Get Started | P056 has 1,084 lines covering AWS/application infrastructure, internal staging examples, and optional Darwin | ADG Self-Hosting group; separate infrastructure how-to, application runbook, and configuration reference |
| Glossary entries conflict or repeat | Two Judgment entries, two Policy meanings, and an overly broad Detector definition | Domain-scoped terms and aliases, stable anchors, and a glossary derived from the confirmed registry |
| SDK reference repeats a model | P092 contains two `### EvaluationResponse` sections | One canonical definition with working anchors; align P091’s method index with its body |

These findings show that the problem extends beyond page length. Conflicting names, units, support status, and transitions between objects are particularly costly for automated readers. The plan therefore separates editorial extraction from product-contract decisions.

## 3. Monitoring: Why the Four Terms Should Not Be Merged

| Name | Observed meaning | Decision |
| --- | --- | --- |
| Observe / Observability | P027 explains the signal domain; P072 covers instrumentation | One Concepts model and one technical setup task |
| Dome Metrics | P051: per-Agent data under Agents → Monitor, with metrics/traces/log links | Keep a separate Console investigation how-to |
| Defend | P049: events from `dlp` Targets, tenant/Target scope, attribution, and sampled counters | Keep a separate Console investigation how-to |

An umbrella term such as runtime observability can be standardized without equating different sources or scopes. In both views, “no events” requires checking ingestion prerequisites rather than automatically concluding there are no threats. Product and engineering should confirm exact product/name relationships.

## 4. OpenAPI: Confirmed Duplication and Sync Findings

Local `openapi/api.json` contains **112 paths and 149 HTTP operations, with no duplicate `operationId` values**. It is therefore inaccurate to attribute duplicate endpoints to duplicate operation IDs.

There are **11 operation pairs** across `/v1/demographics/...` and `/v1/dimensions/...`. Ten pairs are identical apart from operation ID; the bulk-add pair has an additional difference. The public index also contains generated titles such as `List Dimensions` and `List Dimensions-1`, plus separate Persona/Policy pages titled `List Presets`. These represent at least two different cases:

- Potential compatibility aliases with actual distinct routes, which require confirmation before hiding or deprecation.
- Different resources with identical summary titles, which should be disambiguated, for example List Persona Presets and List Policy Presets.

All 149 operations have multiple tags. This may matter for navigation generation, but the audit **does not establish that every multi-tag operation causes duplicate presentation**. Do not remove tags blindly or change real APIs for sidebar aesthetics.

Guides describe `/v1/discover/...`, `/v1/redteam/engagements/...`, evaluation Red Team artifacts, and manifest operations not covered appropriately by this combined specification. The Discover/Engagements/Manifests prefixes are entirely absent. This is a confirmed **coverage gap between guides and the specification**, not proof that backend routes do not exist.

The proposed fix is to publish versioned public-gateway specifications, classify compatibility aliases, and maintain a stable registry of generated documentation routes. `operationId` must be unique and stable, summaries resource-specific, and each public operation represented by one canonical documentation entry. Other entry points can link to it. Manually patching 149 generated pages is not an appropriate solution.

The inspected `docs` checkout has no `.github` directory; it does contain Vale configuration and style rules. This does not establish that the organization has no external CI or specification synchronization. Engineering must identify the current generator, triggers, source repositories, and owners. Drift findings support Dejan’s concern about synchronization, but this audit does not claim to have identified its cause in a specific pipeline implementation.

## 5. Impact of PR #251

Metadata was read through the GitHub connector; local `remove-cli-references` matches its exact head `c75df95b9291806368625203414abc77ba66ab69`. When checked, [PR #251 — docs: Remove CLI references](https://github.com/vijilAI/docs/pull/251) was open, non-draft, and unmerged. Its description says it follows Dejan’s PR #250, moves toward UI/SDK/MCP, retains selected supporting SDK CLI steps, and leaves some Console CLI dependencies for later review.

Compared with the local 92-page TOC, the PR-head TOC contains 84 MDX pages: eight CLI Reference pages P081–P088 are absent. Its diff also deletes an old non-TOC CLI quickstart file, which is not an additional audited page.

A simple search of the confirmed PR head finds CLI candidates on seven retained TOC pages; exact lines are in [pr251-cli-residuals.json](pr251-cli-residuals.json). The search excludes `/vijil` plugin commands, which are not shell CLI commands:

| Page | Remaining content | Treatment |
| --- | --- | --- |
| P032 Targets | CLI tabs and deployment creation, scan, configuration, and deletion commands | Keep the Console task; confirm replacements for uncovered operations |
| P033 Collectors | Setup address and credential mint/list/revoke commands | Owner credential UI where available; operator setup only through a confirmed path |
| P038 Register Agents | Authentication/team commands for standalone MCP setup | Extract into MCP setup; supporting commands do not create a new primary CLI workflow |
| P049 Defend | A `dlp` Target creation command | Do not remove the only prerequisite without a confirmed replacement; N028 remains conditional |
| P054 Quickstart | CLI tabs and evaluation path | Replace with one SDK tutorial; PR251 does not already do this |
| P063 Red Team Overview | Persona/Policy preset shell examples | Replace with confirmed SDK/MCP examples |
| P089 SDK Setup | Supporting `auth login` and `config set` commands | May remain as documented setup necessities after release verification |

Local package manifests also define executable `vijil` for `vijil-sdk` and executable `vijil-console` for `vijil-console`, while older instructions use `vijil` for both command families. This is a version/contract inconsistency to verify, not a reason to restore public CLI reference.

Apply the migration plan after comparing the merged PR #251 state with other active documentation changes. This audit does not require checking out the branch or overwriting the user’s local changes.

## 6. Comparison with Dejan’s Document

Direct Google Drive access returned 404/403. This analysis uses the complete document text supplied by the user in the conversation. It does not claim to have checked comments, revision history, or the separate cheat sheet/checklist mentioned in that document.

| Dejan’s recommendation or claim | Assessment after the audit | Concrete decision |
| --- | --- | --- |
| Retain AOG/ADG/Concepts | Supported and consistent with the user’s constraint | Keep the three tabs; change groups and page purposes |
| Confirm naming before documenting a feature | Necessary where contracts already differ | Terminology registry and product owner per topic; gate dependent content without stopping unrelated fixes |
| One goal per page | The most important principle for current mixed content | One primary intent; brief context and required fields are allowed to prevent excessive fragmentation |
| AOG Console, ADG code? | Resolve by working context | AOG Console; ADG SDK/MCP/plugin and operators. The same person crosses via named counterpart links |
| Explanations only in Concepts | Useful for a canonical model | Centralize general explanations; retain sentences required to perform a step. Lookup/routing pages are Reference, not duplicate explanations |
| Reference in one place | Necessary, but a fourth tab is outside the agreed scope | Central ADG Reference group; Glossary remains a shared entry point in Concepts |
| Three competing developer entry points | Partly addressed by prior consolidation | There is one TOC quickstart and redirects from old entry points. The remaining issue is distinguishing introduction, first exercise, and lifecycle orchestration, plus four tabs inside quickstart |
| No true tutorials | Tutorial-like steps exist, but the experience is insufficiently controlled | Rewrite P029/P054 as complete first-evaluation tutorials; not every step list is a tutorial |
| Remove the Tutorials section | The current TOC has no separate Tutorials tab | The remaining container tutorial URL is a deployment how-to and moves into ADG with a redirect. Folder names do not determine type |
| Duplicate REST endpoints probably result from synchronization | Alias pairs, similar summaries, and coverage gaps are confirmed; cause remains unverified | Engineering investigation of the generator/public API contract; no arbitrary route deletion |
| Darwin has no guides | A gap exists, but product availability is unclear | N033/N034 are planned with explicit publication conditions |
| Trust Runtime has no concept page | Confirmed | N005 and related N004 for the Controls Engine |
| Observe/Observability/Dome Metrics/Defend name one capability | Too broad as a merge rule | One umbrella concept, but separate guides for different data sources and scopes |
| Every page has Related | A useful editorial minimum, insufficient as the only check | Verify link types and destinations, not just a heading; generated API pages receive a systematic equivalent |
| Focused pages rank better and are cited by AI | A reasonable project hypothesis, not established by these sources | Do not promise ranking/citation gains; measure retrieval and task success |
| Vale, frontmatter, and broken-link checks | A practical foundation | Add TOC coverage, redirects/API checks, rendered Markdown, and executable verification of selected examples |
| Section ownership | Essential for maintenance | Separate docs ownership from engineering domain ownership; individuals have not yet been assigned |

Dejan’s direction is retained. This audit turns it into a complete inventory, distinguishes previously addressed issues from remaining ones, and adds precise content destinations and verification conditions.

## 7. Contracts Product/Engineering Still Need to Confirm

These do not prevent producing the proposal. They are explicit implementation dependencies:

| Contract | Confirmation required | Dependent content |
| --- | --- | --- |
| Red Team objects | Whether Evaluation, Engagement, and Campaign are distinct systems, wrappers, or compatibility aliases; public IDs/routes per deployment | P022/P063, N012/N029, SDK/MCP/OpenAPI |
| Trust Score | Scale per field, default threshold, aggregation, missing values, and result readiness | P007/P041/P045/P060, N003/N012/N022 |
| Sampling and taxonomy | Probe/group/prompt definitions, sample_size units, Harness aliases, and catalog release snapshot | P008–P020/P059/P090, N006–N012 |
| Runtime enforcement | Current `Dome`/`VijilDome`/`TrustRuntime` contracts, units/statuses, framework limits | P023–P027/P064–P080, N004/N005/N013–N017 |
| Discovery and DLP | Supported bootstrap without a public CLI workflow; Target/deployment/scan surface mapping | P012/P032/P033/P049, N024–N028 |
| Availability | Releases/tenants supporting Darwin, deploy/evolve, API/SDK preview, White Box, and monitoring reads | N018/N033/N034 and reference |
| UI names and permissions | Tests/Verify, Adaptive visibility, global SUPER ADMIN versus team roles, activate/register, Save/Apply effects | AOG procedures and N011/N012/N013 |

The Glossary records these decisions. It does not become the source of truth for code behavior: code/specification/release contracts and responsible teams confirm facts, while the terminology registry represents them consistently.
