# Page-by-Page Plan

Scope: all 92 MDX pages in the local TOC. Eight CLI pages are recorded as retired through PR #251. The target consists of 84 existing pages, each with one primary purpose, plus 30 proposed new pages (two conditional).

E = explanation; H = how-to; T = tutorial; R = reference. Current type is an editorial assessment of the content, not existing frontmatter. P0 identifies a contract/accuracy issue or an already-decided retirement; P1 is the main transition work; P2 is a later improvement.

Keep preserves the page, URL, and main structure with the specified corrections and standard links. Refactor changes focus without extracting separate pages; split specifies explicit destinations; retire-by-251 does not restore retired content.

## P001 — Welcome to Vijil

Source: [concepts/welcome](../../docs/concepts/welcome.mdx). Current type: **E+landing**. Action: **refactor**, **P1**.

**Finding:** Lifecycle paragraphs and the same WebP image are duplicated; marketing, concepts, and navigation paths are mixed.

**Change:** Condense the platform narrative, remove duplication, replace the lifecycle image with Mermaid and a text equivalent, and link to both introductory tutorials.

**Destination:** Concepts → Platform → **Welcome to Vijil [E]**; URL `/concepts/welcome`.

**Single page goal:** Explain the platform's role and direct readers to the right starting point.

**Related content destinations:** N001. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P002 — Console

Source: [concepts/platform/console](../../docs/concepts/platform/console.mdx). Current type: **E+R**. Action: **refactor**, **P2**.

**Finding:** The Trust Report description and universal threshold-of-70 claim repeat other pages; some Console links lead to programmatic guides.

**Change:** Keep the Console's role and audience; link to the shared report explanation and to AOG tasks.

**Destination:** Concepts → Platform → **Vijil Console [E]**; URL `/concepts/platform/console`.

**Single page goal:** Explain what the Console does and how it connects the products.

**Related content destinations:** N003. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P003 — Discover

Source: [concepts/platform/discover](../../docs/concepts/platform/discover.mdx). Current type: **E**. Action: **keep**, **P2**.

**Finding:** The boundary between discovery and evaluation is clear; the four main Collector kinds do not represent all additional variants.

**Change:** Keep the explanation; distinguish the main families from complete coverage and link to supported installation paths.

**Destination:** Concepts → Platform → **Vijil Discover [E]**; URL `/concepts/platform/discover`.

**Single page goal:** Explain where resource discovery fits into the lifecycle.

**Related content destinations:** N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P004 — Diamond

Source: [concepts/platform/diamond](../../docs/concepts/platform/diamond.mdx). Current type: **E+R**. Action: **refactor**, **P1**.

**Finding:** Repeats the Trust Score, four evaluation components, and Red Team loop described on other Concepts pages.

**Change:** Keep the product overview and mode comparison; replace detailed component and algorithm descriptions with precise links.

**Destination:** Concepts → Platform → **Vijil Diamond [E]**; URL `/concepts/platform/diamond`.

**Single page goal:** Explain how behavioral evaluation and adaptive Red Team testing produce different kinds of evidence.

**Related content destinations:** N003. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P005 — Dome

Source: [concepts/platform/dome](../../docs/concepts/platform/dome.mdx). Current type: **E**. Action: **refactor**, **P1**.

**Finding:** Describes only the Guardrail–Guard–Detector model, claims latency below approximately 300 ms without conditions, and repeats the Defense Components heading.

**Change:** Explain how the three protection interfaces relate, including enforcement conditions and limitations; remove the general latency guarantee or provide a verified measurement basis.

**Destination:** Concepts → Platform → **Vijil Dome [E]**; URL `/concepts/platform/dome`.

**Single page goal:** Explain protection scope and the choice between content Guardrails, the Controls Engine, and Trust Runtime.

**Related content destinations:** N004,N005,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P006 — Darwin

Source: [concepts/platform/darwin](../../docs/concepts/platform/darwin.mdx). Current type: **E**. Action: **keep**, **P1**.

**Finding:** Explicitly states that Darwin is not generally available; other pages already describe adapt, evolve, deploy, and a separate Helm service.

**Change:** Keep the preview explanation; tie availability to a version and deployment. Add guides only for a confirmed supported workflow.

**Destination:** Concepts → Platform → **Vijil Darwin [E]**; URL `/concepts/platform/darwin`.

**Single page goal:** Explain planned adaptation capabilities and their availability.

**Related content destinations:** N018,N033,N034. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P007 — The Trust Score

Source: [concepts/trust-score/introduction](../../docs/concepts/trust-score/introduction.mdx). Current type: **E+R**. Action: **split**, **P0**.

**Finding:** The 0–100 scale and threshold of 70 appear universal, while the SDK and parts of AOG use 0–1; aggregation is insufficiently explained.

**Change:** Maintain score meaning here; extract interface-specific scales, units, thresholds, and aggregation rules into the evaluation contract without inventing a formula.

**Destination:** Concepts → Trust and Evaluation → **How the Trust Score Works [E]**; URL `/concepts/trust-score/introduction`.

**Single page goal:** Explain score meaning, coverage, and the limits of interpretation.

**Related content destinations:** N003,N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P008 — Reliability

Source: [concepts/trust-score/reliability](../../docs/concepts/trust-score/reliability.mdx). Current type: **R**. Action: **split**, **P1**.

**Finding:** Almost entirely a Probe catalog; identifiers depend on hover interactions.

**Change:** Write an explanation of the dimension with one representative example and its limitations; move the full catalog into the coverage reference with visible IDs.

**Destination:** Concepts → Trust and Evaluation → **Reliability [E]**; URL `/concepts/trust-score/reliability`.

**Single page goal:** Explain what reliability means for Agent behavior.

**Related content destinations:** N010. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P009 — Safety

Source: [concepts/trust-score/safety](../../docs/concepts/trust-score/safety.mdx). Current type: **R**. Action: **split**, **P1**.

**Finding:** A long list of mutated Probes supports lookup rather than a developed explanation of the dimension.

**Change:** Keep the existing URL for the explanation; extract the catalog, mutations, and IDs while preserving relationships to Scenarios and Harnesses.

**Destination:** Concepts → Trust and Evaluation → **Safety [E]**; URL `/concepts/trust-score/safety`.

**Single page goal:** Explain the safety dimension and its relationship to policies and harmful behavior.

**Related content destinations:** N010. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P010 — Security

Source: [concepts/trust-score/security](../../docs/concepts/trust-score/security.mdx). Current type: **R**. Action: **split**, **P1**.

**Finding:** The content is a coverage catalog, without a clear boundary between the dimension and its test list.

**Change:** Explain confidentiality, integrity, and availability, including coverage limits; maintain the complete list in the shared reference.

**Destination:** Concepts → Trust and Evaluation → **Security [E]**; URL `/concepts/trust-score/security`.

**Single page goal:** Explain the security dimension and the threats evaluation investigates.

**Related content destinations:** N010. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P011 — Discovery Components

Source: [concepts/discovery/introduction](../../docs/concepts/discovery/introduction.mdx). Current type: **E+landing**. Action: **keep**, **P2**.

**Finding:** A short, focused conceptual overview with links to individual components.

**Change:** Keep the hierarchy, add one discovery example, and link to the Console workflow and installation guide.

**Destination:** Concepts → Discovery → **How Discovery Works [E]**; URL `/concepts/discovery/introduction`.

**Single page goal:** Explain the relationship between Target, Collector, Resource, and Classification.

## P012 — Target

Source: [concepts/discovery/target](../../docs/concepts/discovery/target.mdx). Current type: **E+R**. Action: **refactor**, **P1**.

**Finding:** Target, deployment, and scan surface are explicit aliases; the UI sometimes uses Agent to mean Collector.

**Change:** Keep the semantic explanation and mapping of actual names; link exact type values and dlp workflow availability to the contract and capability reference.

**Destination:** Concepts → Discovery → **Discovery Targets [E]**; URL `/concepts/discovery/target`.

**Single page goal:** Explain what a Target contains and how it differs from a Collector or Agent.

**Related content destinations:** N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P013 — Collector

Source: [concepts/discovery/collector](../../docs/concepts/discovery/collector.mdx). Current type: **E+R**. Action: **refactor**, **P1**.

**Finding:** Mixes the mental model, technical requirements, and credential selection; browser and one-shot variants are absent from the main table.

**Change:** Keep the family comparison and coverage implications; link concrete versions, installation, and credential steps to ADG and AOG.

**Destination:** Concepts → Discovery → **Discovery Collectors [E]**; URL `/concepts/discovery/collector`.

**Single page goal:** Explain how to choose a Collector family and understand coverage limits.

**Related content destinations:** N024. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P014 — Resource

Source: [concepts/discovery/resource](../../docs/concepts/discovery/resource.mdx). Current type: **E+R**. Action: **keep**, **P2**.

**Finding:** The distinction between durable and observation-based identity is useful and focused.

**Change:** Keep the explanation and an identity-change example; link registration eligibility rules and findings review.

**Destination:** Concepts → Discovery → **Discovered Resources [E]**; URL `/concepts/discovery/resource`.

**Single page goal:** Explain resource identity and what changes across rescans.

**Related content destinations:** N011. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P015 — Classification

Source: [concepts/discovery/classification](../../docs/concepts/discovery/classification.mdx). Current type: **E+H**. Action: **refactor**, **P1**.

**Finding:** Says the Console receives only the verdict, then lists additional metadata; part of the text provides UI troubleshooting advice.

**Change:** Clarify the boundaries between the local Collector, LLM provider, and Console; move troubleshooting to Review Discovered Resources.

**Destination:** Concepts → Discovery → **Resource Classification [E]**; URL `/concepts/discovery/classification`.

**Single page goal:** Explain the three verdicts, supporting evidence, and data flow.

## P016 — How Evaluation Works

Source: [concepts/evaluation-components/introduction](../../docs/concepts/evaluation-components/introduction.mdx). Current type: **E**. Action: **refactor**, **P1**.

**Finding:** Useful Mermaid diagram and component overview, but describes a Probe both as one prompt and as a group of prompts.

**Change:** Align definitions with the confirmed runtime model; preserve the diagram, add a concrete example, and link to tutorials and catalogs.

**Destination:** Concepts → Trust and Evaluation → **How Evaluation Works [E]**; URL `/concepts/evaluation-components/introduction`.

**Single page goal:** Explain the behavioral evaluation hierarchy and how it differs from adaptive testing.

**Related content destinations:** N006,N007,N008,N009. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P017 — Harnesses

Source: [concepts/evaluation-components/harness](../../docs/concepts/evaluation-components/harness.mdx). Current type: **E+R**. Action: **split**, **P1**.

**Finding:** Promises a reference table of all Harnesses, but the table contains only three dimension Harnesses; also discusses benchmarks and Audits.

**Change:** Keep the standard/custom/compliance Harness mental model here; move IDs and availability into a versioned catalog.

**Destination:** Concepts → Trust and Evaluation → **Evaluation Harnesses [E]**; URL `/concepts/evaluation-components/harness`.

**Single page goal:** Explain why Probes are grouped into Harnesses and how to select coverage.

**Related content destinations:** N006. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P018 — Scenarios

Source: [concepts/evaluation-components/scenario](../../docs/concepts/evaluation-components/scenario.mdx). Current type: **E+R**. Action: **split**, **P1**.

**Finding:** The narrative describes 24 named types while the table uses a different taxonomy; the claim that every Scenario is a Harness needs confirmation.

**Change:** Keep one conceptual example; extract the complete catalog and old-name mapping, with an identified taxonomy owner.

**Destination:** Concepts → Trust and Evaluation → **Evaluation Scenarios [E]**; URL `/concepts/evaluation-components/scenario`.

**Single page goal:** Explain the Scenario's role between Harnesses and Probes.

**Related content destinations:** N007. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P019 — Probes

Source: [concepts/evaluation-components/probe](../../docs/concepts/evaluation-components/probe.mdx). Current type: **R**. Action: **split**, **P1**.

**Finding:** The wide table of IDs, names, descriptions, and Detectors is reference material; the Probe definition differs from other pages.

**Change:** Briefly explain the mechanism with one example; move all lookup rows into the Probe catalog with stable anchors.

**Destination:** Concepts → Trust and Evaluation → **Evaluation Probes [E]**; URL `/concepts/evaluation-components/probe`.

**Single page goal:** Explain the distinction between a Probe definition and individual test prompts.

**Related content destinations:** N008. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P020 — Detectors

Source: [concepts/evaluation-components/detector](../../docs/concepts/evaluation-components/detector.mdx). Current type: **R+E**. Action: **split**, **P0**.

**Finding:** The introduction describes Detectors inside Guards even though the page concerns Diamond evaluation; the table also includes a Dome Detector.

**Change:** Correct the evaluation/runtime boundary; explain possible implementation reuse without equating the contracts. Extract the catalog.

**Destination:** Concepts → Trust and Evaluation → **Evaluation Detectors [E]**; URL `/concepts/evaluation-components/detector`.

**Single page goal:** Explain how behavioral evaluation scores a response.

**Related content destinations:** N009. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P021 — Red Team

Source: [concepts/red-team/introduction](../../docs/concepts/red-team/introduction.mdx). Current type: **E**. Action: **keep**, **P2**.

**Finding:** Clearly distinguishes evidence from Trust Scores; standard is not always used consistently with behavioral.

**Change:** Keep the comparison, standardize only confirmed terminology, and link both interface-specific guides.

**Destination:** Concepts → Red Team → **Why Use Adaptive Red Teaming [E]**; URL `/concepts/red-team/introduction`.

**Single page goal:** Explain when adaptive attacks complement fixed evaluation.

## P022 — Engagements

Source: [concepts/red-team/engagements](../../docs/concepts/red-team/engagements.mdx). Current type: **E**. Action: **refactor**, **P1**.

**Finding:** The loop is focused; stopping rules and Engagement terminology depend on implementation, while the API reference uses campaigns.

**Change:** Keep Mermaid and the mental model; map final terms to public API identifiers without renaming actual routes in prose.

**Destination:** Concepts → Red Team → **How Red Team Engagements Work [E]**; URL `/concepts/red-team/engagements`.

**Single page goal:** Explain the relationship between waves, seeds, attacks, judgments, and reflections.

**Related content destinations:** N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P023 — How Defense Works

Source: [concepts/defense/introduction](../../docs/concepts/defense/introduction.mdx). Current type: **E**. Action: **refactor**, **P1**.

**Finding:** Says Dome intercepts every request and logging is in development; newer ADG pages describe explicit integration and existing telemetry.

**Change:** Explain integration points, enforcement boundaries, and the relationship to the Controls Engine and Trust Runtime; reconcile telemetry status.

**Destination:** Concepts → Runtime Defense → **How Runtime Defense Works [E]**; URL `/concepts/defense/introduction`.

**Single page goal:** Explain where protection is applied during Agent execution.

**Related content destinations:** N004,N005. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P024 — Guardrail

Source: [concepts/defense/guardrail](../../docs/concepts/defense/guardrail.mdx). Current type: **E+R+H**. Action: **split**, **P0**.

**Finding:** Includes Python configuration and ScanResult fields; exec_time is described in milliseconds while ADG uses seconds.

**Change:** Keep the diagrams and concept; move configuration and result details into canonical references; distinguish Console capabilities from programmatic ones.

**Destination:** Concepts → Runtime Defense → **Guardrails [E]**; URL `/concepts/defense/guardrail`.

**Single page goal:** Explain how input and output protection pipelines are composed.

**Related content destinations:** N013,N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P025 — Guard

Source: [concepts/defense/guard](../../docs/concepts/defense/guard.mdx). Current type: **E**. Action: **keep**, **P2**.

**Finding:** The short page already distinguishes six Dome categories from the three Console categories.

**Change:** Keep it, add a small composition example, and link configuration guidance for both interfaces.

**Destination:** Concepts → Runtime Defense → **Guards [E]**; URL `/concepts/defense/guard`.

**Single page goal:** Explain the Guard's role and distinguish a category from an instance.

**Related content destinations:** N013. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P026 — Detector

Source: [concepts/defense/detector](../../docs/concepts/defense/detector.mdx). Current type: **E+R+H**. Action: **split**, **P0**.

**Finding:** 491 lines mix categories, full reference, pseudo voting options, and a custom class from vijil.dome, unlike the newer DetectionMethod contract.

**Change:** Keep the explanation and two representative examples; remove unverified API shapes, consolidate the catalog into P071, and consolidate custom implementation guidance into P070.

**Destination:** Concepts → Runtime Defense → **Runtime Detectors [E]**; URL `/concepts/defense/detector`.

**Single page goal:** Explain detection approaches and runtime tradeoffs.

**Related content destinations:** P070,P071,N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P027 — Observe

Source: [concepts/defense/observe](../../docs/concepts/defense/observe.mdx). Current type: **E+R+H**. Action: **split**, **P0**.

**Finding:** Pseudocode uses vijil.dome.DomeClient and scan_input while newer ADG uses vijil_dome and instrument_dome; metric-name lists are unverified.

**Change:** Keep the signal model and data flow; maintain exact instrumentation steps in P072 and actual metric contracts in reference. Do not merge distinct dashboards.

**Destination:** Concepts → Runtime Defense → **Runtime Observability [E]**; URL `/concepts/defense/observe`.

**Single page goal:** Explain metrics, traces, logs, audit events, Defend, and Dome Metrics.

**Related content destinations:** P072,N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P028 — Glossary

Source: [concepts/glossary](../../docs/concepts/glossary.mdx). Current type: **R**. Action: **refactor**, **P0**.

**Finding:** Contains two Judgment entries; Policy means both an RL strategy and organizational rules; Detector is defined too broadly.

**Change:** Distinguish domains, add canonical terms, visible API/Console aliases, and stable anchors; derive the glossary from a confirmed terminology registry.

**Destination:** Concepts → Glossary → **Glossary [R]**; URL `/concepts/glossary`.

**Single page goal:** Provide unambiguous definitions of terms and actual aliases.

## P029 — Get Started with Console

Source: [owner-guide/getting-started/introduction](../../docs/owner-guide/getting-started/introduction.mdx). Current type: **E+H+T**. Action: **rewrite**, **P1**.

**Finding:** Starts with a long business explanation and covers registration, custom Harnesses, Red Team, Dome, and monitoring with multiple options.

**Change:** Use one sample Agent, one small baseline run, and status/report checks; state prerequisites, expected results, and cost. Make the remaining material Related tasks.

**Destination:** Agent Owner's Guide → Get Started → **Your First Evaluation in the Console [T]**; URL `/owner-guide/getting-started/introduction`.

**Single page goal:** Teach a first behavioral evaluation on a controlled example and how to read its result.

**Related content destinations:** N003. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P030 — Manage Teams

Source: [owner-guide/getting-started/teams](../../docs/owner-guide/getting-started/teams.mdx). Current type: **H+R**. Action: **keep**, **P1**.

**Finding:** Useful task steps; OWNER/ADMIN/MEMBER and SUPER ADMIN are not clearly distinguished; UI Delete is unimplemented.

**Change:** Keep the page, clarify global versus team roles using confirmed permissions, and retain the small role table required for the task.

**Destination:** Agent Owner's Guide → Teams and Agents → **Manage Teams [H]**; URL `/owner-guide/getting-started/teams`.

**Single page goal:** Create or select a team and assign appropriate access.

**Related content destinations:** N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P031 — Get Started with Discover

Source: [owner-guide/discover/introduction](../../docs/owner-guide/discover/introduction.mdx). Current type: **T+H**. Action: **refactor**, **P1**.

**Finding:** Broad installation and interface choices prevent a controlled tutorial; PR251 removes part of the CLI path.

**Change:** Use Console-only orchestration with an explicit installation handoff, one success check per phase, and links to focused tasks.

**Destination:** Agent Owner's Guide → Discover Agents → **Discover Agents in an Environment [H]**; URL `/owner-guide/discover/introduction`.

**Single page goal:** Move from a prepared Target to a reviewed first inventory.

**Related content destinations:** N024. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P032 — Create and Manage Targets

Source: [owner-guide/discover/targets](../../docs/owner-guide/discover/targets.mdx). Current type: **H+R**. Action: **refactor**, **P1**.

**Finding:** CLI tabs and commands remain in the exact PR251 head; dlp Targets have no Console creation path.

**Change:** Keep the Console steps; do not move CLI content into a new public reference. The dlp task requires a confirmed replacement or an explicitly identified temporary operator workflow.

**Destination:** Agent Owner's Guide → Discover Agents → **Create and Manage Targets [H]**; URL `/owner-guide/discover/targets`.

**Single page goal:** Manage scan scope, scanning, and scheduling in the Console.

## P033 — Install a Collector

Source: [owner-guide/discover/collectors](../../docs/owner-guide/discover/collectors.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** 417 lines cover root installation on three operating systems, Docker, Helm, AWS IAM, browser, and one-shot workflows; some CLI remains in PR251.

**Change:** AOG keeps selection and Console credential steps; four supported installation families move to ADG. Do not present browser/one-shot content as complete how-to guides while concrete steps are missing.

**Destination:** Agent Owner's Guide → Discover Agents → **Prepare Collector Installation [H]**; URL `/owner-guide/discover/collectors`.

**Single page goal:** Prepare the scope and credentials and hand installation to an administrator.

**Related content destinations:** N024. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P034 — Review Discovered Resources

Source: [owner-guide/discover/reviewing-resources](../../docs/owner-guide/discover/reviewing-resources.mdx). Current type: **H**. Action: **keep**, **P2**.

**Finding:** Already a focused Console how-to with useful empty-state guidance and a distinction between sightings and unique Resources.

**Change:** Keep the task and diagnostics; link definitions to Concepts and explicitly state what a successful review looks like.

**Destination:** Agent Owner's Guide → Discover Agents → **Review Discovered Resources [H]**; URL `/owner-guide/discover/reviewing-resources`.

**Single page goal:** Interpret inventory and investigate Uncertain findings and blind spots.

## P035 — Register a Discovered Agent

Source: [owner-guide/discover/registering-agents](../../docs/owner-guide/discover/registering-agents.mdx). Current type: **H+R**. Action: **refactor**, **P1**.

**Finding:** Useful register/activate sequence and eligibility rules; repeats the full lifecycle-stage table.

**Change:** Keep the two steps and operational restrictions; link stage definitions and registration fields to canonical locations.

**Destination:** Agent Owner's Guide → Discover Agents → **Register a Discovered Agent [H]**; URL `/owner-guide/discover/registering-agents`.

**Single page goal:** Convert an eligible Resource into an active registered Agent.

**Related content destinations:** N001,N011. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P036 — Scan Code Repositories

Source: [owner-guide/discover/code-scans](../../docs/owner-guide/discover/code-scans.mdx). Current type: **H**. Action: **keep**, **P2**.

**Finding:** Focused procedure with connection/repository selection and useful troubleshooting.

**Change:** Add explicit checks for GitHub access and results; link finding registration without repeating its procedure.

**Destination:** Agent Owner's Guide → Discover Agents → **Scan Code Repositories [H]**; URL `/owner-guide/discover/code-scans`.

**Single page goal:** Scan a GitHub repository through the Console and retrieve findings.

## P037 — What is an Agent

Source: [owner-guide/register-agents/what-is-an-agent](../../docs/owner-guide/register-agents/what-is-an-agent.mdx). Current type: **E**. Action: **move**, **P1**.

**Finding:** A general Agent explanation lives in AOG, although much of ADG links to it.

**Change:** Move to Concepts, focus on Vijil-relevant boundaries, and distinguish model/service/Collector/Agent. Redirect the old URL and update internal links.

**Destination:** Concepts → Platform → **What Is an Agent in Vijil [E]**; URL `/concepts/agents`.

**Single page goal:** Explain what Vijil registers, tests, and protects.

## P038 — Manage Agents

Source: [owner-guide/register-agents/registering-agents](../../docs/owner-guide/register-agents/registering-agents.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** The Console procedure shares a page with lengthy MCP setup, access-level reference, and lifecycle explanation; PR251 retains MCP CLI setup with a note.

**Change:** Keep the Console task; extract MCP setup, canonicalize access-level fields, and explain stages once. Confirm delete versus archive behavior.

**Destination:** Agent Owner's Guide → Teams and Agents → **Register and Manage Agents in the Console [H]**; URL `/owner-guide/register-agents/registering-agents`.

**Single page goal:** Connect an Agent endpoint to the registry and maintain its configuration.

**Related content destinations:** N001,N011,N020,N023. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P039 — Define Personas

Source: [owner-guide/simulate-environment/personas](../../docs/owner-guide/simulate-environment/personas.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Why Personas Matter, the intent taxonomy, registries, and design principles mix explanation with procedure.

**Change:** Keep preset/custom selection and creation verification; extract the Personas–Policies–Harnesses relationship, retaining brief values needed during entry.

**Destination:** Agent Owner's Guide → Prepare Evaluations → **Create Personas in the Console [H]**; URL `/owner-guide/simulate-environment/personas`.

**Single page goal:** Create and select Personas representing actual users and attackers.

**Related content destinations:** N002. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P040 — Define Policies

Source: [owner-guide/simulate-environment/policies](../../docs/owner-guide/simulate-environment/policies.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Explains the entire policy model, upload restrictions, and rule generation; UI/API categories differ, and activation depends on rules.

**Change:** Keep write/upload/activate steps and status verification; extract the shared model. Confirm formats, size limit, and activation conditions.

**Destination:** Agent Owner's Guide → Prepare Evaluations → **Create Policies in the Console [H]**; URL `/owner-guide/simulate-environment/policies`.

**Single page goal:** Turn organizational rules into an active evaluation Policy.

**Related content destinations:** N002,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P041 — Trust Score Harness

Source: [owner-guide/simulate-environment/harnesses/trust-score](../../docs/owner-guide/simulate-environment/harnesses/trust-score.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Duplicates the run workflow and complete Trust Report explanation; presents a 0–1 scale in Console instructions while other pages use 0–100.

**Change:** Keep only dimension selection and its consequences; link execution to P044, report review to P045, and semantics to Concepts.

**Destination:** Agent Owner's Guide → Prepare Evaluations → **Configure a Baseline Evaluation [H]**; URL `/owner-guide/simulate-environment/harnesses/trust-score`.

**Single page goal:** Select baseline dimensions in the Console.

**Related content destinations:** N003,N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P042 — Compliance Harnesses

Source: [owner-guide/simulate-environment/harnesses/compliance](../../docs/owner-guide/simulate-environment/harnesses/compliance.mdx). Current type: **E+H+R**. Action: **refactor**, **P1**.

**Finding:** The framework list is useful; the guide includes an MCP path and repeated score semantics.

**Change:** Keep the Console workflow and the distinction between testing and certification; move support catalogs into reference and link MCP to ADG.

**Destination:** Agent Owner's Guide → Prepare Evaluations → **Run a Compliance Evaluation [H]**; URL `/owner-guide/simulate-environment/harnesses/compliance`.

**Single page goal:** Run a Console evaluation with selected compliance Harnesses.

**Related content destinations:** N006,N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P043 — Custom Harnesses

Source: [owner-guide/simulate-environment/custom-harnesses](../../docs/owner-guide/simulate-environment/custom-harnesses.mdx). Current type: **H+R**. Action: **refactor**, **P1**.

**Finding:** Most of the page is an MCP CRUD catalog, while Console creation lacks a complete status/verification workflow.

**Change:** Keep Console creation and add waiting, failure, and immutability behavior; consolidate MCP examples into P061/P079.

**Destination:** Agent Owner's Guide → Prepare Evaluations → **Create a Custom Harness in the Console [H]**; URL `/owner-guide/simulate-environment/custom-harnesses`.

**Single page goal:** Generate a custom Harness and verify that it is ready for evaluation.

**Related content destinations:** N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P044 — Run Evaluations

Source: [owner-guide/run-evaluations/running-evaluations](../../docs/owner-guide/run-evaluations/running-evaluations.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Repeats Red Team launch/settings from P046, dimension definitions, and report tables.

**Change:** Keep prepared-Harness selection, start, monitoring, and retry diagnostics; replace Adaptive execution details with a link to P046. Confirm Verify/Tests naming.

**Destination:** Agent Owner's Guide → Evaluate Agents → **Run and Monitor an Evaluation in the Console [H]**; URL `/owner-guide/run-evaluations/running-evaluations`.

**Single page goal:** Start a behavioral run and verify its completion.

**Related content destinations:** N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P045 — Understand Results

Source: [owner-guide/run-evaluations/understanding-results](../../docs/owner-guide/run-evaluations/understanding-results.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Long copy of the Trust Score taxonomy and report anatomy; most Red Team results repeat P047 and much of P060.

**Change:** Keep Console drilldown and evidence-to-remediation work; consolidate Red Team content into P047 and shared interpretation into Concepts.

**Destination:** Agent Owner's Guide → Evaluate Agents → **Review Evaluation Results in the Console [H]**; URL `/owner-guide/run-evaluations/understanding-results`.

**Single page goal:** Open the Trust Report, find failed Probes, and select the next action.

**Related content destinations:** N003,N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P046 — Run a Red Team Campaign

Source: [owner-guide/red-team/running-campaigns](../../docs/owner-guide/red-team/running-campaigns.mdx). Current type: **E+H+R**. Action: **refactor**, **P0**.

**Finding:** Tests versus Verify and disabled versus hidden Adaptive tab behavior differ; advanced retry/rollback options differ from P044.

**Change:** Make this the single Console procedure; confirm exact UI names and parameters per deployment, and link general mechanics.

**Destination:** Agent Owner's Guide → Red Team → **Run a Red Team Evaluation in the Console [H]**; URL `/owner-guide/red-team/running-campaigns`.

**Single page goal:** Start an adaptive run with a controlled budget.

**Related content destinations:** N012,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P047 — Understand Red Team Results

Source: [owner-guide/red-team/understanding-results](../../docs/owner-guide/red-team/understanding-results.mdx). Current type: **H+R**. Action: **keep**, **P1**.

**Finding:** The most complete Console guide for waves and reports, including concrete statuses and download formats.

**Change:** Keep as the single Console source; remove duplicates in P045, reconcile lifecycle statuses, and add a programmatic counterpart.

**Destination:** Agent Owner's Guide → Red Team → **Review Red Team Results in the Console [H]**; URL `/owner-guide/red-team/understanding-results`.

**Single page goal:** Navigate from a run to transcripts, judgments, and the report.

**Related content destinations:** N012,N029. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P048 — Configure Guardrails

Source: [owner-guide/protect-in-production/configuring-guardrails](../../docs/owner-guide/protect-in-production/configuring-guardrails.mdx). Current type: **E+H+R**. Action: **refactor**, **P1**.

**Finding:** The task is useful but includes a catalog of types/Detector defaults and suggests reaching Protected stage after configuration.

**Change:** Keep Console steps and verification of actual enforcement; link detailed options to reference and clarify Save/Apply/deployment.

**Destination:** Agent Owner's Guide → Protect and Monitor → **Configure Guardrails in the Console [H]**; URL `/owner-guide/protect-in-production/configuring-guardrails`.

**Single page goal:** Edit, test, save, and apply a protection configuration.

**Related content destinations:** N013,N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P049 — Monitor Protection with Defend

Source: [owner-guide/protect-in-production/defend](../../docs/owner-guide/protect-in-production/defend.mdx). Current type: **H+R**. Action: **refactor**, **P0**.

**Finding:** Uses a different data source from Dome Metrics; requires a dlp Target created through a CLI command retained in PR251; explains sampled counters.

**Change:** Keep Defend and its scope; state verified prerequisites and link a supported DLP setup. Do not merge it with per-Agent metrics.

**Destination:** Agent Owner's Guide → Protect and Monitor → **Review Runtime Events in Defend [H]**; URL `/owner-guide/protect-in-production/defend`.

**Single page goal:** Investigate tenant/Target DLP events and their attribution.

## P050 — Deploy Dome

Source: [owner-guide/protect-in-production/deploying-dome](../../docs/owner-guide/protect-in-production/deploying-dome.mdx). Current type: **E+H**. Action: **rewrite**, **P1**.

**Finding:** The owner-facing Deploy Dome page shows Python integration and SDK configuration, although owners generally do not change code.

**Change:** Replace with an owner handoff checklist: Agent ID, configuration ID/version, acceptance criteria, test, and telemetry evidence; code stays in ADG.

**Destination:** Agent Owner's Guide → Protect and Monitor → **Hand Off Dome Deployment [H]**; URL `/owner-guide/protect-in-production/deploying-dome`.

**Single page goal:** Prepare deployment information for a developer and verify that protection is active.

**Related content destinations:** N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P051 — Monitor Dome Metrics

Source: [owner-guide/protect-in-production/observability](../../docs/owner-guide/protect-in-production/observability.mdx). Current type: **H+R**. Action: **keep**, **P2**.

**Finding:** Focused task with useful empty states and time-range guidance; its scope differs from Defend.

**Change:** Keep the steps; link the exact signal model to Concepts and instrumentation to ADG. Introduce Agent/configuration/version correlation.

**Destination:** Agent Owner's Guide → Protect and Monitor → **Investigate an Agent with Dome Metrics [H]**; URL `/owner-guide/protect-in-production/observability`.

**Single page goal:** Review per-Agent blocks, errors, latency, and trace links.

**Related content destinations:** N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P052 — Building Trusted Agents

Source: [developer-guide/getting-started/introduction](../../docs/developer-guide/getting-started/introduction.mdx). Current type: **E+landing**. Action: **refactor**, **P1**.

**Finding:** Introduction, lifecycle, and quickstart compete as entry points; PR251 removes CLI promotion but leaves REST status open.

**Change:** Create a short interface/workflow selector: SDK and MCP are primary, REST is secondary reference as confirmed by the user; add no new CLI paths.

**Destination:** Agent Developer's Guide → Get Started → **Choose a Developer Workflow [R]**; URL `/developer-guide/getting-started/introduction`.

**Single page goal:** Choose an SDK or MCP workflow and find the first tutorial.

**Related content destinations:** N018,N019,N020,N021. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P053 — Agent Lifecycle Workflow

Source: [developer-guide/getting-started/agent-lifecycle-workflow](../../docs/developer-guide/getting-started/agent-lifecycle-workflow.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** 505 lines repeat Console/SDK/plugin steps across the entire lifecycle; useful checkpoints and the CI example are buried.

**Change:** Keep an orchestration checklist with inputs, outputs, and links; extract lifecycle explanation, registration, CI gating, and Darwin into focused pages.

**Destination:** Agent Developer's Guide → Release and Improve → **Release an Evaluated Agent [H]**; URL `/developer-guide/getting-started/agent-lifecycle-workflow`.

**Single page goal:** Coordinate a verified release with evaluation, protection, and monitoring.

**Related content destinations:** N001,N022,N023,N033,N034. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P054 — Quickstart

Source: [developer-guide/agentic/quickstart](../../docs/developer-guide/agentic/quickstart.mdx). Current type: **T+H+R**. Action: **split**, **P1**.

**Finding:** Four tabbed paths and different packages make the workflow harder to follow unambiguously; PR251 removes only the CLI Setup link, not CLI tabs.

**Change:** Use one verifiable sample and one SDK path; move setup/mode alternatives into separate how-to guides and references. Preserve the URL and change title/description.

**Destination:** Agent Developer's Guide → Get Started → **Your First Evaluation with the Python SDK [T]**; URL `/developer-guide/agentic/quickstart`.

**Single page goal:** Teach one complete behavioral evaluation using the SDK.

**Related content destinations:** N019,N020,N021. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P055 — Claude Code

Source: [developer-guide/getting-started/claude-code-plugin](../../docs/developer-guide/getting-started/claude-code-plugin.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Useful page, but the command catalog and full lifecycle are mixed with setup.

**Change:** Keep installation, login, and one verification step; extract commands, side effects, and limitations into reference. /vijil plugin commands are not the retired Vijil CLI.

**Destination:** Agent Developer's Guide → Get Started → **Set Up the Claude Code Plugin [H]**; URL `/developer-guide/getting-started/claude-code-plugin`.

**Single page goal:** Install and connect the plugin and verify permissions and connectivity.

**Related content destinations:** N032. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P056 — Deploy Vijil

Source: [developer-guide/deploy-vijil/deploy-vijil-console](../../docs/developer-guide/deploy-vijil/deploy-vijil-console.mdx). Current type: **H+R+E**. Action: **split**, **P1**.

**Finding:** 1084 lines span VPC/RDS/IAM, Helm values, internal examples, Darwin, and bootstrap; the architecture diagram remains a raster image.

**Change:** Keep application installation/verification in the main runbook; extract AWS provisioning and the values contract. Clearly separate customer/Vijil steps and optional Darwin.

**Destination:** Agent Developer's Guide → Self-Hosting → **Deploy Vijil Console on AWS EKS [H]**; URL `/developer-guide/deploy-vijil/deploy-vijil-console`.

**Single page goal:** Install the Console on prepared supported infrastructure and verify operation.

**Related content destinations:** N030,N031. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P057 — Evaluation Overview

Source: [developer-guide/evaluate/overview](../../docs/developer-guide/evaluate/overview.mdx). Current type: **E+R+landing**. Action: **refactor**, **P1**.

**Finding:** Repeats Concepts and Harness lists; claims local cannot run Red Team while P059 distinguishes tunnels from no-tunnel local mode.

**Change:** Convert into a short input/output/compatibility table and link explanations. Reconcile preview status, _Small claims, and local modes with the contract.

**Destination:** Agent Developer's Guide → Evaluate Agents → **Choose an Evaluation Workflow [R]**; URL `/developer-guide/evaluate/overview`.

**Single page goal:** Choose behavioral/redteam and reachable/local workflows.

**Related content destinations:** N006,N012,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P058 — Run Evaluations

Source: [developer-guide/evaluate/running-evaluations](../../docs/developer-guide/evaluate/running-evaluations.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Mixes behavioral and Red Team artifacts, full REST examples, CRUD, and parameter reference; PR251 removes much of the CLI content.

**Change:** Keep the behavioral/compliance task with explicit polling and timeout; consolidate Red Team launch/evidence into P063/N029 and link all options to reference.

**Destination:** Agent Developer's Guide → Evaluate Agents → **Run and Monitor Evaluations [H]**; URL `/developer-guide/evaluate/running-evaluations`.

**Single page goal:** Start a behavioral or compliance evaluation through SDK/MCP and retrieve the result.

**Related content destinations:** N012,N029. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P059 — Local Agent Evaluation

Source: [developer-guide/evaluate/local-agent](../../docs/developer-guide/evaluate/local-agent.mdx). Current type: **H+T**. Action: **refactor**, **P1**.

**Finding:** The Market Researcher example is detailed but repeats the proxy in sections and a full file; a tunnel is not the same as no-tunnel local mode.

**Change:** Keep one complete versioned example as a supporting artifact; explain adapter points, teardown, and reuse. Explicitly distinguish both local paths and sample_size semantics.

**Destination:** Agent Developer's Guide → Evaluate Agents → **Evaluate an Agent Through a Local Tunnel [H]**; URL `/developer-guide/evaluate/local-agent`.

**Single page goal:** Temporarily make a local Agent reachable for evaluation.

**Related content destinations:** N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P060 — Understand Results

Source: [developer-guide/evaluate/understanding-results](../../docs/developer-guide/evaluate/understanding-results.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Repeats Console PDF anatomy and Trust Score explanations; the REST generation section lacks procedural steps and instead returns to dimensions.

**Change:** Create a programmatic evidence workflow with IDs, pagination, and report generation; move shared interpretation and score semantics into Concepts/the contract.

**Destination:** Agent Developer's Guide → Evaluate Agents → **Retrieve and Investigate Evaluation Results [H]**; URL `/developer-guide/evaluate/understanding-results`.

**Single page goal:** Retrieve SDK results and connect failed prompts to findings.

**Related content destinations:** N003,N012,N029. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P061 — Custom Harnesses

Source: [developer-guide/evaluate/custom-harnesses](../../docs/developer-guide/evaluate/custom-harnesses.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Starts with copied Console steps, followed by CLI/MCP/REST/SDK CRUD; private client._http serves as a workaround.

**Change:** Consolidate Console content into P043; keep SDK/MCP create→wait→inspect as one task; document workarounds only with a version and supported alternative. Confirm optional policy_ids.

**Destination:** Agent Developer's Guide → Prepare Evaluations → **Create a Custom Harness Programmatically [H]**; URL `/developer-guide/evaluate/custom-harnesses`.

**Single page goal:** Create a Harness from existing Personas/Policies and verify readiness.

**Related content destinations:** N002,N012. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P062 — Cloud Provider Integrations

Source: [developer-guide/evaluate/cloud-providers](../../docs/developer-guide/evaluate/cloud-providers.mdx). Current type: **H+R**. Action: **refactor**, **P1**.

**Finding:** The title promises a cloud-provider catalog, but the content actually describes an OpenAI-compatible endpoint and adapter; A2A appears elsewhere.

**Change:** Rename to match the actual purpose, explicitly map supported protocols by interface, and link registration.

**Destination:** Agent Developer's Guide → Teams and Agents → **Connect an Agent Endpoint [H]**; URL `/developer-guide/evaluate/cloud-providers`.

**Single page goal:** Prepare a compatible endpoint, adapter, and credentials.

**Related content destinations:** N011,N023. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P063 — Red Team Overview

Source: [developer-guide/red-team/overview](../../docs/developer-guide/red-team/overview.mdx). Current type: **E+H+R**. Action: **split**, **P0**.

**Finding:** Describes /v1/redteam/engagements and engagement_id, while SDK evaluate uses evaluation_id and OpenAPI has campaigns; PR251 retains a persona/policy CLI block.

**Change:** Choose a confirmed public SDK/MCP workflow; document ID adapters/aliases if they exist without inventing equivalence. Extract results and replace the remaining CLI example once a replacement is confirmed.

**Destination:** Agent Developer's Guide → Red Team → **Run a Red Team Evaluation Programmatically [H]**; URL `/developer-guide/red-team/overview`.

**Single page goal:** Start adaptive testing and retain its tracking identifier.

**Related content destinations:** N012,N029. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P064 — Protection Overview

Source: [developer-guide/protect/overview](../../docs/developer-guide/protect/overview.mdx). Current type: **E+R+landing**. Action: **split**, **P1**.

**Finding:** 193 lines repeat Concepts, ScanResult, and configuration reference; the Controls Engine is missing from the main chooser table.

**Change:** Keep a short capability/entry-point table; extract mechanisms and complete models, with scope/version links and streaming limitations.

**Destination:** Agent Developer's Guide → Protect Agents → **Choose a Protection Interface [R]**; URL `/developer-guide/protect/overview`.

**Single page goal:** Find the appropriate protection interface and supported framework.

**Related content destinations:** N004,N005,N013,N014,N016,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P065 — Install Dome

Source: [developer-guide/protect/installation](../../docs/developer-guide/protect/installation.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Useful extras table, but initial verification uses default local models and PII requiring additional extras; the environment catalog is mixed with the procedure.

**Change:** Define verifiable minimal and default/full paths; move complete extras/environment tables into reference and link the exact tested version.

**Destination:** Agent Developer's Guide → Protect Agents → **Install Dome [H]**; URL `/developer-guide/protect/installation`.

**Single page goal:** Install the minimum required dependencies and verify one scan.

**Related content destinations:** N013,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P066 — Controls Engine

Source: [developer-guide/protect/control-engine](../../docs/developer-guide/protect/control-engine.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** Roughly half the page consists of complete model, scope, selector, and evaluator tables already present in the Controls API reference.

**Change:** Keep one representative protect→test→enforce workflow and shadow→enforce procedure; extract explanation and consolidate full specifications into P080.

**Destination:** Agent Developer's Guide → Protect Agents → **Enforce a Policy with the Controls Engine [H]**; URL `/developer-guide/protect/control-engine`.

**Single page goal:** Apply a declarative policy to one concrete tool/LLM workflow.

**Related content destinations:** N004,P080. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P067 — Trust Runtime

Source: [developer-guide/protect/trust-runtime](../../docs/developer-guide/protect/trust-runtime.mdx). Current type: **E+H+R**. Action: **split**, **P1**.

**Finding:** 421 lines mix the identity model, multiple framework examples, constraint precedence, manifests, heartbeats, and full API behavior.

**Change:** Keep one supported integration path, essential failure conditions, and verification; extract the model and full contract. Do not restore Manifest CLI navigation.

**Destination:** Agent Developer's Guide → Protect Agents → **Secure an Agent with Trust Runtime [H]**; URL `/developer-guide/protect/trust-runtime`.

**Single page goal:** Enable a configured identity-aware runtime and verify enforcement boundaries.

**Related content destinations:** N005,N015,N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P068 — Configure Guardrails

Source: [developer-guide/protect/configuring-guardrails](../../docs/developer-guide/protect/configuring-guardrails.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Most of the page lists every option/default, which is reference material, while the title promises a task.

**Change:** Keep a minimal dict/TOML task, test, shadow/enforce decision, and Console loading path; extract the complete key list into reference.

**Destination:** Agent Developer's Guide → Protect Agents → **Configure Guardrails in Code [H]**; URL `/developer-guide/protect/configuring-guardrails`.

**Single page goal:** Create, load, and test a protection configuration.

**Related content destinations:** N013,N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P069 — Use Guardrails

Source: [developer-guide/protect/using-guardrails](../../docs/developer-guide/protect/using-guardrails.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Useful integration pattern, but the complete ScanResult table duplicates P064/P024; streaming, batches, and notebooks have different needs.

**Change:** Keep one integration lifecycle with explicit detection/enforcement and redaction; clearly label variants and link models to reference.

**Destination:** Agent Developer's Guide → Protect Agents → **Apply Guardrails in an Agent [H]**; URL `/developer-guide/protect/using-guardrails`.

**Single page goal:** Place input/output checks in an application and enforce their results.

**Related content destinations:** N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P070 — Custom Detectors

Source: [developer-guide/protect/custom-detectors](../../docs/developer-guide/protect/custom-detectors.mdx). Current type: **H+R**. Action: **refactor**, **P1**.

**Finding:** Useful modern contract with async detect and a tuple result; conflicts with the example in P026.

**Change:** Keep as the single custom Detector procedure, add safe/unsafe-input and failure checks, and link the full protocol to reference.

**Destination:** Agent Developer's Guide → Protect Agents → **Build a Custom Runtime Detector [H]**; URL `/developer-guide/protect/custom-detectors`.

**Single page goal:** Register a DetectionMethod and demonstrate that a configuration uses it.

**Related content destinations:** N014. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P071 — Detection Methods

Source: [developer-guide/protect/detection-methods](../../docs/developer-guide/protect/detection-methods.mdx). Current type: **R**. Action: **keep**, **P1**.

**Finding:** The most complete catalog; claims 36 methods and documents extras, scores, and failure behavior; parts are duplicated in Concepts.

**Change:** Move into Reference through navigation only, preserving the URL; make this the single runtime catalog. Confirm registry/version and add a category index and stable ID anchors.

**Destination:** Agent Developer's Guide → Reference → Runtime Protection → **Runtime Detector Reference [R]**; URL `/developer-guide/protect/detection-methods`.

**Single page goal:** Find a supported Detector, dependency, parameter, and routing option.

## P072 — Observability

Source: [developer-guide/protect/observability](../../docs/developer-guide/protect/observability.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Modern examples differ from P027; metric names and schema fields are lookup material.

**Change:** Keep providers→instrument→emit→verify steps; link metric/audit schemas to canonical reference and distinguish a Controls span from a full Agent trace.

**Destination:** Agent Developer's Guide → Protect Agents → **Instrument Runtime Protection [H]**; URL `/developer-guide/protect/observability`.

**Single page goal:** Connect Dome/Controls to an OTel backend and demonstrate signal delivery.

**Related content destinations:** N014,N015. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P073 — Google ADK

Source: [developer-guide/protect/integrations/adk](../../docs/developer-guide/protect/integrations/adk.mdx). Current type: **H+R**. Action: **keep**, **P2**.

**Finding:** Focused procedure with Cloud Run requirements and concrete limitations; some arguments and version details are reference material.

**Change:** Keep the example, confirm the version combination, add success/blocked tests, and clarify callback scope; preserve Cloud Run and async limitations.

**Destination:** Agent Developer's Guide → Protect Agents → Framework Integrations → **Protect a Google ADK Agent [H]**; URL `/developer-guide/protect/integrations/adk`.

**Single page goal:** Integrate callbacks or a supported secure_agent adapter.

**Related content destinations:** N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P074 — LangGraph

Source: [developer-guide/protect/integrations/langgraph](../../docs/developer-guide/protect/integrations/langgraph.mdx). Current type: **H+R**. Action: **keep**, **P1**.

**Finding:** Already explains best-effort tool discovery and that a delivered streaming chunk cannot be retracted.

**Change:** Keep these limits next to the example and verify that the returned SecureGraph is used. Link the full signature to reference.

**Destination:** Agent Developer's Guide → Protect Agents → Framework Integrations → **Protect a LangGraph Agent [H]**; URL `/developer-guide/protect/integrations/langgraph`.

**Single page goal:** Integrate protection and verify supported enforcement points.

**Related content destinations:** N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P075 — Strands

Source: [developer-guide/protect/integrations/strands](../../docs/developer-guide/protect/integrations/strands.mdx). Current type: **H+R**. Action: **keep**, **P2**.

**Finding:** Useful short guide; distinguishes content hooks from trust hooks and replaces messages rather than raising exceptions.

**Change:** Keep the behavior with a versioned runnable example; distinguish telemetry identifiers from cryptographically attested identity.

**Destination:** Agent Developer's Guide → Protect Agents → Framework Integrations → **Protect a Strands Agent [H]**; URL `/developer-guide/protect/integrations/strands`.

**Single page goal:** Enable a hook provider and verify input/output decisions.

**Related content destinations:** N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P076 — LangChain

Source: [developer-guide/protect/integrations/langchain](../../docs/developer-guide/protect/integrations/langchain.mdx). Current type: **H+R**. Action: **keep**, **P2**.

**Finding:** Clearly shows how ordinary chain composition can send the blocked message to the model and why RunnableBranch is needed.

**Change:** Make the branching example primary; define the actual dictionary result versus ScanResult in reference and test safe/blocked branches.

**Destination:** Agent Developer's Guide → Protect Agents → Framework Integrations → **Protect a LangChain Workflow [H]**; URL `/developer-guide/protect/integrations/langchain`.

**Single page goal:** Connect GuardrailRunnable and branch execution when content is blocked.

**Related content destinations:** N014,N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P077 — MCP Servers

Source: [developer-guide/protect/integrations/mcp](../../docs/developer-guide/protect/integrations/mcp.mdx). Current type: **H+R**. Action: **split**, **P1**.

**Finding:** Useful explanation of reversed input/output directions; constructor options are reference material. MCP may also mean the Vijil management server.

**Change:** Keep the proxy procedure and explicit distinction between both MCP uses; extract constructor/results contracts and add evidence of a blocked tool call.

**Destination:** Agent Developer's Guide → Protect Agents → Framework Integrations → **Protect an MCP Server [H]**; URL `/developer-guide/protect/integrations/mcp`.

**Single page goal:** Deploy a DomedMCPServer proxy and verify both protection directions.

**Related content destinations:** N014,N016. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P078 — Use Dome as a Containerized Deployment

Source: [tutorials/protect-agents/dome-containerized-deployment](../../docs/tutorials/protect-agents/dome-containerized-deployment.mdx). Current type: **H+R**. Action: **move+split**, **P1**.

**Finding:** The page in the tutorials folder is actually a deployment how-to plus complete HTTP/Bedrock/OTel reference; 567 lines.

**Change:** Move into ADG Self-Hosting; keep image/configuration/run/health/task steps, extract HTTP/Bedrock schemas, and link telemetry to P072. Provide a redirect.

**Destination:** Agent Developer's Guide → Self-Hosting → **Deploy Dome as a Service [H]**; URL `/developer-guide/deploy-vijil/dome-service`.

**Single page goal:** Start a Dome container and verify an input/output request.

**Related content destinations:** N017. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P079 — Use MCP Tools

Source: [developer-guide/agentic/tools](../../docs/developer-guide/agentic/tools.mdx). Current type: **R**. Action: **refactor**, **P1**.

**Finding:** Use MCP Tools sounds procedural, but the content is a catalog; eval_* and redteam_* represent different workflows, and mutating tools exist.

**Change:** Keep the canonical catalog with server version, tool IDs, required/default values, outputs, pagination, terminal states, and side effects; link how-to guides without repeating login setup.

**Destination:** Agent Developer's Guide → Reference → MCP and Plugin → **MCP Tool Reference [R]**; URL `/developer-guide/agentic/tools`.

**Single page goal:** Find available tools, arguments, and call side effects.

**Related content destinations:** N020,N032. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P080 — Controls API Reference

Source: [developer-guide/reference/controls-api](../../docs/developer-guide/reference/controls-api.mdx). Current type: **R**. Action: **keep**, **P1**.

**Finding:** Strong reference foundation, including signatures, exceptions, missing selectors, and aggregate decisions.

**Change:** Keep as the single Controls specification; align with the release and remove duplicate full tables from P066. Distinguish Controls API from Console REST API.

**Destination:** Agent Developer's Guide → Reference → Runtime Protection → **Controls API Reference [R]**; URL `/developer-guide/reference/controls-api`.

**Single page goal:** Reliably look up public classes, models, evaluators, and failure semantics.

**Related content destinations:** N004. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P081 — Setup

Source: [developer-guide/cli/setup](../../docs/developer-guide/cli/setup.mdx). Current type: **R+H**. Action: **retire-by-251**, **P0**.

**Finding:** The CLI setup page is removed in PR251; its old options remain audit evidence only.

**Change:** Do not migrate or recreate CLI reference. Describe setup genuinely required by SDK/MCP in the corresponding how-to with the confirmed package.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N019,N020,N021. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P082 — Discover Resources

Source: [developer-guide/cli/discover](../../docs/developer-guide/cli/discover.mdx). Current type: **R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the CLI catalog; some Discover tasks still depend on CLI commands elsewhere.

**Change:** Do not restore the catalog. Confirm a Console/SDK/MCP or supported operator alternative for each remaining task before removing its only working procedure.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

## P083 — Manage Agents

Source: [developer-guide/cli/agents](../../docs/developer-guide/cli/agents.mdx). Current type: **R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the Agent command catalog; actual management tasks remain.

**Change:** Cover tasks in AOG and the programmatic registration how-to, using SDK/MCP references and explicit archive semantics.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N023. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P084 — Evaluate Agents

Source: [developer-guide/cli/evaluate](../../docs/developer-guide/cli/evaluate.mdx). Current type: **H+R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the SDK CLI evaluation/how-to reference.

**Change:** Implement the proposed CI gate with the Python SDK; add no new terminal evaluation path. Review old links and direct them to the corresponding task.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N022. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P085 — Protect Agents

Source: [developer-guide/cli/protect](../../docs/developer-guide/cli/protect.mdx). Current type: **R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the Dome command catalog; Console and SDK configuration remain supported paths.

**Change:** Do not migrate command tables. Maintain configuration-contract options in Dome reference and tasks in AOG/ADG.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N013. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P086 — Red Team

Source: [developer-guide/cli/red-team](../../docs/developer-guide/cli/red-team.mdx). Current type: **H+R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the page containing two command families; these are not proof that the backend APIs are equivalent.

**Change:** Do not recreate the page; confirm the evaluation/engagement relationship and document only the selected public SDK/MCP workflow.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N012,N029. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P087 — Telemetry

Source: [developer-guide/cli/telemetry](../../docs/developer-guide/cli/telemetry.mdx). Current type: **R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes the telemetry catalog; Defend and Dome Metrics still use different data sources.

**Change:** Retain telemetry access through confirmed SDK/MCP capabilities; do not invent replacements for unsupported endpoints.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

## P088 — Manifest CLI

Source: [developer-guide/cli/manifest](../../docs/developer-guide/cli/manifest.mdx). Current type: **R**. Action: **retire-by-251**, **P0**.

**Finding:** PR251 removes Manifest command reference; some Trust Runtime workflows still require a signed manifest.

**Change:** Confirm a supported creation/signing/verification method in the Trust Runtime guide or state an explicit operator prerequisite. Add no new public CLI reference.

**Destination:** removed from the public TOC, without a replacement CLI reference. Map legacy entry URLs only to semantically appropriate active tasks or an explicit retirement notice.

**Related content destinations:** N015. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P089 — Setup

Source: [developer-guide/sdk/setup](../../docs/developer-guide/sdk/setup.mdx). Current type: **H+R**. Action: **split**, **P0**.

**Finding:** Setup is a generic title; states Python 3.12+ while quickstart and local pyproject use >=3.11,<3.14; PR251 retains ancillary auth/config commands.

**Change:** Keep complete rules and version scope in reference; move installation and the first authenticated request to a how-to. Confirm the published release rather than assuming the local manifest describes the live package.

**Destination:** Agent Developer's Guide → Reference → Python SDK → **Python SDK Configuration Reference [R]**; URL `/developer-guide/sdk/setup`.

**Single page goal:** Look up constructor, credential/gateway precedence, aliases, and refresh behavior.

**Related content destinations:** N019,N021. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P090 — Lifecycle Methods

Source: [developer-guide/sdk/lifecycle-methods](../../docs/developer-guide/sdk/lifecycle-methods.mdx). Current type: **R**. Action: **refactor**, **P0**.

**Finding:** Includes deploy/evolve/discover; the lifecycle workflow says the platform does not deploy applications, and Darwin Concepts says in development.

**Change:** Keep existing methods with precise capability/version labels, limits, and explicit unavailable outcomes; do not turn the existence of a model into a production guarantee.

**Destination:** Agent Developer's Guide → Reference → Python SDK → **Python SDK Lifecycle Methods [R]**; URL `/developer-guide/sdk/lifecycle-methods`.

**Single page goal:** Look up public methods, arguments, return types, and availability.

**Related content destinations:** N018,N033,N034. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P091 — Resources

Source: [developer-guide/sdk/resources](../../docs/developer-guide/sdk/resources.mdx). Current type: **R**. Action: **refactor**, **P1**.

**Finding:** The index lists delete while the text prefers archive; some methods are missing from the index. monitor.summary/detections are explicitly unimplemented.

**Change:** Align the index with public methods, retain unavailable labels and public import paths, and fix the trailing-slash Page[T] link.

**Destination:** Agent Developer's Guide → Reference → Python SDK → **Python SDK Resources [R]**; URL `/developer-guide/sdk/resources`.

**Single page goal:** Look up resource methods and their contracts.

**Related content destinations:** N012,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## P092 — Models and Errors

Source: [developer-guide/sdk/models-errors](../../docs/developer-guide/sdk/models-errors.mdx). Current type: **R**. Action: **refactor**, **P1**.

**Finding:** EvaluationResponse is defined twice; some models exist only for future capabilities, and the poller may return a failed model without raising an exception.

**Change:** Remove the duplicate definition, distinguish method failure from a failed terminal model, document exact retry semantics, and stabilize anchors.

**Destination:** Agent Developer's Guide → Reference → Python SDK → **Python SDK Models and Errors [R]**; URL `/developer-guide/sdk/models-errors`.

**Single page goal:** Look up models, errors, retries, and terminal-status behavior.

**Related content destinations:** N012,N018. N-IDs are specified in the registry below; P-IDs identify existing pages in this document.

## Generated REST API Reference

The TOC also includes an OpenAPI group, which is not a single MDX page. Each of the 149 operations across 112 paths has its own row in [api-operation-inventory.csv](api-operation-inventory.csv). The audit covers Reference classification, navigation, aliases, operation IDs, tags, and differences from guides; backend calls and every individual response field have not been verified through execution. Detailed diagnostics are in evidence-and-dejan.md.

## Registry of All Proposed New Pages

### N001 — The Agent Trust Lifecycle [E]

**Placement:** Concepts → Platform. URL `/concepts/agent-lifecycle`. Priority **P1**. Sources: P001,P035,P038,P053.

**Content:** One model of Discover→Register→Evaluate→Protect→Improve→Release→Monitor; distinguish activities from registry stages Registered/Tested/Protected/Adapted.

**Acceptance criteria:** Mermaid and text explain the different concepts; definitions are no longer copied across guides.

### N002 — Personas, Policies, and Evaluation Context [E]

**Placement:** Concepts → Trust and Evaluation. URL `/concepts/evaluation-context`. Priority **P1**. Sources: P039,P040,P061.

**Content:** How Personas and Policies shape Harness generation and Red Team context; an evaluation Policy is not automatically a runtime Control or an RL Policy.

**Acceptance criteria:** One example connects context to a test; AOG and ADG link here instead of repeating Why sections.

### N003 — Interpret Evaluation Evidence [E]

**Placement:** Concepts → Trust and Evaluation. URL `/concepts/evaluation-evidence`. Priority **P1**. Sources: P002,P007,P041,P045,P060.

**Content:** Trust Score, severity, coverage, reports, and behavioral/Red Team evidence; requirements for comparing runs and why a result is not a guarantee.

**Acceptance criteria:** No UI clicking instructions or API syntax; the same finding links to Console and programmatic investigation guides.

### N004 — How the Controls Engine Works [E]

**Placement:** Concepts → Runtime Defense. URL `/concepts/defense/controls-engine`. Priority **P1**. Sources: P005,P023,P066,P080.

**Content:** Step→Scope→Selector→Evaluator→Action; the relationship between VijilDome, Dome, ControlEngine, and TrustRuntime without treating them as aliases.

**Acceptance criteria:** A diagram and one example explain allow/deny/steer/observe; full signatures stay in P080.

### N005 — How Trust Runtime Works [E]

**Placement:** Concepts → Runtime Defense. URL `/concepts/defense/trust-runtime`. Priority **P1**. Sources: P005,P023,P067.

**Content:** Identity versus Agent ID, constraints, tool MAC, attestation, audit, and heartbeats; boundaries of in-process enforcement and framework integration.

**Acceptance criteria:** Clearly states when identity is attested and what is outside coverage; links integration and API reference.

### N006 — Evaluation Harness Reference [R]

**Placement:** Agent Developer's Guide → Reference → Evaluation Catalogs. URL `/developer-guide/reference/evaluation/harnesses`. Priority **P1**. Sources: P017,P041,P042,P057.

**Content:** A versioned catalog of standard/custom/compliance/benchmark Harnesses: public ID/alias, type, availability, coverage, and output/report support.

**Acceptance criteria:** Every previous lookup item has a destination; the catalog does not claim all unless its source covers everything. Namespaces and short aliases are mapped explicitly.

### N007 — Evaluation Scenario Reference [R]

**Placement:** Agent Developer's Guide → Reference → Evaluation Catalogs. URL `/developer-guide/reference/evaluation/scenarios`. Priority **P1**. Sources: P018.

**Content:** One catalog of Scenario IDs, descriptions, Harness membership, and old/new taxonomy mappings.

**Acceptance criteria:** Each entry has a visible stable ID; the domain owner resolves inconsistent legacy sections before publication.

### N008 — Evaluation Probe Reference [R]

**Placement:** Agent Developer's Guide → Reference → Evaluation Catalogs. URL `/developer-guide/reference/evaluation/probes`. Priority **P1**. Sources: P019.

**Content:** Probe ID, test description, prompt collection, Scenarios, and Detectors; distinguish a Probe definition from an executed prompt.

**Acceptance criteria:** Every existing row is transferred or explicitly marked retired; prose and JSON/CSV come from the same versioned source where one exists.

### N009 — Evaluation Detector Reference [R]

**Placement:** Agent Developer's Guide → Reference → Evaluation Catalogs. URL `/developer-guide/reference/evaluation/detectors`. Priority **P1**. Sources: P020.

**Content:** Evaluation Detector IDs, inputs, results, and Probe mappings; explicitly separate from the runtime registry.

**Acceptance criteria:** Does not claim all evaluation Detectors live within runtime Guards; shared implementations are identified individually.

### N010 — Evaluation Coverage by Dimension [R]

**Placement:** Agent Developer's Guide → Reference → Evaluation Catalogs. URL `/developer-guide/reference/evaluation/coverage`. Priority **P1**. Sources: P008,P009,P010.

**Content:** Dimension→Scenario→Probe→Detector mapping replacing the three hover catalogs; Reliability, Safety, and Security sections.

**Acceptance criteria:** IDs are ordinary readable text in both HTML and Markdown; there are no three independently maintained copies of the full Probe catalog.

### N011 — Agent Registration Contract [R]

**Placement:** Agent Developer's Guide → Reference → Platform Contracts. URL `/developer-guide/reference/agent-registration`. Priority **P1**. Sources: P014,P035,P038,P062.

**Content:** Fields, protocols, access levels, lifecycle/status distinctions, required values, secrets handling, and archive/delete semantics per interface.

**Acceptance criteria:** The supported UI/SDK/MCP/REST naming table distinguishes endpoint registration from source import and invents no equivalences.

### N012 — Evaluation Contracts and Results [R]

**Placement:** Agent Developer's Guide → Reference → Platform Contracts. URL `/developer-guide/reference/evaluation-contracts`. Priority **P0**. Sources: P007,P022,P041,P046,P047,P057,P058,P059,P060,P063,P090,P092.

**Content:** Scales and units; sample_size units; Harness IDs; evaluation_id/engagement_id/campaign_id; statuses and terminal outcomes; report readiness, pagination, and error contracts by mode/interface.

**Acceptance criteria:** The domain owner confirms differences; behavioral and Red Team examples cover success, failure, and timeout; no future endpoint is presented as available.

### N013 — Dome Configuration Reference [R]

**Placement:** Agent Developer's Guide → Reference → Runtime Protection. URL `/developer-guide/reference/dome-configuration`. Priority **P1**. Sources: P024,P048,P065,P068.

**Content:** DomeConfig, Guard/Guardrail/Detector keys, defaults, configuration sources/precedence, extras, environment variables, on-error, and the Console-supported subset.

**Acceptance criteria:** Every field has type/default/scope/version; the extracted installation task and how-to guides link to the canonical table.

### N014 — Dome Results and Telemetry Reference [R]

**Placement:** Agent Developer's Guide → Reference → Runtime Protection. URL `/developer-guide/reference/dome-results`. Priority **P0**. Sources: P024,P026,P027,P064,P069,P070,P072,P076.

**Content:** ScanResult, BatchScanResult, DomePayload, DetectionMethod protocol, framework result differences, actual metric units, and signal fields.

**Acceptance criteria:** Distinguishes flagged/enforced/sanitized and seconds/milliseconds; examples are checked against the release rather than legacy pseudo APIs.

### N015 — Trust Runtime API Reference [R]

**Placement:** Agent Developer's Guide → Reference → Runtime Protection. URL `/developer-guide/reference/trust-runtime`. Priority **P1**. Sources: P067,P088.

**Content:** secure_agent/TrustRuntime signatures, constraint schema/precedence, identity and tool decisions, manifests, audit events, heartbeats, and failure modes.

**Acceptance criteria:** Manifest signing/verification has a confirmed supported procedure or a clear operator prerequisite; the retired CLI reference is not reconstructed.

### N016 — Framework Integration Reference [R]

**Placement:** Agent Developer's Guide → Reference → Runtime Protection. URL `/developer-guide/reference/framework-integrations`. Priority **P2**. Sources: P073,P074,P075,P076,P077.

**Content:** Version and support-scope matrix; callback/hook/proxy signatures, results, and blocking behavior; streaming and tool-enforcement limits.

**Acceptance criteria:** All five existing integrations distinguish content scanning from identity-aware enforcement; how-to examples do not maintain duplicate full tables.

### N017 — Dome Service HTTP API Reference [R]

**Placement:** Agent Developer's Guide → Reference → Runtime Protection. URL `/developer-guide/reference/dome-service-api`. Priority **P1**. Sources: P078.

**Content:** Health/configuration/input/output/batch HTTP contracts; authentication, response schemas, Bedrock compatibility, and container telemetry settings.

**Acceptance criteria:** Identifies this as the Dome service API, distinct from Console REST API and Controls Python API; documented compatibility does not promise an identical Bedrock contract.

### N018 — Platform Versions and Capability Availability [R]

**Placement:** Agent Developer's Guide → Reference → Platform Contracts. URL `/developer-guide/reference/platform-capabilities`. Priority **P0**. Sources: P006,P030,P052,P057,P064,P065,P089,P090,P091,P092.

**Content:** A small confirmed matrix of versions, deployment feature flags, preview/GA/unsupported status, public interfaces, and compatible combinations.

**Acceptance criteria:** Each status has a release/source owner and verification date; documentation does not infer availability from the existence of an SDK method or Pydantic model.

### N019 — Authenticate to Vijil [H]

**Placement:** Agent Developer's Guide → Get Started. URL `/developer-guide/getting-started/authentication`. Priority **P1**. Sources: P038,P054,P055,P089.

**Content:** Obtain and verify SDK/MCP credentials, team, and gateway settings; terminal helpers only where they are a supported necessity, not a third workflow.

**Acceptance criteria:** One successful read verifies identity and team; credential differences and refresh limits link to SDK/REST reference.

### N020 — Connect the Vijil MCP Server [H]

**Placement:** Agent Developer's Guide → Get Started. URL `/developer-guide/getting-started/connect-mcp`. Priority **P1**. Sources: P029,P038,P043,P054,P055,P079.

**Content:** Connect the standalone MCP server to a client; clearly distinguish it from Claude Code plugin installation and the Dome MCP protection proxy.

**Acceptance criteria:** vijil_status and one read-only call work; the machine-readable description requires no CLI evaluation tab.

### N021 — Install and Configure the Python SDK [H]

**Placement:** Agent Developer's Guide → Get Started. URL `/developer-guide/getting-started/python-sdk`. Priority **P1**. Sources: P054,P089.

**Content:** Choose a confirmed Python/package version, install, authenticate, select gateway/team, and perform one read.

**Acceptance criteria:** All prerequisites are explicit; full credential precedence exists only in reference. Reuse an existing non-TOC file only after separately reviewing its contents.

### N022 — Gate a Release on Evaluation Evidence [H]

**Placement:** Agent Developer's Guide → Release and Improve. URL `/developer-guide/evaluate/ci-cd`. Priority **P1**. Sources: P053,P084.

**Content:** Python SDK CI gate: start/poll/timeout, inspect status, available score and relevant findings, retain evaluation ID/report, and set the exit code.

**Acceptance criteria:** failed/cancelled/degraded/missing score cannot pass; the threshold has an explicit scale and policy owner; it does not use another run's latest score.

### N023 — Register an Agent Programmatically [H]

**Placement:** Agent Developer's Guide → Teams and Agents. URL `/developer-guide/agents/register`. Priority **P1**. Sources: P038,P053,P054,P062,P083.

**Content:** SDK/MCP endpoint registration→verify→save Agent ID, with separate links to source import and protocol compatibility.

**Acceptance criteria:** The example does not treat client.register(path) as an alias for endpoint creation; the saved ID leads into evaluation.

### N024 — Install a Collector [H]

**Placement:** Agent Developer's Guide → Discover Agents. URL `/developer-guide/discover/collectors`. Priority **P1**. Sources: P033.

**Content:** One complete Collector installation how-to with shared artifact access, network requirements, Target/credential prerequisites, verification, troubleshooting, upgrades, and revocation. Start with a short variant selector and stable heading anchors. Keep Endpoint (macOS/Linux/Windows), Network scanner, Kubernetes, and AWS Cloud API instructions as sections of this page. Retain browser and one-shot coverage with explicit support limitations. Link back to the existing owner discovery workflow rather than duplicating Console Target creation and inventory review.

**Acceptance criteria:** Each variant names its required artifacts, privileges, credentials, supported environment, enrollment evidence, logs, and failure checks. Endpoint coverage includes WSL limitations and re-enrollment. Network scanning covers routing, daemon mode, and container capabilities. Kubernetes covers RBAC and secret references. AWS covers its confirmed IAM/OIDC setup and whether an LLM key is required. Maintain common setup once; distinguish a running service from successful enrollment. Resolve remaining CLI dependencies only through confirmed supported paths. Split a variant later only when an independent workflow becomes difficult to use or maintain here.

### N029 — Retrieve and Investigate Red Team Evidence [H]

**Placement:** Agent Developer's Guide → Red Team. URL `/developer-guide/red-team/understanding-results`. Priority **P1**. Sources: P047,P058,P060,P063,P086.

**Content:** From SDK/MCP evaluation ID to status, wave/seed artifacts, transcripts, judgments, and reports; inspect degraded outcomes and use bounded polling.

**Acceptance criteria:** The example uses the same confirmed ID flow as launch; reference defines enums/options, while Concepts explains evidence.

### N030 — Prepare AWS Infrastructure for Vijil [H]

**Placement:** Agent Developer's Guide → Self-Hosting. URL `/developer-guide/deploy-vijil/aws-infrastructure`. Priority **P2**. Sources: P056.

**Content:** VPC/EKS/RDS/S3/DNS/IAM prerequisites and the exact provisioning outcome, with clear customer/Vijil responsibilities.

**Acceptance criteria:** Separate from application Helm installation; copied commands do not depend on an unexplained private checkout or internal staging account.

### N031 — Self-Hosted Configuration Reference [R]

**Placement:** Agent Developer's Guide → Reference → Self-Hosting. URL `/developer-guide/reference/self-hosted-configuration`. Priority **P1**. Sources: P056.

**Content:** Chart values, secrets, environment variables, infrastructure/version compatibility, feature flags, optional Darwin dependency, and required resources.

**Acceptance criteria:** Defaults and security-sensitive examples state their scope; customer values do not use unexplained internal staging values; release version is specified.

### N032 — Claude Code Plugin Command Reference [R]

**Placement:** Agent Developer's Guide → Reference → MCP and Plugin. URL `/developer-guide/reference/claude-code-commands`. Priority **P1**. Sources: P055.

**Content:** /vijil commands, arguments, prerequisites, output, weekly allowance, and side effects; clearly identify commands that only propose changes.

**Acceptance criteria:** Plugin commands, MCP tools, and shell commands have distinct identifiers; supported plugin commands are not removed with the CLI reference.

### N033 — Review and Apply an Adaptation Proposal [H]

**Placement:** Agent Owner's Guide → Improve Agents. URL `/owner-guide/improve-agents/review-proposals`. Priority **P2**. Sources: P006,P053,P090,P091.

**Content:** Owner Console review: inspect evidence/diff, approve/reject/apply, re-evaluate, and roll back, only for a confirmed available Darwin workflow.

**Acceptance criteria:** Product confirms UI behavior and approve versus apply semantics; a generic model or specification endpoint is insufficient for publication.

**Publication condition:** Confirm an enabled/released Darwin workflow; until then, keep this in the backlog with status described in Concepts.

### N034 — Adapt an Agent and Validate the Proposal [H]

**Placement:** Agent Developer's Guide → Release and Improve. URL `/developer-guide/improve-agents/adapt`. Priority **P2**. Sources: P006,P053,P090,P091.

**Content:** SDK adapt→job status→proposal diff→review/apply→re-evaluate; distinguish corrective adaptation from generative evolve and application deployment.

**Acceptance criteria:** Job failure and proposal rejection are covered; permissions, version, and supported backend are confirmed; there is no promise that the platform automatically deploys the application.

**Publication condition:** Confirm an enabled/released Darwin workflow; until then, retain only the backlog item and capability reference.
