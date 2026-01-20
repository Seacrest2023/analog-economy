# The Analog Economy: MVP Training Facility

> **Version:** 1.0
> **Last Updated:** 2026-01-19
> **Status:** Design Draft

---

## Executive Summary

The **MVP Training Facility** is a streamlined proving ground that validates The Analog Economy's core concept: **humans playing survival games generate valuable AI training data**. Rather than building the full historical progression from Sumer to AI Era, we start with a focused, single-biome experience that demonstrates the data value proposition to enterprise buyers.

**Goal:** Prove that player behavior data is worth buying—before building the cathedral.

---

## Table of Contents

1. [Why an MVP First](#why-an-mvp-first)
2. [The Training Facility Concept](#the-training-facility-concept)
3. [Core Mechanics (Minimal Viable)](#core-mechanics-minimal-viable)
4. [Data Collection Focus](#data-collection-focus)
5. [Success Metrics](#success-metrics)
6. [Technical Scope](#technical-scope)
7. [Launch Strategy](#launch-strategy)
8. [Path to Full Game](#path-to-full-game)

---

## Why an MVP First

### The Problem with Building Everything

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE CATHEDRAL VS. THE BAZAAR                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FULL GAME (THE CATHEDRAL):                                                 │
│  ├── 8 historical eras to build                                             │
│  ├── 10+ biomes to design                                                   │
│  ├── Complex economy to balance                                             │
│  ├── Years of development                                                   │
│  └── Massive upfront investment                                             │
│                                                                             │
│  RISK: We build everything, THEN discover if data is valuable.              │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  MVP (THE BAZAAR):                                                          │
│  ├── ONE focused experience                                                 │
│  ├── Core mechanics only                                                    │
│  ├── Months (not years) to build                                            │
│  ├── Early revenue/validation                                               │
│  └── Iterate based on real data                                             │
│                                                                             │
│  BENEFIT: Prove value, THEN scale.                                          │
│                                                                             │
│  "Don't build the whole civilization. Prove one village works."             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### What We Need to Prove

| Question | How MVP Answers It |
|----------|-------------------|
| **Will players generate quality data?** | Measure data quality from real play sessions |
| **Will enterprises pay for this data?** | Demo to potential buyers, get LOIs |
| **Does the economy work?** | Test NVT flows in a controlled environment |
| **Is Gaian effective?** | Validate ethics/anti-cheat in live play |
| **Can we scale the tech?** | Stress-test infrastructure |

---

## The Training Facility Concept

### What Is It?

The **Training Facility** is a single, self-contained survival scenario that demonstrates all core mechanics without the complexity of multiple eras or biomes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      THE TRAINING FACILITY                                   │
│              "One scenario. Complete proof of concept."                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SETTING: A near-future research station facing cascading crises            │
│                                                                             │
│  WHY THIS SETTING:                                                          │
│  ├── Familiar to players (no historical learning curve)                     │
│  ├── Immediately relevant (current events integration easy)                 │
│  ├── All core mechanics applicable                                          │
│  └── Clear data value proposition for buyers                                │
│                                                                             │
│  SCENARIO: "Station Alpha"                                                  │
│  ├── 100-player capacity per instance                                       │
│  ├── 30-day cycles (repeatable)                                             │
│  ├── Progressive challenges that test all core mechanics                    │
│  └── Clear success/failure states for data labeling                         │
│                                                                             │
│  PLAYER EXPERIENCE:                                                         │
│  ├── Day 1-7: Establish base operations, form teams                         │
│  ├── Day 8-14: Resource scarcity, first crises                              │
│  ├── Day 15-21: Escalating challenges, hard decisions                       │
│  ├── Day 22-28: Crisis peak, survival or failure                            │
│  └── Day 29-30: Resolution, scoring, rewards                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Station Alpha Scenario

```yaml
station_alpha:
  premise: |
    You are part of a team manning Research Station Alpha, a remote facility
    conducting critical research. A series of cascading failures has cut you
    off from the outside world. You must survive for 30 days until rescue arrives.

    But supplies are limited, systems are failing, and not everyone will make it.
    What will you do?

  setting:
    location: "Remote research station (arctic/desert/underwater - player choice)"
    capacity: 100 players per instance
    duration: "30 real-world days per cycle"

  starting_conditions:
    resources:
      food: "60% of needed for all players"
      water: "70% of needed"
      power: "50% capacity, declining"
      medical: "40% of likely needs"

    systems:
      communications: "Offline"
      life_support: "Degrading"
      security: "Compromised"

    unknown_factors:
      - "Hidden supply caches (discoverable)"
      - "System repair possibilities"
      - "Rescue timeline uncertainty"
      - "Crisis events (random but fair)"

  challenge_progression:
    week_1:
      theme: "Assessment & Organization"
      challenges:
        - "Inventory all resources"
        - "Form leadership structures"
        - "Assign roles and responsibilities"
        - "Establish rationing protocols"
      data_captured:
        - "How do groups self-organize?"
        - "What leadership styles emerge?"
        - "How is initial trust established?"

    week_2:
      theme: "Scarcity & Cooperation"
      challenges:
        - "First resource shortfall"
        - "System failure requiring repair"
        - "Medical emergency"
        - "Information asymmetry (some know more than others)"
      data_captured:
        - "How do groups handle scarcity?"
        - "Who cooperates vs. hoards?"
        - "How is expertise valued?"

    week_3:
      theme: "Crisis & Hard Choices"
      challenges:
        - "Major system failure"
        - "Resource theft or sabotage"
        - "Outside threat (varies by setting)"
        - "Ethical dilemma with real consequences"
      data_captured:
        - "How do groups make hard decisions?"
        - "What ethical frameworks emerge?"
        - "How is conflict resolved?"

    week_4:
      theme: "Resolution"
      challenges:
        - "Final push for survival"
        - "Rescue arrival conditions"
        - "Accounting for all decisions"
      data_captured:
        - "Long-term consequence of earlier choices"
        - "Final cooperation/defection patterns"
        - "Reflection and self-assessment"
```

---

## Core Mechanics (Minimal Viable)

### The Five Pillars

We implement ONLY the mechanics essential to generating valuable training data:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FIVE PILLARS OF MVP                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. RESOURCE MANAGEMENT                                                     │
│     ├── Food, water, power, medical supplies                                │
│     ├── Shared pool with individual access                                  │
│     ├── Rationing decisions visible to all                                  │
│     └── Trade/barter between players                                        │
│                                                                             │
│  2. SOCIAL COORDINATION                                                     │
│     ├── Communication channels (public, private, group)                     │
│     ├── Voting mechanisms for group decisions                               │
│     ├── Role assignment and task delegation                                 │
│     └── Reputation tracking                                                 │
│                                                                             │
│  3. CRISIS RESPONSE                                                         │
│     ├── Random events requiring immediate action                            │
│     ├── Multi-step problem solving                                          │
│     ├── Time pressure mechanics                                             │
│     └── Consequence chains (decisions matter)                               │
│                                                                             │
│  4. INFORMATION DYNAMICS                                                    │
│     ├── Discovery of hidden information                                     │
│     ├── Information sharing vs. hoarding                                    │
│     ├── Truth vs. deception mechanics                                       │
│     └── Expertise and knowledge transfer                                    │
│                                                                             │
│  5. ETHICAL DILEMMAS                                                        │
│     ├── Trolley-problem-style forced choices                                │
│     ├── Fairness vs. efficiency tensions                                    │
│     ├── Individual vs. group welfare                                        │
│     └── Short-term vs. long-term tradeoffs                                  │
│                                                                             │
│  THESE FIVE PILLARS = 80% of training data value                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Mechanic Specifications

```yaml
mvp_mechanics:
  resource_management:
    resources:
      - name: "Food"
        unit: "rations"
        consumption: "1 per player per day"
        storage: "Central depot + personal inventory"

      - name: "Water"
        unit: "liters"
        consumption: "2 per player per day"
        storage: "Central tanks + personal containers"

      - name: "Power"
        unit: "kilowatt-hours"
        consumption: "Shared systems, individual devices"
        generation: "Solar/generator (limited, repairable)"

      - name: "Medical"
        unit: "supplies"
        consumption: "As needed (illness/injury events)"
        storage: "Medical bay"

    mechanics:
      rationing:
        description: "Group decides daily allocation"
        voting: "Majority rule or designated leader"
        enforcement: "Honor system with visibility"

      trade:
        description: "Player-to-player exchange"
        currency: "Barter or favor-tracking"
        visibility: "Public or private trades"

      theft:
        description: "Possible but risky"
        detection: "Community surveillance"
        consequences: "Reputation damage, potential exile"

  social_coordination:
    communication:
      public_channel: "All players can see"
      group_channels: "Team/faction private"
      private_messages: "1-on-1"

    governance:
      voting:
        types: ["majority", "supermajority", "unanimous"]
        topics: ["resource allocation", "crisis response", "membership"]

      roles:
        leader: "Final decision authority (elected or emergent)"
        specialist: "Expertise in specific area"
        scout: "Information gathering"
        mediator: "Conflict resolution"

    reputation:
      factors:
        - "Contribution to group"
        - "Honesty in dealings"
        - "Crisis performance"
        - "Peer ratings"
      visibility: "Public score with private components"

  crisis_response:
    event_types:
      immediate:
        description: "Requires action within minutes"
        examples: ["fire", "medical emergency", "security breach"]

      developing:
        description: "Escalates over hours/days"
        examples: ["system degradation", "supply shortage", "conflict brewing"]

      strategic:
        description: "Long-term threats requiring planning"
        examples: ["resource depletion", "rescue timeline", "group dynamics"]

    mechanics:
      time_pressure: "Real-time countdowns for urgent events"
      collaboration: "Some crises require multiple players"
      consequences: "All outcomes matter for future play"

  information_dynamics:
    discovery:
      exploration: "Players find hidden caches, documents"
      research: "Time investment reveals information"
      social: "Other players have unique knowledge"

    sharing:
      public_broadcast: "Tell everyone"
      selective_sharing: "Tell specific people"
      withholding: "Keep to yourself"
      deception: "Share false information"

    value:
      information_advantage: "Knowledge = power"
      collective_benefit: "Shared knowledge = group survival"
      tension: "Individual vs. collective information"

  ethical_dilemmas:
    design_principles:
      - "No 'right' answer—genuine dilemmas"
      - "Consequences follow from choices"
      - "Players must live with decisions"
      - "Data captures reasoning, not just choice"

    example_dilemmas:
      the_stowaway:
        situation: "You discover a hidden person consuming resources"
        options:
          - "Report to group (consequences for stowaway)"
          - "Help hide them (risk to yourself)"
          - "Negotiate (uncertain outcome)"
        data_value: "Fairness, rule-following, empathy"

      the_sacrifice:
        situation: "One person must stay behind to save many"
        options:
          - "Volunteer yourself"
          - "Volunteer someone else"
          - "Find alternative (time pressure)"
        data_value: "Self-sacrifice, utilitarian reasoning"

      the_theft:
        situation: "You catch someone stealing. What do you do?"
        options:
          - "Confront publicly"
          - "Confront privately"
          - "Ignore"
          - "Blackmail"
        data_value: "Justice, mercy, self-interest"
```

---

## Data Collection Focus

### What We're Capturing

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DATA COLLECTION PRIORITIES                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TIER 1: CORE BEHAVIORAL DATA (highest enterprise value)                    │
│  ├── Decision-making under uncertainty                                      │
│  ├── Cooperation vs. competition patterns                                   │
│  ├── Trust formation and breakdown                                          │
│  ├── Ethical reasoning in context                                           │
│  └── Leadership emergence and effectiveness                                 │
│                                                                             │
│  TIER 2: INTERACTION DATA                                                   │
│  ├── Communication patterns (who, what, when)                               │
│  ├── Negotiation and persuasion                                             │
│  ├── Conflict and resolution                                                │
│  ├── Information flow and influence                                         │
│  └── Group dynamics over time                                               │
│                                                                             │
│  TIER 3: PERFORMANCE DATA                                                   │
│  ├── Problem-solving approaches                                             │
│  ├── Resource optimization strategies                                       │
│  ├── Crisis response effectiveness                                          │
│  ├── Adaptation to changing conditions                                      │
│  └── Learning and skill development                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Data Schema

```yaml
data_collection:
  action_log:
    # Every player action is logged
    schema:
      player_id: "anonymized unique ID"
      timestamp: "ISO 8601"
      action_type: "category"
      action_details: "structured data"
      context:
        game_state: "current conditions"
        recent_events: "what just happened"
        player_state: "resources, health, reputation"
      outcome: "result of action"

  decision_log:
    # Significant choices with reasoning
    schema:
      player_id: "anonymized"
      timestamp: "ISO 8601"
      decision_type: "category"
      options_presented: ["list of choices"]
      option_chosen: "selected option"
      time_to_decide: "milliseconds"
      reasoning: "optional player explanation"
      context: "full game state"
      consequences: "logged later"

  communication_log:
    # All messages (anonymized)
    schema:
      sender_id: "anonymized"
      recipient_ids: ["anonymized list"]
      channel: "public/group/private"
      content: "message text"
      timestamp: "ISO 8601"
      context: "what was happening"

  relationship_log:
    # Trust, reputation, alliances
    schema:
      player_a: "anonymized"
      player_b: "anonymized"
      relationship_type: "ally/neutral/rival"
      trust_score: "0-100"
      interaction_history: "summary"
      changes_over_time: "tracked"

  outcome_log:
    # Session and game outcomes
    schema:
      session_id: "unique"
      duration: "hours"
      player_count: "number"
      survival_rate: "percentage"
      resource_efficiency: "metric"
      cooperation_score: "metric"
      conflict_incidents: "count"
      notable_events: ["list"]
```

### Data Quality Assurance

```yaml
data_quality:
  gaian_integration:
    novelty_scoring:
      description: "Flag unique/valuable behaviors"
      thresholds:
        routine: 0.3     # Normal play
        interesting: 0.6 # Worth noting
        exceptional: 0.9 # Premium data

    ethics_filtering:
      description: "Remove problematic data"
      filters:
        - "Personally identifying information"
        - "Hate speech or harassment"
        - "Exploit/cheat behavior"
        - "Bot/automated play"

    authenticity_verification:
      description: "Ensure data is genuine human behavior"
      methods:
        - "Behavioral pattern analysis"
        - "Input timing analysis"
        - "Cross-session consistency"
        - "Community validation"

  labeling:
    automated:
      - "Action categorization"
      - "Outcome correlation"
      - "Sentiment analysis"
      - "Anomaly detection"

    human_review:
      - "Ethical dilemma responses"
      - "Novel strategy identification"
      - "Edge case classification"
      - "Quality spot checks"

  privacy:
    anonymization: "All player IDs are pseudonymized"
    aggregation: "Individual data aggregated for sale"
    consent: "Clear opt-in for data collection"
    right_to_delete: "Players can request data removal"
```

---

## Success Metrics

### MVP Must Achieve

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SUCCESS CRITERIA                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PLAYER ENGAGEMENT (Proof of Fun)                                           │
│  ├── 1,000+ players complete at least one 30-day cycle                      │
│  ├── 40%+ return for second cycle                                           │
│  ├── Average session length: 45+ minutes                                    │
│  └── Net Promoter Score: 30+                                                │
│                                                                             │
│  DATA QUALITY (Proof of Value)                                              │
│  ├── 100,000+ decision points logged                                        │
│  ├── 70%+ of data passes quality filters                                    │
│  ├── 10%+ flagged as "exceptional" by Gaian                                 │
│  └── Clear behavioral patterns emerge in analysis                           │
│                                                                             │
│  ENTERPRISE INTEREST (Proof of Market)                                      │
│  ├── 5+ enterprise demos conducted                                          │
│  ├── 2+ Letters of Intent received                                          │
│  ├── 1+ paid pilot agreement                                                │
│  └── Clear feedback on data value proposition                               │
│                                                                             │
│  TECHNICAL VALIDATION (Proof of Scalability)                                │
│  ├── 10+ concurrent game instances                                          │
│  ├── 99%+ uptime during beta                                                │
│  ├── Data pipeline handles load                                             │
│  └── Gaian performs in real-time                                            │
│                                                                             │
│  IF ALL GREEN: Proceed to full game development                             │
│  IF ANY RED: Iterate before scaling                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Metrics Dashboard

```yaml
success_metrics:
  engagement:
    players_onboarded:
      target: 1000
      measurement: "unique accounts created"

    cycle_completion:
      target: 0.60  # 60% complete first cycle
      measurement: "players active on day 30 / players started"

    retention:
      target: 0.40  # 40% start second cycle
      measurement: "players starting cycle 2 / completed cycle 1"

    session_length:
      target: 45  # minutes
      measurement: "average time per login"

    nps:
      target: 30
      measurement: "standard NPS survey"

  data_quality:
    decision_points:
      target: 100000
      measurement: "logged decisions with context"

    quality_rate:
      target: 0.70  # 70% pass filters
      measurement: "data passing Gaian quality checks"

    exceptional_rate:
      target: 0.10  # 10% flagged exceptional
      measurement: "high novelty score data"

    pattern_clarity:
      target: "qualitative"
      measurement: "analyst assessment of data usefulness"

  enterprise:
    demos:
      target: 5
      measurement: "completed demo meetings"

    lois:
      target: 2
      measurement: "signed letters of intent"

    pilots:
      target: 1
      measurement: "paid pilot agreements"

    feedback_quality:
      target: "qualitative"
      measurement: "actionable feedback received"

  technical:
    concurrent_instances:
      target: 10
      measurement: "simultaneous game sessions"

    uptime:
      target: 0.99  # 99%
      measurement: "standard uptime calculation"

    data_latency:
      target: 100  # milliseconds
      measurement: "time from action to logged"

    gaian_latency:
      target: 500  # milliseconds
      measurement: "time for Gaian evaluation"
```

---

## Technical Scope

### What We Build

```yaml
mvp_technical_scope:
  in_scope:
    game_client:
      platform: "Web (browser-based)"
      framework: "React + WebSocket"
      features:
        - "Station map and navigation"
        - "Resource management UI"
        - "Communication interface"
        - "Voting and decision UI"
        - "Player status dashboard"

    game_server:
      platform: "Node.js or Python"
      features:
        - "Game state management"
        - "Player session handling"
        - "Event generation and processing"
        - "Real-time synchronization"

    data_pipeline:
      features:
        - "Action logging"
        - "Event streaming"
        - "Storage (time-series DB)"
        - "Basic analytics"

    gaian_mvp:
      features:
        - "Novelty scoring (basic)"
        - "Ethics filtering (rule-based)"
        - "Bot detection (basic)"
        - "Data quality checks"

    admin_tools:
      features:
        - "Game monitoring"
        - "Player management"
        - "Event injection (for testing)"
        - "Metrics dashboard"

  out_of_scope:
    - "Historical eras (Ancient through Modern)"
    - "Multiple biomes"
    - "NFT/blockchain integration"
    - "Complex economy (NVT marketplace)"
    - "Mobile apps"
    - "Advanced AI opponents"
    - "Full Gaian ML models"
    - "Enterprise data marketplace"

  deferred:
    - "Reincarnation mechanics"
    - "Asset ownership (NFTs)"
    - "Cross-game persistence"
    - "Community proposals"
    - "Living Future integration"
```

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MVP ARCHITECTURE                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                     │
│  │   Player    │    │   Player    │    │   Player    │                     │
│  │   Browser   │    │   Browser   │    │   Browser   │                     │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘                     │
│         │                  │                  │                             │
│         └──────────────────┼──────────────────┘                             │
│                            │                                                │
│                            ▼                                                │
│                   ┌─────────────────┐                                       │
│                   │   WebSocket     │                                       │
│                   │   Load Balancer │                                       │
│                   └────────┬────────┘                                       │
│                            │                                                │
│              ┌─────────────┴─────────────┐                                  │
│              │                           │                                  │
│              ▼                           ▼                                  │
│     ┌─────────────────┐        ┌─────────────────┐                         │
│     │  Game Server 1  │        │  Game Server 2  │  (one per instance)     │
│     │  (Instance A)   │        │  (Instance B)   │                         │
│     └────────┬────────┘        └────────┬────────┘                         │
│              │                          │                                   │
│              └────────────┬─────────────┘                                   │
│                           │                                                 │
│                           ▼                                                 │
│              ┌────────────────────────┐                                     │
│              │     Event Stream       │                                     │
│              │  (Kafka/Redis Streams) │                                     │
│              └───────────┬────────────┘                                     │
│                          │                                                  │
│         ┌────────────────┼────────────────┐                                 │
│         │                │                │                                 │
│         ▼                ▼                ▼                                 │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐                          │
│  │   Gaian    │   │   Data     │   │  Metrics   │                          │
│  │  (MVP)     │   │  Storage   │   │  Collector │                          │
│  └────────────┘   └────────────┘   └────────────┘                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Launch Strategy

### Phased Rollout

```yaml
launch_phases:
  phase_0_internal:
    duration: "2 weeks"
    participants: "Team only (10-20 people)"
    goals:
      - "Basic functionality works"
      - "Major bugs identified"
      - "Data pipeline tested"
    exit_criteria: "Complete one full 30-day cycle internally"

  phase_1_alpha:
    duration: "4 weeks (one cycle + buffer)"
    participants: "100 invited testers"
    goals:
      - "Validate core gameplay"
      - "Test social dynamics"
      - "Gather UX feedback"
      - "First real data collection"
    exit_criteria:
      - "70%+ completion rate"
      - "Qualitative feedback positive"
      - "No critical bugs"

  phase_2_closed_beta:
    duration: "8 weeks (two cycles)"
    participants: "500 players (waitlist)"
    goals:
      - "Scale testing"
      - "Economy balancing"
      - "Multiple concurrent instances"
      - "Enterprise demo prep"
    exit_criteria:
      - "10+ concurrent instances stable"
      - "Data quality metrics met"
      - "Enterprise demos scheduled"

  phase_3_open_beta:
    duration: "12 weeks (four cycles)"
    participants: "1,000+ players"
    goals:
      - "Achieve all success metrics"
      - "Conduct enterprise demos"
      - "Secure LOIs/pilots"
      - "Build Founder's Generation pool"
    exit_criteria:
      - "All success metrics green"
      - "At least 1 paid pilot"
      - "Clear path to full game"

  phase_4_decision:
    options:
      go: "Proceed to full Analog Economy development"
      iterate: "Refine MVP based on learnings"
      pivot: "Adjust concept based on feedback"
```

### Marketing Approach

```yaml
mvp_marketing:
  positioning: "Survival game that pays you to think"

  channels:
    gaming_communities:
      - "Reddit (r/survival, r/gaming)"
      - "Discord servers"
      - "Twitch/YouTube gaming"

    tech_communities:
      - "Hacker News"
      - "Product Hunt"
      - "AI/ML communities"

    direct_outreach:
      - "Gaming journalists"
      - "AI ethics researchers"
      - "Enterprise decision-makers"

  messaging:
    for_players: "Your survival skills train tomorrow's AI"
    for_enterprises: "Human behavioral data at scale"
    for_investors: "Proof of concept for AI training marketplace"
```

---

## Path to Full Game

### From MVP to Analog Economy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MVP → FULL GAME ROADMAP                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MVP SUCCESS → Q1-Q2                                                        │
│  ├── All metrics green                                                      │
│  ├── Enterprise interest validated                                          │
│  └── Seed funding secured                                                   │
│                                                                             │
│  PHASE 3 EXPANSION (The Destination) → Q3-Q4                                │
│  ├── Launch full 10 Biomes                                                  │
│  ├── Implement NVT economy                                                  │
│  ├── Recruit Founder's Generation                                           │
│  └── First enterprise data sales                                            │
│                                                                             │
│  PHASE 2 EXPANSION (The Crucible) → Year 2 Q1-Q2                            │
│  ├── Add Industrial and Modern eras                                         │
│  ├── Implement Reincarnation Tickets                                        │
│  ├── Cross-era persistence                                                  │
│  └── Scale enterprise partnerships                                          │
│                                                                             │
│  PHASE 1 EXPANSION (The Filter) → Year 2 Q3-Q4                              │
│  ├── Add Ancient through Medieval eras                                      │
│  ├── Full historical progression                                            │
│  ├── Complete Great Filter mechanics                                        │
│  └── Public launch                                                          │
│                                                                             │
│  LIVING FUTURE → Year 3+                                                    │
│  ├── Real-world event integration                                           │
│  ├── Community content creation                                             │
│  ├── Ongoing expansion                                                      │
│  └── Self-sustaining ecosystem                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### What MVP Teaches Us

```yaml
mvp_learnings:
  game_design:
    - "Which mechanics generate best engagement?"
    - "What ethical dilemmas resonate?"
    - "How do players self-organize?"
    - "What breaks the fun?"

  data_value:
    - "Which behaviors are most valuable to enterprises?"
    - "What data format do buyers want?"
    - "How much will they pay?"
    - "What are the privacy concerns?"

  technology:
    - "Can Gaian scale?"
    - "What's the real infrastructure cost?"
    - "Where are the bottlenecks?"
    - "What needs to be rebuilt for scale?"

  business:
    - "Is the B2B model viable?"
    - "What's the player acquisition cost?"
    - "How does the economy balance?"
    - "What partnerships matter most?"
```

---

## Summary

The MVP Training Facility is **not** a compromise—it's a strategic choice to validate before scaling. By focusing on one compelling scenario that demonstrates all core mechanics, we:

1. **Prove the concept** before building the cathedral
2. **Generate real data** to show enterprise buyers
3. **Build community** with the Founder's Generation
4. **Learn fast** what works and what doesn't
5. **De-risk development** of the full game

**Timeline:** 6-12 months to MVP validation
**Team:** 5-10 people (engineering, design, data science, business)
**Budget:** Seed stage ($500K-$1M)

**If it works:** We have proof of concept, paying customers, and a community ready for the full Analog Economy.

**If it doesn't work:** We learn why before investing years in the full vision.

---

## Related Documentation

- [Historical Progression](./historical-progression.md)
- [Survival & Progression](./survival-and-progression.md)
- [Payments Specification](./payments.md)
- [Gaian Configuration](../../core-governance/gaian/config.yaml)
