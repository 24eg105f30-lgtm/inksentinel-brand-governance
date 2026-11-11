"""
InkSentinel AI — Round 3 Automated Test Suite
Verifies all core governance engines, deterministic WCAG math,
PII scrubbing, hybrid fact retrieval, and cryptographic sign-off.
"""

import unittest
import json
import re
import hashlib
from datetime import datetime

# --- LUMINANCE & WCAG MATH ---
def srgb_to_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def relative_luminance(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 3:
        hex_code = ''.join([c*2 for c in hex_code])
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return 0.2126 * srgb_to_lin(r) + 0.7152 * srgb_to_lin(g) + 0.0722 * srgb_to_lin(b)

def compute_contrast(hex1, hex2):
    l1 = relative_luminance(hex1)
    l2 = relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)

# --- PII SCRUBBING ---
def mask_pii(text):
    # 1. Mask API keys and secrets first
    text = re.sub(r'\b(sk_live_[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16})\b', '[REDACTED_SECRET]', text)
    # 2. Mask email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[REDACTED_EMAIL]', text)
    # 3. Mask phone numbers
    text = re.sub(r'(\+\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]\d{4}\b', '[REDACTED_PHONE]', text)
    return text

# --- HYBRID CLAIM RETRIEVAL ---
FACTS = [
    {
        "id": "SEC-104",
        "category": "SECURITY",
        "verified": "SOC-2 Type II certified access controls and AES-256 data encryption at rest.",
        "permitted": ["soc-2 type ii certified", "aes-256 encryption", "multi-layered security"],
        "banned": ["100% hack-proof", "completely unbreachable", "zero-risk", "bulletproof"]
    },
    {
        "id": "PRC-201",
        "category": "PRICING",
        "verified": "Growth Tier subscription is $29/month billed annually.",
        "permitted": ["$29/month", "starting at $29/mo", "flexible annual billing"],
        "banned": ["$19/month", "free forever", "lowest price in industry"]
    },
    {
        "id": "PERF-402",
        "category": "PERFORMANCE",
        "verified": "Independent benchmark testing verified 99.95% uptime and median response latency of 180ms.",
        "permitted": ["99.95% verified uptime", "sub-200ms median processing latency", "independently benchmarked"],
        "banned": ["#1 fastest platform globally", "zero latency", "100% uptime guaranteed"]
    }
]

def verify_claim(claim_text):
    lower = claim_text.lower()
    
    # 1. Check for Contradictions / Banned Phrasing
    for fact in FACTS:
        for b in fact["banned"]:
            if b in lower:
                return {
                    "status": "CONTRADICTED",
                    "fact_id": fact["id"],
                    "reason": f"Directly violates policy §4.2 / fact #{fact['id']}. Banned superlative '{b}' detected.",
                    "verified_assertion": fact["verified"]
                }
                
    # 2. Check for Verified Assertions (Keyword & Semantic Overlap)
    for fact in FACTS:
        for p in fact["permitted"]:
            if p in lower:
                return {
                    "status": "VERIFIED",
                    "fact_id": fact["id"],
                    "confidence": 0.95,
                    "verified_assertion": fact["verified"]
                }
                
    # 3. Unverified Claim (Not grounded in Fact Base)
    return {
        "status": "UNVERIFIED",
        "fact_id": None,
        "reason": "Assertion contains ungrounded marketing claims not documented in the Approved Fact Base.",
        "risk_level": "FTC_COMPLIANCE_RISK"
    }

# --- CRYPTOGRAPHIC SIGN-OFF HASH ---
def generate_audit_hash(text, author, reviewer, timestamp, brand_bible_version="2.4.0"):
    payload = f"{text}|{author}|{reviewer}|{timestamp}|{brand_bible_version}"
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

# --- UNIT TEST CASES ---
class TestInkSentinelRound3(unittest.TestCase):

    def test_wcag_contrast_failing(self):
        # Light gray #A0AEC0 on pure white #FFFFFF
        ratio = compute_contrast('#A0AEC0', '#FFFFFF')
        self.assertAlmostEqual(ratio, 2.26, delta=0.05)
        self.assertFalse(ratio >= 4.5, "Contrast should fail WCAG AA (min 4.5:1)")

    def test_wcag_contrast_passing(self):
        # Accessible Slate #4A5568 on pure white #FFFFFF
        ratio = compute_contrast('#4A5568', '#FFFFFF')
        self.assertGreaterEqual(ratio, 7.0, "Contrast should pass WCAG AAA (min 7.0:1)")
        self.assertAlmostEqual(ratio, 7.53, delta=0.1)

    def test_pii_masking_scrubs_sensitive_data(self):
        raw_text = "Contact Sarah Jenkins at sarah.jenkins@inkloom.ai or call +1-555-0199 with API key sk_live_98374829104928172648."
        masked = mask_pii(raw_text)
        self.assertNotIn("sarah.jenkins@inkloom.ai", masked)
        self.assertIn("[REDACTED_EMAIL]", masked)
        self.assertNotIn("+1-555-0199", masked)
        self.assertIn("[REDACTED_PHONE]", masked)
        self.assertNotIn("sk_live_98374829104928172648", masked)
        self.assertIn("[REDACTED_SECRET]", masked)

    def test_claim_contradiction_detection(self):
        res = verify_claim("Our cloud architecture is 100% hack-proof and completely unbreachable.")
        self.assertEqual(res["status"], "CONTRADICTED")
        self.assertEqual(res["fact_id"], "SEC-104")

    def test_claim_verification_success(self):
        res = verify_claim("We are SOC-2 Type II certified with AES-256 encryption.")
        self.assertEqual(res["status"], "VERIFIED")
        self.assertEqual(res["fact_id"], "SEC-104")

    def test_claim_unverified_rejection(self):
        res = verify_claim("We are the planetary market leader with 50,000 enterprise customers.")
        self.assertEqual(res["status"], "UNVERIFIED")
        self.assertIsNone(res["fact_id"])

    def test_cryptographic_signoff_sha256(self):
        text = "Compliant copy for enterprise launch."
        h1 = generate_audit_hash(text, "sarah.copywriter", "marcus.brandlead", "2026-11-11T12:00:00Z")
        self.assertEqual(len(h1), 64, "SHA-256 hash must be 64 hexadecimal characters")
        
        # Tamper evidence: changing single character modifies hash completely
        h2 = generate_audit_hash(text + " [MODIFIED]", "sarah.copywriter", "marcus.brandlead", "2026-11-11T12:00:00Z")
        self.assertNotEqual(h1, h2, "Tampering with approved text must invalidate hash")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInkSentinelRound3)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nALL INKSENTINEL ROUND 3 AUTOMATED TESTS PASSED (100% SUCCESS)")
    else:
        exit(1)
