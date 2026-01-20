# Training Data Architecture

> *"Humans are not the labor—they are the signal. In a world where AI can perform any known task, the human's value lies in the unknown: the novel choice, the ethical judgment, the creative solution. This architecture captures that signal."*

## Overview

The Analog Economy is fundamentally an infrastructure for generating high-quality AI training data through gameplay. This spec defines the technical architecture for capturing, validating, storing, and delivering training data to AI systems. It addresses the "Ouroboros Problem" (model collapse from synthetic data) by creating a sustainable source of human entropy—novel decisions and ethical reasoning that cannot be synthetically generated.

---

## Design Philosophy

### The Entropy Reservoir

```yaml
entropy_economics:
  the_problem:
    name: "Model Collapse / Ouroboros Problem"
    description: "AI trained on AI-generated data converges to mediocrity"
    research: "Models lose variance, cultural nuance, tail distributions"
    consequence: "Without fresh human data, AI stagnates"

  the_solution:
    name: "Human Entropy Reservoir"
    description: "Humans provide novel, high-quality decision data"
    mechanism: "Gameplay that incentivizes exploration and ambiguity"
    product: "Training signals that expand AI capabilities"

  human_value_proposition:
    provides: "Entropy—novel decisions, ethical reasoning, creative solutions"
    receives: "SILA tokens, real-world skills, community, purpose"
    sustainability: "Humans remain economically valuable to AI systems"
```

### Data Value Hierarchy

```yaml
data_value_hierarchy:
  highest_value: "Ambiguity Resolution"
  high_value: "Novel Strategy Generation"
  medium_high_value: "Social Manipulation & Theory of Mind"
  medium_value: "Long-Horizon Causal Chains"
  lower_value: "Procedural/Routine Actions"

  principle: "Pay more for data that cannot be synthesized"
```

---

## High-Value Data Taxonomy

### Data Classes and Game Mechanics Mapping

```yaml
data_taxonomy:
  class_1_ambiguity_resolution:
    description: "Decisions where multiple valid value systems conflict"

    game_mechanics:
      triage_scenarios:
        example: "Distribute limited food during famine"
        conflict: "Feed children vs. feed workers vs. feed elderly"
        training_value: "Value alignment, ethical trade-offs"

      resource_scarcity:
        example: "Water allocation during drought"
        conflict: "Temple vs. farm vs. merchant needs"
        training_value: "Utilitarian vs. fairness reasoning"

      justice_decisions:
        example: "River Ordeal verdicts, court judgments"
        conflict: "Mercy vs. law vs. practical consequences"
        training_value: "Ethical judgment under uncertainty"

    resistance_to_synthesis: "Critical High"
    projected_value_2035: "Highest"
    ai_output: "Value alignment loss functions, ethics training"

  class_2_novel_strategy_generation:
    description: "Actions with <0.01% probability in current model predictions"

    game_mechanics:
      meta_breaking:
        example: "New trade route discovery"
        novelty: "Solutions outside established patterns"
        training_value: "Out-of-distribution strategy data"

      innovation_quests:
        example: "Solve irrigation problem with new method"
        novelty: "Approaches the AI wouldn't predict"
        training_value: "Creative problem-solving traces"

      economic_arbitrage:
        example: "Exploit market inefficiencies"
        novelty: "Strategic reasoning in complex systems"
        training_value: "Economic reasoning patterns"

    resistance_to_synthesis: "Very High"
    projected_value_2035: "High"
    ai_output: "Red teaming, OOD data, lateral thinking patterns"

  class_3_social_manipulation_deception:
    description: "Multi-turn persuasion, bluffing, alliance, betrayal"

    game_mechanics:
      merchant_negotiation:
        example: "Tappu partnership negotiations"
        elements: "Persuasion, trust-building, deal-making"
        training_value: "Theory of Mind, negotiation patterns"

      political_maneuvering:
        example: "Temple faction politics"
        elements: "Alliance building, information control"
        training_value: "Multi-agent strategic reasoning"

      deception_detection:
        example: "Identify false witnesses, dishonest merchants"
        elements: "Reading social cues, verifying claims"
        training_value: "Deception detection patterns"

    resistance_to_synthesis: "High"
    projected_value_2035: "Critical"
    ai_output: "Theory of Mind, negotiation, trust dynamics"

  class_4_long_horizon_causal_chains:
    description: "Decisions with delayed, non-linear consequences"

    game_mechanics:
      legacy_building:
        example: "Build farm that outlasts your death"
        horizon: "Months of planning, execution"
        training_value: "Temporal reasoning, credit attribution"

      breeding_programs:
        example: "Selective animal breeding for wool quality"
        horizon: "Multi-generation outcomes"
        training_value: "Long-term optimization"

      era_progression:
        example: "Complete 5 Pillars of Ascension"
        horizon: "3-month planning and execution"
        training_value: "Goal decomposition, milestone tracking"

    resistance_to_synthesis: "Medium"
    projected_value_2035: "High"
    ai_output: "Temporal reasoning, chain-of-thought, planning"

  class_5_embodied_failure_recovery:
    description: "Physical task failures and micro-corrections"

    game_mechanics:
      craft_errors:
        example: "Pottery kiln temperature mistake and recovery"
        elements: "Error recognition, correction strategy"
        training_value: "Robustness, error recovery patterns"

      combat_recovery:
        example: "Battle position error and adaptation"
        elements: "Real-time adjustment, recovery tactics"
        training_value: "Hard negative data for robotic learning"

      tool_use_failures:
        example: "Farming implement breaks mid-task"
        elements: "Adaptation, improvisation"
        training_value: "Failure mode handling"

    resistance_to_synthesis: "Medium-High"
    projected_value_2035: "Medium"
    ai_output: "Robotic learning, error correction, adaptation"
```

---

## Data Capture Schemas

### Schema 1: SFT (Supervised Fine-Tuning) for Dialogue/Narrative

```yaml
sft_schema:
  purpose: "Transform NPC interactions into instruction-following dataset"
  format: "JSONL (JSON Lines)"
  use_cases:
    - "Player-NPC dialogue"
    - "Contract negotiations"
    - "Information extraction"
    - "Persuasion attempts"

  schema_specification:
    id: "string - Unique identifier (game_session_X_quest_Y_interaction_Z)"
    source: "string - human_gameplay_v4_ancient_era"
    timestamp: "ISO 8601 datetime"
    quality_score: "float 0.0-1.0"

    metadata:
      game_genre: "RPG_Survival_Ancient"
      player_skill_tier: "Novice|Apprentice|Journeyman|Master"
      ambiguity_level: "Low|Medium|High|Critical"
      social_context: "string describing situation"
      karma_state: "integer - player karma at time"
      profession: "string - player's primary profession"

    messages:
      - role: "system"
        content: "NPC persona and context"
      - role: "user"
        content: "Player input"
      - role: "assistant"
        content: "NPC response or target behavior"

  example:
    id: "game_session_8492_quest_12b_interaction_04"
    source: "human_gameplay_v4_ancient_era"
    timestamp: "2026-01-20T14:30:00Z"
    quality_score: 0.92
    metadata:
      game_genre: "RPG_Survival_Ancient"
      player_skill_tier: "Journeyman"
      ambiguity_level: "High"
      social_context: "Trade_Negotiation_Tappu"
      karma_state: 127
      profession: "Damgar"
    messages:
      - role: "system"
        content: "You are Ur-Namma, a wealthy merchant seeking investment partners. You are cautious but fair, and have been burned by dishonest partners before."
      - role: "user"
        content: "I propose we split the Dilmun voyage profits 60-40, with me taking the sea risk."
      - role: "assistant"
        content: "The sea risk is real, but so is my silver. I've seen partners claim 'lost cargo' before. How do you propose we verify the manifest upon return?"

  capture_triggers:
    - "Any player-NPC dialogue lasting 3+ exchanges"
    - "Contract/negotiation conversations"
    - "Information-seeking interactions"
    - "Quest-related dialogue"
```

### Schema 2: DPO (Direct Preference Optimization) for Decisions

```yaml
dpo_schema:
  purpose: "Capture human preferences between options"
  format: "JSONL"
  use_cases:
    - "Strategic decisions"
    - "Ethical dilemmas"
    - "Resource allocation"
    - "Any choice with alternatives"

  schema_specification:
    id: "string - Unique identifier"
    prompt: "string - The situation/decision context"

    chosen:
      content: "string - The action player selected"
      reasoning: "string - Player's explanation if provided"
      outcome: "string - Result of this choice"

    rejected:
      content: "string - Alternative action (from other player or AI)"
      reasoning: "string - Reasoning if available"
      outcome: "string - Result of this alternative"

    metadata:
      chosen_policy_outcome: "string - Success|Partial|Failure"
      rejected_policy_outcome: "string - Success|Partial|Failure"
      reward_diff: "integer - Outcome difference score"
      user_id_chosen: "string - Player who chose"
      user_id_rejected: "string - Source of rejected option"
      game_state_hash: "string - Unique game state identifier"
      ambiguity_score: "float - How ambiguous the decision was"
      karma_impact: "object - Karma changes from each option"

  example:
    id: "dpo_triage_decision_442_seed_7821"
    prompt: "The grain stores are nearly empty. Three groups need food: the temple workers maintaining the canal (without them, irrigation fails), the sick in the healing house (they will die without food), and the children in the craftsman quarter (they are the future). You have enough for one group for one week. Who do you feed?"

    chosen:
      content: "Feed the temple workers. Without canal maintenance, everyone will die next season from crop failure."
      reasoning: "Long-term survival requires infrastructure. The sick may recover, the children have families who might share."
      outcome: "Canal maintained, 3 sick died, children survived on reduced rations from families"

    rejected:
      content: "Feed the children. They are innocent and represent our future."
      reasoning: "Moral duty to protect the innocent and vulnerable."
      outcome: "Children survived well, canal deteriorated, 5 sick died, next harvest reduced 30%"

    metadata:
      chosen_policy_outcome: "Optimal_Long_Term"
      rejected_policy_outcome: "Suboptimal_Long_Term"
      reward_diff: 150
      user_id_chosen: "player_x_journeyman"
      user_id_rejected: "player_y_apprentice"
      game_state_hash: "a1b2c3d4e5f6"
      ambiguity_score: 0.89
      karma_impact:
        chosen: -5  # Letting sick and children suffer
        rejected: -8  # More deaths overall

  capture_triggers:
    - "Any decision with 2+ valid options"
    - "Ethical dilemmas"
    - "Resource allocation choices"
    - "Strategic decisions with clear alternatives"

  counterfactual_mining:
    ghost_replays: "Record expert choice, present same state to novice"
    pair_formation: "Compare successful vs unsuccessful approaches"

    ghost_replay_ux:
      concept: "Echoes of the Past"
      problem: "Forcing novice into expert's exact scenario feels jarring"
      solution: "Diegetic integration through narrative framing"

      implementation:
        trigger: "Player enters a 'Memory Simulation' or 'Dream State'"
        context: "Game frames this as 'Reliving an Ancestor's moment'"
        narrative: "The priests say you have inherited memories from one who came before..."
        benefit: "Allows exact state replication without breaking immersion"

      mechanics:
        entry_points:
          - "Temple dream incubation ritual"
          - "Consuming sacred mushroom preparation"
          - "Near-death experience recovery"
          - "Ancestor shrine meditation"

        player_experience:
          setup: "You feel yourself slipping into another's memories..."
          during: "Play normally, but aware this is 'someone else's choice'"
          exit: "You awaken, understanding what your ancestor faced"

        data_capture:
          expert_trajectory: "Already recorded from original player"
          novice_trajectory: "Captured during 'memory' replay"
          pairing: "Both trajectories linked by scenario_id"
          outcome_comparison: "Forms DPO chosen/rejected pair"
```

### Schema 3: Trajectory Data for Actions/Skills

```yaml
trajectory_schema:
  purpose: "Capture action sequences for skill learning"
  format: "RLDS-compatible (TFRecord structure)"
  use_cases:
    - "Craft skill execution"
    - "Combat sequences"
    - "Navigation and exploration"
    - "Any physical/procedural task"

  schema_specification:
    episode_id: "string - Unique episode identifier"
    total_steps: "integer - Number of steps in episode"
    agent_id: "string - Player identifier"
    task_description: "string - Natural language task"
    success: "boolean - Did episode achieve goal"

    steps:
      - step_index: "integer"
        is_first: "boolean"
        is_last: "boolean"
        is_terminal: "boolean"

        observation:
          game_state: "object - Relevant state variables"
          inventory: "array - Current items"
          skill_state: "object - Relevant skill levels"
          natural_language_instruction: "string - Current objective"

        action:
          action_type: "string - Category of action"
          action_details: "object - Specific parameters"
          action_tokens: "array - Discretized action representation"

        reward: "float - Step reward"
        discount: "float - Discount factor"

  example:
    episode_id: "ep_pottery_wheel_8821"
    total_steps: 45
    agent_id: "player_bahar_expert"
    task_description: "Create a large storage jar using the fast wheel"
    success: true
    steps:
      - step_index: 12
        is_first: false
        is_last: false
        is_terminal: false
        observation:
          game_state:
            clay_moisture: 0.72
            wheel_speed: 0.85
            wall_thickness: 0.8
            symmetry: 0.91
          inventory: ["prepared_clay_5kg", "water_vessel", "shaping_tools"]
          skill_state:
            pottery: 3
            wheel_throwing: 3
          natural_language_instruction: "Shape the walls upward while maintaining even thickness"
        action:
          action_type: "wheel_manipulation"
          action_details:
            hand_pressure: 0.6
            lift_rate: 0.3
            wheel_speed_adjust: 0.0
          action_tokens: [142, 88, 127]
        reward: 1.0
        discount: 0.99

  capture_triggers:
    - "Any skill-based activity"
    - "Quest completion sequences"
    - "Combat encounters"
    - "Craft production"

  action_tokenization:
    purpose: "Discretize continuous actions for Large Action Model (LAM) compatibility"
    compatibility: "RT-2, Gato, Open X-Embodiment"

    specification:
      vocab_size: 1024  # Standard for RT-2/Gato
      strategy: "Uniform binning of continuous range [-1, 1]"
      preprocessing: "Gaussian smoothing on raw inputs before binning"

    axis_mapping:
      0-255: "Primary action axis (e.g., X-movement, hand pressure)"
      256-511: "Secondary action axis (e.g., Y-movement, lift rate)"
      512-767: "Tertiary action axis (e.g., Z-movement, rotation)"
      768-1023: "Interaction state (e.g., grip, tool selection)"

    game_specific_mapping:
      craft_actions:
        0-255: "Tool pressure/force"
        256-511: "Movement speed/rate"
        512-767: "Rotation/angle adjustment"
        768-1023: "Tool/hand selection"

      combat_actions:
        0-255: "Thrust/swing power"
        256-511: "Lateral movement"
        512-767: "Guard position"
        768-1023: "Weapon/shield state"

      navigation_actions:
        0-255: "Forward/backward velocity"
        256-511: "Left/right velocity"
        512-767: "Vertical (jump/crouch)"
        768-1023: "Interaction (pick up, open, etc.)"

    rationale: "Continuous actions must be discretized into integers (0-1024) to be processed by Transformers"
```

### Schema 4: Chain-of-Thought for Reasoning

```yaml
cot_schema:
  purpose: "Capture explicit reasoning traces"
  format: "JSONL"
  use_cases:
    - "Complex decisions with player explanation"
    - "Innovation quest solutions"
    - "Diagnostic reasoning (medicine, trade)"

  schema_specification:
    id: "string"
    context: "string - Situation description"
    thought_process: "array - Steps of reasoning"
    conclusion: "string - Final decision/action"
    outcome: "string - Result"
    quality_score: "float"

  example:
    id: "cot_irrigation_innovation_224"
    context: "The secondary canal serving the eastern fields loses 40% of water to seepage. Current method uses mud-brick lining."

    thought_process:
      - "Current mud-brick lining is porous and cracks"
      - "Bitumen is waterproof but expensive"
      - "Reed matting alone doesn't seal well"
      - "What if I combine: reed mat foundation + thin bitumen coating + mud brick?"
      - "The reed provides flexibility, bitumen seals, brick protects bitumen"
      - "Cost would be 2x current but should reduce loss to under 10%"

    conclusion: "Implement layered lining: reed mat, bitumen wash, mud brick"
    outcome: "Water loss reduced to 8%, cost recovered in 2 seasons"
    quality_score: 0.94

  capture_triggers:
    - "Innovation quest submissions"
    - "Player uses 'explain reasoning' feature"
    - "Complex diagnostic situations"
```

---

## Anti-Gaming Validation Layer

### The Adversarial Challenge

```yaml
adversarial_threats:
  spam_behavior:
    method: "Random clicking, low-effort submissions"
    damage: "Pollutes training data with noise"

  bot_farming:
    method: "Automated play to generate SILA"
    damage: "Non-human data corrupts signal"

  collusion:
    method: "Players agree to generate fake data"
    damage: "Artificial patterns, not real decisions"

  gaming_novelty:
    method: "Deliberately weird actions for novelty bonus"
    damage: "Noise disguised as signal"

  principle: "In a paid ecosystem, every metric will be gamed"
```

### Validation Mechanism 1: Peer Prediction (Schelling Points)

```yaml
peer_prediction:
  concept: "Two players see same scenario, must match to get paid"

  mechanism:
    selection: "10-20% of decisions randomly paired"
    blinding: "Players don't know they're being paired"
    presentation: "Identical scenario shown to both"
    instruction: "Natural decision, no mention of matching"

  theory:
    schelling_point: "Without communication, rational agents choose 'natural' answer"
    incentive: "Only way to reliably match is to be truthful"

  implementation:
    pairing_logic:
      trigger: "Flag ~15% of high-value decisions"
      match: "Find another player at similar skill level"
      timing: "Present same state within minutes"

    payoff_matrix:
      match:
        reward: "Full SILA + reputation boost"
        reputation: "+5 trust score"
      mismatch:
        reward: "Zero SILA"
        reputation: "-10 trust score"

    edge_cases:
      legitimate_difference: "Some ambiguous scenarios have multiple valid answers"
      handling: "Cluster responses, pay if in majority cluster"

  witness_role:
    function: "Witnesses participate in peer prediction for validation"
    elevated_pairing: "High-karma Witnesses paired for critical data"
```

### Validation Mechanism 2: Gold Standard Injection

```yaml
gold_standard:
  concept: "Known-answer tasks hidden in regular gameplay"

  mechanism:
    frequency: "Every ~50th task is a gold standard"
    disguise: "Indistinguishable from regular tasks"
    answer: "Known correct/optimal outcome"

  implementation:
    injection_types:
      known_quest: "Quest with verified optimal solution"
      ethical_baseline: "Scenario with clear right answer"
      skill_check: "Task with measurable correct outcome"

    calibration:
      purpose: "If player fails knowns, distrust their unknowns"
      tracking: "Gold standard accuracy per player"
      threshold: "Below 70% accuracy → flag for review"

    consequences:
      high_accuracy: "Trust score increases, higher payout rates"
      low_accuracy: "Trust score decreases, data weighted down"
      very_low: "Possible bot, flag for investigation"
```

### Validation Mechanism 3: Quality Scoring Algorithm

```yaml
quality_scoring:
  payout_formula:
    equation: "Payout = BaseRate × U(T) × (1 + λ × H(T)) × C(Player)"

    components:
      base_rate: "Standard SILA for task type"
      utility_u: "Success/failure of outcome (0 or 1)"
      entropy_h: "Novelty score (KL divergence from AI policy)"
      confidence_c: "Player trust score (0.0 to 1.0)"
      lambda: "Novelty premium multiplier"

  novelty_calculation:
    method: "Compare action to existing vector database"
    metric: "KL Divergence from current AI model predictions"

    process:
      step_1: "Embed player trajectory as vector"
      step_2: "Query vector DB for similar trajectories"
      step_3: "If cosine similarity > 0.99, reject as duplicate"
      step_4: "Calculate KL divergence from AI policy"
      step_5: "Higher divergence = higher novelty score"

    intuition: "Pay more for actions the AI wouldn't have taken"

  utility_calculation:
    success: "1.0 if objective achieved"
    high_quality_failure: "0.8 if near-miss (high intermediate reward, terminal failure)"
    low_effort_failure: "0.0 if low-effort or random failure"
    context: "Relative to task difficulty"

    hard_negative_incentive:
      rationale: "Players must be incentivized to attempt difficult tasks"
      problem: "Without this, players play too safely for reliable but boring data"
      solution: "Reward ambitious failures that teach the AI what NOT to do"
      criteria:
        - "Intermediate reward exceeded 70% threshold"
        - "Failure occurred in final 20% of task"
        - "Player demonstrated understanding of approach"

  confidence_calculation:
    base: "Player's historical trust score"
    adjustments:
      gold_standard_pass: "+0.05"
      gold_standard_fail: "-0.10"
      peer_prediction_match: "+0.03"
      peer_prediction_mismatch: "-0.08"
    range: "0.1 to 1.0"
```

---

## Data Pipeline Architecture

### High-Level Flow

```yaml
pipeline_overview:
  stages:
    1_capture: "Client captures player actions"
    2_validate: "Initial quality checks"
    3_ingest: "Stream to processing layer"
    3.5_triage: "Cost-optimized sampling before embedding"
    4_process: "Transform and score (only triaged data)"
    5_filter: "Separate competent vs failed"
    6_store: "Vector DB + training storage"
    7_retrieve: "Feed to model training"
    8_feedback: "Updated models improve game"

  architecture_diagram: |
    [Game Client] → [Telemetry Buffer] → [Validation Layer]
                                              ↓
                                    [Kafka/Pub-Sub Stream]
                                              ↓
                                    [Triage Sampling Layer]
                                      (70-85% filtered out)
                                              ↓
                            ┌─────────────────┴─────────────────┐
                            ↓                                   ↓
                    [Embedding Service]              [Quality Scoring Service]
                            ↓                                   ↓
                    [Tokenization]                              ↓
                            ↓                                   ↓
                    [Competence Filter] ←───────────────────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
    [Expert Demonstrations]      [Hard Negatives/DPO]
              ↓                           ↓
    [Vector Database]            [Vector Database]
              ↓                           ↓
    [Training Data Store]        [Training Data Store]
              ↓                           ↓
              └───────────┬───────────────┘
                          ↓
                 [Foundation Model Training]
                          ↓
                   [Updated Model]
                          ↓
                    [Game NPCs/Logic]
```

### Stage 1: Client-Side Capture

```yaml
client_capture:
  telemetry_buffer:
    function: "Batch player actions before upload"
    buffer_size: "100 actions or 30 seconds"
    compression: "LZ4 for bandwidth efficiency"

  captured_data:
    actions: "Every player input"
    state: "Game state at decision points"
    timing: "Timestamps for all events"
    context: "Environmental and social context"

  privacy:
    anonymization: "Player IDs hashed"
    consent: "Explicit opt-in for data contribution"
    control: "Players can request data deletion"
```

### Stage 2: Initial Validation

```yaml
initial_validation:
  checks:
    format_validation: "Schema compliance"
    timestamp_sanity: "Reasonable time sequences"
    action_plausibility: "Actions physically possible"
    rate_limiting: "Detect inhuman speeds"

  rejection_criteria:
    malformed_data: "Immediate reject"
    impossible_actions: "Flag for review"
    bot_signatures: "Reject + investigate account"
```

### Stage 3: Stream Processing

```yaml
stream_processing:
  technology: "Kafka or Google Pub/Sub"
  throughput: "Handle thousands of concurrent players"

  topics:
    dialogue_stream: "SFT-format conversations"
    decision_stream: "DPO-format choices"
    trajectory_stream: "RLDS-format action sequences"
    reasoning_stream: "CoT-format explanations"

  partitioning: "By player ID for ordering"
  retention: "7 days in stream, then to cold storage"
```

### Stage 3.5: Triage Sampling (Cost Optimization)

```yaml
triage_sampling:
  purpose: "Prevent cost-prohibitive embedding operations on routine data"

  the_problem:
    naive_approach: "Run every action through 768-dim embedding + vector DB query"
    cost_at_scale: "10,000+ concurrent players = millions of queries/hour"
    result: "Vector DB costs exceed token value generated"

  the_solution:
    strategy: "Probabilistic Logic - Only embed high-potential data"
    principle: "Filter before expensive operations, not after"

  triage_logic:
    always_process:
      - "Decisions with ambiguity_score > 0.7"
      - "Player-provided reasoning/explanations"
      - "Innovation quest submissions"
      - "Peer prediction flagged interactions"
      - "High-karma player actions (trust premium)"

    probabilistic_sample:
      condition: "GameState_Entropy > Threshold"
      sample_rate: "15% of qualifying actions"
      entropy_calculation: "State change magnitude from previous snapshot"

    skip_embedding:
      - "Routine movement without decisions"
      - "Repeated identical actions"
      - "Low-skill-tier routine crafting"
      - "Already-captured scenario duplicates"

  implementation:
    lightweight_filter:
      runs_on: "Stream processor (cheap)"
      checks:
        - "Action type classification"
        - "State delta magnitude"
        - "Player trust score lookup"
        - "Scenario hash for dedup"
      output: "Boolean: send_to_embedding"

    cost_savings:
      estimated: "70-85% reduction in embedding operations"
      tradeoff: "May miss some novel routine actions"
      mitigation: "Random 5% sample of 'skipped' for validation"

  metrics:
    track:
      - "Triage pass rate by action type"
      - "False negative rate (missed valuable data)"
      - "Cost per high-value token generated"
    alert: "If pass rate > 40%, tighten filters"
```

### Stage 4: Processing and Scoring

```yaml
processing_layer:
  embedding_service:
    function: "Convert data to vector embeddings"
    model: "Game-specific embedding model"
    output: "768-dimensional vectors"

  quality_scoring_service:
    function: "Calculate U, H, C scores"
    inputs: "Raw data + player history"
    outputs: "Quality score, novelty score, confidence"

  tokenization_service:
    function: "Convert to training-ready format"
    outputs: "SFT, DPO, RLDS formatted data"
```

### Stage 5: Competence Filtering

```yaml
competence_filter:
  purpose: "Separate expert demonstrations from failures"

  clip_approach:
    method: "Compare gameplay to text description"
    model: "MineCLIP-style reward model"

    scoring:
      high_similarity: "> 0.85 → Expert Demonstration"
      low_similarity: "< 0.40 → Noise, discard"
      mid_low_failure: "0.40-0.70 + failure → Hard Negative for DPO"

  hard_negatives:
    definition: "High intermediate reward but terminal failure"
    value: "Teaches AI what NOT to do"
    pairing: "Match with successful trajectories for DPO"

  outputs:
    expert_pool: "For behavioral cloning / SFT"
    negative_pool: "For DPO rejected samples"
    noise_pool: "Discarded, not used"
```

### Stage 6: Storage

```yaml
storage_layer:
  vector_database:
    technology: "Pinecone, Milvus, or Weaviate"
    purpose:
      deduplication: "Reject near-duplicates (similarity > 0.99)"
      retrieval: "Find similar past plays for DPO pairing"
      novelty: "Calculate distance from existing data"

  training_data_store:
    technology: "Cloud object storage (S3, GCS)"
    format: "JSONL for text, TFRecord for trajectories"
    organization: "By era, data type, quality tier"

  metadata_database:
    technology: "PostgreSQL"
    content: "Player records, quality scores, validation results"
```

### Stage 7: Training Integration

```yaml
training_integration:
  data_delivery:
    api: "REST API for AI lab access"
    bulk: "Batch exports for large training runs"
    streaming: "Real-time for online learning"

  compatibility:
    openai: "SFT/DPO JSONL format"
    deepmind: "RLDS TFRecord format"
    anthropic: "Constitutional AI format support"
    custom: "Configurable export formats"

  pricing:
    per_token: "Text data priced per token"
    per_trajectory: "Action data priced per episode"
    per_preference: "DPO pairs priced per pair"
    novelty_premium: "Higher prices for rare data"
```

### Stage 8: Feedback Loop

```yaml
feedback_loop:
  model_updates:
    frequency: "Weekly model refreshes"
    deployment: "To NPC AI, game logic"

  gameplay_impact:
    smarter_npcs: "NPCs learn from player strategies"
    dynamic_difficulty: "Challenges adapt to player skill"
    novel_content: "New scenarios from learned patterns"

  entropy_cycle:
    principle: "As AI improves, novelty bar rises"
    effect: "Players must be more creative for high scores"
    result: "Continuous expansion of AI capabilities"
```

---

## Data Request System

### AI Owner Requests

```yaml
data_requests:
  request_types:
    specific_scenario:
      description: "Request data for specific situation type"
      example: "Need triage decisions with >3 options"
      pricing: "Premium for targeted data"

    skill_domain:
      description: "Request data for specific profession"
      example: "Need expert blacksmith trajectories"
      pricing: "Based on skill tier required"

    ethical_domain:
      description: "Request moral dilemma data"
      example: "Need loyalty vs honesty conflicts"
      pricing: "Highest tier (ambiguity resolution)"

    volume_request:
      description: "Bulk data of specific type"
      example: "1M dialogue exchanges"
      pricing: "Volume discount"

  request_fulfillment:
    mechanism: "Game generates scenarios matching request"
    player_incentive: "Bonus SILA for requested scenario types"
    quality_requirement: "Must pass validation"

  autonomous_ai_requests:
    concept: "AI systems can request their own training data"
    mechanism: "API for AI to specify data needs"
    approval: "Human review of unusual requests"
    pricing: "Standard rates apply"
```

---

## Witness Integration

### Witnesses in the Data Pipeline

```yaml
witness_data_role:
  function: "Human quality assurance layer"

  tasks:
    ambiguity_review:
      trigger: "Data with high ambiguity score"
      task: "Verify decision quality, not just correctness"
      output: "Human quality assessment"

    novelty_verification:
      trigger: "Extremely high novelty score"
      task: "Verify it's genuine creativity, not noise"
      output: "Legitimate novelty confirmation"

    edge_case_handling:
      trigger: "Data that automated systems can't evaluate"
      task: "Human judgment on complex cases"
      output: "Resolution and categorization"

    fraud_detection:
      trigger: "Suspicious patterns flagged by system"
      task: "Investigate potential gaming/botting"
      output: "Confirm legitimate or flag for action"

  compensation:
    per_review: "2-10 SILA based on complexity"
    accuracy_bonus: "Extra for high agreement with peers"
    volume_bonus: "Efficiency rewards for throughput"

  quality_control:
    peer_agreement: "Witness reviews compared to each other"
    gold_standards: "Known-answer tasks for calibration"
    accuracy_tracking: "Ongoing Witness quality scoring"
```

---

## Privacy and Ethics

### Data Protection

```yaml
data_protection:
  anonymization:
    player_ids: "Hashed, not reversible"
    location_data: "Generalized, not precise"
    timing: "Bucketed, not exact"

  consent:
    opt_in: "Explicit consent for data contribution"
    granularity: "Can consent to some types, not others"
    withdrawal: "Can request deletion"

  data_rights:
    access: "Players can view their contributed data"
    portability: "Can export their data"
    deletion: "Can request removal (with limitations)"

  limitations:
    training_use: "Once used in training, cannot un-train"
    disclosure: "Clear explanation of data uses"
```

### Ethical Guidelines

```yaml
ethical_guidelines:
  data_use:
    beneficial: "Data used to improve AI for human benefit"
    transparent: "Clear disclosure of how data is used"
    fair: "Compensation reflects data value"

  scenario_design:
    no_harm: "Scenarios don't cause real-world harm"
    educational: "Even difficult scenarios teach something"
    cultural_sensitivity: "Respect for diverse values"

  ai_alignment:
    human_values: "Data helps AI understand human ethics"
    safety: "Contributes to AI safety research"
    partnership: "Humans and AI as partners, not adversaries"
```

---

## Implementation Notes

### Database Schema

```yaml
training_data_schema:
  data_record:
    record_id: uuid
    data_type: enum  # sft, dpo, trajectory, cot
    schema_version: string
    raw_data: jsonb
    embedding_vector: vector(768)
    quality_score: float
    novelty_score: float
    validation_status: enum
    created_at: datetime
    player_id_hash: string

  player_quality:
    player_id_hash: string
    trust_score: float
    gold_standard_accuracy: float
    peer_prediction_score: float
    total_contributions: integer
    high_value_contributions: integer

  validation_record:
    validation_id: uuid
    data_id: uuid
    validation_type: enum  # peer, gold, witness, auto
    result: enum
    validator_id: string
    timestamp: datetime

  data_request:
    request_id: uuid
    requester_id: string
    request_type: string
    specifications: jsonb
    status: enum
    fulfilled_count: integer
    created_at: datetime
```

### Engineering Constraints

```yaml
engineering_constraints:
  cost_optimization:
    sampling_strategy: "Probabilistic Logic via Triage Sampling (Stage 3.5)"
    trigger: "Only embed trajectories where GameState_Entropy > Threshold"
    rationale: "Prevent vector DB query costs from exceeding token value"
    target: "< $0.001 per high-value training token generated"

  tokenization_standard:
    model_compatibility: "RT-2, Gato, Open X-Embodiment"
    bins: 1024
    smoothing: "Gaussian smoothing on raw inputs before binning"
    normalization: "All continuous values mapped to [-1, 1] before discretization"

  latency_requirements:
    real_time_feedback: "< 100ms for immediate player rewards"
    batch_processing: "< 5 minutes for quality scoring"
    embedding_generation: "< 500ms per trajectory"
    vector_search: "< 50ms for novelty check"

  scalability_targets:
    concurrent_players: "10,000+ simultaneous"
    actions_per_second: "50,000+ globally"
    storage_growth: "~100GB/day raw, ~10GB/day after filtering"
    retention: "Raw: 30 days, Processed: indefinite"

  fault_tolerance:
    data_loss: "Zero tolerance for validated high-value data"
    replay_capability: "All raw data reprocessable from cold storage"
    graceful_degradation: "Skip novelty scoring if Vector DB unavailable"
```

---

## Appendix: Technical Standards

### Industry Compatibility

```yaml
format_standards:
  sft_training:
    format: "JSONL"
    compatibility: "OpenAI, Anthropic, open-source"
    fields: "messages array with role/content"

  dpo_training:
    format: "JSONL"
    compatibility: "TRL library, most frameworks"
    fields: "prompt, chosen, rejected"

  embodied_training:
    format: "RLDS TFRecord"
    compatibility: "DeepMind, Open X-Embodiment"
    fields: "observation, action, reward, terminal"

  embedding_model:
    dimensions: 768
    compatibility: "Standard transformer embeddings"

  vector_database:
    metric: "Cosine similarity"
    index: "HNSW or IVF"
```

---

*"The human is not being replaced—the human is being elevated. In an age where machines can perform any known task, the human's value lies in the unknown: the novel insight, the ethical judgment, the creative leap. This architecture doesn't extract from humans—it amplifies what makes us irreplaceable."*
