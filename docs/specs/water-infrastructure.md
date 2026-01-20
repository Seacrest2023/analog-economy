# Water & Infrastructure

> *"Control water, control life. The canal is law made mud. The levee is promise made earth. Break either, and the city breaks with it."*

## Overview

Water management is the foundation of civilization in Eridu. Over 4,000 secondary canals and 200 primary canals support the region's agriculture. This spec covers the irrigation system, corvée labor obligations, the Gugallu (Canal Inspector) role, water rights and disputes, and the infrastructure maintenance that every citizen must contribute to.

---

## Design Philosophy

### Core Principles

1. **Water = Survival**: No irrigation = no agriculture = death
2. **Community Obligation**: Everyone must contribute to maintenance
3. **Strict Liability**: Negligence has severe consequences
4. **Political Conflict**: Water rights cause wars
5. **Training Data Value**: Resource management, civic duty, conflict resolution

### The Inverted Challenge

```yaml
mesopotamian_water_problem:
  nile_comparison:
    egypt: "River floods during growing season"
    mesopotamia: "Rivers peak AFTER planting, lowest when needed"

  solution:
    canals: "Store and distribute water"
    levees: "Control flooding"
    timing: "Precise management required"

  consequence:
    success: "Abundant harvests"
    failure: "Famine and death"
```

---

## The Canal System

### Infrastructure Hierarchy

```yaml
canal_hierarchy:
  primary_canals:
    count: "~200 in region"
    width: "10-30 meters"
    source: "Direct from Euphrates"
    maintenance: "Royal/temple authority"
    flow: "Year-round (ideally)"

  secondary_canals:
    count: "~4,000+ in region"
    width: "2-10 meters"
    source: "Branch from primaries"
    maintenance: "Community responsibility"
    flow: "Seasonal variation"

  tertiary_channels:
    description: "Field-level irrigation"
    width: "Under 2 meters"
    source: "Branch from secondaries"
    maintenance: "Individual farmer"
    control: "Personal sluice gates"

  reservoirs:
    purpose: "Store water for dry periods"
    size: "Variable"
    management: "Community or temple"
```

### Water Flow Mechanics

```yaml
water_distribution:
  gravity_system:
    principle: "High river levees allow gravity flow"
    slope: "Gradual descent to fields"
    no_pumps: "Entirely gravity-fed"

  seasonal_variation:
    peak_flow: "April-May (snowmelt)"
    problem: "Just before harvest"
    low_flow: "September (planting season)"
    challenge: "Water needed when scarce"

  sluice_gates:
    purpose: "Control water to individual fields"
    operation: "Open/close manually"
    timing: "Scheduled allocation"
```

---

## Corvée Labor System

### The Labor Tax

```yaml
corvee_system:
  description: "Mandatory public labor contribution"

  obligation:
    who: "All land-holding males"
    frequency: "Seasonal (dry season)"
    duration: "Days to weeks per project"
    authority: "King/temple commands"

  exemptions:
    priests: "Sometimes exempt"
    elderly: "May pay substitute"
    ill: "Medical excuse (documented)"
    essential_workers: "Case by case"

  refusal:
    consequence: "Loss of water rights"
    social: "Community shunning"
    legal: "Fines, forced labor"
```

### The Silt-Basket Chain

```yaml
silt_removal:
  the_problem:
    cause: "Euphrates carries heavy silt"
    rate: "Can block canal in one season"
    consequence: "No water = no crops"

  the_solution:
    method: "Silt-basket chain"
    process:
      step_1: "Workers at canal bottom fill baskets"
      step_2: "Pass baskets up human chain"
      step_3: "Empty on levee banks"
      step_4: "Return empty baskets down"
    duration: "Hours to days per section"

  participation:
    composition: "All classes work together"
    roles:
      - "Farmers"
      - "Shepherds"
      - "Craftsmen"
      - "Temple workers"
      - "Even some scribes"
    equality: "Physical labor levels hierarchy"

  gameplay:
    karma: "+3 per day of labor"
    sanity: "-2 per day (exhausting)"
    social: "Build community bonds"
    skip: "Major reputation damage"
```

### Levee Construction and Repair

```yaml
levee_engineering:
  purpose:
    flood_control: "Prevent uncontrolled flooding"
    water_retention: "Keep water in channels"
    path_function: "Roads along levee tops"

  construction:
    foundation:
      material: "Reeds soaked in bitumen"
      purpose: "Waterproofing base"

    structure:
      material: "Mud bricks"
      technique: "Layered construction"

    maintenance:
      inspection: "Regular checks"
      repair: "Immediate when damage found"

  failure_consequences:
    breach: "Uncontrolled flooding"
    crop_loss: "Entire fields destroyed"
    blame: "Section owner responsible"
```

---

## The Gugallu (Canal Inspector)

### Role and Authority

```yaml
gugallu_role:
  title: "Gugallu - Canal Inspector"
  authority: "Water law enforcement"
  appointment: "Temple or royal"

  responsibilities:
    distribution:
      - "Manage water allocation"
      - "Enforce time limits"
      - "Ensure fair access"

    maintenance:
      - "Inspect levee conditions"
      - "Order repairs"
      - "Organize corvée labor"

    disputes:
      - "Mediate neighbor conflicts"
      - "Document violations"
      - "Report serious cases"

  tools:
    water_clock:
      purpose: "Measure allocation time precisely"
      operation: "Draining vessel"
      authority: "Decisions are binding"

    official_seal:
      purpose: "Authenticate documents"
      power: "Legal weight"
```

### Water Allocation System

```yaml
water_allocation:
  scheduling:
    method: "Rotation by field/farmer"
    timing: "Set hours per landholding"
    measurement: "Water clock"

  priority:
    temple_lands: "First priority"
    royal_lands: "Second priority"
    private_lands: "By established rights"

  process:
    step_1: "Farmer's turn arrives"
    step_2: "Open personal sluice gate"
    step_3: "Water clock started"
    step_4: "Time expires - close gate"
    step_5: "Next farmer's turn"

  violations:
    exceeding_time:
      detection: "Gugallu monitoring"
      penalty: "Fines, reduced future allocation"

    unauthorized_diversion:
      detection: "Neighbor complaints, inspection"
      penalty: "Severe fines, legal action"
```

### Gugallu as Player Path

```yaml
gugallu_profession:
  entry_requirements:
    land_ownership: "Must own irrigated land"
    literacy: "Basic cuneiform helpful"
    reputation: "Clean community standing"
    connections: "Temple or political support"

  progression:
    assistant:
      duties: "Help with measurements"
      income: "Small stipend"

    junior_inspector:
      duties: "Monitor section of canal"
      income: "Modest salary"

    full_gugallu:
      duties: "Control entire district"
      income: "Significant + benefits"

    chief_inspector:
      duties: "Coordinate multiple districts"
      income: "Elite status"

  temptations:
    bribes:
      offer: "Extra water for payment"
      karma_cost: "-20 if discovered"
      risk: "Career ending"

    favoritism:
      temptation: "Help friends, hurt enemies"
      karma_cost: "-10 to -30"
      detection: "Community resentment"

  sila_rewards:
    fair_dispute_resolution: 30
    successful_maintenance_project: 50
    prevent_water_crisis: 100
```

---

## Water Rights and Disputes

### Legal Framework

```yaml
water_rights:
  establishment:
    basis: "Land ownership"
    documentation: "Recorded allocations"
    inheritance: "Passes with land"

  hierarchy:
    1: "Temple/state lands"
    2: "Long-established rights"
    3: "Recent grants"
    4: "New settlers"

  modification:
    process: "Petition to authority"
    approval: "Rare, contentious"
    compensation: "May require payment"
```

### Common Disputes

```yaml
water_disputes:
  neighbor_conflicts:
    cause: "Exceeded allocation time"
    resolution: "Gugallu mediation"
    penalty: "Fines, reduced time"

  upstream_diversion:
    cause: "Farmer blocks or diverts canal"
    resolution: "Legal action"
    penalty: "Restoration + damages"

  levee_neglect:
    cause: "Failed to maintain section"
    consequence: "Neighbor's crops flooded"
    liability: "Replace all lost grain"
    basis: "Strict liability - no excuses"

  channel_encroachment:
    cause: "Building on canal right-of-way"
    resolution: "Forced removal"
    penalty: "Fines + restoration costs"
```

### Interstate Water Conflicts

```yaml
city_state_conflicts:
  historical_example:
    parties: "Umma vs. Lagash"
    cause: "Upstream diversion of Euphrates"
    duration: "Century-long conflict"
    resolution: "Mesilim Treaty (2550 BCE)"

  gameplay_implications:
    trade: "Water conflicts affect commerce"
    politics: "Alliances form around water"
    war: "Ultimate resolution method"

  player_involvement:
    diplomacy: "Negotiate water rights"
    espionage: "Investigate diversions"
    military: "Fight for water access"
```

---

## Liability and Law

### Personal Responsibility

```yaml
liability_rules:
  levee_section:
    principle: "Your land = your levee section"
    duty: "Maintain to standard"
    inspection: "Gugallu checks"

  breach_liability:
    if_your_section_fails:
      responsibility: "Full liability"
      damages: "Replace neighbor's crop loss"
      calculation: "Grain quantity destroyed"
      defense: "None - strict liability"

  negligence_standard:
    minor: "Warning, small fine"
    moderate: "Significant fine"
    severe: "Full replacement + additional penalty"
    repeated: "Loss of water rights"
```

### Dispute Resolution

```yaml
resolution_process:
  level_1_gugallu:
    scope: "Minor disputes"
    process: "On-site mediation"
    authority: "Binding for small matters"

  level_2_elder_council:
    scope: "Significant disputes"
    process: "Hearing with witnesses"
    authority: "Community judgment"

  level_3_temple_court:
    scope: "Major disputes, sacred water"
    process: "Formal legal proceeding"
    authority: "Religious sanction"

  level_4_royal_court:
    scope: "Interstate, catastrophic"
    process: "King's judgment"
    authority: "Final appeal"
```

---

## Infrastructure Projects

### Major Works

```yaml
major_projects:
  new_canal:
    scope: "Extend irrigation to new areas"
    authority: "King orders"
    labor: "Massive corvée"
    duration: "Months to years"
    player_role: "Labor, supervision, planning"

  canal_widening:
    scope: "Increase capacity"
    reason: "Growing demand"
    labor: "Large corvée"
    player_role: "Participate or supervise"

  reservoir_construction:
    scope: "Create water storage"
    benefit: "Buffer for dry periods"
    engineering: "Complex project"
    player_role: "Planning, labor, maintenance"

  levee_reinforcement:
    scope: "Strengthen flood defenses"
    trigger: "After near-breach or flood"
    urgency: "High priority"
    player_role: "Emergency labor"
```

### Maintenance Calendar

```yaml
maintenance_schedule:
  dry_season: "Primary maintenance period"
    activities:
      - "Silt removal"
      - "Levee repair"
      - "Gate replacement"
      - "Channel clearing"
    labor: "Corvée obligations"

  pre_flood: "Inspection and preparation"
    activities:
      - "Check all gates"
      - "Reinforce weak points"
      - "Clear debris"
    urgency: "Critical timing"

  flood_season: "Monitoring and emergency"
    activities:
      - "Watch for breaches"
      - "Emergency repairs"
      - "Water level tracking"
    risk: "Highest"

  growing_season: "Minimal disturbance"
    activities:
      - "Routine allocation"
      - "Minor repairs only"
    priority: "Don't disrupt farming"
```

---

## Gameplay Integration

### Player Obligations

```yaml
player_duties:
  land_owners:
    corvee: "Mandatory labor participation"
    levee: "Maintain your section"
    reporting: "Inform Gugallu of problems"

  tenants:
    labor: "May substitute for owner"
    gate: "Proper operation"
    compliance: "Follow allocation rules"

  squatters:
    limited_access: "No guaranteed water rights"
    opportunity: "Earn rights through labor"
    vulnerability: "Last priority"
```

### Consequences

```yaml
consequences:
  skip_corvee:
    reputation: "Major damage"
    legal: "Fines"
    social: "Community anger"
    karma: "-15"

  neglect_levee:
    inspection: "Gugallu cites you"
    deadline: "Must repair"
    failure: "Liability for damages"
    karma: "-10 to -50"

  water_theft:
    detection: "Gugallu or neighbor"
    penalty: "Severe fines"
    reputation: "Pariah status"
    karma: "-25"

  exemplary_service:
    recognition: "Community praise"
    benefit: "Favor with authorities"
    karma: "+20"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  resource_management:
    - "Water allocation decisions"
    - "Scarcity response"
    - "Long-term planning"

  civic_reasoning:
    - "Balancing personal vs. community"
    - "Obligation fulfillment"
    - "Fairness judgments"

  conflict_resolution:
    - "Dispute mediation"
    - "Evidence evaluation"
    - "Compromise negotiation"

  engineering_knowledge:
    - "Infrastructure design"
    - "Maintenance planning"
    - "Failure prevention"
```

---

## Implementation Notes

### Database Schema

```yaml
infrastructure_records:
  canal_section:
    section_id: uuid
    parent_canal: uuid
    responsible_party: uuid  # land owner
    condition: integer  # 0-100
    last_inspection: datetime
    maintenance_due: boolean

  water_allocation:
    allocation_id: uuid
    land_parcel: uuid
    time_units: integer
    priority: integer
    current_status: enum

  corvee_record:
    player_id: uuid
    season: string
    days_owed: integer
    days_completed: integer
    projects: array
```

---

## Appendix: Sumerian Water Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Gugallu** | Canal Inspector | Water authority |
| **Id** | Canal/river | Water source |
| **Eg** | Levee/dike | Flood control |
| **A** | Water | Basic resource |
| **A-gar** | Irrigated field | Farmland |

---

*"The canal does not care who you are. It demands its tribute of labor from all. Refuse, and the water refuses you. This is not cruelty—this is the covenant between people and land."*
