# Director AI: The Invisible Hand

> "The best game masters are invisible. Players should feel the world is alive, not that they're being managed."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Core Systems](#3-core-systems)
4. [Drama Curve Management](#4-drama-curve-management)
5. [Event Orchestration](#5-event-orchestration)
6. [Player State Monitoring](#6-player-state-monitoring)
7. [Era-Specific Behaviors](#7-era-specific-behaviors)
8. [Training Data Implications](#8-training-data-implications)
9. [Implementation Phases](#9-implementation-phases)

---

## 1. Overview

The Director AI is the invisible orchestrator that manages pacing, tension, and narrative flow across all game instances. It ensures players experience meaningful challenges without feeling manipulated, creating the conditions for authentic decision-making that generates valuable training data.

### What the Director Is

- A **tension manager** that prevents both boredom and overwhelming chaos
- An **event scheduler** that times challenges for maximum dramatic impact
- A **difficulty balancer** that adapts to player skill without obvious rubberbanding
- A **story enabler** that creates the conditions for emergent narratives

### What the Director Is NOT

- A storyteller (players create their own stories)
- A difficulty slider (it's about pacing, not making things easier/harder)
- A punishment system (challenges are opportunities, not penalties)
- A visible character or narrator

---

## 2. Design Philosophy

### 2.1 The Goldilocks Principle

The Director maintains what we call the "Goldilocks Zone" - a state where players face:
- Enough challenge to stay engaged
- Enough success to feel competent
- Enough uncertainty to create tension
- Enough agency to feel in control

```
Disengagement Curve:

Player State     |  Too Easy  |  Goldilocks  |  Too Hard  |
-----------------|------------|--------------|------------|
Engagement       |    Low     |     High     |    Low     |
Decision Quality |   Lazy     |   Thoughtful |   Panicked |
Training Value   |    Low     |     High     |    Low     |
Retention        |   Churn    |    Retain    |   Churn    |
```

### 2.2 Invisible Hand Doctrine

Players should never:
- Feel "saved" by the game
- Notice artificial difficulty spikes
- Recognize scripted events as scripted
- Attribute outcomes to anything but their choices and circumstance

Players should always:
- Feel the world is indifferent to them
- Attribute success to their skill and preparation
- Attribute failure to their mistakes or bad luck
- Believe they could have done better

### 2.3 Authentic Decision Training

For AI training data, we need decisions made under realistic conditions:
- Not too stressed (panic responses are low-quality)
- Not too relaxed (autopilot responses are low-quality)
- Facing genuine tradeoffs (not obvious choices)
- With time to deliberate (but not infinite time)

---

## 3. Core Systems

### 3.1 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      DIRECTOR AI                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   MONITOR   │  │  EVALUATE   │  │  ORCHESTRATE│         │
│  │             │  │             │  │             │         │
│  │ - Players   │  │ - Tension   │  │ - Events    │         │
│  │ - Resources │  │ - Pacing    │  │ - Resources │         │
│  │ - Events    │  │ - Fairness  │  │ - NPCs      │         │
│  │ - Time      │  │ - Variety   │  │ - Weather   │         │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘         │
│         │                │                │                 │
│         └────────────────┼────────────────┘                 │
│                          │                                  │
│                    ┌─────▼─────┐                            │
│                    │  DECIDE   │                            │
│                    │           │                            │
│                    │ Rule-based│                            │
│                    │ Thresholds│                            │
│                    │ Cooldowns │                            │
│                    └───────────┘                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 State Variables

The Director tracks these aggregate variables per instance:

```yaml
director_state:
  # Tension Metrics (0.0 - 1.0)
  global_tension: 0.45          # Average stress across all players
  resource_scarcity: 0.30       # How constrained resources are
  conflict_level: 0.25          # Active disputes/wars
  environmental_threat: 0.40    # Weather, disasters, disease

  # Pacing Metrics
  time_since_major_event: 72    # Hours since last catastrophe
  time_since_relief: 24         # Hours since last good news
  current_phase: "rising"       # rising, climax, falling, calm

  # Player Aggregate Metrics
  average_wellbeing: 0.65       # Across all players
  player_churn_risk: 0.15       # Predicted departure rate
  decision_quality: 0.70        # Based on outcome variance

  # Balance Metrics
  gini_coefficient: 0.35        # Resource inequality
  cooperation_index: 0.60       # vs competition
  knowledge_progress: 0.45      # Codex completion in this era
```

### 3.3 Input Channels

The Director receives data from:

| Channel | Data Type | Update Frequency |
|---------|-----------|------------------|
| Player Telemetry | Health, stress, inventory, actions | Real-time |
| Economy Monitor | Prices, trade volume, scarcity | Every 5 minutes |
| Social Graph | Alliances, conflicts, isolation | Every 15 minutes |
| Environment State | Weather, seasons, disasters | Every hour |
| Event History | Recent events, player reactions | Continuous |
| NPC Reports | AI population mood, needs | Every 30 minutes |

---

## 4. Drama Curve Management

### 4.1 The Natural Drama Arc

Every play session should feel like a story, even without explicit narrative:

```
Tension
   │
   │         ╭───╮ Climax
   │        ╱     ╲
   │       ╱       ╲ Falling Action
   │      ╱         ╲
   │  ╱──╱ Rising    ╲──╮
   │ ╱   Action         ╲ Resolution
   │╱ Setup               ╲_____ New Setup
   └────────────────────────────────────▶ Time
          Session Arc (4-6 hours)
```

### 4.2 Tension Bands

The Director operates within defined tension bands:

```yaml
tension_bands:
  critical_low:
    range: [0.0, 0.2]
    action: "inject_challenge"
    examples:
      - "Trigger resource scarcity event"
      - "Introduce rival faction pressure"
      - "Spawn environmental challenge"

  low:
    range: [0.2, 0.35]
    action: "gentle_pressure"
    examples:
      - "Reduce spawn rates slightly"
      - "Introduce rumors of coming hardship"
      - "Create minor social friction"

  optimal:
    range: [0.35, 0.65]
    action: "maintain"
    examples:
      - "Let player agency drive events"
      - "Respond reactively, not proactively"
      - "Introduce opportunities, not threats"

  high:
    range: [0.65, 0.8]
    action: "offer_relief"
    examples:
      - "Improve weather conditions"
      - "Spawn helpful NPC encounter"
      - "Create cooperation opportunity"

  critical_high:
    range: [0.8, 1.0]
    action: "emergency_relief"
    examples:
      - "Deus ex machina (very rare)"
      - "Enemy faction faces own crisis"
      - "Resource discovery event"
```

### 4.3 Pacing Rules

```yaml
pacing_rules:
  # Major catastrophe cooldowns
  catastrophe_cooldown_hours: 48
  catastrophe_per_instance_week: 1-2

  # Relief windows
  min_calm_between_crises: 24h
  max_continuous_pressure: 8h

  # Session pacing
  target_session_climax: "60-70% through session"
  resolution_before_logout: "allow 30min cooldown"

  # Player-specific
  new_player_protection: "48h reduced pressure"
  returning_player_ramp: "gradual reintroduction"

  # Fairness
  max_consecutive_disasters_per_settlement: 2
  bad_luck_protection_threshold: 3  # If 3 bad events, next skews positive
```

---

## 5. Event Orchestration

### 5.1 Event Categories

```yaml
event_categories:
  environmental:
    - drought
    - flood
    - storm
    - earthquake
    - wildfire
    - volcanic_activity
    - plague_outbreak

  social:
    - faction_conflict
    - trade_disruption
    - migration_wave
    - cultural_shift
    - religious_movement
    - technology_leak

  economic:
    - resource_discovery
    - resource_depletion
    - market_crash
    - trade_route_change
    - currency_crisis

  narrative:
    - mysterious_stranger
    - lost_artifact_found
    - prophecy_event
    - historical_figure_appearance
```

### 5.2 Event Selection Algorithm

```python
def select_next_event(director_state, eligible_events):
    """
    Select the most appropriate event given current state.

    Priority order:
    1. Emergency interventions (critical tension states)
    2. Pacing requirements (time since last event type)
    3. Variety requirements (avoid repetition)
    4. Training data needs (underrepresented scenarios)
    5. Player-driven opportunities (react to player actions)
    """

    scored_events = []

    for event in eligible_events:
        score = 0.0

        # Tension adjustment score
        tension_delta = event.predicted_tension_impact
        if director_state.needs_more_tension():
            score += tension_delta * 10
        elif director_state.needs_less_tension():
            score -= tension_delta * 10

        # Variety score (penalize recent event types)
        recency_penalty = director_state.recency_of(event.category)
        score -= recency_penalty * 5

        # Training data score (boost underrepresented scenarios)
        data_gap_bonus = training_data_needs.gap_score(event.type)
        score += data_gap_bonus * 3

        # Contextual fit score (does this make sense right now?)
        fit_score = event.contextual_fit(director_state)
        score += fit_score * 4

        scored_events.append((event, score))

    # Weighted random selection from top candidates
    return weighted_random_select(scored_events, top_n=3)
```

### 5.3 Event Injection Methods

Events are introduced through plausible in-world mechanisms:

| Event Type | Injection Method | Visibility |
|------------|------------------|------------|
| Drought | Gradual weather shift over days | Observable |
| Raid | Scout sightings, then attack | Foreshadowed |
| Disease | First cases appear, then spread | Emergent |
| Discovery | Player exploration triggers | Player-driven feel |
| Market crash | Trade rumors precede collapse | Diegetic |
| Stranger arrival | NPC mentions seeing traveler | Natural |

**Never:** Instant appearance without cause, game notification of event, breaking immersion for drama.

---

## 6. Player State Monitoring

### 6.1 Individual Player Metrics

```yaml
player_monitoring:
  engagement_signals:
    - session_length
    - actions_per_minute
    - decision_time_average
    - logout_triggers
    - return_frequency

  stress_indicators:
    - rapid_inventory_checking
    - hesitation_before_actions
    - resource_hoarding_behavior
    - social_withdrawal
    - erratic_movement_patterns

  mastery_indicators:
    - challenge_success_rate
    - resource_efficiency
    - social_influence
    - knowledge_contribution
    - era_progression_speed

  risk_signals:
    - consecutive_failures
    - resource_depletion_trajectory
    - isolation_from_community
    - inactivity_periods
```

### 6.2 Player Archetypes (for calibration)

```yaml
player_archetypes:
  builders:
    tension_preference: 0.3-0.5
    event_preferences: ["resource_discovery", "technology_leak"]
    avoidance: ["faction_conflict", "raid"]

  explorers:
    tension_preference: 0.4-0.6
    event_preferences: ["mysterious_stranger", "lost_artifact"]
    avoidance: ["economic_crisis", "repetitive_events"]

  achievers:
    tension_preference: 0.5-0.7
    event_preferences: ["challenge_events", "competition"]
    avoidance: ["slow_burn", "social_drama"]

  socializers:
    tension_preference: 0.3-0.5
    event_preferences: ["faction_conflict", "cultural_shift"]
    avoidance: ["isolation_events", "pure_combat"]

  survivors:
    tension_preference: 0.5-0.8
    event_preferences: ["environmental", "scarcity"]
    avoidance: ["easy_mode", "handouts"]
```

### 6.3 Cohort Balancing

The Director must balance individual player needs against community health:

```
Individual Tension Target: Player's archetype preference
Community Tension Target: Average of all players, weighted by engagement

Conflict Resolution:
- If player significantly below community: allow natural exposure
- If player significantly above community: provide subtle relief opportunities
- Priority: Community health > Individual optimization
```

---

## 7. Era-Specific Behaviors

### 7.1 Ancient Era (Sumer, Egypt, etc.)

```yaml
ancient_era:
  dominant_threats:
    - environmental: 0.4  # Drought, flood, famine
    - social: 0.3         # Tribal conflict, succession
    - supernatural: 0.2   # Perceived divine intervention
    - economic: 0.1       # Trade disruption

  tension_baseline: 0.45

  era_specific_events:
    - river_flood_cycle
    - locust_swarm
    - neighboring_tribe_migration
    - religious_omens
    - royal_succession_crisis

  pacing_notes: |
    Slower pace, seasonal rhythms matter.
    Major events tied to agricultural calendar.
    Divine/supernatural framing for natural events.
```

### 7.2 Classical Era (Rome, Han, etc.)

```yaml
classical_era:
  dominant_threats:
    - social: 0.35        # Political intrigue, rebellion
    - military: 0.25      # Invasion, civil war
    - economic: 0.25      # Trade, currency, taxation
    - environmental: 0.15 # Still relevant but manageable

  tension_baseline: 0.50

  era_specific_events:
    - senate_conspiracy
    - border_incursion
    - trade_route_disruption
    - bread_and_circuses_shortage
    - provincial_rebellion

  pacing_notes: |
    Faster political cycles.
    Urban vs rural tension dynamics.
    Information travels faster (relatively).
```

### 7.3 Industrial Era

```yaml
industrial_era:
  dominant_threats:
    - economic: 0.35      # Boom/bust, labor disputes
    - social: 0.30        # Class conflict, reform movements
    - environmental: 0.20 # Pollution, resource depletion
    - technological: 0.15 # Disruption, obsolescence

  tension_baseline: 0.55

  era_specific_events:
    - factory_strike
    - market_panic
    - cholera_outbreak
    - railroad_expansion
    - reform_movement_surge

  pacing_notes: |
    Rapid change as baseline.
    Economic cycles are dominant rhythm.
    Class dynamics critical to monitor.
```

### 7.4 AI Era (Post-Singularity)

```yaml
ai_era:
  dominant_threats:
    - technological: 0.40 # AI systems, cyber
    - existential: 0.25   # Post-human challenges
    - social: 0.20        # Meaning, purpose
    - environmental: 0.15 # Climate aftermath

  tension_baseline: 0.60

  era_specific_events:
    - ai_system_malfunction
    - meaning_crisis_wave
    - human_obsolescence_event
    - digital_divide_conflict
    - biome_collapse_cascade

  pacing_notes: |
    Highest baseline tension.
    Existential themes require delicate handling.
    Players here are elite; expect high challenge.
```

---

## 8. Training Data Implications

### 8.1 Decision Quality Optimization

The Director's primary purpose for training data:

```yaml
training_data_goals:
  decision_richness:
    - Ensure decisions have multiple viable options
    - Avoid obviously correct choices
    - Create time pressure without panic
    - Include moral/ethical dimensions

  scenario_variety:
    - Track underrepresented decision types
    - Actively create conditions for rare scenarios
    - Balance individual vs collective decisions
    - Ensure cross-cultural decision contexts

  authenticity:
    - Decisions must feel consequential
    - Players must believe outcomes matter
    - No "game-y" optimization patterns
    - Natural information asymmetry
```

### 8.2 Data Collection Enhancement

```yaml
data_collection_triggers:
  high_value_moments:
    - Major resource allocation decisions
    - Alliance/conflict inflection points
    - Ethical dilemma presentations
    - Knowledge consolidation contributions
    - Leadership succession events

  director_enhancement:
    - If scenario underrepresented → nudge toward it
    - If player archetype rare → protect engagement
    - If decision quality dropping → adjust tension
    - If repetitive patterns → inject novelty
```

### 8.3 Anti-Gaming Measures

Prevent players from farming the system:

```yaml
anti_gaming:
  pattern_detection:
    - Repetitive optimal-path behavior
    - Coordination for easy scenarios
    - Artificial stress avoidance

  countermeasures:
    - Reduce predictability of events
    - Vary rewards for same actions
    - Introduce asymmetric information
    - Randomize within acceptable bounds
```

---

## 9. Implementation Phases

### 9.1 Phase 1: MVP (Rule-Based)

```yaml
mvp_director:
  implementation: "Rule-based threshold system"
  complexity: "Low"

  features:
    - Global tension tracking
    - Event cooldown timers
    - Basic catastrophe triggers
    - New player protection

  excluded:
    - Individual player profiling
    - Predictive modeling
    - Dynamic archetype detection
    - Cross-instance coordination

  rules_count: "~50 hand-crafted rules"
  update_frequency: "Weekly tuning"
```

### 9.2 Phase 2: Adaptive

```yaml
adaptive_director:
  implementation: "Statistical model with feedback loops"
  complexity: "Medium"

  additions:
    - Player archetype detection
    - Cohort-level optimization
    - A/B testing framework
    - Seasonal event calendars

  model_type: "Regression models for tension prediction"
```

### 9.3 Phase 3: Intelligent

```yaml
intelligent_director:
  implementation: "ML-driven with human oversight"
  complexity: "High"

  additions:
    - Predictive player modeling
    - Dynamic event generation
    - Cross-instance narrative coherence
    - Self-tuning parameters

  safeguards:
    - Human review for new event types
    - Bounded action space
    - Explainable decision logging
    - Kill switches for runaway patterns
```

---

## Appendix A: Director API

```python
class DirectorAPI:
    """Public interface for Director AI interactions."""

    def get_tension_state(self, instance_id: str) -> TensionState:
        """Get current tension metrics for an instance."""

    def request_event(
        self,
        instance_id: str,
        category: EventCategory,
        urgency: float = 0.5
    ) -> EventRequest:
        """Request a specific event type (Director may modify or reject)."""

    def report_player_state(
        self,
        player_id: str,
        metrics: PlayerMetrics
    ) -> None:
        """Report updated player metrics."""

    def get_recommendations(
        self,
        instance_id: str,
        lookahead_hours: int = 24
    ) -> list[EventRecommendation]:
        """Get Director's recommended events for planning."""

    def override_tension(
        self,
        instance_id: str,
        target: float,
        duration_hours: int,
        reason: str
    ) -> OverrideResult:
        """Admin override for testing or special events."""
```

---

## Appendix B: Configuration Schema

```yaml
# director_config.yaml

director:
  enabled: true
  mode: "rule_based"  # rule_based | adaptive | intelligent

  tension:
    target_range: [0.35, 0.65]
    measurement_window_minutes: 30
    smoothing_factor: 0.7

  events:
    min_cooldown_hours: 4
    max_per_day: 6
    catastrophe_cooldown_hours: 48
    variety_lookback_days: 7

  player_protection:
    new_player_hours: 48
    returning_player_ramp_hours: 24
    consecutive_failure_relief: 3

  training_data:
    scenario_variety_weight: 0.3
    decision_quality_weight: 0.4
    authenticity_weight: 0.3

  overrides:
    admin_can_override: true
    max_override_duration_hours: 168
    log_all_overrides: true
```

---

*The Director sees all but touches lightly. The best sessions are those where players never knew they were being guided.*
