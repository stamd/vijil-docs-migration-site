# Vijil Documentation: Proposed Transition

Meeting brief

## Recommendation

**Keep the three existing tabs and give every page one clear purpose.** Apply a hybrid Diátaxis approach: use the current audience structure for navigation, and distinguish tutorials, how-to guides, reference, and explanations within it.

The goal is to make documentation easier to navigate, use, and maintain for both people and AI agents.

## Why Change

The existing structure is a useful foundation, but some pages combine explanations, instructions, and technical catalogs. Other pages repeat the same definitions or workflows. This makes it harder to find the right answer and keep information consistent.

The biggest opportunities are clearer starting points, focused task guides, shared explanations, and reliable technical reference.

## What We Propose

| Area | Purpose |
| --- | --- |
| **Concepts** | Shared explanations of products, architecture, terminology, and results. |
| **Agent Owner’s Guide** | A first-evaluation tutorial and practical Console workflows. |
| **Agent Developer’s Guide** | A first-evaluation tutorial, SDK/MCP/plugin workflows, integrations, self-hosting, and a central technical reference. |

Each page has one primary job:

- **Tutorial:** teach through a guided, working example.
- **How-to:** help complete a specific task.
- **Reference:** provide exact options, parameters, and behavior.
- **Explanation:** build understanding of how and why things work.

For example, a Harness page in Concepts explains its role; the complete Harness catalog lives in Reference. Console and SDK guides link to both, while keeping their own task-specific steps.

Align the refactor with the CLI removal in PR #251. SDK and MCP/plugin remain the primary developer paths; REST stays available as reference and a secondary integration path.

<!-- pagebreak -->

## How We Deliver It

**1. Align the foundations.** Confirm the post-CLI-removal baseline, assign content owners, and agree on inconsistent terminology and behavior that affect the first workflows. Introduce a short writing standard and basic automated checks.

**2. Pilot with Diamond evaluations.** Improve one complete journey: run a first evaluation in the Console or SDK, inspect the results, understand the evidence, and find the relevant technical details. Remove duplicated explanations and connect the pages clearly.

**3. Expand in small batches.** Apply the validated approach to Red Team, runtime protection, Discover, and self-hosting. Preserve useful URLs and add redirects where pages move. Add guides for evolving capabilities, such as Darwin, once their supported workflows are confirmed.

The pilot provides the basis for estimating and scheduling the remaining work.

## Make Every Page Easy to Use

Start with its purpose, supported interface, and prerequisites. Include clear steps or definitions, expected results, and a way to verify success. Use visible identifiers, readable Markdown, and meaningful links to related concepts, tasks, and reference.

Build on the existing Mermaid diagrams. Keep shared definitions and specifications in canonical locations, and check that generated API/SDK reference stays aligned with supported releases.

## How We Know It Works

Test the same representative tasks before and after the pilot with people and AI agents:

- Can they find the correct guide and interface?
- Can they complete the task and verify its result?
- Do they encounter fewer conflicting answers or unnecessary detours?
- Can maintainers update a shared definition in one place?

## Decisions for This Meeting

1. Endorse the hybrid structure and Diamond pilot.
2. Assign a documentation lead and product/engineering reviewers.
3. Agree on the pilot’s sample Agent, success criteria, and review process.

**Proposed next step:** deliver and review the Diamond pilot, then use its results to confirm the wider migration plan.
