# Complete Proposed TOC

Target-state design; new page content has not been authored. E = explanation, H = how-to, T = tutorial, R = reference. ⚑ = conditional page: do not publish until the condition in the new-page registry is confirmed.

```text
Concepts
  Platform
    [E] Welcome to Vijil (P001)
    [E] Vijil Console (P002)
    [E] Vijil Discover (P003)
    [E] Vijil Diamond (P004)
    [E] Vijil Dome (P005)
    [E] Vijil Darwin (P006)
    [E] What Is an Agent in Vijil (P037)
    [E] The Agent Trust Lifecycle (N001)
  Trust and Evaluation
    [E] How the Trust Score Works (P007)
    [E] Reliability (P008)
    [E] Safety (P009)
    [E] Security (P010)
    [E] How Evaluation Works (P016)
    [E] Evaluation Harnesses (P017)
    [E] Evaluation Scenarios (P018)
    [E] Evaluation Probes (P019)
    [E] Evaluation Detectors (P020)
    [E] Personas, Policies, and Evaluation Context (N002)
    [E] Interpret Evaluation Evidence (N003)
  Discovery
    [E] How Discovery Works (P011)
    [E] Discovery Targets (P012)
    [E] Discovery Collectors (P013)
    [E] Discovered Resources (P014)
    [E] Resource Classification (P015)
  Red Team
    [E] Why Use Adaptive Red Teaming (P021)
    [E] How Red Team Engagements Work (P022)
  Runtime Defense
    [E] How Runtime Defense Works (P023)
    [E] Guardrails (P024)
    [E] Guards (P025)
    [E] Runtime Detectors (P026)
    [E] Runtime Observability (P027)
    [E] How the Controls Engine Works (N004)
    [E] How Trust Runtime Works (N005)
  Glossary
    [R] Glossary (P028)
Agent Owner's Guide
  Get Started
    [T] Your First Evaluation in the Console (P029)
  Teams and Agents
    [H] Manage Teams (P030)
    [H] Register and Manage Agents in the Console (P038)
  Discover Agents
    [H] Discover Agents in an Environment (P031)
    [H] Create and Manage Targets (P032)
    [H] Prepare Collector Installation (P033)
    [H] Review Discovered Resources (P034)
    [H] Register a Discovered Agent (P035)
    [H] Scan Code Repositories (P036)
  Prepare Evaluations
    [H] Create Personas in the Console (P039)
    [H] Create Policies in the Console (P040)
    [H] Configure a Baseline Evaluation (P041)
    [H] Run a Compliance Evaluation (P042)
    [H] Create a Custom Harness in the Console (P043)
  Evaluate Agents
    [H] Run and Monitor an Evaluation in the Console (P044)
    [H] Review Evaluation Results in the Console (P045)
  Red Team
    [H] Run a Red Team Evaluation in the Console (P046)
    [H] Review Red Team Results in the Console (P047)
  Protect and Monitor
    [H] Configure Guardrails in the Console (P048)
    [H] Review Runtime Events in Defend (P049)
    [H] Hand Off Dome Deployment (P050)
    [H] Investigate an Agent with Dome Metrics (P051)
  Improve Agents
    [H] Review and Apply an Adaptation Proposal (N033) ⚑
Agent Developer's Guide
  Get Started
    [R] Choose a Developer Workflow (P052)
    [T] Your First Evaluation with the Python SDK (P054)
    [H] Set Up the Claude Code Plugin (P055)
    [H] Authenticate to Vijil (N019)
    [H] Connect the Vijil MCP Server (N020)
    [H] Install and Configure the Python SDK (N021)
  Teams and Agents
    [H] Connect an Agent Endpoint (P062)
    [H] Register an Agent Programmatically (N023)
  Discover Agents
    [H] Install an Endpoint Collector (N024)
    [H] Install a Network Collector (N025)
    [H] Install a Kubernetes Collector (N026)
    [H] Install an AWS Cloud API Collector (N027)
    [H] Connect Runtime Events to Defend (N028) ⚑
  Prepare Evaluations
    [H] Create a Custom Harness Programmatically (P061)
  Evaluate Agents
    [R] Choose an Evaluation Workflow (P057)
    [H] Run and Monitor Evaluations (P058)
    [H] Evaluate an Agent Through a Local Tunnel (P059)
    [H] Retrieve and Investigate Evaluation Results (P060)
  Red Team
    [H] Run a Red Team Evaluation Programmatically (P063)
    [H] Retrieve and Investigate Red Team Evidence (N029)
  Protect Agents
    [R] Choose a Protection Interface (P064)
    [H] Install Dome (P065)
    [H] Enforce a Policy with the Controls Engine (P066)
    [H] Secure an Agent with Trust Runtime (P067)
    [H] Configure Guardrails in Code (P068)
    [H] Apply Guardrails in an Agent (P069)
    [H] Build a Custom Runtime Detector (P070)
    [H] Instrument Runtime Protection (P072)
    Framework Integrations
      [H] Protect a Google ADK Agent (P073)
      [H] Protect a LangGraph Agent (P074)
      [H] Protect a Strands Agent (P075)
      [H] Protect a LangChain Workflow (P076)
      [H] Protect an MCP Server (P077)
  Release and Improve
    [H] Release an Evaluated Agent (P053)
    [H] Gate a Release on Evaluation Evidence (N022)
    [H] Adapt an Agent and Validate the Proposal (N034) ⚑
  Self-Hosting
    [H] Deploy Vijil Console on AWS EKS (P056)
    [H] Deploy Dome as a Service (P078)
    [H] Prepare AWS Infrastructure for Vijil (N030)
  Reference
    Runtime Protection
      [R] Runtime Detector Reference (P071)
      [R] Controls API Reference (P080)
      [R] Dome Configuration Reference (N013)
      [R] Dome Results and Telemetry Reference (N014)
      [R] Trust Runtime API Reference (N015)
      [R] Framework Integration Reference (N016)
      [R] Dome Service HTTP API Reference (N017)
    MCP and Plugin
      [R] MCP Tool Reference (P079)
      [R] Claude Code Plugin Command Reference (N032)
    Python SDK
      [R] Python SDK Configuration Reference (P089)
      [R] Python SDK Lifecycle Methods (P090)
      [R] Python SDK Resources (P091)
      [R] Python SDK Models and Errors (P092)
    Evaluation Catalogs
      [R] Evaluation Harness Reference (N006)
      [R] Evaluation Scenario Reference (N007)
      [R] Evaluation Probe Reference (N008)
      [R] Evaluation Detector Reference (N009)
      [R] Evaluation Coverage by Dimension (N010)
    Platform Contracts
      [R] Agent Registration Contract (N011)
      [R] Evaluation Contracts and Results (N012)
      [R] Platform Versions and Capability Availability (N018)
    Self-Hosting
      [R] Self-Hosted Configuration Reference (N031)
    [R] REST API Reference — generated from openapi/api.json (149 source operations)
```

Exact URLs, content origins, and publication conditions are recorded in target-pages.json and new-pages.csv. A page's type does not depend on its folder; existing meaningful URLs are preserved.
