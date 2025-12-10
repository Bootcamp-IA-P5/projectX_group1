import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

try:
    from backend.toxic_keywords import (ALL_TOXIC_PATTERNS,
                                        MULTIPLE_MATCHES_BONUS,
                                        SAFE_CONTEXT_PATTERNS,
                                        SAFE_CONTEXT_REDUCTION,
                                        TOXICITY_THRESHOLD)
except ImportError:
    from toxic_keywords import (ALL_TOXIC_PATTERNS, MULTIPLE_MATCHES_BONUS,
                                SAFE_CONTEXT_PATTERNS, SAFE_CONTEXT_REDUCTION,
                                TOXICITY_THRESHOLD)


class HateSpeechHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self._send_cors_headers()
            self.end_headers()
            response = {
                "message": "ProjectX Hate Speech Detector API",
                "status": "running",
            }
            self.wfile.write(json.dumps(response).encode())

        elif parsed_path.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self._send_cors_headers()
            self.end_headers()
            response = {"status": "ok"}
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self._send_cors_headers()
            self.end_headers()
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/predict":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            try:
                payload = json.loads(post_data.decode())
                text = payload.get("text", "")

                if not text or not text.strip():
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self._send_cors_headers()
                    self.end_headers()
                    response = {"error": "Text cannot be empty"}
                    self.wfile.write(json.dumps(response).encode())
                    return

                # Enhanced keyword-based classifier with scoring
                text_lower = text.lower()

                # Calculate toxicity score
                max_toxicity = 0.0
                matches_found = []

                for pattern, weight in ALL_TOXIC_PATTERNS.items():
                    if re.search(pattern, text_lower, re.IGNORECASE):
                        max_toxicity = max(max_toxicity, weight)
                        matches_found.append(pattern)

                # Check for safe context
                has_safe_context = any(
                    re.search(ctx, text_lower, re.IGNORECASE)
                    for ctx in SAFE_CONTEXT_PATTERNS
                )

                # Adjust score based on context
                if has_safe_context and max_toxicity > 0:
                    max_toxicity *= SAFE_CONTEXT_REDUCTION

                # Multiple toxic words increase confidence
                if len(matches_found) > 1:
                    max_toxicity = min(0.99, max_toxicity + MULTIPLE_MATCHES_BONUS)

                # Determine label and confidence
                if max_toxicity >= TOXICITY_THRESHOLD:
                    label = "toxic"
                    score = max_toxicity
                else:
                    label = "safe"
                    score = max(0.7, 1.0 - max_toxicity)

                response = {
                    "label": label,
                    "score": round(score, 4),
                    "prediction": label,
                    "confidence": round(score, 4),
                    "probabilities": {
                        label: round(score, 4),
                        "other": round(1 - score, 4),
                    },
                    "text_length": len(text),
                    "model": "enhanced_keyword_classifier_v2",
                    "matches_count": len(matches_found),
                    "safe_context_detected": has_safe_context,
                }

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self._send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "application/json")
                self._send_cors_headers()
                self.end_headers()
                response = {"error": f"Internal server error: {str(e)}"}
                self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self._send_cors_headers()
            self.end_headers()
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode())


def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, HateSpeechHandler)
    print(f"🚀 Backend server running on http://localhost:{port}")
    print(f"📝 Test the API at: http://localhost:{port}/health")
    print(f"🔍 Prediction endpoint: POST http://localhost:{port}/predict")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
