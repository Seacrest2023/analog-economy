# Multiplayer Architecture: The Shared World

> "A city is not one person. A civilization is not one family. We rise and fall together."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [World Structure](#3-world-structure)
4. [Player Interaction Modes](#4-player-interaction-modes)
5. [The Settlement System](#5-the-settlement-system)
6. [PvP Philosophy & Rules](#6-pvp-philosophy--rules)
7. [Cooperation Mechanics](#7-cooperation-mechanics)
8. [Competition Mechanics](#8-competition-mechanics)
9. [Social Systems](#9-social-systems)
10. [Technical Architecture](#10-technical-architecture)
11. [Training Data Value](#11-training-data-value)
12. [Implementation Notes](#12-implementation-notes)

---

## 1. Overview

The Analog Economy is not a single-player experience with optional multiplayer. It is a shared world where player actions affect each other, economies interconnect, and civilizations rise through cooperation and competition.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Shared persistent world** | One world, all players affect it |
| **Meaningful interaction** | Player actions impact other players |
| **Cooperation rewarded** | Group achievements > individual |
| **Conflict structured** | PvP through systems, not griefing |
| **Settlement focus** | Communities are the unit of play |

---

## 2. Design Philosophy

### 2.1 The Shared World Vision

```yaml
shared_world:
  principle: |
    All players exist in the same world. When someone builds a canal,
    it exists for everyone. When someone drains a resource, others
    feel the scarcity. When someone starts a war, everyone is affected.

  implications:
    economy:
      - "Supply and demand driven by all players"
      - "Scarcity creates real stakes"
      - "Trade is meaningful"

    social:
      - "Reputation matters across the world"
      - "Information spreads through networks"
      - "Communities form organically"

    conflict:
      - "Wars affect regional stability"
      - "Refugees flee to other areas"
      - "Victory and defeat have witnesses"
```

### 2.2 Cooperation as Optimal Strategy

```yaml
cooperation_philosophy:
  principle: |
    The game is designed so cooperation is usually the optimal strategy.
    Solo play is possible but harder. Groups achieve more than individuals.

  design_elements:
    production_bonuses:
      - "Settlements produce more than isolated players"
      - "Specialized roles more efficient than generalists"
      - "Infrastructure shared benefits everyone"

    defense_advantages:
      - "Groups can defend; individuals cannot"
      - "Walls require community investment"
      - "Watchmen need coordination"

    knowledge_sharing:
      - "Teaching is rewarded"
      - "Apprenticeships accelerate learning"
      - "Codex contributions require community"

    social_pressure:
      - "Reputation is public"
      - "Antisocial behavior has consequences"
      - "Trust is a valuable currency"
```

### 2.3 Competition with Constraints

```yaml
competition_philosophy:
  principle: |
    Competition is natural and valuable—but unconstrained competition
    destroys the experience. The game provides structures for meaningful
    rivalry without enabling griefing.

  constrained_competition:
    economic: "Compete for markets, not by destroying competitors"
    territorial: "Compete for land through systems, not murder"
    military: "Wars declared, not random killing"
    social: "Reputation competition, not harassment"
```

---

## 3. World Structure

### 3.1 World Layers

```
THE WORLD OF ERIDU
════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│                    PERSISTENT LAYER                          │
│    (Shared by all players, changes persist)                  │
│                                                              │
│    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│    │  CITY OF    │    │   TRADE     │    │   WORLD     │   │
│    │   ERIDU     │    │   ROUTES    │    │   EVENTS    │   │
│    │             │    │             │    │             │   │
│    │ • Temple    │    │ • Roads     │    │ • Floods    │   │
│    │ • Harbor    │    │ • Rivers    │    │ • Wars      │   │
│    │ • Markets   │    │ • Caravans  │    │ • Seasons   │   │
│    └─────────────┘    └─────────────┘    └─────────────┘   │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                  SETTLEMENT LAYER                            │
│    (Instanced by settlement, neighbors visible)              │
│                                                              │
│    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│    │ SETTLEMENT  │    │ SETTLEMENT  │    │ SETTLEMENT  │   │
│    │     A       │◄──►│     B       │◄──►│     C       │   │
│    │             │    │             │    │             │   │
│    │ • Farms     │    │ • Farms     │    │ • Farms     │   │
│    │ • Workshops │    │ • Workshops │    │ • Workshops │   │
│    │ • Homes     │    │ • Homes     │    │ • Homes     │   │
│    └─────────────┘    └─────────────┘    └─────────────┘   │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                    PRIVATE LAYER                             │
│    (Owned by individuals, access controlled)                 │
│                                                              │
│    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│    │   PLAYER    │    │   PLAYER    │    │   PLAYER    │   │
│    │  PROPERTY   │    │  PROPERTY   │    │  PROPERTY   │   │
│    │             │    │             │    │             │   │
│    │ • Land      │    │ • Land      │    │ • Land      │   │
│    │ • Buildings │    │ • Buildings │    │ • Buildings │   │
│    │ • Storage   │    │ • Storage   │    │ • Storage   │   │
│    └─────────────┘    └─────────────┘    └─────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Layer Details

```yaml
world_layers:
  persistent_layer:
    description: "Shared by all players, changes are permanent"
    contents:
      - "City of Eridu (public areas)"
      - "Major trade routes"
      - "Rivers and major geography"
      - "Temple complexes"
      - "World events (floods, wars)"
    instancing: "None—everyone shares"
    persistence: "Full—changes stay forever"

  settlement_layer:
    description: "Player communities with neighbors"
    contents:
      - "Agricultural zones"
      - "Craft workshops"
      - "Residential areas"
      - "Settlement infrastructure"
    instancing: "Settlements see neighbors within range"
    persistence: "Full—settlement changes persist"

  private_layer:
    description: "Individual player-owned spaces"
    contents:
      - "Owned land parcels"
      - "Private buildings"
      - "Personal storage"
      - "NPC workers"
    instancing: "Owner controls access"
    persistence: "Full—your stuff stays yours"
```

### 3.3 Population & Capacity

```yaml
population_design:
  eridu_city:
    player_capacity: "500-1000 concurrent in city proper"
    npc_population: "5000 simulated"
    instancing: "Dynamic based on density"

  regional_area:
    settlement_capacity: "10-50 players per settlement"
    settlements_per_region: "10-30"
    total_regional_capacity: "500-1500 players"

  world_total:
    initial_target: "5000-10000 concurrent players"
    scaling: "Add regions as population grows"
```

---

## 4. Player Interaction Modes

### 4.1 Interaction Matrix

| Mode | Description | Training Data Value |
|------|-------------|---------------------|
| **Trade** | Exchange goods/services | Negotiation, price discovery |
| **Cooperation** | Joint projects | Coordination, trust |
| **Competition** | Market/reputation rivalry | Strategy, adaptation |
| **Conflict** | Declared war | Group tactics, leadership |
| **Teaching** | Knowledge transfer | Pedagogy, patience |
| **Social** | Community building | Relationship dynamics |

### 4.2 Trade Interactions

```yaml
trade_interactions:
  direct_trade:
    description: "Player-to-player barter or sale"
    interface:
      - "Approach other player"
      - "Propose trade"
      - "Negotiate terms"
      - "Complete exchange"
    trust_mechanics:
      - "Trade history tracked"
      - "Reputation visible"
      - "Escrow for high-value trades (optional)"

  marketplace_trade:
    description: "Sell through market stalls"
    interface:
      - "Rent stall at market"
      - "Set prices"
      - "NPC or player manages"
      - "Buyers purchase directly"
    economics:
      - "Market fees apply"
      - "Price competition"
      - "Location matters"

  contract_trade:
    description: "Formal agreements for future delivery"
    interface:
      - "Negotiate terms"
      - "Create contract (clay tablet)"
      - "Fulfill over time"
      - "Penalties for breach"
```

### 4.3 Cooperation Interactions

```yaml
cooperation_interactions:
  joint_construction:
    description: "Building projects requiring multiple players"
    examples:
      - "Canal construction"
      - "Wall building"
      - "Temple expansion"
    mechanics:
      - "Project initiated by settlement"
      - "Resources pooled"
      - "Labor contributed"
      - "Benefits shared"

  mutual_defense:
    description: "Defending together against threats"
    examples:
      - "Raid defense"
      - "Patrol duty"
      - "Wall manning"
    mechanics:
      - "Defense roster"
      - "Alert systems"
      - "Coordinated response"

  knowledge_sharing:
    description: "Teaching and learning between players"
    examples:
      - "Apprenticeship"
      - "Skill demonstration"
      - "Codex collaboration"
    mechanics:
      - "Teacher earns SILA"
      - "Student learns faster"
      - "Both build reputation"
```

---

## 5. The Settlement System

### 5.1 Settlement Formation

```yaml
settlement_formation:
  requirements:
    minimum_players: 3
    minimum_land: "Adjacent properties"
    declaration: "Formal agreement among founders"

  process:
    1: "Players with adjacent land agree to form settlement"
    2: "Choose initial leader (rotation or election)"
    3: "Name the settlement"
    4: "Register with Temple (official recognition)"
    5: "Begin building shared infrastructure"

  benefits:
    - "Shared defense (NPCs protect whole settlement)"
    - "Communal projects possible"
    - "Trade bonuses (bulk deals)"
    - "Shared NPC workforce pool"
    - "Political representation in region"
```

### 5.2 Settlement Governance

```yaml
settlement_governance:
  leadership_models:
    autocratic:
      description: "One player rules"
      selection: "Founder, conquest, or appointment"
      powers: "Full control of settlement decisions"
      risk: "Abuse possible, rebellion possible"

    council:
      description: "Multiple players share power"
      selection: "Elected or property-based"
      powers: "Decisions by vote"
      risk: "Gridlock, factions"

    rotating:
      description: "Leadership rotates"
      selection: "Scheduled or lottery"
      powers: "Full power during term"
      risk: "Inconsistent policy"

  decision_types:
    individual: "Player decides for their property"
    settlement: "Council/leader decides for community"
    emergency: "Leader can act unilaterally in crisis"

  taxation:
    authority: "Settlement can levy taxes"
    purposes: ["Defense", "Infrastructure", "NPC wages"]
    resistance: "Players can leave if taxes too high"
```

### 5.3 Settlement Benefits

```yaml
settlement_benefits:
  defense:
    walls: "Settlement can build walls (requires cooperation)"
    guards: "Shared guard force"
    militia: "Call up members for defense"
    alert: "Warning system for threats"

  economy:
    bulk_trade: "Better prices from caravans"
    specialization: "Efficient division of labor"
    market: "Internal market for members"
    storage: "Shared granaries and warehouses"

  infrastructure:
    irrigation: "Larger canal systems"
    roads: "Maintained paths"
    wells: "Shared water access"
    temples: "Settlement shrine"

  social:
    festivals: "Community celebrations"
    courts: "Dispute resolution"
    education: "Shared teaching"
    records: "Settlement archive"
```

---

## 6. PvP Philosophy & Rules

### 6.1 The Anti-Griefing Stance

```yaml
anti_griefing:
  philosophy: |
    Random player-killing destroys communities, drives away players,
    and generates low-quality training data. We want meaningful
    conflict, not murder simulators.

  design_decisions:
    no_random_murder:
      - "Attacking unprovoked = severe karma penalty"
      - "NPCs defend victims"
      - "Outlaw status if repeated"

    structured_conflict:
      - "Wars must be declared"
      - "Raids follow rules"
      - "Consequences are real"

    protection_systems:
      - "Safe zones (Temple, markets)"
      - "New player protection"
      - "Property rights enforced"
```

### 6.2 Legal PvP Scenarios

```yaml
legal_pvp:
  declared_war:
    requirements:
      - "Settlement leader declares"
      - "Casus belli stated"
      - "3-day warning period"
    rules:
      - "Combatants may attack combatants"
      - "Civilians still protected"
      - "Property can be destroyed/captured"
    karma: "Reduced penalty for legitimate combat"

  raid_events:
    requirements:
      - "Settlement authorizes raid"
      - "Target is enemy settlement"
      - "Raid window (specific times)"
    rules:
      - "Hit and withdraw"
      - "Loot limited to what can carry"
      - "Defenders respond"
    karma: "Moderate penalty"

  ritual_duel:
    requirements:
      - "Both players agree"
      - "Witness present"
      - "Terms stated (death, first blood, submission)"
    rules:
      - "Combat to agreed terms"
      - "Winner gets agreed stakes"
      - "Loser accepts consequences"
    karma: "Minimal penalty"

  self_defense:
    requirements:
      - "Other player attacks first"
      - "Response is proportional"
    rules:
      - "Defend yourself"
      - "Can pursue if immediate"
    karma: "No penalty"

  property_defense:
    requirements:
      - "Intruder on your property"
      - "Intruder refuses to leave"
    rules:
      - "Warn first"
      - "Can use force to remove"
    karma: "No penalty if proportional"
```

### 6.3 Illegal PvP & Consequences

```yaml
illegal_pvp:
  murder:
    definition: "Killing without legal justification"
    consequences:
      karma: "-50 to -100"
      legal: "Hunted by guards, blood price owed"
      social: "All NPCs hostile, prices skyrocket"
      mechanical: "Cannot enter cities safely"

  assault:
    definition: "Attack without killing"
    consequences:
      karma: "-15 to -30"
      legal: "Fined, possible imprisonment"
      social: "Reputation damage"

  repeated_offenses:
    threshold: "3+ illegal PvP incidents"
    status: "Outlaw"
    consequences:
      - "Kill on sight for guards"
      - "Bounty placed"
      - "No legal protections"
      - "Other players can kill with reduced karma cost"
```

---

## 7. Cooperation Mechanics

### 7.1 Joint Projects

```yaml
joint_projects:
  infrastructure:
    canals:
      scope: "Multi-property irrigation"
      requirements: ["Labor", "Materials", "Coordination"]
      benefits: "Shared water access"
      maintenance: "Shared responsibility"

    walls:
      scope: "Settlement perimeter defense"
      requirements: ["Massive labor", "Materials", "Time"]
      benefits: "Raid protection"
      maintenance: "Ongoing repair needed"

    temples:
      scope: "Settlement religious center"
      requirements: ["Materials", "Skilled labor", "Temple approval"]
      benefits: "Temple favor, services access"
      maintenance: "Offerings, upkeep"

  economic:
    trade_missions:
      scope: "Organized caravan"
      requirements: ["Goods", "Guards", "Transport"]
      benefits: "Better trade rates"
      risk: "Shared if mission fails"

    bulk_purchasing:
      scope: "Combined buying power"
      requirements: ["Coordinated demand"]
      benefits: "Lower prices"
      challenge: "Distribution"
```

### 7.2 Mutual Aid

```yaml
mutual_aid:
  emergency_response:
    flood: "Neighbors help with levees, rescue, recovery"
    raid: "Settlement members defend together"
    illness: "Community care for sick"
    famine: "Food sharing during scarcity"

  regular_support:
    harvest: "Labor sharing during busy times"
    construction: "Barn-raising style cooperation"
    childcare: "NPCs and players share duties"
    education: "Community teaching"

  reciprocity:
    tracking: "Informal 'who owes whom'"
    culture: "Helping builds social capital"
    enforcement: "Reputation for reliability"
```

---

## 8. Competition Mechanics

### 8.1 Economic Competition

```yaml
economic_competition:
  market_competition:
    description: "Compete for customers through price and quality"
    rules:
      - "Set your own prices"
      - "Quality affects reputation"
      - "Location matters"
    limits:
      - "Cannot destroy competitor's stall"
      - "Cannot assault competitor"
      - "Cannot steal inventory"

  resource_competition:
    description: "Compete for limited resources"
    rules:
      - "First to harvest claims resources"
      - "Land ownership protects resources"
      - "Water rights can be contested legally"
    limits:
      - "Cannot trespass to take resources"
      - "Cannot poison others' land"

  contract_competition:
    description: "Compete for lucrative contracts"
    rules:
      - "Submit bids"
      - "Reputation affects selection"
      - "Fulfill contracts reliably"
    limits:
      - "Cannot sabotage competitors"
      - "Cannot bribe (well, shouldn't be caught)"
```

### 8.2 Reputation Competition

```yaml
reputation_competition:
  status_seeking:
    description: "Compete for social standing"
    methods:
      - "Temple donations"
      - "Public works"
      - "Festival sponsorship"
      - "Codex contributions"
    visibility: "Leaderboards for achievements"

  political_competition:
    description: "Compete for leadership roles"
    methods:
      - "Build faction support"
      - "Demonstrate competence"
      - "Form alliances"
    outcomes:
      - "Settlement leadership"
      - "Temple positions"
      - "Regional influence"
```

---

## 9. Social Systems

### 9.1 Communication

```yaml
communication:
  proximity_chat:
    range: "Nearby players hear"
    privacy: "None—can be overheard"
    use: "Daily interaction"

  messenger_system:
    method: "Send written message via NPC courier"
    cost: "Small SILA fee"
    time: "Delivery based on distance"
    privacy: "Message can be intercepted"

  settlement_announcements:
    method: "Posted in settlement center"
    visibility: "All settlement members"
    use: "Official communications"

  trade_postings:
    method: "Market board"
    visibility: "Anyone at market"
    use: "Advertising goods/services"
```

### 9.2 Social Organization

```yaml
social_organization:
  families:
    formation: "Marriage contract + shared household"
    benefits:
      - "Inheritance mechanics"
      - "Labor pooling"
      - "Reputation sharing"
    challenges:
      - "Coordination required"
      - "Disputes possible"

  guilds:
    formation: "Craftsmen of same trade organize"
    benefits:
      - "Price coordination"
      - "Quality standards"
      - "Training programs"
      - "Political influence"
    challenges:
      - "Entry requirements"
      - "Dues"
      - "Rule following"

  factions:
    formation: "Players with shared interests align"
    benefits:
      - "Political power"
      - "Mutual support"
      - "Shared resources"
    challenges:
      - "Internal politics"
      - "Enemy factions"
```

---

## 10. Technical Architecture

### 10.1 Server Architecture

```yaml
server_architecture:
  world_server:
    responsibility: "Global state, economy, events"
    technology: "Central database, event processing"
    scaling: "Vertical (powerful single instance)"

  region_servers:
    responsibility: "Settlement simulation, local physics"
    technology: "Distributed instances"
    scaling: "Horizontal (add servers for regions)"

  player_servers:
    responsibility: "Individual player state, inventory"
    technology: "Sharded by player ID"
    scaling: "Horizontal (add shards as needed)"

  communication:
    between_players: "Real-time within region"
    between_regions: "Async for messages, sync for travel"
    to_world: "Batch updates for economy, events"
```

### 10.2 Synchronization

```yaml
synchronization:
  high_priority:
    what: "Combat, trade, immediate interaction"
    latency: "<100ms"
    method: "Direct server communication"

  medium_priority:
    what: "NPC behavior, environmental state"
    latency: "<500ms"
    method: "Regular updates"

  low_priority:
    what: "Economy aggregates, distant events"
    latency: "<5s"
    method: "Batch processing"

  eventual_consistency:
    what: "Reputation, historical records"
    latency: "Minutes to hours"
    method: "Background sync"
```

### 10.3 Offline Handling

```yaml
offline_handling:
  property:
    - "NPCs continue working (delegated tasks)"
    - "Defenses remain active"
    - "Storage protected"

  economy:
    - "Shop NPCs sell at set prices"
    - "Resources accumulate"
    - "Taxes still due"

  events:
    - "Log of significant events"
    - "Notification on login"
    - "Damage/loss recorded"

  limitations:
    - "Cannot defend personally"
    - "Cannot respond to opportunities"
    - "NPCs have limited capability"
```

---

## 11. Training Data Value

### 11.1 Social Dynamics Data

```yaml
social_training_data:
  cooperation_patterns:
    - "How do groups form?"
    - "What enables trust?"
    - "How is free-riding handled?"
    - "What makes cooperation stable?"

  conflict_patterns:
    - "What causes conflicts?"
    - "How do conflicts escalate?"
    - "How are conflicts resolved?"
    - "What prevents conflicts?"

  leadership_emergence:
    - "How do leaders emerge?"
    - "What makes leaders effective?"
    - "How do leaders lose power?"
    - "How do followers decide who to follow?"

  economic_behavior:
    - "How do markets form?"
    - "How is price discovered?"
    - "How do monopolies form and fall?"
    - "How does scarcity affect behavior?"
```

### 11.2 Coordination Data

```yaml
coordination_training_data:
  group_decision_making:
    - "How do groups make decisions?"
    - "What causes gridlock?"
    - "How is consensus reached?"
    - "How do minorities affect decisions?"

  resource_allocation:
    - "How do groups share resources?"
    - "What is perceived as fair?"
    - "How are contributions tracked?"
    - "How is shirking punished?"

  communication_patterns:
    - "How does information spread?"
    - "What gets communicated?"
    - "How do rumors form?"
    - "How is misinformation handled?"
```

---

## 12. Implementation Notes

### 12.1 MVP Scope

```yaml
mvp_multiplayer:
  included:
    world_structure:
      - "Single region with Eridu"
      - "Settlement formation (basic)"
      - "Property ownership"

    interaction:
      - "Direct trade"
      - "Proximity chat"
      - "Joint construction (simple)"

    pvp:
      - "Self-defense legal"
      - "Murder illegal with karma"
      - "Basic war declaration"

    social:
      - "Reputation system"
      - "Simple settlement governance"

  deferred:
    - "Multiple regions"
    - "Complex guild system"
    - "Political factions"
    - "Elaborate war mechanics"
    - "Cross-region trade"
```

### 12.2 Performance Targets

```yaml
performance_targets:
  player_density:
    city_center: "100 players visible simultaneously"
    settlement: "50 players"
    wilderness: "10-20 players"

  latency:
    combat: "<100ms"
    trade: "<200ms"
    chat: "<300ms"

  uptime:
    target: "99.5%"
    maintenance: "Scheduled, announced"
```

---

## Appendix: Quick Reference

### Interaction Mode Summary

| Mode | Legal? | Karma Cost | Requirements |
|------|--------|------------|--------------|
| Trade | Always | None | Agreement |
| Cooperation | Always | None | Participation |
| Economic Competition | Always | None | Market participation |
| War (Declared) | Yes | Reduced | Declaration + waiting |
| Raid | If sanctioned | Moderate | Settlement approval |
| Duel | If agreed | Minimal | Both consent + witness |
| Self-Defense | Yes | None | Being attacked first |
| Murder | No | Severe | Breaking the rules |

### Settlement Size Benefits

| Size | Defense | Economy | Politics |
|------|---------|---------|----------|
| 3-5 | Basic walls | Shared storage | Informal |
| 6-15 | Guard force | Market | Council |
| 16-30 | Full fortification | Guild presence | Formal governance |
| 31+ | Regional power | Trade hub | Political faction |

---

*"One reed breaks easily. A bundle of reeds cannot be broken."*
