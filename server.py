"""
InkSentinel AI — Local Full-Stack Server & REST API
Zero external dependencies required (runs on standard Python 3.10+).
"""
import http.server
import socketserver
import json
import os
import re
import urllib.parse
from datetime import datetime

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
    ratio = (lighter + 0.05) / (darker + 0.05)
    return round(ratio, 2)

class InkSentinelHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/guidelines':
            self.send_json_file(os.path.join(BASE_DIR, 'data', 'brand_bible.json'))
        elif parsed.path == '/api/facts':
            self.send_json_file(os.path.join(BASE_DIR, 'data', 'fact_base.json'))
        elif parsed.path == '/api/ambiguity':
            self.send_json_file(os.path.join(BASE_DIR, 'data', 'ambiguity_stats.json'))
        elif parsed.path == '/api/health':
            self.send_json_response({"status": "healthy", "service": "InkSentinel Engine", "version": "2.0.0"})
        else:
            # Serve static files
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')
        try:
            req_data = json.loads(post_body) if post_body else {}
        except Exception:
            req_data = {}

        if parsed.path == '/api/wcag':
            c1 = req_data.get('foreground', '#A0AEC0')
            c2 = req_data.get('background', '#FFFFFF')
            ratio = compute_contrast(c1, c2)
            passes_aa = ratio >= 4.5
            passes_aaa = ratio >= 7.0
            self.send_json_response({
                "foreground": c1,
                "background": c2,
                "contrast_ratio": ratio,
                "passes_wcag_aa": passes_aa,
                "passes_wcag_aaa": passes_aaa,
                "suggested_accessible_token": "#4A5568" if not passes_aa else c1
            })
        elif parsed.path == '/api/audit':
            text = req_data.get('text', '')
            results = self.audit_text(text)
            self.send_json_response(results)
        else:
            self.send_response(404)
            self.end_headers()

    def send_json_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.send_json_response(data)
        else:
            self.send_json_response({"error": "File not found"}, status=404)

    def send_json_response(self, data, status=200):
        body = json.dumps(data, indent=2).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def audit_text(self, text):
        violations = []
        lower = text.lower()

        # Check 1: Absolute Security Claims
        sec_matches = list(re.finditer(r'\b(100%\s*hack-?proof|completely\s+unbreachable|zero-risk\s+security|bulletproof)\b', lower))
        for m in sec_matches:
            violations.append({
                "id": "viol-1",
                "span": [m.start(), m.end()],
                "flagged_text": text[m.start():m.end()],
                "category": "UNSUBSTANTIATED_CLAIM",
                "rule_id": "SEC-GOV-04",
                "severity": "CRITICAL",
                "citation": "Brand Bible §4.2: Absolute security claims prohibited without third-party cryptanalytic audit documentation.",
                "fact_base_ref": "SEC-104",
                "explanation": "Absolute security superlatives violate FTC Section 5 guidelines. The Approved Fact Base verifies SOC-2 Type II certification and AES-256 encryption.",
                "suggested_replacement": "SOC-2 Type II certified with AES-256 encryption",
                "suggested_action": "SUBSTITUTE_FACT_SNIPPET"
            })

        # Check 2: Outdated Pricing Spec
        prc_matches = list(re.finditer(r'\b(\$19(?:\.00)?(?:\s*\/\s*mo(?:nth)?)?)\b', lower))
        for m in prc_matches:
            violations.append({
                "id": "viol-2",
                "span": [m.start(), m.end()],
                "flagged_text": text[m.start():m.end()],
                "category": "OUTDATED_SPEC",
                "rule_id": "PRC-GOV-01",
                "severity": "HIGH",
                "citation": "Brand Bible §2.1: Legacy $19/mo tier deprecated Q3 2026. Active marketing must quote $29/mo Growth tier.",
                "fact_base_ref": "PRC-201",
                "explanation": "Citing superseded pricing models causes customer churn and checkout confusion.",
                "suggested_replacement": "$29/month",
                "suggested_action": "UPDATE_SPEC"
            })

        # Check 3: Tone Drift / Slang
        tone_matches = list(re.finditer(r'\b(super\s+dope|folks|stuff|cuz|gonna|wanna)\b', lower))
        for m in tone_matches:
            repl = "enterprise-grade platform" if m.group() in ["stuff", "super dope"] else "colleagues"
            violations.append({
                "id": "viol-3",
                "span": [m.start(), m.end()],
                "flagged_text": text[m.start():m.end()],
                "category": "TONE_DRIFT",
                "rule_id": "TONE-GOV-03",
                "severity": "MEDIUM",
                "citation": "Brand Bible §1.3: External publications must maintain professional, clear language. Slang and informal filler prohibited.",
                "fact_base_ref": None,
                "explanation": "Conversational internet slang weakens brand authority in external collateral.",
                "suggested_replacement": "cloud architecture" if m.group() == "stuff" else "elevates operational agility",
                "suggested_action": "ELEVATE_TONE"
            })

        # Check 4: Deprecated Trademark Token
        trd_matches = list(re.finditer(r'\b(inkloom\s+classic)\b', lower))
        for m in trd_matches:
            violations.append({
                "id": "viol-4",
                "span": [m.start(), m.end()],
                "flagged_text": text[m.start():m.end()],
                "category": "TRADEMARK_VIOLATION",
                "rule_id": "TRD-GOV-05",
                "severity": "HIGH",
                "citation": "Brand Bible §3.4: 'Inkloom Classic' was officially renamed to 'Inkloom Pro'.",
                "fact_base_ref": "FEAT-305",
                "explanation": "Using retired trademark tokens creates brand dilution across search and marketing.",
                "suggested_replacement": "Inkloom Pro",
                "suggested_action": "EXACT_TOKEN_SWAP"
            })

        # Check 5: Unsubstantiated Speed/Performance Superlatives
        perf_matches = list(re.finditer(r'\b(#1\s+fastest(?:\s+platform)?\s+globally|fastest\s+on\s+earth|zero\s+latency)\b', lower))
        for m in perf_matches:
            violations.append({
                "id": "viol-5",
                "span": [m.start(), m.end()],
                "flagged_text": text[m.start():m.end()],
                "category": "UNSUBSTANTIATED_CLAIM",
                "rule_id": "PERF-GOV-02",
                "severity": "HIGH",
                "citation": "Brand Bible §4.5: Unsubstantiated speed superlatives violate ASA/FTC standards without comparative benchmark data.",
                "fact_base_ref": "PERF-402",
                "explanation": "Superlative claims require contemporaneous substantiation. Verified Fact #PERF-402 confirms 180ms median latency and 99.95% uptime.",
                "suggested_replacement": "independently verified with sub-200ms median processing latency",
                "suggested_action": "SUBSTITUTE_FACT_SNIPPET"
            })

        # Calculate Brand Health Score
        base_score = 100
        for v in violations:
            if v["severity"] == "CRITICAL":
                base_score -= 22
            elif v["severity"] == "HIGH":
                base_score -= 14
            else:
                base_score -= 8
        score = max(base_score, 15)

        return {
            "audit_timestamp": datetime.utcnow().isoformat() + "Z",
            "total_violations": len(violations),
            "brand_health_score": score,
            "status": "APPROVED" if len(violations) == 0 else "ACTION_REQUIRED",
            "violations": violations
        }

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), InkSentinelHandler) as httpd:
        print(f"InkSentinel Engine serving at http://localhost:{PORT}")
        print("API endpoints: /api/audit, /api/guidelines, /api/facts, /api/wcag, /api/ambiguity")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down InkSentinel Engine.")
