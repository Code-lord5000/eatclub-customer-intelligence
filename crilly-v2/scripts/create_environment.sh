#!/bin/bash
set -euo pipefail

environment=$(
  curl -sS --fail-with-body https://api.anthropic.com/v1/environments \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{"name": "crilly-v2-env", "config": {"type": "cloud", "networking": {"type": "unrestricted"}}}'
)

ENVIRONMENT_ID=$(jq -er '.id' <<<"$environment")
echo "Environment ID: $ENVIRONMENT_ID"
echo $ENVIRONMENT_ID > crilly-v2/ENVIRONMENT_ID.txt
