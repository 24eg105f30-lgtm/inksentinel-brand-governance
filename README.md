# InkSentinel AI — Autonomous Brand Governance & Safety Platform
> **Round 3 — The Finish (Final Product Submission)** | Inkloom AI Hackathon Track  
> **Team:** Team Sentinel (Solo Lead Engineer & AI Architect) | **Contact:** 24eg105f30@anurag.edu.in  
> **Live Product:** [https://inksentinel-brand-governance.vercel.app](https://inksentinel-brand-governance.vercel.app)  
> **Source Code (Public):** [https://github.com/24eg105f30-lgtm/inksentinel-brand-governance](https://github.com/24eg105f30-lgtm/inksentinel-brand-governance)  

---

## 🔑 Demo Accounts & Judge Evaluation Quick-Launch

As recommended in the Round 3 hackathon guidelines, InkSentinel AI features built-in demo credentials for immediate, self-guided evaluation by the judging panel:

| Role | Username | Password | Enforced Permissions |
| :--- | :--- | :--- | :--- |
| **Content Creator** | `sarah.copywriter@inkloom.ai` | `sentinel-creator-2026` | Draft editing, audit execution, 1-click diff adoption, PII inspection, draft saving. |
| **Brand Director & Reviewer** | `marcus.brandlead@inkloom.ai` | `sentinel-lead-2026` | Threaded reviewer commenting, approval/rejection, cryptographic SHA-256 sign-off authorization. |

> **Quick Switcher:** You can switch between Sarah (Creator) and Marcus (Reviewer) instantly with 1 click using the role toggles in the top navigation bar.

---

## 🎯 Executive Summary & The Core Problem

High-growth enterprises generate promotional content at unprecedented velocity across distributed squads, agencies, and generative AI tools. This creates compounding **Brand Debt**:
1. **Unsubstantiated Promotional Claims:** High-risk superlatives (*"100% hack-proof"*, *"#1 fastest platform"*) that trigger FTC Section 5 and UK ASA regulatory enforcement.
2. **Outdated Specs & Superseded Pricing:** Marketing collateral quoting legacy tiers (e.g. deprecated $19/mo tiers instead of active $29/mo Growth plans).
3. **Tone Drift & Nomenclature Slips:** Conversational slang and retired trademarks (*"Inkloom Classic"*) diluting enterprise market authority.
4. **Visual Accessibility Non-Compliance:** Ad creatives failing WCAG 2.1 AA/AAA contrast ratios before publication.

### The Solution: InkSentinel AI
Unlike blunt LLM wrappers that output vague rejections, **InkSentinel AI** operates as a deterministic, explainable brand guardian:
* Flags exact infraction character spans and links to specific Brand Bible clauses (§1.3, §2.1, §3.4, §4.2, §4.5, §5.1).
* Generates **1-click intent-preserving diff suggestions** strictly grounded in an Approved Fact Base.
* Deepened OCR visual guard measuring contrast directly against sampled pixels behind text blocks.
* Multi-role review workflow with token-level redline editing, threaded comments, and cryptographic SHA-256 sign-off certificates.

---

## 🏆 The Three Named Improvements Delivered (Round 3)

### 1. Multi-Modal Visual & Accessibility Guard, Deepened (Named Impr. #1)
* **OCR Text Block Localization:** Detects individual text blocks within uploaded creatives with exact bounding box coordinates `[x, y, width, height]`.
* **Per-Region Mathematical Contrast:** Instead of guessing from global color frequencies, it samples foreground glyph pixels and the background pixels directly behind each specific text block, computing exact WCAG 2.1 relative luminance:
  $$\text{Luminance } (L) = 0.2126 R' + 0.7152 G' + 0.0722 B'$$
  $$\text{Contrast Ratio} = \frac{L_{\text{lighter}} + 0.05}{L_{\text{darker}} + 0.05}$$
* **Brand Palette Conformity Guard:** Extracts dominant colors and matches them against the 5 Approved Brand Tokens (`#1E1B4B`, `#4338CA`, `#0F172A`, `#4A5568`, `#F8FAFC`), flagging unapproved off-brand tokens with a 1-click snap-to-palette optimization.

### 2. Grounded Fact & Claim Verification Engine (Named Impr. #2)
* **Hybrid Retrieval (Sparse + Dense):** Extracts factual propositions and matches them against the Approved Fact Base using token overlap combined with character/subword n-gram cosine vector similarity.
* **Tri-State Claim Labeling:**
  1. `VERIFIED` (Green): Matches verified assertion and permitted phrasing with citation clause and confidence score.
  2. `CONTRADICTED` (Red): Conflicts with verified facts or uses banned phrasing (e.g. *"100% hack-proof"* contradicts `#SEC-104`).
  3. `UNVERIFIED / HALLUCINATED` (Amber): Assertions with no ground truth in the Fact Base (blocks ungrounded claims).
* **Fact-Grounding Invariant:** Rewrites strictly draw assertions *only* from verified facts, guaranteeing zero invented metrics.
* **Client-Side Presidio PII Masking:** Scrubs employee names, email addresses, phone numbers, and API secrets *before* external transit.

### 3. Interactive Diff & Multi-Role Review Workflow (Named Impr. #3)
* **Token-Level Inline-Editable Redline:** Side-by-side or unified redline with deleted tokens in strikethrough red and inserted replacements in green. Users can edit replacement tokens directly in place before adopting.
* **Role-Based Enforcement:** Creator role can draft and accept diffs; Reviewer role can leave threaded comments and authorize publication.
* **Threaded Reviewer Comments:** Reviewers can post inline notes on individual findings (e.g., *"Sarah, FTC Section 5 strictly bars '100% hack-proof'"*), and authors can reply in-thread.
* **Saved Drafts & Version History:** Persistent document versions (`v1.0`, `v1.1`, `v1.2`) saved to browser local storage.
* **Cryptographic Sign-Off Certificate:** Uses the native Web Crypto API (`crypto.subtle.digest`) to generate an immutable SHA-256 digital fingerprint across the approved copy, signer identity, and Brand Bible version.

---

## 📊 Originality Feature: Guideline Ambiguity Heatmap

Inverts conventional brand governance: rather than solely policing writers, InkSentinel aggregates infraction frequency across squads to identify confusing corporate guidelines.
* **Live Session Telemetry:** Combines enterprise baseline telemetry (1,420 historical audits) with real-time audit counts from the active session.
* **Root Cause Diagnostics:** Pinpoints why creators struggle (e.g., balancing "approachable" with "authoritative").
* **Autonomous Policy Rewrites:** Generates clarifying Brand Bible amendments with 1-click simulation.

---

## 🛠️ Technical Architecture & Implementation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INKSENTINEL AI ARCHITECTURE                       │
└─────────────────────────────────────────────────────────────────────────────┘

    [ Content Creator ]                  [ Brand Director / Reviewer ]
             │                                         │
             ▼                                         ▼
   ┌───────────────────┐                     ┌───────────────────┐
   │ Draft Studio &    │                     │ Reviewer Mode &   │
   │ PII Scrubbing     │                     │ Threaded Comments │
   └─────────┬─────────┘                     └─────────┬─────────┘
             │                                         │
             ├───────────────────┬─────────────────────┤
             ▼                   ▼                     ▼
   ┌───────────────────┐ ┌───────────────┐   ┌───────────────────┐
   │ Deterministic     │ │ Deepened OCR  │   │ Hybrid Grounding  │
   │ Rule Engine       │ │ Visual Guard  │   │ Retrieval Engine  │
   │ (§1.3, §2.1, etc.)│ │ (WCAG 2.1)    │   │ (Fact Base JSON)  │
   └─────────┬─────────┘ └───────┬───────┘   └─────────┬─────────┘
             │                   │                     │
             └───────────────────┼─────────────────────┘
                                 ▼
                     ┌───────────────────────┐
                     │ Intent-Preserving     │
                     │ Token-Level Diff      │
                     └───────────┬───────────┘
                                 ▼
                     ┌───────────────────────┐
                     │ Web Crypto SHA-256    │
                     │ Audit Sign-Off Cert   │
                     └───────────────────────┘
```

---

## 🧪 Automated Test Suite & Local Verification

InkSentinel AI includes a complete automated test suite validating rule execution, WCAG math, PII redaction, hybrid claim verification, and SHA-256 certificate hashing:

```bash
# 1. Run the automated test suite (Zero external dependencies)
python test_suite.py

# Expected Output:
# test_claim_contradiction_detection (__main__.TestInkSentinelRound3) ... ok
# test_claim_unverified_rejection (__main__.TestInkSentinelRound3) ... ok
# test_claim_verification_success (__main__.TestInkSentinelRound3) ... ok
# test_cryptographic_signoff_sha256 (__main__.TestInkSentinelRound3) ... ok
# test_pii_masking_scrubs_sensitive_data (__main__.TestInkSentinelRound3) ... ok
# test_wcag_contrast_failing (__main__.TestInkSentinelRound3) ... ok
# test_wcag_contrast_passing (__main__.TestInkSentinelRound3) ... ok
# ----------------------------------------------------------------------
# Ran 7 tests in 0.003s
# OK
# ALL INKSENTINEL ROUND 3 AUTOMATED TESTS PASSED (100% SUCCESS)
```

### Starting the Local REST API Server
```bash
python server.py
```
Open **`http://localhost:8080`** in any browser.

#### REST Endpoints:
* `GET /api/health` — System status, engine version (`3.0.0`), and round verification.
* `POST /api/audit` — Rule engine span audit and intent-preserving replacement generation.
* `POST /api/wcag` — Mathematical WCAG 2.1 luminance contrast calculation.
* `POST /api/claims/verify` — Hybrid keyword and semantic claim verification.
* `POST /api/pii/mask` — Presidio-style sensitive entity redaction.
* `POST /api/ocr/analyze` — Per-region text bounding box and brand palette analysis.
* `POST /api/signoff` — Cryptographic SHA-256 certificate generation.

---

## 🗺️ Product Roadmap & Future Commercial Development

| Phase | Milestone | Deliverables |
| :--- | :--- | :--- |
| **Q1 2027** | **Design Tool Integrations** | Native Figma plugin and Adobe Creative Cloud extension for real-time visual WCAG & palette inspection directly on canvas. |
| **Q2 2027** | **CI/CD & Headless CMS Guard** | GitHub Action and Contentful / Sanity webhooks blocking unapproved marketing copy in pull requests before deployment. |
| **Q3 2027** | **Enterprise SSO & Audit Compliance** | Okta / SAML 2.0 integration, multi-tenant Fact Base isolation, and SOC-2 Type II audit trail exports. |
| **Q4 2027** | **Multi-Lingual Global Governance** | Localization support for EMEA and APAC Brand Bibles with jurisdiction-specific regulatory rules (FTC, UK ASA, EU AI Act). |

---

## 👨‍💻 Team & License
* **Team:** Team Sentinel (Solo Lead Engineer & AI Architect)
* **Track:** Inkloom AI Brand-Governance Track
* **License:** MIT License — Open source for hackathon evaluation.