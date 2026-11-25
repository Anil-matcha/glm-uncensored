#!/usr/bin/env python3
"""Submit a prompt to one of Muapi's GLM low-refusal endpoints."""

import argparse
import json
import os
import sys
import time

import requests


API_ROOT = "https://api.muapi.ai/api/v1"
MODELS = (
    "glm-5-3-flash-abliterated",
    "glm-5-3-abliterated",
    "glm-4-6-derestricted-v5",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Prompt text to send")
    parser.add_argument("--model", choices=MODELS, default=MODELS[0])
    args = parser.parse_args()

    api_key = os.environ.get("MUAPI_KEY")
    if not api_key:
        print("Set MUAPI_KEY before running this example.", file=sys.stderr)
        return 2

    headers = {"x-api-key": api_key, "Content-Type": "application/json"}
    response = requests.post(
        f"{API_ROOT}/{args.model}",
        headers=headers,
        json={"prompt": args.prompt},
        timeout=60,
    )
    response.raise_for_status()
    submission = response.json()
    request_id = submission.get("request_id") or submission.get("id")
    if not request_id:
        print(json.dumps(submission, indent=2))
        raise SystemExit("Muapi did not return a request_id.")

    print(f"Submitted {args.model} request {request_id}; polling for the result.")
    for _ in range(120):
        result_response = requests.get(
            f"{API_ROOT}/predictions/{request_id}/result",
            headers=headers,
            timeout=30,
        )
        result_response.raise_for_status()
        result = result_response.json()
        status = result.get("status")
        if status in {"completed", "failed", "cancelled"}:
            print(json.dumps(result, indent=2))
            return 0 if status == "completed" else 1
        time.sleep(2)

    print(f"Request {request_id} is still running. Poll its result URL again.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
