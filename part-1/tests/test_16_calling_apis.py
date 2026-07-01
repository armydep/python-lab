import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from tests.helpers import load_challenge


apis = load_challenge("16-calling-apis")


SAMPLE_ANALYSIS_RESULT = {
    "requestId": "abc-123",
    "color": {"dominantColorBackground": "White"},
    "description": {
        "tags": ["polar bear", "snow", "outdoor"],
        "captions": [{"text": "a polar bear walking in the snow"}],
    },
}


class MockVisionHandler(BaseHTTPRequestHandler):
    """Small test-only mock for the Computer Vision analyze endpoint."""

    last_body = b""
    last_headers = None
    last_path = ""

    def do_POST(self) -> None:
        type(self).last_path = self.path
        type(self).last_headers = self.headers

        content_length = int(self.headers.get("Content-Length", 0))
        type(self).last_body = self.rfile.read(content_length)

        if not self.path.startswith("/vision/v2.0/analyze"):
            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps(SAMPLE_ANALYSIS_RESULT).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        """Keep test output quiet."""


#@unittest.skip("Disabled while focusing on 12-loops.")
class CallingApisChallengeTest(unittest.TestCase):
    def test_build_analyze_url(self) -> None:
        self.assertEqual(
            apis.build_analyze_url("https://example.com/vision/v2.0/"),
            "https://example.com/vision/v2.0/analyze",
        )
        self.assertEqual(
            apis.build_analyze_url("https://example.com/vision/v2.0"),
            "https://example.com/vision/v2.0/analyze",
        )

    def test_build_analyze_parameters(self) -> None:
        self.assertEqual(
            apis.build_analyze_parameters(),
            {"visualFeatures": "Description,Color", "language": "en"},
        )

    def test_build_image_headers(self) -> None:
        self.assertEqual(
            apis.build_image_headers("secret-key"),
            {
                "Content-Type": "application/octet-stream",
                "Ocp-Apim-Subscription-Key": "secret-key",
            },
        )

    def test_summarize_analysis_result(self) -> None:
        self.assertEqual(
            apis.summarize_analysis_result(SAMPLE_ANALYSIS_RESULT),
            {
                "request_id": "abc-123",
                "dominant_background_color": "White",
                "first_tag": "polar bear",
                "caption_text": "a polar bear walking in the snow",
            },
        )

    def test_summarize_analysis_result_uses_none_for_missing_values(self) -> None:
        self.assertEqual(
            apis.summarize_analysis_result({}),
            {
                "request_id": None,
                "dominant_background_color": None,
                "first_tag": None,
                "caption_text": None,
            },
        )

    def test_analyze_image_calls_mock_server_and_returns_json(self) -> None:
        server = HTTPServer(("localhost", 0), MockVisionHandler)
        thread = threading.Thread(target=server.serve_forever)
        thread.start()

        with tempfile.NamedTemporaryFile(delete=False) as image_file:
            image_file.write(b"image-bytes")
            image_path = Path(image_file.name)

        host, port = server.server_address
        vision_service_address = f"http://{host}:{port}/vision/v2.0/"

        try:
            result = apis.analyze_image(
                image_path=image_path,
                subscription_key="secret-key",
                vision_service_address=vision_service_address,
            )
        finally:
            image_path.unlink()
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

        self.assertEqual(result, SAMPLE_ANALYSIS_RESULT)
        self.assertEqual(MockVisionHandler.last_body, b"image-bytes")
        self.assertEqual(
            MockVisionHandler.last_headers["Content-Type"],
            "application/octet-stream",
        )
        self.assertEqual(
            MockVisionHandler.last_headers["Ocp-Apim-Subscription-Key"],
            "secret-key",
        )
        self.assertTrue(MockVisionHandler.last_path.startswith("/vision/v2.0/analyze?"))


if __name__ == "__main__":
    unittest.main()
