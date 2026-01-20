# Ascension & Karma System

> *"The soul is not bound by the clay of the body. It rises or falls through lives beyond counting, shaped by every choice, every kindness, every cruelty. The path to liberation is long—but the path downward is swift."*

## Overview

The Ascension & Karma System governs player progression through The Analog Economy's multi-era journey from Ancient Eridu to the AI Era. This spec defines the requirements for graduating between eras, the persistent karma system that spans all lifetimes, the reincarnation mechanics following death, the secret Anunnaki quest layer, and the Witness role that connects player achievement to training data validation.

---

## Design Philosophy

### Core Principles

1. **Skill Transfer**: Knowledge learned in-game must be applicable outside the game
2. **Persistent Consequence**: Karma follows the soul across all eras and deaths
3. **Earned Progression**: Ascension requires demonstrated competence, not just time
4. **Meaningful Choice**: Decisions have real weight because consequences persist
5. **Human Value Generation**: Every mechanic serves the dual purpose of gameplay AND training data

### The Post-Labor Partnership

```yaml
human_ai_partnership:
  human_value:
    provides: "Entropy—novel decisions, ethical reasoning, ambiguity resolution"
    receives: "SILA tokens, real-world applicable skills, community"

  ai_value:
    provides: "Infrastructure, persistent world, NPC behavior, economic system"
    receives: "High-quality training data that cannot be synthetically generated"

  mutual_survival:
    principle: "Humans who can't contribute become irrelevant"
    solution: "Game teaches 'old ways'—skills for self-sufficiency"
    insurance: "If AI fails, players know how to survive"
```

---

## Ascension Requirements

### The Five Pillars of Era Graduation

```yaml
ascension_pillars:
  overview:
    time_limit: "3 months real-time maximum per era"
    purpose: "Prove readiness for next civilization stage"
    philosophy: "Not just survival—demonstrated mastery"

  pillar_1_wealth_threshold:
    name: "Economic Competence"
    requirement: "Accumulate minimum net worth"

    ancient_era_threshold: "10,000 SILA equivalent"

    what_counts:
      currency: "SILA tokens held"
      property: "Land, buildings, workshops"
      inventory: "Goods, materials, tools"
      contracts: "Active income streams"

    purpose: "Proves understanding of economic systems"
    training_data: "Economic decision-making traces"

    sila_reward: 500  # Bonus for achieving threshold

  pillar_2_legacy_creation:
    name: "Something That Outlasts You"
    requirement: "Build an inheritable enterprise or contribution"

    valid_legacies:
      productive_enterprise:
        examples:
          - "Farm with trained NPC workers"
          - "Workshop producing goods"
          - "Trade route with active contracts"
          - "Tavern or service business"
        requirement: "Must generate income without your presence"

      knowledge_transfer:
        examples:
          - "Trained apprentice who reached Journeyman"
          - "Documented innovation in the Codex"
          - "Teaching position at Edubba"
        requirement: "Knowledge persists beyond your death"

      infrastructure:
        examples:
          - "Canal section you built/maintained"
          - "Building that serves the community"
          - "Trade agreement between parties"
        requirement: "Community benefit continues"

    transfer_rules:
      inheritance:
        to: "Friend, family member, or another player"
        condition: "You release ALL rights permanently"
        benefit: "Recipient gets full ownership"
        your_benefit: "Legacy Karma bonus (+25)"

      auction:
        to: "Highest bidder"
        condition: "You receive SILA payment"
        your_benefit: "Wealth toward Pillar 1"

    training_data: "Long-horizon planning, value creation reasoning"
    sila_reward: 1000  # Bonus for creating valid legacy

  pillar_3_skill_mastery:
    name: "Transferable Knowledge"
    requirement: "Reach Journeyman (Tier 3) in at least one profession"

    why_tier_3:
      rationale: "Journeyman means true competence, not just familiarity"
      real_world: "Skills at this level are actually useful outside the game"

    valid_professions:
      any_profession: "From our 20+ documented professions"

    certification:
      method: "Witness-verified skill demonstration"
      record: "Permanent achievement in player profile"

    purpose: "Ensures players leave each era with real knowledge"
    training_data: "Skill acquisition traces, mastery demonstrations"
    sila_reward: 750

  pillar_4_karma_minimum:
    name: "Ethical Foundation"
    requirement: "Maintain karma above threshold"

    ancient_era_threshold: "50+ karma points"

    rationale:
      ethical_grounding: "Higher eras = more power = need ethical foundation"
      progression_gate: "Cannot ascend while in karmic debt"

    remediation:
      if_below: "Must earn karma before ascension allowed"
      methods: "Temple service, restitution, good deeds"

    training_data: "Ethical decision traces, value alignment data"
    sila_reward: 500

  pillar_5_innovation_contribution:
    name: "Solve Era-Defining Problems"
    requirement: "Complete 5 Innovation Quests"

    innovation_quest_system:
      source: "Era's 'Most Pressing Problems' list"
      selection: "Player chooses from available quests"
      completion: "Verified solution submitted to Codex"

    ancient_era_examples:
      irrigation:
        problem: "Water distribution inefficiency"
        solution_types: "New channel design, scheduling system"

      metallurgy:
        problem: "Bronze alloy inconsistency"
        solution_types: "Ratio optimization, process improvement"

      medicine:
        problem: "Disease outbreak response"
        solution_types: "Treatment protocol, prevention method"

      storage:
        problem: "Grain loss to pests/rot"
        solution_types: "Container design, preservation technique"

      trade:
        problem: "Contract dispute frequency"
        solution_types: "Standard terms, verification method"

    scaling:
      simultaneous_players: "Thousands working on same problems"
      different_solutions: "Many valid approaches exist"
      not_winner_take_all: "Your solution just needs to work"

    training_data: "Novel strategy generation, problem-solving traces"
    sila_reward: 200 per quest (1000 total)
```

### Time Pressure Mechanics

```yaml
time_mechanics:
  era_duration:
    maximum: "3 months real-time"
    soft_limit: "Diminishing returns begin at month 2"

  diminishing_returns:
    month_1:
      sila_multiplier: "1.0x (full rewards)"
      karma_multiplier: "1.0x"

    month_2:
      sila_multiplier: "0.75x"
      karma_multiplier: "1.0x"

    month_3:
      sila_multiplier: "0.5x"
      karma_multiplier: "1.0x"
      note: "Still possible to complete pillars"

  early_ascension:
    bonus: "Complete all 5 pillars before 60 days"
    reward: "1000 SILA bonus + 'Swift Ascender' title"

  failure_to_ascend:
    after_3_months:
      option_1: "Remain in era indefinitely"
      option_2: "Reset and try again"

    staying_indefinitely:
      allowed: "Yes, player choice"
      income: "Continue earning SILA at reduced rate"
      progression: "Cannot advance to next era"
      community: "Can help newer players"
```

### Ascension Ceremony

```yaml
ascension_event:
  trigger: "All 5 pillars completed"

  ceremony_phases:
    phase_1_verification:
      process: "System verifies all requirements"
      witness: "Assigned Witness confirms achievements"
      duration: "Immediate"

    phase_2_legacy_transfer:
      process: "Complete inheritance or auction of legacy"
      requirement: "Cannot ascend with unresolved property"
      choice: "Player decides transfer method"

    phase_3_ceremony:
      location: "Temple of relevant deity"
      event: "Ritual marking transition"
      community: "Other players can attend"

    phase_4_transition:
      process: "Character enters 'between eras' state"
      duration: "Brief (loading next era)"

    phase_5_rebirth:
      process: "Arrive in next era"
      starting_conditions: "Based on karma and achievements"
      carryover: "Karma, some knowledge, legacy bonuses"

  rewards:
    ascension_nft: "Unique NFT marking achievement"
    sila_bonus: "Era completion bonus"
    karma_bonus: "+50 karma for successful ascension"
    title: "Era-specific title (e.g., 'Ancient Adept')"
```

---

## Karma System

### Fundamental Mechanics

```yaml
karma_fundamentals:
  starting_karma: 100

  persistence:
    scope: "Karma survives death"
    duration: "Persists across ALL eras and lifetimes"
    reset: "Never resets (except through gameplay)"

  visibility:
    to_player: "Current karma shown"
    to_others: "Reputation (derived from karma) visible"
    hidden: "Total lifetime karma (Sanchita) hidden"

  range:
    minimum: 0
    maximum: "No cap (can accumulate indefinitely)"
    meaningful_thresholds:
      0: "Soul death, lowest reincarnation"
      1-24: "Animal reincarnation range"
      25-49: "Penalized human rebirth"
      50-99: "Standard human rebirth"
      100-149: "Favored human rebirth"
      150+: "Witness eligibility, special opportunities"
```

### Karma Types (Hindu Framework)

```yaml
karma_types:
  sanchita:
    name: "Total Accumulated Karma"
    description: "Sum of all karma from all lives"
    visibility: "Hidden from player"
    purpose: "Determines ultimate spiritual progress"

  prarabdha:
    name: "Active Karma"
    description: "Portion affecting current life circumstances"
    visibility: "Visible as current karma score"
    effects:
      starting_conditions: "Determines rebirth quality"
      npc_reactions: "Affects how NPCs treat you"
      luck_factor: "Influences random events slightly"

  agami:
    name: "New Karma"
    description: "Karma generated by current actions"
    visibility: "Changes shown in real-time"
    feedback: "Player sees +/- karma notifications"
```

### Karma Earning and Losing

```yaml
karma_actions:
  positive_karma:
    religious_service:
      temple_attendance: "+1 per visit"
      offering_given: "+1 to +5 based on value"
      festival_participation: "+5 per festival"
      priestly_duties: "+2 per service"

    community_service:
      corvee_labor_completed: "+3 per day"
      helping_stranger: "+2 to +10"
      teaching_skill: "+5 per student advanced"
      fair_dealing: "+1 per honest transaction"

    justice_actions:
      honest_testimony: "+3"
      helping_innocent: "+10"
      fair_judgment: "+5"
      restitution_paid: "+5"

    exceptional_deeds:
      saving_life: "+20"
      major_community_contribution: "+15"
      innovation_benefiting_many: "+10"

  negative_karma:
    religious_violations:
      temple_neglect_30_days: "-1 per additional day"
      desecration: "-50"
      false_oath: "-25"

    crimes:
      theft: "-10 to -30"
      assault: "-15 to -40"
      murder: "-100"
      false_accusation: "-15"
      perjury: "-25"

    social_violations:
      contract_breach: "-10"
      exploitation: "-15"
      betrayal: "-20 to -50"

    gameplay_meta:
      low_quality_data_submission: "-5"
      failed_validation_check: "-10"
      spam_behavior: "-20"
```

### Karma Recovery

Players can recover karma through positive actions. The system rewards genuine contribution over grinding.

```yaml
karma_recovery:
  # Daily/Routine Actions
  temple_service:
    method: "Extended religious service"
    rate: "+1 karma per day"
    notes: "Consistent small gains, requires genuine participation"

  canal_maintenance:
    method: "Infrastructure work for community"
    rate: "+2 to +5 karma per task"
    notes: "Community infrastructure, scales with difficulty"

  community_service:
    method: "Public works without payment"
    rate: "+3 karma per day"
    examples: "Building repair, cleaning, corvée labor"

  # Helping Others
  healing_the_sick:
    method: "Providing medical care to those in need"
    rate: "+3 to +10 karma"
    notes: "Scales with severity of illness and patient's poverty"

  teaching_others:
    method: "Knowledge transfer to learners"
    rate: "+5 karma"
    requirement: "Verified knowledge transfer (student demonstrates skill)"

  helping_others_succeed:
    method: "Assisting others achieve their goals"
    rate: "+10 karma"
    notes: "Major assistance, not casual help"

  # Ethical Actions
  returning_lost_property:
    method: "Return found items to rightful owner"
    rate: "+5 to +15 karma"
    notes: "Based on value of returned property"

  mediation:
    method: "Peacefully resolving conflicts between parties"
    rate: "+10 karma"
    notes: "Preventing violence through diplomacy"

  rescue_from_danger:
    method: "Saving life in perilous situations"
    rate: "+15 to +25 karma"
    notes: "Saving a life, risk to self considered"

  # Major Actions
  pilgrimage:
    method: "Journey to sacred sites"
    rate: "+20 karma"
    requirement: "Physical multi-day journey, not fast travel"

  restitution:
    method: "Pay back those wronged"
    rate: "Varies by offense (typically restores 50-75% of karma lost)"
    requirement: "Victim must accept"

  witness_verification:
    method: "Become a Witness and serve faithfully"
    rate: "+2 per validated review"
    requirement: "High accuracy rate maintained"
```

**Karma Recovery Summary Table:**

| Action | Karma Gain | Notes |
|--------|------------|-------|
| Temple service | +1/day | Consistent small gains |
| Canal maintenance | +2-5/task | Community infrastructure |
| Community service | +3/day | Public works without payment |
| Healing the sick | +3-10 | Depends on severity |
| Teaching others | +5 | Verified knowledge transfer |
| Returning lost property | +5-15 | Based on value |
| Mediation | +10 | Preventing violence |
| Helping others succeed | +10 | Altruistic major assistance |
| Rescue from danger | +15-25 | Saving a life |
| Temple pilgrimage | +20 | Multi-day journey |
| Witness service | +2/review | Training data validation |

### Sanity Recovery

Sanity represents mental well-being. It depletes through trauma, isolation, and neglect of basic needs. Recovery requires rest, social connection, and spiritual practice.

```yaml
sanity_recovery:
  # Basic Recovery
  sleep_in_safe_location:
    method: "Rest in secure shelter"
    rate: "+5 sanity per night"
    notes: "Basic recovery, requires owned or rented shelter"

  social_interaction:
    method: "Positive conversations with others"
    rate: "+2 to +5 sanity"
    notes: "Casual conversation to meaningful discussion"
    requirement: "15+ minutes of genuine interaction"

  shared_meal:
    method: "Eating with companions"
    rate: "+5 sanity"
    notes: "30+ minutes, social bonding"

  # Entertainment & Leisure
  music_entertainment:
    method: "Attending performances or listening to music"
    rate: "+5 to +10 sanity"
    notes: "Depends on performance quality"

  game_playing:
    method: "Playing games (Royal Game of Ur, etc.)"
    rate: "+5 to +10 sanity"
    notes: "Win or lose, the play itself restores"

  tavern_relaxation:
    method: "Moderate drinking and socializing"
    rate: "+5 to +8 sanity"
    warning: "Excessive drinking causes -10 sanity"

  # Temple & Spiritual
  temple_meditation:
    method: "Contemplation in sacred space"
    rate: "+10 sanity"
    requirement: "Temple access (social standing dependent)"

  confession_to_priest:
    method: "Unburdening guilt to religious authority"
    rate: "+20 sanity"
    notes: "Powerful one-time recovery for guilty conscience"
    requirement: "Access to priest, genuine confession"

  festival_participation:
    method: "Joining community celebrations"
    rate: "+15 to +25 sanity"
    notes: "Major festivals provide highest restoration"

  # Achievement & Purpose
  accomplishing_goals:
    method: "Completing major personal objectives"
    rate: "+15 sanity"
    notes: "Quest completion, business milestones, skill achievements"

  helping_others_succeed:
    method: "Assisting others achieve their goals"
    rate: "+10 sanity"
    notes: "Altruistic acts restore mental well-being"

sanity_drain_sources:
  isolation:
    3_days_alone: "Loneliness debuff begins"
    7_days_alone: "-2 sanity per day"
    14_days_alone: "-5 sanity per day"

  temple_neglect:
    7_days: "-1 sanity per day"
    14_days: "-2 sanity per day"
    30_days: "-5 sanity per day"
    60_days: "-10 sanity per day"

  trauma:
    witnessing_death: "-5 to -15 sanity"
    personal_injury: "-3 to -10 sanity"
    major_loss: "-10 to -20 sanity"
```

**Sanity Recovery Summary Table:**

| Action | Sanity Gain | Notes |
|--------|-------------|-------|
| Sleep in safe location | +5/night | Basic recovery |
| Social interaction | +2-5 | Positive conversations |
| Shared meal | +5 | Eating with companions |
| Music/entertainment | +5-10 | Attending performances |
| Game playing | +5-10 | Win or lose |
| Tavern relaxation | +5-8 | Moderate drinking |
| Temple meditation | +10 | Requires temple access |
| Accomplishing goals | +15 | Completing major tasks |
| Festival participation | +15-25 | Community celebrations |
| Helping others succeed | +10 | Altruistic acts |
| Confession to priest | +20 | Unburdening guilt |

### Cross-System Integration

Karma and Sanity interact but are not identical:

```yaml
karma_sanity_relationship:
  positive_karma_actions:
    often_restore_sanity: true
    examples:
      - "Helping others succeed (+10 karma, +10 sanity)"
      - "Teaching (+5 karma, +5 sanity from purpose)"

  sanity_without_karma:
    possible: true
    examples:
      - "Sleep restores sanity but not karma"
      - "Entertainment restores sanity but not karma"

  karma_without_sanity:
    possible: true
    examples:
      - "Dangerous rescue may cost sanity (-trauma) but gain karma"
      - "Temple service during crisis restores karma, sanity may drain"

  spiral_warning:
    low_sanity_effect: "Poor decisions, karma loss more likely"
    low_karma_effect: "Social rejection, sanity harder to maintain"
    recovery_priority: "Address sanity first—clear mind makes better choices"
```

---

## Reincarnation System

### Death Outcomes

```yaml
death_outcomes:
  karma_above_100:
    result: "Favored Human Reincarnation"
    benefits:
      starting_wealth: "50% of previous wealth carried"
      starting_conditions: "Choose profession, location"
      starting_relationships: "Some NPCs remember you fondly"
      bonus: "+10% SILA earning for first month"

  karma_50_to_99:
    result: "Standard Human Reincarnation"
    conditions:
      starting_wealth: "25% of previous wealth"
      starting_conditions: "Random within reasonable range"
      starting_relationships: "Fresh start"

  karma_25_to_49:
    result: "Penalized Human Reincarnation"
    penalties:
      starting_wealth: "0% carried"
      starting_conditions: "Unfavorable (poverty, low status)"
      starting_relationships: "Some NPCs distrust you"
      debuff: "-10% SILA earning until karma improves"

  karma_1_to_24:
    result: "Animal Reincarnation"
    species_by_karma:
      20-24: "Large animal (donkey, ox, dog)"
      15-19: "Medium animal (goat, pig)"
      10-14: "Small animal (cat, rat, bird)"
      5-9: "Tiny animal (lizard, fish)"
      1-4: "Insect (beetle, fly)"

  karma_zero:
    result: "Soul Death → Lowest Reincarnation"
    process: "Immediate death, rebirth as lowest creature"
    species: "Worm, maggot, or similar"
    path_back: "Long journey through animal forms"
```

### Animal Reincarnation Gameplay

```yaml
animal_gameplay:
  mode: "Simplified survival mode"

  perspective:
    view: "Third-person animal view"
    abilities: "Species-appropriate actions only"
    communication: "Cannot speak, limited interaction"

  objectives:
    survival: "Eat, drink, avoid predators"
    karma_earning: "Through behavior choices"

  karma_as_animal:
    positive_actions:
      helping_humans: "+5 (e.g., warning of danger)"
      peaceful_behavior: "+1 per day"
      natural_actions: "+0.5 (just existing peacefully)"

    negative_actions:
      attacking_humans: "-10"
      spreading_disease: "-5"
      destruction: "-3"
      excessive_aggression: "-2"

  ascension_through_forms:
    mechanism: "Reach karma threshold → die → rebirth as higher form"

    hierarchy:
      insect: "0-10 karma → small animal"
      small_animal: "10-20 karma → medium animal"
      medium_animal: "20-30 karma → large animal"
      large_animal: "30-50 karma → human rebirth (penalized)"

    death_as_animal:
      natural: "Rebirth based on current karma"
      violent: "May lose karma"

  time_scale:
    animal_lifespan: "Shortened (1 day = 1 season)"
    purpose: "Don't trap players forever in animal form"
    typical_recovery: "1-7 real days to return to human"
```

### The Cycle of Samsara

```yaml
samsara_cycle:
  concept: "Continuous cycle of birth, death, rebirth"

  escape_condition:
    name: "Moksha (Liberation)"
    requirement: "Complete all eras + karma threshold"
    threshold: "500+ karma at final era completion"

  moksha_achievement:
    event: "Final ascension ceremony"
    reward: "Genesis NFT + permanent legacy"
    option: "Return as guide/mentor OR exit the cycle"

  returning_as_mentor:
    role: "Help new players"
    powers: "Special Witness abilities"
    income: "Percentage of mentee SILA"
    karma: "Cannot lose karma in this state"
```

---

## The Witness System

### Role Definition

```yaml
witness_role:
  dual_purpose:
    in_game: "Sacred observers who verify truth and contracts"
    meta_game: "Human validators ensuring training data quality"

  eligibility:
    karma_requirement: "150+ karma"
    completion_requirement: "Ascended from at least one era"
    reputation_requirement: "No recent serious violations"

  invitation:
    method: "Temple priests approach with 'divine calling'"
    acceptance: "Optional but lucrative"
    training: "Brief orientation on duties"
```

### Witness Duties

```yaml
witness_duties:
  in_world_responsibilities:
    contract_witnessing:
      description: "Present at major transactions"
      process: "Observe, verify, sign tablet"
      reward: "5-20 SILA per witnessing"
      frequency: "On-demand from players"

    court_testimony:
      description: "Testify in legal disputes"
      process: "Called by court, provide truthful account"
      karma_impact: "Truth = +5, Lies = -50"
      reward: "10-30 SILA per testimony"

    skill_certification:
      description: "Verify player skill mastery claims"
      process: "Observe demonstration, confirm tier"
      reward: "10-50 SILA per certification"
      importance: "Gates Pillar 3 of ascension"

    ritual_observation:
      description: "Witness religious ceremonies"
      process: "Present at major temple events"
      reward: "15 SILA + karma"

  meta_responsibilities:
    training_data_review:
      description: "Evaluate submitted quest data"

      process:
        receive: "Flagged data needing human review"
        evaluate: "Quality, authenticity, value"
        verdict: "Approve, reject, or flag for deeper review"

      criteria:
        quality: "Is this useful training data?"
        authenticity: "Did a human genuinely do this?"
        novelty: "Is this different from existing data?"

      reward: "SILA based on reviews completed"
      bonus: "Extra for catching errors/fraud"

    peer_prediction_participation:
      description: "Schelling point validation"

      process:
        pairing: "Matched with another Witness blindly"
        scenario: "Both review same ambiguous decision"
        goal: "Responses should match if both truthful"

      reward:
        match: "Full payout + reputation boost"
        mismatch: "Zero payout + reputation penalty"

    gold_standard_verification:
      description: "Calibration checks"
      frequency: "Every 50th task is known answer"
      purpose: "Verify Witness is performing well"
      consequence: "Fail too many → lose Witness status"
```

### Witness Economics

```yaml
witness_economics:
  income_sources:
    contract_witnessing: "5-50 SILA per event"
    data_validation: "2-10 SILA per review"
    skill_certification: "10-50 SILA per certification"
    court_testimony: "10-30 SILA per appearance"

  expected_earnings:
    casual: "500-1000 SILA per month"
    dedicated: "2000-5000 SILA per month"
    elite: "5000+ SILA per month"

  benefits:
    status: "High social standing"
    access: "Temple inner circles"
    influence: "Political connections"
    karma: "Steady karma from faithful service"

  risks:
    false_witness: "-50 karma, potential exile"
    bribery: "Loss of Witness status, severe penalty"
    negligence: "Miss fraud → reputation damage"
    poor_accuracy: "Lose Witness status"
```

### Connection to Training Data Pipeline

```yaml
witness_data_connection:
  insight: "Witnesses ARE the human verification layer"

  data_flow:
    step_1: "Player completes quest/action, generates data"
    step_2: "System evaluates novelty and utility scores"
    step_3: "High-value data flagged for Witness review"
    step_4: "Witness validates quality and authenticity"
    step_5: "Validated data enters training pipeline"
    step_6: "Witness earns reward based on accuracy"

  why_witnesses:
    human_judgment: "Some quality requires human evaluation"
    adversarial_defense: "Catch bots, spam, gaming attempts"
    alignment: "Humans verify human-generated data"
    employment: "Creates jobs for high-karma players"

  quality_metrics:
    accuracy: "Witness decisions compared to gold standards"
    consistency: "Agreement with other Witnesses (peer prediction)"
    speed: "Timely reviews"
    throughput: "Volume of quality reviews"
```

---

## The Anunnaki Mystery Quest

### Discovery Mechanics

```yaml
anunnaki_discovery:
  availability:
    era: "Ancient Era only"
    rarity: "< 1% of players will complete"

  seven_fragments:
    concept: "Like collecting Boardwalk + Park Place"
    requirement: "Discover and possess all 7 clue fragments"

    fragment_sources:
      fragment_1_tablets:
        location: "Temple archive deep storage"
        access: "Requires scribe skills + temple trust"
        clue_type: "Ancient texts mentioning 'those who came before'"

      fragment_2_sailor_tales:
        location: "Taverns near the Karum"
        access: "Build relationships with old sailors"
        clue_type: "Stories of strange lights over Dilmun"

      fragment_3_metal_shards:
        location: "Deep in copper mines"
        access: "Mining skill + exploration"
        clue_type: "Metal that shouldn't exist in this era"

      fragment_4_shepherd_memory:
        location: "Remote grazing areas"
        access: "Find specific elderly NPC"
        clue_type: "Childhood vision at sacred site"

      fragment_5_star_charts:
        location: "Temple astronomical records"
        access: "High-level priest access"
        clue_type: "Planet that returns every 3,600 years"

      fragment_6_merchant_artifacts:
        location: "Trade from Magan or Meluhha"
        access: "Merchant connections, high wealth"
        clue_type: "Objects with impossible craftsmanship"

      fragment_7_dream_sequence:
        location: "Sacred site during specific astronomical event"
        access: "High karma, complete pilgrimage"
        clue_type: "Vision revealing the location"
```

### The Journey

```yaml
anunnaki_journey:
  activation:
    trigger: "Possess all 7 fragments"
    requirement: "75+ karma, close to era completion"
    event: "Vision reveals the path"

  quest_structure:
    style: "Zelda-like adventure"
    duration: "5-15 hours of gameplay"
    difficulty: "Extreme"

  phases:
    phase_1_decryption:
      task: "Combine fragments to reveal location"
      skill_needed: "Scribe ability to read ancient text"
      challenge: "Puzzle solving, language translation"

    phase_2_preparation:
      task: "Gather supplies for long journey"
      requirements:
        - "30 days of provisions"
        - "Weapons and armor"
        - "Specific ritual items"
        - "Companion or alone (choice)"

    phase_3_journey:
      terrain: "Cross desert, mountains, unknown lands"
      hazards:
        - "Environmental (heat, cold, storms)"
        - "Predators (lions, wolves)"
        - "Hostile NPCs (bandits, rival seekers)"

    phase_4_waypoints:
      number: "3 major waypoints"
      each_waypoint:
        - "NPC encounter with clues"
        - "Mini-boss or challenge"
        - "Resource resupply opportunity"

    phase_5_the_mine:
      location: "Ancient gold mine in mountains"
      discovery: "Entrance hidden, requires solving puzzle"
      atmosphere: "Growing sense of wrongness"

    phase_6_underground:
      exploration: "Descend through mine levels"
      evidence:
        - "Impossible mining equipment"
        - "Strange lighting systems"
        - "Genetic experimentation remnants"
        - "Records of human creation"

    phase_7_the_laboratory:
      discovery: "Find the Anunnaki facility"
      revelation: "Evidence of human genetic engineering"
      choice_point: "Continue deeper or retreat"

    phase_8_the_encounter:
      condition: "Only if player continues"
      meeting: "Encounter remaining Anunnaki/hybrid"
      interaction: "Dialogue, revelation, test"
      outcome: "Based on player choices"
```

### Rewards

```yaml
anunnaki_rewards:
  completion_rewards:
    tokens: "1,000,000 SILA"
    era_bypass: "Skip directly to next era"
    technology: "One advanced tech item from future era"
    title: "Touched by the Apkallu (permanent)"

  unique_benefits:
    knowledge: "Understand humanity's true origins"
    artifact: "Possess Anunnaki technology"
    connection: "Can receive 'guidance' in future eras"

  legacy:
    record: "Achievement recorded in Codex"
    nft: "Unique Anunnaki Discoverer NFT"
    community: "Join exclusive group of discoverers"

  training_data_value:
    novelty: "Extreme (< 1% will generate this data)"
    categories:
      - "Long-horizon planning and execution"
      - "Novel strategy under ambiguity"
      - "Ethical decision-making under pressure"
      - "Puzzle-solving and deduction"
```

---

## Era End-Game

### Late-Game Ancient Era

```yaml
late_game_content:
  for_ascending_players:
    focus: "Complete remaining pillars"
    activities:
      - "Final innovation quests"
      - "Legacy preparation"
      - "Witness duties if eligible"
      - "Help newer players"

  for_staying_players:
    choice: "Some may choose not to ascend"
    valid_reasons:
      - "Enjoy Ancient Era lifestyle"
      - "Building wealth without pressure"
      - "Community leadership role"
      - "Anunnaki quest pursuit"

    gameplay:
      income: "Continue earning (reduced rate after 3 months)"
      role: "Elder, mentor, community pillar"
      limitation: "Cannot progress to next era"

  community_dynamics:
    veterans: "Experienced players help newcomers"
    economy: "Mature market with established trades"
    politics: "Player governance structures mature"
```

### Failure States

```yaml
failure_handling:
  never_ascending:
    allowed: "Yes, player choice"
    consequence: "Stay in current era indefinitely"
    income: "Reduced but continuous"
    value: "Still generating training data"

  multiple_reincarnations:
    expected: "Most players need 2-3 lives per era"
    design: "Era designed for iteration"
    learning: "Each death teaches something"

  karma_death_spiral:
    risk: "Repeated bad choices → animal reincarnation"
    recovery: "Possible but time-consuming"
    design: "Natural consequence, not punishment"

  permanently_marginalized:
    possible: "If player consistently makes poor choices"
    escape: "Always possible through karma recovery"
    support: "Community and temple can help"
```

---

## Training Data Integration

### Every Mechanic Generates Data

```yaml
data_generation_mapping:
  ascension_pillars:
    pillar_1_wealth:
      data_type: "Economic reasoning traces"
      value: "Long-horizon planning, resource allocation"

    pillar_2_legacy:
      data_type: "Value creation and transfer decisions"
      value: "Long-term thinking, inheritance reasoning"

    pillar_3_skills:
      data_type: "Skill acquisition traces"
      value: "Learning patterns, mastery demonstrations"

    pillar_4_karma:
      data_type: "Ethical decision traces"
      value: "Value alignment, moral reasoning"

    pillar_5_innovation:
      data_type: "Novel strategy generation"
      value: "Problem-solving, creative solutions"

  karma_system:
    choices:
      data_type: "DPO preference pairs"
      value: "Ethical trade-off resolutions"

    consequences:
      data_type: "Causal reasoning chains"
      value: "Long-horizon consequence attribution"

  reincarnation:
    life_trajectories:
      data_type: "Full episode data"
      value: "Complete decision sequences"

  witness_system:
    validations:
      data_type: "Human quality assessment"
      value: "Data quality filtering"
```

---

## Implementation Notes

### Database Schema

```yaml
ascension_karma_schema:
  player_karma:
    player_id: uuid
    current_karma: integer
    lifetime_karma: integer  # Sanchita, hidden
    karma_history: array  # Recent changes
    current_form: enum  # human, animal_type
    reincarnation_count: integer

  ascension_progress:
    player_id: uuid
    era: string
    era_start_date: datetime
    pillar_1_wealth: object  # current value, threshold, complete
    pillar_2_legacy: object  # legacy_id if exists, complete
    pillar_3_skills: object  # highest tier, profession, complete
    pillar_4_karma: object  # current, threshold, complete
    pillar_5_innovations: object  # completed quests, required, complete

  witness_record:
    witness_id: uuid
    player_id: uuid
    appointment_date: datetime
    reviews_completed: integer
    accuracy_score: float
    reputation: integer
    earnings_total: integer
    status: enum  # active, suspended, revoked

  anunnaki_progress:
    player_id: uuid
    fragments_collected: array
    quest_started: boolean
    current_phase: integer
    completed: boolean
    completion_date: datetime
```

---

## Appendix: Philosophical Framework

### The Purpose of the Journey

```yaml
journey_purpose:
  for_the_player:
    skills: "Learn things applicable outside the game"
    income: "Earn real value (SILA)"
    community: "Connect with others on same journey"
    meaning: "Contribute to something larger"

  for_humanity:
    preservation: "Old ways knowledge preserved"
    partnership: "Humans remain valuable to AI"
    insurance: "Self-sufficiency skills if AI fails"

  for_ai:
    training_data: "High-quality human decision traces"
    alignment: "Value alignment through gameplay"
    novelty: "Entropy to prevent model collapse"
```

---

*"The soul that rises does so through its own choices—not through luck, not through birth, but through the accumulated weight of every decision, every kindness extended, every harm avoided. The path is long, but it leads somewhere. The alternative is to circle forever, learning nothing, becoming less."*
