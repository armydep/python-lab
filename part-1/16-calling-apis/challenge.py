"""Exercise 16: calling APIs.

Based on Microsoft Python for Beginners lesson "16 - Calling APIs".

The tests for this exercise start a local mock server automatically, so you can
practice the API flow without an Azure subscription key.

To call this file manually, run it while a compatible server is listening at
http://localhost:8000/vision/v2.0/ or pass your own address to analyze_image().

Run:

    python3 16-calling-apis/challenge.py
"""

import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


LESSON_DIR = Path(__file__).resolve().parent
DEFAULT_SUBSCRIPTION_KEY = "fake-key"
DEFAULT_VISION_SERVICE_ADDRESS = "http://localhost:8000/vision/v2.0/"
DEFAULT_IMAGE_PATH = LESSON_DIR / "TestImages" / "PolarBear.jpg"


def build_analyze_url(vision_service_address: str) -> str:
    """Return the Computer Vision analyze endpoint URL."""
    return vision_service_address.rstrip("/") + "/analyze"


def build_analyze_parameters() -> dict[str, str]:
    """Return the query parameters used by the Microsoft example."""
    return {
        "visualFeatures": "Description,Color",
        "language": "en",
    }


def build_image_headers(subscription_key: str) -> dict[str, str]:
    """Return the headers needed to upload image bytes to the API."""
    return {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": subscription_key,
    }


def analyze_image(
    image_path: str | Path = DEFAULT_IMAGE_PATH,
    subscription_key: str = DEFAULT_SUBSCRIPTION_KEY,
    vision_service_address: str = DEFAULT_VISION_SERVICE_ADDRESS,
) -> dict[str, Any]:
    """POST image bytes to the analyze endpoint and return the JSON response."""
    analyze_url = build_analyze_url(vision_service_address)
    query_string = urllib.parse.urlencode(build_analyze_parameters())
    request_url = f"{analyze_url}?{query_string}"

    image_data = Path(image_path).read_bytes()
    request = urllib.request.Request(
        request_url,
        data=image_data,
        headers=build_image_headers(subscription_key),
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode("utf-8")
        return json.loads(response_data)


def summarize_analysis_result(results: dict) -> dict[str, str | None]:
    """Return key values from a Computer Vision analyze JSON result."""
    color = results.get("color") or {}
    description = results.get("description") or {}
    tags = description.get("tags") or []
    captions = description.get("captions") or []
    first_caption = captions[0] if captions else {}

    return {
        "request_id": results.get("requestId"),
        "dominant_background_color": color.get("dominantColorBackground"),
        "first_tag": tags[0] if tags else None,
        "caption_text": first_caption.get("text"),
    }


def main() -> None:
    results = analyze_image()
    print(json.dumps(results))


if __name__ == "__main__":
    main()
