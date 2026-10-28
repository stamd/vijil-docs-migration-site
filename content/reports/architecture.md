# Target Architecture and Diátaxis Rules

## 1. What Hybrid Diátaxis Means Here

The hybrid model has three independent dimensions: **working context** (Console or programmatic), **domain/task** (discover, evaluate, protect…), and **the reader’s immediate need** (learn, accomplish a task, look up information, understand). The first two organize the existing tabs and their groups. The third determines each page’s content and form.

Agent Owner and Agent Developer should therefore be understood as two paths through the product, rather than mutually exclusive identities. A developer using the Console should be able to move directly to the relevant AOG task. An agent writing Python uses ADG; when explaining findings to a risk owner, it uses the shared Concepts material.

Diátaxis starts with two axes: practical action versus cognition/information, and acquiring a skill versus applying an existing skill. Their four intersections produce four documentation forms. This models user needs rather than ranking content by importance. [Diátaxis: Foundations](https://diataxis.fr/foundations/)

| Need | Primary type | What the reader should obtain | Vijil example |
| --- | --- | --- | --- |
| Learning through guided practice | Tutorial (T) | A successful first experience and a repeatable skill | Your First Evaluation with the Python SDK |
| Completing a specific job | How-to (H) | A result on their own Agent in a real context | Run and Monitor Evaluations |
| Reliable lookup during work | Reference (R) | An exact name, type, default, condition, output, or limit | Evaluation Contracts and Results |
| Developing a mental model | Explanation (E) | Reasons, relationships, tradeoffs, and interpretation limits | How the Trust Score Works |

### Tutorial: A Controlled First Experience

A tutorial selects the example, path, and scope for a beginner. The author takes responsibility for working prerequisites, sequencing, results, and the complete experience. A long workflow that immediately requires choosing among four interfaces and supplying an endpoint already consumes knowledge the beginner is meant to acquire. [Diátaxis: Tutorials](https://diataxis.fr/tutorials/)

For Vijil, I recommend two main tutorials: Console and Python SDK. Each uses an available test Agent or a precisely supplied fixture, one small behavioral run, and review of one finding. Self-hosting the platform is not a normal prerequisite. Neither promises a fixed LLM score or completion time; each verifies completion and the shape of available evidence.

MCP/plugin remains an equally supported working interface, but does not require a copy of every tutorial. Its setup links to the same focused tasks and tool reference. A separate MCP learning tutorial can be added later if interviews or task evaluations demonstrate a need.

### How-to: One Real Outcome

A how-to starts from the user’s goal and assumes appropriate foundational knowledge. It can branch when the real problem requires it. It need not reteach the entire domain or enumerate every capability of the tool. [Diátaxis: How-to guides](https://diataxis.fr/how-to-guides/)

“Create a custom Harness and verify that it is active” is one goal, even though it requires create, poll, and inspect operations. “Everything you can do with Harnesses” is an operation catalog. “Release an Evaluated Agent” can remain a complex orchestration how-to: its outcome is a release with evidence, but it links detailed registration, evaluation, and instrumentation steps instead of repeating them.

A brief prerequisite explanation or small table of required fields does not require another page. A split is justified when it serves a separate reading intent or a reusable contract.

### Reference: A Contract During Work

Reference should follow the product’s structure and be precise, neutral, and consistent. A small usage example is appropriate; a complete beginner walkthrough or lengthy rationale makes lookup harder. Generation can help accuracy, but does not replace a description of semantics. [Diátaxis: Reference](https://diataxis.fr/reference/)

Vijil lacks canonical contracts above isolated methods: which status actually completes a run, when results are persisted, the unit of `sample_size`, whether different IDs identify the same object, which scale applies to each field, and how `flagged` differs from `enforced`. These contracts are particularly important to agents composing multiple calls.

### Explanation: Relationships and Reasons

Explanation develops context and connects concepts. It suits architecture, design rationale, and tradeoffs. The group can be called Concepts, Architecture, or Background; it need not be named Explanation. [Diátaxis: Explanation](https://diataxis.fr/explanation/)

Vijil’s Concepts area should explain the difference between behavioral measurement and adaptive exploration, the actual relationships between products and their interfaces, the separate protection models, and what evidence permits readers to conclude. A list of every Probe ID does not serve this purpose. Existing dimension and component URLs therefore remain as real explanations, while their catalogs receive reference destinations.

### Resolving Boundary Cases

For each section, ask whether it guides action or supplies information, and whether it serves learning or immediate work. This “compass” helps detect when a page has quietly changed into another type. [Diátaxis: The compass](https://diataxis.fr/compass/)

One type does not mean one sentence or no context. A tutorial can explain an immediate result; a how-to can list required fields; reference can provide an example; Concepts can show a small illustrative object. The problem arises when a reader seeking a method argument must read a tutorial, or a reader seeking to understand a dimension receives only a test table. [Diátaxis: Reference and explanation](https://diataxis.fr/reference-explanation/)

Do not create four empty sections for every product or require equal page counts across types. Diátaxis recommends improving content iteratively, allowing structure to develop. The requested architecture plan is a testable target hypothesis; migration remains small and iterative. [Diátaxis: Guide to work](https://diataxis.fr/how-to-use-diataxis/)

## 2. Responsibilities Across the Three Tabs

| Tab | Canonical content | Content linked elsewhere |
| --- | --- | --- |
| Concepts | Explanations of products, models, lifecycle, results, discovery, and protection; a shared Glossary as a Reference exception | Console/code procedures, complete parameters, and catalogs |
| Agent Owner’s Guide | Console tutorial and focused Console how-to guides; decisions, review, configuration, and monitoring | Software installation, SDK/MCP setup, broad conceptual definitions, and technical reference |
| Agent Developer’s Guide | SDK tutorial; SDK/MCP/plugin how-to guides; integrations, CI/CD, Collectors, and self-hosting; central technical Reference | Console procedures and general conceptual explanations |

Central reference within ADG does not mean an owner must learn the SDK to look up a UI field. An AOG task links directly to the appropriate lookup with explicit Console scope. Small tables necessary to complete the task can stay local. The Glossary remains in Concepts because it is an entry point for all three tabs; it is canonical for definitions rather than a copy of technical specifications.

There is no fourth Reference tab because the user explicitly retained the existing three. Self-Hosting is an ADG group, not a separate tab. This removes the 1,084-line AWS runbook from the beginner Get Started path while keeping operator content discoverable.

Landing/routing pages are not a fifth Diátaxis type. Welcome remains a short explanation with navigation. Developer introduction and workflow selectors have a Reference purpose: looking up available entry points and suitable guides without repeating mechanism explanations.

## 3. Proposed Organization

The complete navigation with all 118 target MDX pages is in [proposed-toc.md](proposed-toc.md). This is an architectural overview, not another alternative TOC.

```text
Concepts
  Platform: products, Agent, lifecycle
  Trust and Evaluation: Trust Score, dimensions, components, context, evidence
  Discovery: Target, Collector, Resource, Classification
  Red Team: choosing an approach, Engagement loop
  Runtime Defense: Guardrails, Controls Engine, Trust Runtime, observability
  Glossary

Agent Owner's Guide
  Get Started: first Console evaluation [T]
  Teams and Agents
  Discover Agents
  Prepare Evaluations
  Evaluate Agents
  Red Team
  Protect and Monitor
  Improve Agents [conditional: confirmed Darwin workflow]

Agent Developer's Guide
  Get Started: workflow selector, first SDK evaluation [T], SDK/auth/MCP/plugin setup
  Teams and Agents: endpoint and programmatic registration
  Discover Agents: technical Collector installation; DLP setup requires a confirmed path
  Prepare Evaluations: custom Harness through SDK/MCP
  Evaluate Agents: execution, local tunnel, evidence retrieval
  Red Team: execution and investigation
  Protect Agents: install, configure, enforce, custom Detector, instrument, integrations
  Release and Improve: orchestration, Python CI gate; conditional Darwin content
  Self-Hosting: AWS infrastructure, Console installation, Dome service
  Reference
    Evaluation Catalogs
    Platform Contracts
    Runtime Protection
    Python SDK
    MCP and Plugin
    Self-Hosting
    REST API [generated]
```

Group names mostly use task language. Page types live in the editorial registry and in each page’s clear purpose statement. Every sidebar title need not begin “How to.” This avoids an extra Tutorials/How-to/Reference layer inside every product group.

## 4. Canonical Content Locations

| Topic | Explanation | How-to | Reference |
| --- | --- | --- | --- |
| Agent and lifecycle | P037→Concepts, N001 | AOG P038; ADG N023 and P053 | N011; SDK/MCP/REST contracts |
| Evaluation | P007–P020, N002, N003 | AOG P041–P045; ADG P058–P061 | N006–N012 and existing SDK/API reference |
| Red Team | P021, P022 | AOG P046/P047; ADG P063/N029 | N012; public MCP/SDK and updated REST specification |
| Content Guardrails | P023–P026 | AOG P048/P050; ADG P068–P070 | P071, N013, N014 |
| Controls | N004 | P066 | P080 |
| Trust Runtime | N005 | P067 and framework guides | N015, N016 |
| Monitoring | P027 | AOG P049/P051; ADG P072 | N014/N015 and confirmed data-source contracts |
| Darwin | P006 and relevant lifecycle context | N033/N034 only when supported | Existing SDK models/methods with N018 availability |

Separate Console and SDK procedures for the same business task are justified. Two independently maintained Trust Score definitions or repeated descriptions of all six PDF report sections are not. Canonical explanations are shared; steps and result verification are interface-specific.

## 5. A Navigation Graph, Not Only a Tree

Documentation must work when readers arrive directly at a deep URL. Diátaxis does not require traversing all four types in a fixed order; entry can occur anywhere. [Diátaxis: The map](https://diataxis.fr/map/)

Related links should represent different needs: understand the model, perform a related task, look up options, and switch interfaces for the same task. Three generic links to Welcome/Overview/Glossary do not meet that need. In large reference catalogs, link the relevant resource or anchor rather than always the top of a large page.

Example of a complete Diamond path: Welcome → First Evaluation → Review Evaluation Results → Interpret Evaluation Evidence → Evaluation Contracts and Results. A direct query such as “retrieve failed prompts” should instead reach the programmatic results how-to, which names the SDK method and its reference anchor.

## 6. What to Optimize for AI Readers

These are design recommendations for Vijil, not claims that Diátaxis itself guarantees better rankings or agent success.

1. **Recognizable intent immediately.** State the goal, interface, and expected result in one concrete sentence. Descriptions must distinguish “Configure Guardrails in the Console” from “Configure Guardrails in Code.”
2. **Explicit prerequisites and scope.** Include package and confirmed version, Python/framework version, deployment/feature flag, team and permissions, required IDs, and authentication. Agents should not reconstruct these from previous pages.
3. **A contract for the whole workflow.** Creation returns an ID used by the next example; polling has terminal statuses, a timeout, and a failure branch; report retrieval has a readiness condition. The latest Agent score does not substitute for the result of a specific CI evaluation.
4. **Self-contained examples.** Complete imports, defined variables, marked placeholders, and a minimal runnable example. Necessary context must not depend on hidden state in another UI tab.
5. **Clear outputs and verification.** Show shapes, required fields, and evidence of success. For generative results, use structural criteria rather than promising identical text or scores.
6. **Visible identifiers.** IDs, enums, units, and relationship keys appear in text/tables. Hover, color, and screenshots cannot be their only representation.
7. **Precise names and versions.** `Dome`, `VijilDome`, `ControlEngine`, and `TrustRuntime` are not synonyms. Management MCP, Claude Code plugin commands, and the Dome MCP proxy perform different jobs.
8. **Small, relevant context.** Use concise opening facts and precise anchors; large catalogs need indexes. Avoid arbitrary word limits or splitting every N tokens: intent and contract define the boundary.
9. **The same public contract for people and agents.** Text alternatives to visual content must derive from the same data. Do not maintain contradictory parallel “AI docs.”

Mintlify already provides `.md` export and content negotiation through `Accept` headers. Inspect actual page/component output in the pilot rather than assuming every Tab or Accordion must be removed. The goal is that agents can read clear variant labels and all prerequisites for their task. [Mintlify: Markdown export](https://www.mintlify.com/docs/ai/markdown-export)

Vijil already has `llms.txt`. Prefer generation from the TOC and good descriptions; a hand-maintained copy introduces a second inventory. Mintlify generates the index and `llms-full.txt`; descriptions and navigation affect discoverability. No index repairs an incorrect API contract. [Mintlify: llms.txt](https://www.mintlify.com/docs/ai/llmstxt)

The move to Mermaid is a useful foundation, but the audit still finds two unique raster diagrams, included three times. Supply text relationships and convert genuinely structural diagrams. Existing Mermaid also needs correct node names, directions, and product-availability assumptions.

The 77% figure justifies checking machine-readable paths, but does not establish that reference is the only important content type. Separate crawlers, retrieval agents, and task-executing agents when analytics supports that distinction.

## 7. Why This Architecture Is Preferable to a Larger Redesign

It preserves existing entry points and the product mental map while reducing the places where the same fact can change independently. Most meaningful URLs remain, even if their sidebar placement changes. The only two required moves of existing pages are What Is an Agent into Concepts and containerized Dome deployment into ADG.

The cost is editorial discipline and more links between focused pages. Control fragmentation through the pilot, sufficient local context, and verification that each extraction serves a distinct lookup or task need. Accuracy, completeness, and consistency come first; polished structure cannot compensate for their absence. [Diátaxis: Quality](https://diataxis.fr/quality/)
