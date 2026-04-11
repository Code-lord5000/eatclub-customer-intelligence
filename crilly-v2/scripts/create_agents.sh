#!/bin/bash
set -euo pipefail

BASE="$HOME/PM/customer-repo 2/crilly-v2"

create_agent() {
  local name=$1
  local model=$2
  local prompt_file=$3
  local id_file=$4

  echo "Creating $name..."

  system_prompt=$(cat "$BASE/prompts/$prompt_file")

  agent=$(
    curl -sS --fail-with-body https://api.anthropic.com/v1/agents \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: managed-agents-2026-04-01" \
      -H "content-type: application/json" \
      -d "{
        \"name\": \"$name\",
        \"model\": \"$model\",
        \"system\": $(echo "$system_prompt" | python3.11 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
        \"tools\": [{\"type\": \"agent_toolset_20260401\"}]
      }"
  )

  agent_id=$(echo "$agent" | python3.11 -c 'import json,sys; print(json.load(sys.stdin)["id"])')
  echo "$name: $agent_id"
  echo "$agent_id" > "$BASE/$id_file"
}

create_agent "crilly-slack-collector"    "claude-sonnet-4-6" "slack_collector.txt"    "AGENT_SLACK_ID.txt"
create_agent "crilly-granola-collector"  "claude-sonnet-4-6" "granola_collector.txt"  "AGENT_GRANOLA_ID.txt"
create_agent "crilly-hubspot-collector"  "claude-sonnet-4-6" "hubspot_collector.txt"  "AGENT_HUBSPOT_ID.txt"
create_agent "crilly-sms-collector"      "claude-sonnet-4-6" "sms_collector.txt"      "AGENT_SMS_ID.txt"
create_agent "crilly-churn-collector"    "claude-sonnet-4-6" "churn_collector.txt"    "AGENT_CHURN_ID.txt"
create_agent "crilly-dealscore-collector" "claude-sonnet-4-6" "dealscore_collector.txt" "AGENT_DEALSCORE_ID.txt"
create_agent "crilly-mixpanel-collector" "claude-sonnet-4-6" "mixpanel_collector.txt" "AGENT_MIXPANEL_ID.txt"
create_agent "crilly-orchestrator"       "claude-opus-4-6"   "orchestrator.txt"       "AGENT_ORCH_ID.txt"

echo ""
echo "All agents created. IDs saved to crilly-v2/"
