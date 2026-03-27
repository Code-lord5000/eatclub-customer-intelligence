# Slack Signal Capture Guide

## Channel-by-channel extraction discipline

### #customer-feedback
**What it contains**: Direct customer feedback, venue complaints, positive moments, feature requests passed through AMs or support.

**What to log**:
- Specific venue complaints with context (what happened, what they said)
- Recurring friction moments — same issue appearing from different venues
- Workarounds venues describe ("we just manually do X")
- Anything prefaced with "a venue asked..." or "customer said..."

**What to ignore**:
- Generic positive feedback with no specifics
- One-off technical bugs already escalated
- Internal ops chatter that's not customer-facing

**Watch for**: The same phrase or problem type appearing across multiple messages in a week — that's a theme forming.

---

### #am-team
**What it contains**: AM internal discussion, handoffs, operational questions, informal flagging of venue issues.

**What to log**:
- "Has anyone else seen..." — these are early pattern signals
- Manual workarounds AMs describe doing
- Questions about how to handle situations (implies product doesn't support it)
- Venue escalations being discussed
- "I had to explain to a venue that..." — always a friction point

**What to ignore**:
- Pure logistics/scheduling
- Individual AM performance discussions
- One-off venue-specific ops issues

**Watch for**: Questions being asked multiple times by different AMs — if three AMs ask how to do the same thing in a month, that's a usability or workflow problem.

---

### #urgent
**What it contains**: High-priority escalations, live issues, things that need immediate attention.

**What to log**:
- The nature of what's urgent — not just that it's urgent
- How it was resolved (workarounds reveal product gaps)
- Whether the same type of urgency has appeared before

**What to ignore**:
- Pure technical incidents being handled by engineering
- Duplicate alerts

**Watch for**: The category of urgency. A bug is a bug. But "venue can't see their deal" appearing as urgent repeatedly is a visibility/trust problem worth a card.

---

### #cs-am
**What it contains**: Customer success and AM crossover — handoffs, venue health conversations, escalations.

**What to log**:
- Venue health concerns that surface ("this venue is going quiet")
- Handoff friction between CS and AM roles
- Anything about a venue feeling underserved or unheard
- AM capacity issues that affect venue experience

**Watch for**: Venues being discussed across multiple channels in the same week — multi-surface appearance for a single venue is a churn risk signal.

---

## Weekly Slack sweep — how to do it

Don't try to read everything. Use this discipline:

1. **Search for signal words** across all four channels for the past 7 days:
   - "venue said", "customer said", "they asked", "we had to", "workaround", "can't figure out", "frustrated", "leaving", "churned", "manually", "has anyone else"
   
2. **Scan thread starters** — replies to a message mean it resonated. A message with 5+ replies usually contains a real problem.

3. **Log signals, not messages** — you don't need to log every message. You need to log the problem each message represents. One signal block per distinct problem.

4. **Note frequency** — if you see the same issue appear 3 times in a week across channels, note it as 3 separate signals with the same theme tag, not one merged signal. Frequency is data.
