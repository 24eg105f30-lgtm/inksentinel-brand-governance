# InkSentinel AI — AI-Assisted Brand Governance & Safety Platform
> **Round 3 — The Finish (Final Product Submission)** | Inkloom AI Hackathon Track  
> **Team:** Team Sentinel (Solo Lead Engineer & AI Architect) | **Contact:** 24eg105f30@anurag.edu.in  
> **Live Product:** [https://inksentinel-brand-governance.vercel.app](https://inksentinel-brand-governance.vercel.app)  
> **Source Code (Public):** [https://github.com/24eg105f30-lgtm/inksentinel-brand-governance](https://github.com/24eg105f30-lgtm/inksentinel-brand-governance)  

---

## ⚡ Quick Start (Clone & Run Locally)

You can clone and run InkSentinel AI locally in less than 60 seconds with **zero third-party package installations** (uses Python's standard library):

```bash
# 1. Clone repository
git clone https://github.com/24eg105f30-lgtm/inksentinel-brand-governance.git
cd inksentinel-brand-governance

# 2. Check Python version (Requires Python 3.9+; tested on 3.10 and 3.11)
python --version

# 3. Run automated core algorithm test suite
python test_suite.py

# 4. Start local development server
python server.py
```

Now open **`http://localhost:8080`** in your browser. All deterministic rule checks, WCAG luminance math, hybrid claim grounding, and Web Crypto sign-off certificates execute natively in the browser and on the local Python mirror server.

### AI Tone Review & Environment Variable Configuration
The AI Tone Review feature is powered by a Vercel serverless function (`api/tone.js`) using Google Gemini via its OpenAI-compatible endpoint:
- **Environment Variable:** `AI_API_KEY` (or `GEMINI_API_KEY`). Optional: `AI_BASE_URL` and `AI_MODEL` (defaults to `gemini-1.5-flash`).
- **Resilient Fallback Mode (Without API Key or During Provider Spikes):** If `AI_API_KEY` is omitted, or if the external provider returns `503 Service Unavailable` / `429 Rate Limit`, InkSentinel **never breaks or hangs**. Both `api/tone.js` and the client-side engine automatically engage deterministic brand-voice heuristics (`clientSideToneReview()`). It evaluates tone formality, colloquial slang, aggressive sales superlatives, and empathy against Brand Bible §1.3, providing an authentic 0–100 score and specific rewrites.

---

## 🔑 Demo Accounts & Role Enforcement

To enable self-guided evaluation by judges without external authentication infrastructure, InkSentinel provides two pre-configured demo roles:

| Role | Username | Password | Permitted Actions |
| :--- | :--- | :--- | :--- |
| **Content Creator** | `sarah.copywriter@inkloom.ai` | `sentinel-creator-2026` | Draft editing, audit execution, 1-click diff adoption, PII stream inspection, draft version switching. |
| **Brand Director & Reviewer** | `marcus.brandlead@inkloom.ai` | `sentinel-lead-2026` | Threaded reviewer commenting, approval/rejection, cryptographic SHA-256 sign-off authorization. |

> **Role Implementation Details:** Roles are implemented as client-side UI state toggles with browser `localStorage` persistence. When logged in as Sarah (Creator), the official sign-off button is disabled and `signOffAudit()` programmatically checks `currentRole === 'reviewer'`. If a Creator attempts to sign off, execution is blocked with a permission dialog. You can switch between Sarah and Marcus instantly using the toggles in the top navigation bar.

---

## 🎯 Executive Summary & The Problem We Solve

Enterprise marketing teams and generative AI copilyzers produce content at breakneck speed across siloed squads. This rapid publishing velocity creates compounding **Brand Debt**:
1. **Unsubstantiated Promotional Claims:** High-risk superlatives (*"100% hack-proof"*, *"#1 fastest platform"*) that invite FTC Section 5 and UK ASA regulatory enforcement.
2. **Outdated Specs & Superseded Pricing:** Marketing collateral quoting legacy tiers (e.g. deprecated $19/mo tiers instead of active $29/mo Growth plans).
3. **Tone Drift & Nomenclature Slips:** Conversational slang and retired trademarks (*"Inkloom Classic"*) diluting enterprise market authority.
4. **Visual Accessibility Non-Compliance:** Ad creatives failing WCAG 2.1 AA/AAA contrast ratios before publication.

### The Solution: InkSentinel AI
Rather than acting as a blunt "black-box" LLM linter that rejects copy, **InkSentinel AI** operates as an explainable brand governance copilot:
- Pinpoints infractions with exact character offsets `[start, end]` and citations to specific Brand Bible clauses (§1.3, §2.1, §3.4, §4.2, §4.5, §5.1).
- Provides **1-click intent-preserving diff suggestions** strictly drawing assertions only from an Approved Fact Base.
- Evaluates per-region text luminance against background pixels for visual accessibility.
- Enforces human-in-the-loop review: suggestions are strictly advisory and require explicit creator acceptance.

---

## 📋 Complete Feature List

1. **Text & Claim Governance Studio:** Split-pane real-time audit workspace calculating an aggregate Brand Health Score (0–100) across 5 core failure classes.
2. **Explainable Redline & Diff Engine:** Intent-preserving minimal-edit diffs with clause citations, grounded fact IDs, and 1-click individual or batch adoption.
3. **Token-Level Inline-Editable Redline Canvas:** Granular word-level diff view with strikethrough deletions (`<del>`) and editable inline insertions (`<ins>`).
4. **Grounded Fact & Claim Verification Engine:** Interactive sandbox evaluating marketing statements as `VERIFIED`, `CONTRADICTED`, or `UNVERIFIED / HALLUCINATED`.
5. **Fact-Grounding Invariant Enforcer:** Strict policy invariant ensuring automated suggestions never invent speculative claims or unverified metrics.
6. **Client-Side Regex PII Masking Shield:** Presidio-inspired pattern rules redacting personal names, email addresses, phone numbers, and API tokens before any external transmission.
7. **Visual & WCAG 2.1 Contrast Guard:** Canvas-based luminance calculation checking contrast ratios (`AA >= 4.5:1`, `AAA >= 7.0:1`) with interactive region inspection.
8. **Brand Palette Conformity Guard:** Palette compliance validator matching sampled colors against 5 approved enterprise tokens (`#1E1B4B`, `#4338CA`, `#0F172A`, `#4A5568`, `#F8FAFC`).
9. **AI Tone & Persona Review:** Multi-agent style evaluation via Gemini 1.5/2.5 Flash with resilient deterministic fallback.
10. **Threaded Reviewer Comments:** Reviewer-to-creator commenting system attached to individual violations with localStorage persistence.
11. **Draft Version Switcher:** Quick switcher supporting multiple campaign drafts (`Draft 1 v1.2`, `Draft 2 v1.0`, `Draft 3 v2.0`).
12. **Approved Fact Base Ingestion:** Interactive modal allowing compliance teams to ingest new verified fact records during runtime.
13. **Guideline Ambiguity Heatmap:** Telemetry dashboard analyzing recurring violation trends and suggesting policy rewrites.
14. **Web Crypto SHA-256 Audit Certificate:** Cryptographic compliance fingerprinting over approved copy, signer, timestamp, and Brand Bible version, with downloadable JSON certificate receipt.
15. **Local Python REST Mirror Server:** Standard-library server (`server.py`) serving static files and API endpoints (`/api/audit`, `/api/wcag`, `/api/facts`, `/api/guidelines`).
16. **Automated Python Algorithm Test Suite:** Zero-dependency unit test suite (`test_suite.py`) verifying core algorithms.

---

## 🚀 Improvements Completed After Round 2

In Round 2, we delivered a functional MVP that proved the governance concept. In Round 3, we hardened the platform into a cohesive, reliable product.

### The Three Explicitly Named Improvements Delivered:

1. **Named Improvement 1: Multi-Modal Visual & Accessibility Guard, Deepened**
   - *What changed:* In Round 2, image checks relied on global pixel averages without region awareness. In Round 3, we implemented segmented text block bounding boxes (`[x, y, w, h]`) on creative assets. The system samples foreground text pixels and background pixels directly behind each specific text block, computing exact WCAG 2.1 relative luminance and matching colors against the 5 approved brand tokens with a 1-click accessible snap optimizer.

2. **Named Improvement 2: Grounded Fact & Claim Verification Engine (Hybrid Retrieval)**
   - *What changed:* Upgraded from simple string matching to a hybrid retrieval architecture combining lexical keywords with character n-gram cosine vector similarity against `data/fact_base.json`. Categorizes claims into tri-state labels (`VERIFIED`, `CONTRADICTED`, `UNVERIFIED`). Enforces the Fact-Grounding Invariant (blocking ungrounded claims from automated rewrites) and integrates client-side regex PII sanitization.

3. **Named Improvement 3: Interactive Diff and Real Review Workflow**
   - *What changed:* Replaced static cards with a token-level inline-editable redline diff. Added role-enforced separation between Creator (Sarah) and Reviewer (Marcus), persistent threaded comments on individual findings, saved version states, and a tamper-evident Web Crypto SHA-256 sign-off certificate with JSON export.

### Additional Improvements Completed in Round 3:
- **Interactive Fact Ingestion Modal:** Added GUI dialog to ingest new verified fact records directly into the active Fact Base table during runtime.
- **Resilient AI Tone Review:** Implemented edge-fallback heuristics in both `api/tone.js` and client JavaScript, ensuring zero crashes or 503 errors during external LLM outages.
- **Interactive Canvas Region Selection:** Connected canvas click events directly to bounding boxes so judges can inspect ad regions with a single click.
- **Persistent Local Storage:** Connected draft comments and cryptographic sign-off history to browser `localStorage` so data survives page refreshes.

---

## 🔬 Truthful Implementation Architecture & Algorithmic Design

To ensure full transparency during judging, the following details describe the exact technical implementation:

### 1. Visual & WCAG Guard (Text Region Detection & Math)
- **Region Detection:** Text regions in the interactive ad creative use preset demo bounding box coordinates `[x, y, width, height]` with client-side HTML5 Canvas pixel luminance sampling. Custom image upload demonstrates the workflow and falls back to preset demo bounding regions; arbitrary in-browser OCR (e.g., Tesseract.js / Cloud Vision API) is planned for the commercial roadmap.
- **Mathematical Contrast Formula:**
```
Relative Luminance (L):
For each channel C in {R, G, B} normalized to [0, 1]:
  C_linear = C / 12.92              if C <= 0.04045
  C_linear = ((C + 0.055) / 1.055) ^ 2.4  otherwise
L = 0.2126 * R_linear + 0.7152 * G_linear + 0.0722 * B_linear

Contrast Ratio:
Ratio = (L_lighter + 0.05) / (L_darker + 0.05)
Passing WCAG 2.1 AA  : Ratio >= 4.50 : 1
Passing WCAG 2.1 AAA : Ratio >= 7.00 : 1
```

### 2. Fact Grounding & Claim Verification (Hybrid Retrieval)
- **Retrieval Mechanism:** Rather than introducing heavy external vector databases (e.g. ChromaDB/Pinecone) which introduce substantial latency and bundle overhead for a web client, InkSentinel employs **hybrid keyword plus character n-gram vector retrieval**.
- It tokenizes statements, cross-references permitted/banned lexicon entries, and computes character n-gram cosine vector similarity against `data/fact_base.json`.
- **Tri-State Labeling:**
  - `VERIFIED`: Confirmed against permitted assertions with clause citations.
  - `CONTRADICTED`: Conflicts with verified ground truth or uses banned absolutes (e.g. *"100% hack-proof"* contradicts `#SEC-104`).
  - `UNVERIFIED / HALLUCINATED`: Quantitative claims with no matching evidentiary record.

### 3. Client-Side Regex PII Masking Shield
- Operates client-side before any text is dispatched to external LLMs.
- Employs Presidio-inspired pattern rules for:
  - Secrets: `\b(sk_live_[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16})\b`
  - Emails: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
  - Phones: `(\+\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]\d{4}\b`
  - Names: `\b(Sarah\s+Jenkins|Marcus\s+Vance)\b`

### 4. Cryptographic Sign-Off Certificate (Web Crypto API)
- The tamper-evident audit fingerprint uses the browser's native `crypto.subtle.digest('SHA-256')`.
- The exact hashed payload string is:
```javascript
const payload = `${text}|${author}|${reviewer}|${timestamp}|BrandBible-2.4.0`;
```
- Initial UI displays `Pending Reviewer Sign-Off`. Upon Marcus signing off, the live SHA-256 digest is generated and recorded.

---

## 🛠️ Technical Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INKSENTINEL AI ARCHITECTURE                       │
└─────────────────────────────────────────────────────────────────────────────┘

 [ BROWSER CLIENT (Single Page App) ]
  │
  ├── 1. Presentation Layer (HTML5, Tailwind CSS, Lucide Icons)
  │    ├── Creator Workspace (Sarah) ──> Draft text, PII Drawer, 1-Click Diff
  │    └── Reviewer Workspace (Marcus) ──> Threaded Comments, Sign-Off Button
  │
  ├── 2. Client-Side Execution Engines (Zero External Dependencies)
  │    ├── Deterministic Rule Engine (§1.3, §2.1, §3.4, §4.2, §4.5, §5.1)
  │    ├── Hybrid Claim Retrieval (Keyword + n-gram vector matching vs Fact Base)
  │    ├── Canvas Luminance Math Engine (WCAG 2.1 relative luminance)
  │    ├── Regex PII Sanitization Shield (Client-side pre-inference masking)
  │    └── Web Crypto API (crypto.subtle.digest SHA-256 audit fingerprint)
  │
  └── 3. Browser Storage Layer
       └── localStorage ──> Persists drafts, threaded comments & sign-off history
  │
  │ (Optional network call on user click)
  ▼
 [ EDGE / VERCEL SERVERLESS (api/tone.js) ]
  ├── Calls Google Gemini 1.5/2.5 Flash via OpenAI-compatible endpoint
  └── Graceful Fallback ──> Engages local brand-voice heuristics on error/503
  │
 [ LOCAL PYTHON BACKEND (Optional server.py) ]
  └── Serves static files, mirrors WCAG math & rule audit endpoints locally
```

---

## 🧪 Comprehensive Testing Details & Verification Matrix

### 1. Automated Algorithm Unit Tests (`test_suite.py`)
InkSentinel includes an automated unit test suite verifying the Python server logic and core deterministic algorithms (WCAG contrast math, regex PII masking, claim verification tri-state logic, and SHA-256 certificate hashing):

```bash
python test_suite.py
```

**Test Coverage Summary:**
- `test_wcag_contrast_failing`: Verifies failing contrast ratio calculation on `#A0AEC0` over `#FFFFFF` (2.26:1, fails AA).
- `test_wcag_contrast_passing`: Verifies passing contrast ratio calculation on `#4A5568` over `#FFFFFF` (7.53:1, passes AAA).
- `test_pii_masking_scrubs_sensitive_data`: Validates regex redaction of email, phone, and employee names.
- `test_claim_contradiction_detection`: Validates that *"100% hack-proof"* is classified as `CONTRADICTED` under `#SEC-104`.
- `test_claim_verification_success`: Validates that permitted SOC-2 phrasing is classified as `VERIFIED`.
- `test_claim_unverified_rejection`: Validates that ungrounded quantitative assertions are marked `UNVERIFIED`.
- `test_cryptographic_signoff_sha256`: Validates deterministic SHA-256 digest creation over signed copy.

*Result:* **All 7 core algorithm test cases passing (0 failures).**

### 2. Manual End-to-End Test Matrix (Edge Cases & Failure Recovery)

| Test ID | Test Journey / Action | Input / Trigger | Expected Behavior | Observed Result |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Empty Editor State | Click *Run Audit* with empty textarea | Score displays 100, 0 infractions, shows "100% Compliant" empty state. No crash. | Passed |
| **TC-02** | Empty Tone Review | Click *AI Tone Review* with empty textarea | Displays clean "Editor is Empty" dialog with OK button. Does not hang. | Passed |
| **TC-03** | Long Copy Stress Test | Paste 2,000+ word enterprise document | Instantaneous regex audit (<20ms). Scrollable container remains responsive. | Passed |
| **TC-04** | Double Action | Click *1-Click Accept Diff* or *Accept All* twice | First click applies all replacements; second click detects 0 remaining violations. | Passed |
| **TC-05** | Browser Refresh | Execute sign-off, then press `F5` / Refresh | Saved comments and sign-off records reload from `localStorage`. | Passed |
| **TC-06** | Custom Image Upload | Upload arbitrary `.png` / `.jpg` in Visual tab | Displays filename alert, explains demo scope, and gracefully renders canvas. | Passed |
| **TC-07** | AI API Outage / Missing Key | Click *AI Tone Review* with no API key or network down | Resilient edge fallback catches error; displays complete brand persona evaluation. | Passed |
| **TC-08** | Unauthorized Sign-Off | Attempt sign-off while logged in as Sarah (Creator) | Button is disabled; if triggered, displays role permission denial prompt. | Passed |
| **TC-09** | Authorized Sign-Off | Switch to Marcus (Reviewer) and click *Official Sign-Off* | Prompts if infractions remain, hashes payload via Web Crypto, appends to audit table. | Passed |
| **TC-10** | Fact Base Search | Filter fact base search input by "SOC-2" or "Pricing" | Real-time table filtering displaying matching ground truth rows instantly. | Passed |

---

## ⚠️ Known Limitations & Scope Boundaries

In the spirit of honest engineering demonstrated in Round 2, the following scope boundaries are explicitly declared:
1. **Client-Side Role Enforcement:** The Creator vs. Reviewer roles are client-side UI state toggles with browser `localStorage` persistence, designed for immediate hackathon demonstration rather than full multi-tenant enterprise SSO (Okta/SAML 2.0).
2. **Visual Guard OCR Scope:** The Visual & WCAG Guard uses preset demo bounding box coordinates for the built-in ad creative. Uploading a custom image previews the asset and falls back to preset demo bounding regions; production in-browser OCR (Tesseract.js / Google Cloud Vision API) is placed on the Q1 2027 roadmap.
3. **Heatmap Telemetry Baseline:** The Ambiguity Heatmap uses simulated historical baseline data (1,420 simulated historical audits) combined with live session telemetry to demonstrate policy amendment workflows.
4. **Data Persistence Boundary:** Saved draft versions, threaded reviewer notes, and cryptographic sign-off history are stored in browser `localStorage`. They are per-device and per-browser; clearing browser storage resets data to the demo defaults.

---

## 🗺️ Product Roadmap & Future Commercial Development

| Phase | Milestone | Deliverables |
| :--- | :--- | :--- |
| **Q1 2027** | **Design Tool Integrations** | Native Figma plugin and Adobe Creative Cloud extension for real-time visual WCAG & palette inspection directly on canvas. |
| **Q2 2027** | **CI/CD & Headless CMS Guard** | GitHub Action and Contentful / Sanity webhooks blocking unapproved marketing copy in pull requests before deployment. |
| **Q3 2027** | **Enterprise SSO & Multi-Tenancy** | Okta / SAML 2.0 integration, multi-tenant Fact Base isolation, and automated SOC-2 Type II audit trail exports. |
| **Q4 2027** | **Multi-Lingual Global Governance** | Localization support for EMEA and APAC Brand Bibles with jurisdiction-specific regulatory rules (FTC, UK ASA, EU AI Act). |

---

## 👨‍💻 Team & License
* **Team:** Team Sentinel (Solo Lead Engineer & AI Architect)
* **Track:** Inkloom AI Brand-Governance Track
* **Contact:** `24eg105f30@anurag.edu.in`
* **License:** MIT License — Open source for hackathon evaluation (see `LICENSE` file in repository root).
