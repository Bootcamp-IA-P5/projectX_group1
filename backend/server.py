import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


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

                # Simple keyword-based classifier
                hate_keywords = [
                    "odio",
                    "idiota",
                    "estúpido",
                    "tonto",
                    "imbécil",
                    "pendejo",
                    "mierda",
                    "hate",
                    "stupid",
                    "idiot",
                    "dumb",
                    "moron",
                    "trash",
                    "garbage",
                    "kill",
                ]

                text_lower = text.lower()
                has_hate_words = any(keyword in text_lower for keyword in hate_keywords)

                if has_hate_words:
                    label = "toxic"
                    score = 0.75
                else:
                    label = "safe"
                    score = 0.85

                response = {
                    "label": label,
                    "score": score,
                    "prediction": label,
                    "confidence": score,
                    "probabilities": {label: score, "other": 1 - score},
                    "text_length": len(text),
                    "model": "fallback_keyword_classifier",
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
