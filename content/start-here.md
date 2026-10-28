## The approach

**Keep the three existing documentation tabs and give every page one clear purpose.** Use the current audience structure for navigation, and apply Diátaxis within it: tutorials for learning, how-to guides for completing tasks, reference for looking up details, and explanations for understanding concepts.

The goal is documentation that people and AI agents can navigate, use, and maintain more easily.

## Why the documentation needs to change

The existing structure is a useful foundation, but some pages combine explanations, instructions, and technical catalogs. Other pages repeat definitions or workflows. This makes it harder to find the right answer and keep information consistent.

The main improvements are clearer starting points, focused task guides, shared explanations, and reliable technical reference.

## Where content belongs

| Area | Purpose |
| --- | --- |
| **Concepts** | Shared explanations of products, architecture, terminology, and results. |
| **Agent Owner’s Guide** | A first-evaluation tutorial and practical Console workflows. |
| **Agent Developer’s Guide** | A first-evaluation tutorial, SDK/MCP/plugin workflows, integrations, self-hosting, and central technical reference. |

Each page has one primary job:

- **Tutorial:** teach through a guided, working example.
- **How-to:** help complete a specific task.
- **Reference:** provide exact options, parameters, and behavior.
- **Explanation:** build understanding of how and why things work.

For example, a Harness page in Concepts explains its role; the complete Harness catalog lives in Reference. Console and SDK guides link to both while keeping their own task-specific steps.

The migration aligns with the planned CLI removal in PR #251. SDK and MCP/plugin remain the primary developer paths; REST stays available as reference and a secondary integration path.

## How the migration works

1. **Align the foundations.** Confirm the post-CLI-removal baseline, assign content owners, and resolve inconsistent terminology and behavior that affect the first workflows. Introduce a short writing standard and basic automated checks.
2. **Pilot with Diamond evaluations.** Improve one complete journey: run a first evaluation in the Console or SDK, inspect the results, understand the evidence, and find the relevant technical details. Remove duplicated explanations and connect the pages clearly.
3. **Expand in small batches.** Apply the approach to Red Team, runtime protection, Discover, and self-hosting. Preserve useful URLs and add redirects where pages move. Add guides for evolving capabilities, such as Darwin, once their supported workflows are confirmed.

The pilot provides the basis for estimating and scheduling the remaining work.

## What makes a useful page

Start with its purpose, supported interface, and prerequisites. Include clear steps or definitions, expected results, and a way to verify success. Use visible identifiers, readable Markdown, and meaningful links to related concepts, tasks, and reference.

Build on the existing Mermaid diagrams. Keep shared definitions and specifications in canonical locations, and check that generated API/SDK reference stays aligned with supported releases.
