# Quest & Mission Framework: The World Has Needs

> "No god marks the worthy with floating symbols. The world has problems. You may choose to solve them."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Quest Discovery](#3-quest-discovery)
4. [Quest Types](#4-quest-types)
5. [The Contract System](#5-the-contract-system)
6. [Quest Progression](#6-quest-progression)
7. [Rewards & Consequences](#7-rewards--consequences)
8. [Failure Creates Quests](#8-failure-creates-quests)
9. [Community Quests](#9-community-quests)
10. [Training Data Value](#10-training-data-value)
11. [Implementation Notes](#11-implementation-notes)

---

## 1. Overview

Quests in The Analog Economy are not glowing markers over NPC heads. They are the natural needs, problems, and opportunities that arise from a living world. Players discover them through observation, conversation, and experience—just as people discovered opportunities in the real ancient world.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **No quest markers** | No "!" or "?" floating over NPCs |
| **Organic discovery** | Quests emerge from world state and relationships |
| **Contract formalization** | Major quests use clay tablet contracts (Sumerian innovation) |
| **Failure creates quests** | Your mistakes become obligations |
| **Player-driven** | Many quests are player-to-player opportunities |

---

## 2. Design Philosophy

### 2.1 The Anti-Quest Design

```yaml
anti_quest_philosophy:
  what_we_reject:
    - "Floating markers showing quest locations"
    - "Quest logs filled with dozens of tasks"
    - "NPCs standing in one place waiting to give quests"
    - "'Kill 10 rats' fetch quests"
    - "Quests that pause the world while you complete them"

  what_we_embrace:
    - "NPCs mention problems in conversation"
    - "World state creates obvious needs"
    - "Relationships unlock opportunities"
    - "Contracts formalize important agreements"
    - "Time passes whether you act or not"
```

### 2.2 The Living World Approach

```yaml
living_world_quests:
  principle: |
    The world has needs. Crops need harvesting. Trade goods need
    moving. Disputes need resolution. Invaders need repelling.
    These needs exist whether players address them or not.

  examples:
    natural_need:
      situation: "The flood season approaches"
      discovery: "Elders discuss levee condition"
      quest: "Reinforce the levee before floods come"
      consequence_if_ignored: "Flood damage to fields"

    social_need:
      situation: "Two merchants dispute a contract"
      discovery: "Arguments overheard at market"
      quest: "Serve as witness or mediator"
      consequence_if_ignored: "Dispute escalates, affects trade"

    economic_need:
      situation: "Caravan needs escort through dangerous route"
      discovery: "Merchant seeking guards at tavern"
      quest: "Protect the caravan"
      consequence_if_ignored: "Caravan goes without you (or fails)"
```

### 2.3 Training Data Philosophy

```yaml
quest_training_data:
  questions_studied:
    - "How do players discover opportunities without markers?"
    - "What makes players choose to help vs ignore?"
    - "How do players evaluate risk/reward?"
    - "How do contracts affect behavior?"
    - "How do failed quests affect future decisions?"

  valuable_behaviors:
    - "Organic information gathering"
    - "Social network utilization"
    - "Time-pressure decision making"
    - "Commitment and follow-through"
    - "Failure processing and recovery"
```

---

## 3. Quest Discovery

### 3.1 Discovery Methods

```yaml
discovery_methods:
  overheard_conversations:
    description: "NPCs discuss problems with each other"
    mechanic:
      - "Linger near NPC groups"
      - "Overhear fragments of conversation"
      - "Piece together information"
    example: |
      Two farmers talking: "The canal upstream is blocked again.
      The water barely reaches my field anymore..."
    player_action: "Investigate the canal blockage"

  direct_requests:
    description: "NPCs ask players directly for help"
    trigger:
      - "Player has positive relationship"
      - "Player has relevant skills"
      - "NPC is desperate enough to ask strangers"
    example: |
      Merchant approaches: "You look capable. I need someone
      to watch my stall while I make deliveries. Pay well."

  observation:
    description: "Player notices problems in the world"
    mechanic:
      - "Damaged structures visible"
      - "NPCs behaving unusually"
      - "Resources out of place"
    example: |
      Player notices: Temple storehouse door is open at night.
      Unusual. Investigation reveals theft in progress.

  rumor_network:
    description: "Information spreads through gossip"
    locations:
      - "Beer houses (primary rumor mill)"
      - "Market stalls"
      - "Temple courtyards"
      - "City gates (travelers bring news)"
    example: |
      Tavern keeper: "Heard the Lugal's looking for anyone who
      can work copper. The royal smith took ill."

  failure_consequences:
    description: "Your mistakes create obligations"
    mechanic:
      - "Damage something → Must repair or pay"
      - "Break contract → Must make amends"
      - "Harm someone → Blood price owed"
    example: |
      Player's levee fails, floods neighbor's field.
      Now owes compensation or labor to repair damage.

  world_events:
    description: "Major events create mass opportunities"
    types:
      - "Caravan arrival (trade, escort needs)"
      - "Festival preparation (labor, goods needed)"
      - "War declaration (military needs)"
      - "Natural disaster (rebuilding needs)"
    example: |
      Flood season creates: levee repair needs, rescue opportunities,
      rebuilding contracts, supply shortages to fill.
```

### 3.2 The Information Economy

```yaml
information_economy:
  information_has_value:
    principle: "Knowing about an opportunity is valuable"
    implications:
      - "Players may sell quest information"
      - "NPCs may charge for detailed directions"
      - "Early knowledge = competitive advantage"

  building_information_networks:
    strategy:
      - "Regular visits to information hubs"
      - "Building NPC relationships"
      - "Trading information with other players"
      - "Positioning in high-traffic areas"

  information_decay:
    - "Opportunities don't wait forever"
    - "Old news becomes worthless"
    - "Acting quickly has value"
```

---

## 4. Quest Types

### 4.1 Quest Category Matrix

| Type | Source | Urgency | Reward | Risk |
|------|--------|---------|--------|------|
| **Survival** | Environment | High | Self-preservation | High |
| **Economic** | NPCs/Market | Variable | SILA, goods | Low-Medium |
| **Social** | Relationships | Low-Medium | Reputation, favors | Low |
| **Temple** | Religious duty | Scheduled | Favor, SILA | Low-Medium |
| **Innovation** | Discovery | None | SILA, knowledge | Low |
| **Mystery** | Lore | None | Knowledge, Witness cost | Variable |
| **Conflict** | War/dispute | High | SILA, reputation | High |

### 4.2 Detailed Quest Types

```yaml
quest_types:
  survival_quests:
    description: "Immediate threats to life or livelihood"
    examples:
      prepare_for_flood:
        trigger: "Flood season approaching"
        task: "Reinforce levees, secure goods"
        deadline: "Before flood arrives"
        failure: "Property damage, possible death"

      water_shortage:
        trigger: "Upstream blockage or drought"
        task: "Find water source or resolve blockage"
        deadline: "Before crops die"
        failure: "Starvation, economic ruin"

      disease_outbreak:
        trigger: "Illness spreading in area"
        task: "Quarantine, treat, or flee"
        deadline: "Before you catch it"
        failure: "Health loss, possible death"

  economic_quests:
    description: "Opportunities for profit"
    examples:
      caravan_escort:
        source: "Merchant seeking protection"
        task: "Guard goods from point A to B"
        reward: "SILA or trade goods"
        risk: "Bandits, environmental hazards"

      trade_opportunity:
        source: "Market information"
        task: "Buy low here, sell high there"
        reward: "Profit margin"
        risk: "Capital loss, travel danger"

      contract_fulfillment:
        source: "Temple or wealthy patron"
        task: "Produce specific goods by deadline"
        reward: "SILA, reputation, future contracts"
        risk: "Penalty for failure"

  social_quests:
    description: "Relationship-based opportunities"
    examples:
      dispute_resolution:
        source: "Conflicting parties"
        task: "Mediate or witness agreement"
        reward: "Reputation, favors from both"
        risk: "Making enemies if biased"

      favor_request:
        source: "Friend or ally"
        task: "Help with their problem"
        reward: "Strengthened relationship"
        risk: "Time investment, possible complications"

      reputation_building:
        source: "Community need"
        task: "Public service (repair, defense)"
        reward: "Community standing"
        risk: "Failure is public embarrassment"

  temple_quests:
    description: "Religious obligations and opportunities"
    examples:
      temple_service:
        source: "Temple duty"
        task: "Work temple fields, clean, maintain"
        reward: "Temple favor"
        risk: "Time investment"

      ritual_requirements:
        source: "Priest request"
        task: "Obtain specific items for ritual"
        reward: "Temple favor, possible blessing"
        risk: "Scarcity of items"

      pilgrimage:
        source: "Religious tradition"
        task: "Visit sacred site, perform observance"
        reward: "Favor, spiritual benefit"
        risk: "Travel dangers"

  innovation_quests:
    description: "Discovering new knowledge"
    examples:
      technique_mastery:
        source: "Skill tree progress"
        task: "Practice until breakthrough"
        reward: "New ability, SILA"
        risk: "Material cost of practice"

      knowledge_seeking:
        source: "Clay tablet hints"
        task: "Find missing information"
        reward: "Complete knowledge"
        risk: "Search may be fruitless"

      teaching_opportunity:
        source: "Novice seeking instruction"
        task: "Teach what you know"
        reward: "SILA from student, reputation"
        risk: "Time investment"

  mystery_quests:
    description: "Pursuing hidden knowledge"
    examples:
      artifact_investigation:
        source: "Unusual find"
        task: "Research origin and meaning"
        reward: "Lore knowledge, possible power"
        risk: "Witness cost"

      apkallu_encounter:
        source: "Rare NPC appearance"
        task: "Pass the sage's test"
        reward: "Innovation shortcut"
        risk: "Witness cost, failure penalty"

      hidden_site_discovery:
        source: "Accumulated clues"
        task: "Find and explore hidden location"
        reward: "Unique knowledge, Legacy Points"
        risk: "Significant Witness cost"

  conflict_quests:
    description: "War and violence opportunities"
    examples:
      settlement_defense:
        source: "Attack incoming"
        task: "Defend walls, repel attackers"
        reward: "Survival, loot, reputation"
        risk: "Death, destruction"

      military_campaign:
        source: "Declared war"
        task: "Join army, fight in battles"
        reward: "Loot, land, reputation"
        risk: "Death, karma cost"

      raid_participation:
        source: "Raid opportunity"
        task: "Attack enemy resources"
        reward: "Loot"
        risk: "Death, karma cost, retaliation"
```

---

## 5. The Contract System

### 5.1 Contract Philosophy

```yaml
contract_philosophy:
  historical_basis: |
    Sumerians invented the written contract. They documented
    everything: sales, loans, marriages, labor agreements.
    Clay tablets with cylinder seal impressions were legally binding.

  gameplay_purpose:
    - "Formalize important agreements"
    - "Create enforceable obligations"
    - "Enable complex multi-party deals"
    - "Generate training data on contract behavior"
```

### 5.2 Contract Types

```yaml
contract_types:
  temple_contracts:
    description: "Work assigned by Temple"
    formalization: "Scribe records on official tablet"
    enforcement: "Temple authority"
    benefits:
      - "Guaranteed payment"
      - "Clear terms"
      - "Reputation gain"
    risks:
      - "Strict deadlines"
      - "Penalties for failure"
      - "Temple favor loss if breach"

  merchant_contracts:
    description: "Trade agreements"
    formalization: "Witnessed agreement, possibly written"
    enforcement: "Merchant reputation, legal recourse"
    benefits:
      - "Higher potential reward"
      - "Trade relationship building"
      - "Access to rare goods"
    risks:
      - "Payment may be in goods (variable value)"
      - "Partner may not honor terms"
      - "No guaranteed success"

  personal_favors:
    description: "Informal agreements between individuals"
    formalization: "Verbal, witnesses optional"
    enforcement: "Reputation only"
    benefits:
      - "Flexibility"
      - "Relationship currency"
      - "No formal penalty for failure"
    risks:
      - "No guaranteed reward"
      - "Reputation damage if renege"
      - "Favor may be called later"

  blood_debts:
    description: "Obligations from crimes or accidents"
    formalization: "Mandatory legal record"
    enforcement: "Temple law, social pressure"
    benefits:
      - "Path to redemption"
      - "Avoid worse punishment"
    risks:
      - "Must be fulfilled"
      - "Failure worsens standing"
```

### 5.3 Contract Interface

```yaml
contract_creation:
  temple_contracts:
    process:
      1: "Receive assignment from Temple official"
      2: "Scribe records terms on clay tablet"
      3: "Both parties apply cylinder seal"
      4: "Copy stored in Temple archive"
    terms_include:
      - "Task description"
      - "Deadline"
      - "Payment (amount, form)"
      - "Penalty for breach"
      - "Special conditions"

  player_to_player_contracts:
    process:
      1: "Negotiate terms verbally"
      2: "Optionally hire scribe to record"
      3: "Optionally have NPC witness"
      4: "Seal if literate, mark if not"
    enforcement:
      written_witnessed: "Legal recourse available"
      written_unwitnessed: "Partial legal standing"
      verbal: "Reputation enforcement only"

  contract_tracking:
    player_journal:
      - "Active contracts listed"
      - "Deadlines shown"
      - "Progress tracked"
      - "No map markers (you must remember locations)"
```

---

## 6. Quest Progression

### 6.1 Quest States

```yaml
quest_states:
  unknown:
    description: "Quest opportunity exists but player unaware"
    player_status: "No journal entry"
    world_status: "Need exists in world"

  discovered:
    description: "Player has learned of opportunity"
    player_status: "Can add to personal notes"
    world_status: "No commitment yet"

  accepted:
    description: "Player has committed to task"
    player_status: "Active in journal"
    world_status: "Others may know you're working on it"

  in_progress:
    description: "Player actively working on task"
    player_status: "Tracking progress"
    world_status: "Clock may be ticking"

  completed:
    description: "Task finished successfully"
    player_status: "Rewards received"
    world_status: "World state updated"

  failed:
    description: "Task not completed"
    player_status: "Consequences applied"
    world_status: "Problem may worsen or be solved by others"

  expired:
    description: "Deadline passed without completion"
    player_status: "Failure consequences"
    world_status: "Opportunity gone"
```

### 6.2 Time Pressure

```yaml
time_pressure:
  timed_quests:
    real_deadlines:
      - "Caravan leaves in 2 hours"
      - "Festival is in 3 days"
      - "Flood arrives in 1 week"
    implication: "Miss it, miss the opportunity"

  competitive_quests:
    description: "Other players/NPCs may complete first"
    examples:
      - "First to deliver supplies gets contract"
      - "Limited temple positions available"
      - "Treasure found is treasure gone"

  degrading_opportunities:
    description: "Rewards decrease over time"
    examples:
      - "Rescue reward highest immediately after disaster"
      - "Information value decreases as it spreads"
      - "Crops worth more at harvest than later"

  no_pressure_quests:
    description: "Some opportunities wait"
    examples:
      - "Learning a skill"
      - "Building relationships"
      - "Long-term exploration"
```

### 6.3 Quest Complexity

```yaml
quest_complexity:
  simple:
    steps: "1-2"
    example: "Deliver this package to the scribe"
    tracking: "Minimal, obvious completion"

  moderate:
    steps: "3-5"
    example: "Gather materials, craft item, deliver to temple"
    tracking: "Player must remember steps"

  complex:
    steps: "5-10"
    example: "Investigate theft, identify suspects, gather evidence, present to authorities"
    tracking: "Player notes essential"

  epic:
    steps: "10+"
    example: "Build a successful smithy from nothing"
    tracking: "Long-term project, many sub-tasks"
    note: "These are player-defined goals, not assigned quests"
```

---

## 7. Rewards & Consequences

### 7.1 Reward Types

```yaml
reward_types:
  sila:
    description: "Direct currency payment"
    source: "Contracts, sales, services"
    variability: "Fixed for contracts, negotiable otherwise"

  goods:
    description: "Items instead of currency"
    source: "Trade, loot, payment in kind"
    variability: "Value depends on your needs"

  reputation:
    description: "Standing with individuals or groups"
    source: "Completing tasks, behavior"
    value: "Opens doors, improves prices"

  relationships:
    description: "Stronger bonds with NPCs/players"
    source: "Helping, keeping promises"
    value: "Future opportunities, information access"

  knowledge:
    description: "Information or skills gained"
    source: "Investigation, teaching, discovery"
    value: "Enables future capabilities"

  access:
    description: "Entry to restricted areas/opportunities"
    source: "Favor, reputation, completion"
    value: "Unique content available"

  temple_favor:
    description: "Standing with religious institution"
    source: "Temple service, donations"
    value: "Rituals, blessings, positions"

  legacy_points:
    description: "Meta-progression currency"
    source: "Significant achievements"
    value: "Bloodline advancement"
```

### 7.2 Consequence Types

```yaml
consequence_types:
  reputation_damage:
    trigger: "Breaking commitments, failing publicly"
    effect: "Worse prices, closed doors, suspicion"
    recovery: "Consistent good behavior over time"

  material_loss:
    trigger: "Failure to protect goods, pay debts"
    effect: "Lost SILA, items, property"
    recovery: "Earn replacements"

  relationship_damage:
    trigger: "Betrayal, negligence, failure"
    effect: "Reduced NPC disposition"
    recovery: "Effort to rebuild trust"

  legal_consequences:
    trigger: "Contract breach, crime"
    effect: "Fines, imprisonment, exile"
    recovery: "Pay penalties, serve time"

  blood_debt:
    trigger: "Causing death or serious harm"
    effect: "Owe compensation to victim's family"
    recovery: "Payment or service"

  karma_cost:
    trigger: "Unethical actions"
    effect: "Affects reincarnation"
    recovery: "Good deeds over time"

  new_obligations:
    trigger: "Failure creates problems"
    effect: "Must fix what you broke"
    recovery: "Complete the obligation"
```

---

## 8. Failure Creates Quests

### 8.1 The Failure Philosophy

```yaml
failure_philosophy:
  principle: |
    In a living world, failure doesn't mean "try again."
    Failure means the world changed because of your failure.
    New problems arise. New obligations appear.
    This makes failure meaningful, not just frustrating.

  examples:
    failed_levee:
      initial_task: "Repair your levee before flood"
      failure: "Didn't finish in time"
      new_reality: "Your field flooded, neighbor's too"
      new_quest: "Compensate neighbor, salvage what you can"

    failed_delivery:
      initial_task: "Deliver goods to merchant"
      failure: "Goods stolen en route"
      new_reality: "You owe the merchant"
      new_quest: "Pay debt or recover goods"

    failed_promise:
      initial_task: "Promised to help farmer with harvest"
      failure: "Didn't show up"
      new_reality: "Farmer's crop partially lost, angry"
      new_quest: "Make amends or accept damaged relationship"
```

### 8.2 Failure-Generated Quest Types

```yaml
failure_quests:
  debt_obligations:
    trigger: "You owe someone (contract breach, damage caused)"
    structure:
      - "Amount owed calculated"
      - "Payment plan negotiable"
      - "Work alternative possible"
    resolution: "Pay or work off debt"

  repair_quests:
    trigger: "You damaged something"
    structure:
      - "Damage assessed"
      - "Materials needed identified"
      - "Labor required estimated"
    resolution: "Fix what you broke"

  reconciliation_quests:
    trigger: "You harmed a relationship"
    structure:
      - "Understand what went wrong"
      - "Find way to make amends"
      - "Rebuild trust gradually"
    resolution: "Relationship recovered (partially or fully)"

  redemption_quests:
    trigger: "Serious crime or moral failing"
    structure:
      - "Acknowledge wrongdoing"
      - "Accept appropriate punishment"
      - "Demonstrate change"
    resolution: "Karma recovery, community acceptance"
```

---

## 9. Community Quests

### 9.1 Settlement-Level Quests

```yaml
community_quests:
  description: |
    Some challenges are too big for individuals. These require
    coordinated effort from multiple players and NPCs.

  types:
    infrastructure_projects:
      examples:
        - "Build new canal section"
        - "Construct city walls"
        - "Erect new temple"
      coordination:
        - "Settlement leader initiates"
        - "Resources pooled"
        - "Labor assigned"
        - "Rewards distributed"

    defense_operations:
      examples:
        - "Repel incoming raid"
        - "Siege another settlement"
        - "Patrol trade routes"
      coordination:
        - "Military leader organizes"
        - "Roles assigned (fighters, support)"
        - "Rewards based on contribution"

    economic_initiatives:
      examples:
        - "Corner a market"
        - "Establish trade route"
        - "Sponsor festival"
      coordination:
        - "Merchants cooperate"
        - "Resources invested"
        - "Profits shared"
```

### 9.2 Player-Created Quests

```yaml
player_created_quests:
  bounties:
    creator: "Wronged player or settlement"
    target: "Specific player or NPC"
    reward: "SILA offered by creator"
    mechanics:
      - "Post bounty publicly"
      - "Others can attempt collection"
      - "Proof of completion required"

  job_postings:
    creator: "Player with needs"
    task: "Work they need done"
    reward: "Payment offered"
    mechanics:
      - "Advertise at relevant locations"
      - "Other players apply"
      - "Contract created"

  apprenticeship_offers:
    creator: "Skilled player"
    task: "Learn under their guidance"
    reward: "Knowledge transfer"
    mechanics:
      - "Post availability"
      - "Students apply"
      - "Teaching relationship formed"

  partnership_proposals:
    creator: "Player with plan"
    task: "Joint venture"
    reward: "Shared profits"
    mechanics:
      - "Proposal explained"
      - "Partners recruited"
      - "Formal or informal agreement"
```

---

## 10. Training Data Value

### 10.1 Decision Data from Quests

```yaml
quest_training_data:
  opportunity_evaluation:
    - "How do players assess quest value?"
    - "What factors drive acceptance vs rejection?"
    - "How does risk tolerance affect choices?"
    - "How do deadlines affect decisions?"

  commitment_behavior:
    - "Do players complete what they start?"
    - "What causes quest abandonment?"
    - "How do contracts affect completion?"
    - "How is reputation valued?"

  failure_processing:
    - "How do players respond to failure?"
    - "Do they make amends or avoid?"
    - "How does failure affect future behavior?"
    - "What enables recovery?"

  social_coordination:
    - "How do players organize for group quests?"
    - "How are rewards negotiated?"
    - "How is free-riding handled?"
    - "What makes cooperation succeed?"
```

### 10.2 Information Behavior Data

```yaml
information_training_data:
  discovery_patterns:
    - "How do players find opportunities?"
    - "What information sources do they trust?"
    - "How do they evaluate rumor reliability?"
    - "How do they build information networks?"

  information_sharing:
    - "Do players share or hoard information?"
    - "What is information worth to them?"
    - "How does competition affect sharing?"
    - "How do information markets emerge?"
```

---

## 11. Implementation Notes

### 11.1 MVP Scope

```yaml
mvp_quests:
  included:
    discovery_methods:
      - "Direct NPC requests"
      - "Overheard conversations (scripted)"
      - "World state observation (damage, needs)"

    quest_types:
      - "Simple economic (delivery, trade)"
      - "Simple social (favors, disputes)"
      - "Temple service (basic)"
      - "Survival (flood preparation)"

    contract_system:
      - "Temple contracts (formal)"
      - "Verbal agreements (tracked)"
      - "Basic consequences for breach"

    failure_quests:
      - "Debt obligations"
      - "Simple repair requirements"

  deferred:
    - "Complex mystery quests"
    - "Full community quests"
    - "Player bounty system"
    - "Dynamic rumor network"
```

### 11.2 Technical Considerations

```yaml
technical:
  quest_generation:
    - "World state triggers quest availability"
    - "NPC schedules determine availability"
    - "Random elements add variety"
    - "Player history affects offers"

  tracking:
    - "No global quest log"
    - "Player journal is personal notes"
    - "Contract tablets are items"
    - "Progress inferred from world state"

  time_management:
    - "Deadlines use server time"
    - "Grace periods for connection issues"
    - "Batch processing for mass events"
```

---

## Appendix: Quest Examples

### Sample Quest Flow: The Blocked Canal

```yaml
blocked_canal_quest:
  setup:
    world_state: "Canal serving multiple farms is blocked upstream"
    affected_npcs: "Farmers complaining about water shortage"

  discovery:
    overheard: "Farmers arguing at market about whose fault it is"
    direct: "Farmer asks player if they've seen the canal"
    observation: "Player's own crops suffering (if they farm)"

  investigation:
    options:
      - "Talk to farmers to learn situation"
      - "Travel upstream to find blockage"
      - "Ask Temple Sa-gid about canal rights"

  resolution_paths:
    repair: "Remove blockage (labor, possibly tools)"
    diplomacy: "Negotiate with whoever caused blockage"
    legal: "Report to Temple for official resolution"
    force: "Destroy blockage regardless of ownership"

  rewards:
    repair: "Gratitude of farmers (+reputation), possible SILA"
    diplomacy: "Both parties appreciative"
    legal: "Temple favor, formal resolution"
    force: "Farmers happy, but you made enemies"

  consequences_of_ignoring:
    - "Crops die, farmers angry at everyone"
    - "Food prices rise"
    - "Someone else may solve it (and get rewards)"
```

### Sample Quest Flow: The Temple Commission

```yaml
temple_commission_quest:
  setup:
    source: "Temple Sanga posts need for specific goods"
    discovery: "Announcement at temple, scribes know details"

  contract:
    terms:
      task: "Produce 50 copper bowls for Festival of Enki"
      deadline: "30 days"
      payment: "500 SILA on completion"
      penalty: "200 SILA if late, 400 if failed"
    formalization:
      - "Written contract by Temple scribe"
      - "Player applies seal or mark"
      - "Copy retained in archive"

  execution:
    challenges:
      - "Must source copper (supply chain)"
      - "Must have skill to produce (crafting)"
      - "Must produce at scale (time management)"
    solutions:
      - "Buy copper from harbor merchants"
      - "If lacking skill, subcontract to another smith"
      - "Hire apprentice NPC to assist"

  outcomes:
    success:
      - "500 SILA payment"
      - "Temple favor increase"
      - "Reputation as reliable contractor"
      - "Future contracts more likely"

    late:
      - "300 SILA payment (500 - 200 penalty)"
      - "Minor reputation damage"
      - "Future contracts harder to get"

    failure:
      - "No payment"
      - "400 SILA owed to Temple"
      - "Significant reputation damage"
      - "Temple favor lost"
```

---

*"The world does not wait for heroes. It waits for workers, thinkers, doers. Be one of them."*
