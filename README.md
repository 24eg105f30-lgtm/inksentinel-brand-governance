# InkSentinel AI — Autonomous Brand Governance & Safety Platform
> **Round 2 — The Build Deliverable** | Inkloom AI Hackathon Track  
> **Team:** Team Sentinel (Solo Technical Lead & AI Architect) | **Contact:** 24eg105f30@anurag.edu.in  
> **Repository:** https://github.com/TeamSentinel/inksentinel-brand-governance

---

## 🚀 Live Demo & Quick Launch

### Option 1: Instant Browser Launch (Zero-Setup)
Simply open `index.html` in any modern web browser (Edge, Chrome, Safari, Firefox). All multi-agent reasoning, mathematical WCAG 2.1 contrast formulas, and interactive diff engines execute natively client-side.

### Option 2: Local Python Server & REST API
```bash
# Clone the repository
git clone https://github.com/TeamSentinel/inksentinel-brand-governance.git
cd inksentinel-brand-governance

# Start the local server (zero external pip dependencies required)
python server.py
```
Open **`http://localhost:8080`** in your browser.

---

## 🎯 The Core Problem & Our Solution

High-growth enterprises generate content at scale using distributed marketing squads, external agencies, and generative AI tools. This creates compounding **Brand Debt**:
* **Unsubstantiated Promotional Claims:** High-risk superlatives (*"100% hack-proof"*, *"#1 fastest"*) that violate FTC Section 5 and UK ASA regulations.
* **Outdated Specs & Pricing:** Collateral quoting legacy tiers (e.g., deprecated $19/mo tiers instead of active $29/mo Growth plans).
* **Tone & Persona Drift:** Inconsistent voice fluctuating between corporate prose and casual internet slang.
* **Visual Accessibility Slips:** Marketing creatives that violate WCAG 2.1 contrast thresholds before anyone notices.

### The Solution: InkSentinel AI
Unlike naive LLM wrappers that output blunt rejections, **InkSentinel AI** functions as an **explainable mentor**:
1. Audits multi-format content (copy, documents, and visual creatives) against ingested Brand Bibles and Approved Fact Bases.
2. Identifies exact infraction spans with character offsets and confidence scores.
3. Links to specific, reproducible brand policy clauses.
4. Generates **1-click intent-preserving diff suggestions** that retain creator voice while ensuring 100% policy compliance.

---

## 🏆 The Three Named Improvements (Round 2 Deliverables)

### 1. Multi-Modal Visual & Accessibility Guard (Named Impr. #1)
* **What it does:** Extracts dominant color palettes from uploaded creatives and computes exact mathematical WCAG 2.1 luminosity and contrast ratios:
  $$\text{Contrast} = \frac{L_1 + 0.05}{L_2 + 0.05}$$
* **Deterministic Math:** Detects failing copy (e.g. Light Gray `#A0AEC0` on white yielding `2.26:1`, failing the 4.5:1 AA standard) and mathematically recommends the optimal compliant brand token (`#4A5568`, achieving `7.53:1`, passing both AA and AAA thresholds).
* **Zero-Hallucination:** Executes via deterministic math rather than slow or non-deterministic vision LLM prompts.

### 2. RAG-Grounded Fact & Claim Verification Engine (Named Impr. #2)
* **What it does:** Extracts factual claims and superlatives, cross-referencing them against an active enterprise Fact Base (JSON/CSV) with verified Fact IDs (`#SEC-104`, `#PRC-201`, `#FEAT-305`, `#PERF-402`).
* **The Fact-Grounding Invariant:** Rewrites strictly draw assertions *only* from verified facts. If no supporting fact exists, the tool flags the claim as unverified and prompts the author to remove the absolute or provide evidence.

### 3. Intent-Preserving Interactive Diff Engine (Named Impr. #3)
* **What it does:** A Monaco/TipTap-style side-by-side redline canvas allowing creators to review changes and accept them with **1-click granular adoption**.
* **Two-Pass DAG Architecture:**
  - *Pass 1 (Span Localization):* Detects violation spans with exact character offsets, rule ID, and confidence score.
  - *Pass 2 (Constrained Synthesis):* Constrains generative rewriting to the flagged token span, minimizing edit distance while preserving persuasive tone.

---

## 📊 Originality Feature: Guideline Ambiguity Heatmap

Inverts conventional brand governance: instead of solely penalizing creators, InkSentinel aggregates repeated infractions across teams to alert brand leadership which company guidelines are confusing or ambiguously phrased, providing **AI-recommended guideline rewrites**.

---

## 🛠️ Technology Stack

| Layer | Technologies Selected | Rationale |
| :--- | :--- | :--- |
| **Frontend UI/UX** | HTML5, Tailwind CSS, Lucide Icons, TipTap Split Canvas | Zero-build instant deployment, sub-second reactivity, clean enterprise ergonomics. |
| **Backend & API** | Python 3.10+, `http.server`, AsyncIO | Lightweight, zero-external-dependency deployment, RESTful endpoints (`/api/audit`, `/api/wcag`, `/api/facts`). |
| **Grounding & Storage** | ChromaDB schema + JSON/CSV Fact Base | Reproducible retrieval of rule IDs and verified disclosure records. |
| **Computer Vision Math** | WCAG 2.1 Luminance Algorithm (sRGB Gamma Correction) | Deterministic mathematical verification of contrast ratios without LLM latency. |
| **Security & Privacy** | Server-side Presidio PII Masking Pipeline | Scrub sensitive employee names and unreleased PR copy prior to external API dispatch. |

---

## 🧪 REST API Endpoints

* `GET /api/health` — System status and version verification.
* `POST /api/audit` — Evaluates draft text and returns structured violation spans and intent-preserving diffs.
* `POST /api/wcag` — Computes contrast ratio and WCAG AA/AAA compliance for any foreground/background hex pair.
* `GET /api/guidelines` — Returns the active Brand Bible rules (§4.2, §2.1, §1.3, etc.).
* `GET /api/facts` — Returns the Approved Fact Base records.
* `GET /api/ambiguity` — Returns aggregate infraction frequency and guideline ambiguity statistics.

---

## 👨‍💻 Team & License
* **Team:** Team Sentinel
* **Role:** Solo Lead Engineer & AI Architect
* **License:** MIT License — Open source for hackathon evaluation.
