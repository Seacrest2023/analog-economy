# NPC Behavior: The Living World

> "The city breathes. The people remember. Your reputation walks with you."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [NPC Categories](#3-npc-categories)
4. [Behavior Modes](#4-behavior-modes)
5. [Information & Intelligence](#5-information--intelligence)
6. [Law Enforcement & Social Order](#6-law-enforcement--social-order)
7. [NPC Delegation System](#7-npc-delegation-system)
8. [Relationships & Memory](#8-relationships--memory)
9. [Daily Life Simulation](#9-daily-life-simulation)
10. [Training Data Value](#10-training-data-value)
11. [Implementation Notes](#11-implementation-notes)

---

## 1. Overview

NPCs in The Analog Economy are not quest dispensers or combat fodder. They are the living fabric of society—sources of knowledge, enforcers of norms, potential allies, and witnesses to your deeds. They remember, they talk, and they react.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Mostly benign** | NPCs default to helpful or neutral, not hostile |
| **Information sources** | NPCs share hints, rumors, and knowledge |
| **Social enforcers** | NPCs defend victims and uphold community norms |
| **Memory persistence** | NPCs remember player actions across sessions |
| **Delegation capable** | NPCs can run your business while you're away |

---

## 2. Design Philosophy

### 2.1 The World Reacts

```yaml
world_reaction_philosophy:
  principle: |
    The game world is not passive scenery. NPCs observe player behavior
    and adjust their responses accordingly. Good behavior opens doors;
    bad behavior closes them—sometimes permanently.

  examples:
    positive_spiral:
      - "Help a farmer → They remember"
      - "Farmer tells friends → Reputation spreads"
      - "Friends offer better deals → Opportunities expand"
      - "Community embraces you → Become a trusted member"

    negative_spiral:
      - "Steal from a merchant → They remember"
      - "Merchant tells guards → Watch list"
      - "Guards warn others → Prices increase"
      - "Community distrusts you → Doors close"
```

### 2.2 Benign by Default

```yaml
benign_default:
  principle: |
    NPCs are not looking for reasons to attack players.
    They want to go about their daily lives peacefully.
    Hostility must be earned through player action.

  default_behaviors:
    stranger_player: "Neutral, slightly wary"
    known_player_positive: "Friendly, helpful"
    known_player_negative: "Wary, uncooperative"
    known_player_criminal: "Hostile, call for guards"

  escalation_requirement: |
    NPCs only become aggressive when:
    - Player commits crime in their presence
    - Player threatens them directly
    - Player has severe negative reputation
    - Player is officially outlawed
```

### 2.3 NPCs as Training Data Sources

```yaml
npc_training_data:
  social_modeling:
    - "How do players build trust with NPCs?"
    - "What behaviors earn cooperation?"
    - "How do players repair damaged relationships?"
    - "What makes players choose deception vs honesty?"

  information_seeking:
    - "How do players extract information?"
    - "What questions do they ask?"
    - "How do they evaluate NPC reliability?"
    - "How does information spread through player networks?"
```

---

## 3. NPC Categories

### 3.1 By Function

```yaml
npc_functional_categories:
  essential_services:
    description: "NPCs that provide core game services"
    examples:
      - "Temple priests (favor, rituals)"
      - "Merchants (trade goods)"
      - "Craftsmen (specialized goods)"
      - "Officials (permits, contracts)"
    behavior: "Professional, transactional, remember regulars"

  information_sources:
    description: "NPCs with knowledge to share"
    examples:
      - "Tavern keepers (rumors)"
      - "Travelers (distant news)"
      - "Elders (history, lore)"
      - "Scribes (records, contracts)"
    behavior: "Talkative, helpful if treated well"

  law_enforcement:
    description: "NPCs that maintain social order"
    examples:
      - "Temple guards (sacred areas)"
      - "City watchmen (streets, gates)"
      - "Lugal's soldiers (official force)"
      - "Citizen vigilantes (spontaneous)"
    behavior: "Observant, respond to crimes, remember offenders"

  labor_pool:
    description: "NPCs available for delegation"
    examples:
      - "Farm hands"
      - "Shop assistants"
      - "Apprentices"
      - "Guards for hire"
    behavior: "Follow instructions, require payment"

  background_population:
    description: "NPCs that create atmosphere"
    examples:
      - "Commoners going about daily life"
      - "Children playing"
      - "Beggars, travelers, workers"
    behavior: "Ambient, reactive to major events"
```

### 3.2 By Social Class

```yaml
npc_social_classes:
  elite_npcs:
    examples: ["Sanga", "High priests", "Wealthy merchants"]
    accessibility: "Difficult—requires introduction or high reputation"
    information_value: "High (political, economic secrets)"
    hostility_threshold: "Low (protected by guards)"

  professional_npcs:
    examples: ["Scribes", "Master craftsmen", "Physicians"]
    accessibility: "Moderate—payment or relationship required"
    information_value: "High in specialty (trade secrets)"
    hostility_threshold: "Medium (report crimes, avoid violence)"

  commoner_npcs:
    examples: ["Farmers", "Fishers", "Laborers"]
    accessibility: "Easy—will talk to anyone"
    information_value: "Local (neighborhood events, rumors)"
    hostility_threshold: "Medium (will defend community)"

  marginalized_npcs:
    examples: ["Beggars", "Refugees", "Marsh dwellers"]
    accessibility: "Very easy—desperate for interaction"
    information_value: "Underworld, margins (things others miss)"
    hostility_threshold: "High (avoid conflict, nothing to lose)"
```

---

## 4. Behavior Modes

### 4.1 Standard Behavior States

```yaml
behavior_states:
  idle:
    description: "Going about daily routines"
    activities:
      - "Working their profession"
      - "Socializing with other NPCs"
      - "Eating, resting"
      - "Traveling between locations"
    player_interaction: "Will respond if approached"

  alert:
    description: "Something unusual is happening"
    triggers:
      - "Loud noise"
      - "Running player"
      - "Unfamiliar face in area"
      - "Signs of conflict"
    behavior: "Watch, assess, may investigate"

  helpful:
    description: "Actively assisting player"
    triggers:
      - "Player asks politely"
      - "Player has good reputation"
      - "Player paid for service"
    behavior: "Answer questions, offer guidance"

  suspicious:
    description: "Wary of player"
    triggers:
      - "Player has poor reputation"
      - "Player acting strangely"
      - "Player seen near crime"
    behavior: "Short answers, watch closely, may report"

  hostile:
    description: "Actively opposing player"
    triggers:
      - "Witnessed player crime"
      - "Player attacked them"
      - "Player is outlawed"
    behavior: "Call guards, attack if threatened, flee if outmatched"

  fleeing:
    description: "Running from danger"
    triggers:
      - "Combat nearby"
      - "Threatened directly"
      - "Fire, flood, disaster"
    behavior: "Run to safety, call for help"
```

### 4.2 Reaction Decision Tree

```
NPC ENCOUNTERS PLAYER
         │
         ▼
┌─────────────────────┐
│ Check Reputation    │
│ with this NPC/group │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
POSITIVE    NEGATIVE
    │           │
    ▼           ▼
Friendly    Suspicious
greeting    observation
    │           │
    ▼           ▼
┌───────────────────────────┐
│ Observe Player Behavior   │
└─────────────┬─────────────┘
              │
    ┌─────────┴─────────┐
    ▼                   ▼
NORMAL              CRIMINAL
behavior            behavior
    │                   │
    ▼                   ▼
Continue            Escalate
interaction         response
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          MINOR              MAJOR
          offense            offense
              │                   │
              ▼                   ▼
          Warning            Call guards/
          or report          attack/flee
```

---

## 5. Information & Intelligence

### 5.1 NPCs as Information Sources

```yaml
information_sources:
  purpose: |
    NPCs are the primary way players learn about:
    - Quest locations and opportunities
    - Hidden areas and artifacts
    - Other players' reputations
    - Market conditions and prices
    - Lore and history
    - Skills and techniques

  information_types:
    directions:
      example: "The old shrine? Head east past the canal, then follow the goat path."
      source_npcs: ["Any local", "Travelers", "Merchants"]
      reliability: "High for common locations"

    rumors:
      example: "They say the marsh dwellers found something strange in the reeds..."
      source_npcs: ["Tavern keepers", "Gossips", "Merchants"]
      reliability: "Variable—may be exaggerated or false"

    trade_secrets:
      example: "The key to bronze that doesn't crack? More tin than they tell you."
      source_npcs: ["Master craftsmen", "Scribes with records"]
      reliability: "High if source is genuine expert"

    historical_knowledge:
      example: "Before the temple was built, this was sacred ground to older gods..."
      source_npcs: ["Priests", "Elders", "Scribes"]
      reliability: "High for documented, medium for oral"

    current_events:
      example: "The Lugal's daughter is ill. Healers coming from Ur tomorrow."
      source_npcs: ["Servants", "Guards", "Anyone in city center"]
      reliability: "Decays with distance from event"
```

### 5.2 Extracting Information

```yaml
information_extraction:
  asking_directly:
    method: "Simple question to NPC"
    success_factors:
      - "NPC knows the information"
      - "NPC has positive disposition"
      - "Information is not sensitive"
    failure_mode: "NPC doesn't know or won't tell"

  building_relationship:
    method: "Repeated positive interactions"
    success_factors:
      - "Help NPC with tasks"
      - "Regular respectful visits"
      - "Gifts (appropriate to status)"
    unlock: "NPC shares sensitive information over time"

  payment:
    method: "SILA for information"
    success_factors:
      - "NPC is mercenary type (merchants, some guides)"
      - "Payment matches information value"
    unlock: "Immediate information transfer"

  observation:
    method: "Watch NPC behavior"
    success_factors:
      - "Patience (real-time investment)"
      - "Stealth (not noticed observing)"
    unlock: "Learn routines, locations, relationships"

  eavesdropping:
    method: "Listen to NPC conversations"
    success_factors:
      - "Correct location at correct time"
      - "Stealth (blend into background)"
    unlock: "Overhear information not directed at player"
    risk: "Caught eavesdropping = reputation penalty"
```

### 5.3 Information Network Effects

```yaml
information_networks:
  npcs_talk_to_each_other:
    description: |
      Information spreads between NPCs. If you ask a question,
      other NPCs may learn you were asking.

    examples:
      - "Ask merchant about tin → Other merchants know you need tin"
      - "Ask about hidden shrine → Priest learns of your interest"
      - "Inquire about person → That person may find out"

  reputation_spreading:
    mechanism: "NPCs share opinions of players"
    speed: "Local area: 1 day. City-wide: 3-5 days. Regional: weeks"
    content:
      - "Actions witnessed"
      - "Transaction history"
      - "General disposition (trustworthy, dangerous, etc.)"

  strategic_implications:
    - "Asking questions leaves traces"
    - "Information can be used against you"
    - "Spreading false information is possible but risky"
```

---

## 6. Law Enforcement & Social Order

### 6.1 The Social Contract

```yaml
social_contract:
  what_is_acceptable:
    - "Trade at fair prices"
    - "Verbal disputes"
    - "Competition within rules"
    - "Asking questions"
    - "Observing others"

  minor_offenses:
    examples:
      - "Petty theft (small items)"
      - "Trespassing (non-sacred areas)"
      - "Minor assault (shoving)"
      - "Disrespect to authorities"
    consequences:
      - "Warning from NPCs"
      - "Report to guards"
      - "Fine if caught"
      - "Reputation damage"

  major_offenses:
    examples:
      - "Theft of significant value"
      - "Assault causing injury"
      - "Trespassing in sacred areas"
      - "Destruction of property"
    consequences:
      - "Immediate guard response"
      - "Arrest attempt"
      - "Significant fines"
      - "Possible imprisonment"
      - "Major reputation damage"

  severe_offenses:
    examples:
      - "Murder"
      - "Temple desecration"
      - "Treason"
      - "Repeated major offenses"
    consequences:
      - "City-wide hunt"
      - "Outlaw status"
      - "Kill on sight (some cases)"
      - "Exile"
      - "Execution"
```

### 6.2 NPC Response to Crime

```yaml
npc_crime_response:
  witness_response:
    civilian_witness:
      first_response: "Shout alert, back away"
      if_minor: "Report to nearest guard or official"
      if_major: "Call for help loudly, may attempt to stop"
      if_severe: "All nearby civilians respond"

    merchant_victim:
      first_response: "Call for guards"
      if_theft: "Try to identify thief, report"
      if_violence: "May fight back or flee depending on odds"
      aftermath: "Share thief description with other merchants"

    guard_response:
      if_called: "Arrive in 1-3 minutes (city)"
      if_witnessed: "Immediate intervention"
      methods: ["Verbal command to stop", "Physical restraint", "Combat if resisted"]
      backup: "Call for reinforcements if outmatched"

  community_defense:
    trigger: "Serious crime in progress, no guards nearby"
    response: "Multiple civilians may intervene"
    example: "Player attacks merchant → Nearby NPCs swarm to defend"
    note: "This is NOT mob justice—it's protecting community member"
```

### 6.3 Tolerance Thresholds

```yaml
tolerance_thresholds:
  philosophy: |
    Ancient societies were not perfectly just. Some crimes were
    overlooked, especially by the powerful against the weak.
    The game reflects this uncomfortable reality while still
    providing consequences.

  factors_affecting_tolerance:
    player_status:
      high_status: "More leeway, lighter consequences"
      low_status: "Less tolerance, harsher treatment"
      elite_victim: "Swift response"
      marginalized_victim: "Slower response"

    offense_visibility:
      witnessed_publicly: "Immediate response"
      suspected: "Investigation, suspicion"
      rumored: "Watched more closely"
      unseen: "No immediate consequence (karma still applies)"

    offense_frequency:
      first_offense: "Warning possible"
      second_offense: "Full consequences"
      repeated: "Escalating severity"

  realistic_imperfections:
    - "Bribes can reduce consequences (at cost)"
    - "Powerful protectors can shield you (temporarily)"
    - "Evidence matters (no witness = harder to convict)"
    - "But karma is always tracked"
```

### 6.4 Aggression Escalation Levels

```yaml
aggression_levels:
  level_0_normal:
    description: "Standard interactions"
    npc_behavior: "Helpful or neutral"
    trigger_to_next: "Minor offense"

  level_1_warning:
    description: "NPCs express displeasure"
    npc_behavior: "Verbal warnings, refuse service"
    examples:
      - "'I saw what you did. Don't come back.'"
      - "'The guards will hear about this.'"
    trigger_to_next: "Ignore warning, repeat offense"

  level_2_reporting:
    description: "NPCs actively report you"
    npc_behavior: "Summon guards, share description"
    examples:
      - "Guard approaches to question you"
      - "Merchants refuse to trade"
    trigger_to_next: "Major offense, resist guards"

  level_3_intervention:
    description: "NPCs physically intervene"
    npc_behavior: "Guards attempt arrest, civilians may help"
    examples:
      - "Guards attempt to restrain you"
      - "Crowd blocks your escape"
    trigger_to_next: "Violence against interveners"

  level_4_combat:
    description: "NPCs use force"
    npc_behavior: "Guards attack, civilians may join"
    examples:
      - "Armed response"
      - "Mob defense of community"
    trigger_to_next: "Escape or defeat"

  level_5_hunt:
    description: "City-wide pursuit"
    npc_behavior: "All guards searching, gates watched"
    examples:
      - "Outlaw status declared"
      - "Cannot safely enter city"
    resolution: "Capture, death, or escape to wilderness"
```

---

## 7. NPC Delegation System

### 7.1 The Delegation Concept

```yaml
delegation_philosophy:
  purpose: |
    Players cannot do everything themselves. As they build businesses
    and properties, they need NPCs to handle routine tasks while they
    focus on mastery, expansion, or exploration.

  developer_revenue_model:
    - "NPC wages are paid in SILA"
    - "Developer takes 10% of all NPC wages"
    - "Premium NPCs (better skills) cost more"
    - "This creates sustainable economy sink"

  player_benefit:
    - "Passive income while offline"
    - "Focus on skill development"
    - "Run multiple operations simultaneously"
    - "Scale beyond personal capacity"
```

### 7.2 Delegable Tasks

```yaml
delegable_tasks:
  sales_operations:
    npc_type: "Shop Assistant"
    tasks:
      - "Sell items at fixed prices you set"
      - "Accept payment"
      - "Basic inventory management"
    limitations:
      - "Cannot negotiate prices"
      - "Cannot make purchasing decisions"
      - "Cannot handle complex transactions"
    upgrade: "Trained Merchant can negotiate within bounds"

  production_support:
    npc_type: "Apprentice / Journeyman"
    tasks:
      - "Produce items you've mastered"
      - "Maintain equipment"
      - "Process raw materials"
    limitations:
      - "Lower quality than player"
      - "Cannot learn new techniques"
      - "Cannot handle unusual orders"
    upgrade: "Master NPCs can produce higher quality"

  agricultural_labor:
    npc_type: "Farm Hand"
    tasks:
      - "Plant and harvest crops"
      - "Maintain irrigation"
      - "Feed animals"
    limitations:
      - "Cannot make crop decisions"
      - "Cannot handle emergencies"
      - "Cannot sell (without separate NPC)"
    upgrade: "Overseer can manage multiple hands"

  property_protection:
    npc_type: "Watchman / Guard"
    tasks:
      - "Alert you to intruders"
      - "Basic defense"
      - "Patrol property"
    limitations:
      - "Limited combat ability"
      - "Cannot pursue off property"
      - "Cannot make legal decisions"
    upgrade: "Trained Guard better in combat"

  logistics:
    npc_type: "Porter / Carrier"
    tasks:
      - "Transport goods between locations"
      - "Deliver to customers"
      - "Pick up supplies"
    limitations:
      - "Fixed routes only"
      - "Cannot negotiate"
      - "Vulnerable to theft"
    upgrade: "Caravan Leader can manage multiple porters"
```

### 7.3 NPC Hiring & Management

```yaml
npc_hiring:
  finding_npcs:
    labor_market: "City center, dawn gathering"
    temple_assignment: "Request through Temple (higher quality, higher cost)"
    word_of_mouth: "NPCs recommend relatives/friends"
    player_referral: "Other players recommend NPCs"

  hiring_process:
    1: "Negotiate wage (SILA per month or per task)"
    2: "Set term (temporary, seasonal, permanent)"
    3: "Agree on duties"
    4: "Clay tablet contract (if formal)"

  npc_quality_tiers:
    unskilled:
      wage: "30 SILA/month"
      capability: "Basic labor only"
      reliability: "May skip work, steal"
      developer_cut: "3 SILA/month"

    trained:
      wage: "60 SILA/month"
      capability: "Specific trade skills"
      reliability: "Generally reliable"
      developer_cut: "6 SILA/month"

    skilled:
      wage: "100 SILA/month"
      capability: "High-quality work"
      reliability: "Very reliable"
      developer_cut: "10 SILA/month"

    expert:
      wage: "200+ SILA/month"
      capability: "Master-level skills"
      reliability: "Completely reliable"
      developer_cut: "20+ SILA/month"

  management_interface:
    set_tasks: "Assign specific duties"
    set_prices: "For sales NPCs, set item prices"
    set_hours: "When NPC works"
    set_authority: "What decisions NPC can make"
    review_logs: "See what NPC did while you were away"
```

### 7.4 NPC Loyalty & Morale

```yaml
npc_loyalty:
  factors:
    positive:
      - "Paid on time and fairly"
      - "Safe working conditions"
      - "Reasonable workload"
      - "Respectful treatment"
      - "Bonuses for good work"

    negative:
      - "Late or missing payment"
      - "Dangerous conditions"
      - "Excessive demands"
      - "Abuse or disrespect"
      - "Illegal orders"

  consequences_of_low_loyalty:
    minor: "Reduced productivity"
    moderate: "Theft, sabotage"
    severe: "Quit without notice"
    extreme: "Report you to authorities"

  building_loyalty:
    - "Fair wages (market rate or better)"
    - "Regular appreciation"
    - "Advancement opportunities"
    - "Protection in conflicts"
```

---

## 8. Relationships & Memory

### 8.1 NPC Memory System

```yaml
npc_memory:
  what_npcs_remember:
    about_players:
      - "Direct interactions (positive and negative)"
      - "Witnessed actions"
      - "Transactions"
      - "Reputation information from others"
      - "Promises made and kept/broken"

    memory_duration:
      positive_interactions: "Long-lasting (months)"
      negative_interactions: "Very long-lasting (years)"
      transactions: "Records kept indefinitely"
      rumors: "Fade over time unless reinforced"

  memory_sharing:
    npcs_talk: "Information spreads to associated NPCs"
    guild_memory: "Merchants share info with merchants"
    temple_records: "Official records are permanent"
    family_memory: "NPC family remembers what affects relatives"
```

### 8.2 Relationship Mechanics

```yaml
relationship_mechanics:
  relationship_levels:
    hostile: -100 to -50
    unfriendly: -50 to -10
    neutral: -10 to +10
    friendly: +10 to +50
    allied: +50 to +100

  building_relationships:
    positive_actions:
      - "Help with tasks (+5 to +15)"
      - "Fair trades (+1 to +5)"
      - "Gifts appropriate to status (+5 to +20)"
      - "Defend from threat (+20 to +50)"
      - "Keep promises (+10 to +20)"

    negative_actions:
      - "Crimes against them (-20 to -100)"
      - "Insults (-5 to -15)"
      - "Broken promises (-15 to -30)"
      - "Crimes against their group (-10 to -30)"
      - "Unfair dealings (-5 to -15)"

  relationship_decay:
    positive: "Slow decay without interaction (1 point/week)"
    negative: "Very slow decay (1 point/month)"
    note: "Severe negative events may never fully decay"

  relationship_benefits:
    friendly:
      - "Better prices"
      - "More willing to share information"
      - "May offer help unprompted"

    allied:
      - "Significant discounts"
      - "Share secrets"
      - "Active assistance in conflicts"
      - "Warn you of dangers"
```

### 8.3 Reputation System Integration

```yaml
reputation_integration:
  individual_vs_group:
    individual: "Your relationship with specific NPC"
    group: "Your reputation with merchant guild, Temple, etc."
    city: "Your general standing in Eridu"

  reputation_sources:
    witnessed_actions: "Most impactful"
    reported_actions: "Secondary impact"
    rumors: "Minor impact unless confirmed"

  reputation_effects:
    on_prices: "-20% to +50% based on reputation"
    on_access: "High rep opens doors, low rep closes them"
    on_npc_behavior: "Determines default disposition"
    on_legal_treatment: "Affects punishment severity"
```

---

## 9. Daily Life Simulation

### 9.1 NPC Schedules

```yaml
npc_schedules:
  typical_commoner:
    dawn: "Wake, morning prayers"
    early_morning: "Work begins"
    midday: "Main meal break"
    afternoon: "Work continues"
    evening: "Return home, evening meal"
    night: "Social time, sleep"

  variations:
    by_profession:
      farmers: "Dawn start, field work all day"
      merchants: "Market hours only"
      priests: "Ritual schedule dominates"
      laborers: "Work gangs, shift-based"

    by_season:
      planting: "Everyone works fields"
      harvest: "Extended hours"
      flood: "Emergency schedules"
      festivals: "Work reduced"

  player_implications:
    - "NPCs available at specific times"
    - "Empty shops have reasons"
    - "Night activities different from day"
    - "Schedules can be learned"
```

### 9.2 NPC Needs & Motivations

```yaml
npc_motivations:
  survival_needs:
    - "Food and water"
    - "Shelter"
    - "Safety"
    - "Rest"

  social_needs:
    - "Family and friends"
    - "Community belonging"
    - "Status and respect"
    - "Religious observance"

  personal_goals:
    examples:
      - "Merchant wants to expand business"
      - "Farmer wants to buy own land"
      - "Craftsman wants Temple commission"
      - "Parent wants child to succeed"
    player_interaction: "Helping NPC goals builds relationship"

  behavioral_implications:
    - "NPCs won't sacrifice needs for player convenience"
    - "NPCs have lives beyond player interaction"
    - "NPCs make decisions based on their goals"
```

### 9.3 NPC Interactions with Each Other

```yaml
npc_npc_interactions:
  social_web:
    - "NPCs have relationships with other NPCs"
    - "Families, guilds, neighborhoods"
    - "Rivalries and friendships"
    - "Information flows through connections"

  emergent_behavior:
    - "NPCs gather at social locations"
    - "News spreads through conversations"
    - "Conflicts arise between NPCs"
    - "Cooperative activities occur"

  player_observation:
    - "Watching NPCs reveals information"
    - "NPC conversations can be overheard"
    - "NPC conflicts create opportunities"
    - "NPC networks can be mapped"
```

---

## 10. Training Data Value

### 10.1 Social Interaction Data

```yaml
social_training_data:
  relationship_building:
    - "How do players approach NPCs?"
    - "What builds trust effectively?"
    - "How do players repair damaged relationships?"
    - "What makes players loyal to NPCs?"

  information_seeking:
    - "How do players extract information?"
    - "How do they evaluate reliability?"
    - "How does information affect decisions?"
    - "How do players spread information?"

  social_strategy:
    - "How do players build networks?"
    - "How do they navigate social hierarchy?"
    - "How do they handle social conflicts?"
    - "How do they balance multiple relationships?"
```

### 10.2 Authority & Compliance Data

```yaml
authority_training_data:
  compliance_patterns:
    - "When do players follow rules?"
    - "What makes rules feel legitimate?"
    - "How do players respond to enforcement?"
    - "What drives rebellion vs acceptance?"

  crime_decisions:
    - "What tempts players to crime?"
    - "How do consequences affect behavior?"
    - "How do players weigh risk vs reward?"
    - "How does getting away with crime affect future behavior?"

  delegation_data:
    - "How do players manage NPC workers?"
    - "What trust levels do they assign?"
    - "How do they respond to NPC failures?"
    - "How do they balance control vs delegation?"
```

---

## 11. Implementation Notes

### 11.1 MVP Scope

```yaml
mvp_npc_behavior:
  included:
    behavior_modes:
      - "Idle, alert, helpful, hostile"
      - "Basic crime response"
      - "Memory of direct interactions"

    information_sharing:
      - "Directions and basic hints"
      - "Rumors (3-5 per NPC type)"
      - "Trade information"

    delegation:
      - "Shop assistant (sell at fixed price)"
      - "Watchman (alert to intruders)"
      - "Farm hand (basic crop tending)"

    law_enforcement:
      - "Guards respond to witnessed crimes"
      - "Basic tolerance thresholds"
      - "Reputation affecting NPC disposition"

  deferred:
    - "Complex NPC schedules"
    - "Deep NPC-NPC relationships"
    - "Advanced delegation (caravans, etc.)"
    - "Bribery system"
    - "NPC political factions"
```

### 11.2 Performance Considerations

```yaml
performance:
  npc_culling:
    - "Only simulate detailed behavior for nearby NPCs"
    - "Distant NPCs run simplified routines"
    - "Memory stored in database, loaded on demand"

  memory_storage:
    - "Player interactions logged to database"
    - "Reputation calculated, not stored for each NPC"
    - "Group memory shared across NPCs"

  delegation_processing:
    - "Batch process delegation results"
    - "Calculate at login, not real-time"
    - "Simplify off-screen activities"
```

---

## Appendix: Quick Reference

### NPC Disposition by Reputation

| Player Reputation | NPC Default Disposition | Access Level |
|-------------------|------------------------|--------------|
| +50 and above | Friendly, eager to help | Full access |
| +10 to +49 | Positive, willing to help | Good access |
| -9 to +9 | Neutral, transactional | Standard access |
| -10 to -49 | Suspicious, reluctant | Limited access |
| -50 and below | Hostile, may refuse | Denied, may report |

### Crime Response Summary

| Offense Severity | Witness Response | Guard Response | Consequence |
|------------------|------------------|----------------|-------------|
| Minor | Warning, report | Question if reported | Fine, reputation loss |
| Major | Call for help | Arrest attempt | Large fine, imprisonment |
| Severe | Community defense | Combat, pursuit | Exile, execution |

### Delegation Cost Summary

| NPC Type | Base Wage | Dev Cut | Capability |
|----------|-----------|---------|------------|
| Unskilled | 30 SILA/mo | 3 SILA | Basic labor |
| Trained | 60 SILA/mo | 6 SILA | Specific skills |
| Skilled | 100 SILA/mo | 10 SILA | Quality work |
| Expert | 200+ SILA/mo | 20+ SILA | Master level |

---

*"The city has a thousand eyes. A thousand ears. A thousand memories. Walk carefully."*
