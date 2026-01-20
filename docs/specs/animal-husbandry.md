# Animal Husbandry

> *"The shepherd who knows his flock knows wealth. The breeder who improves bloodlines builds dynasty. The veterinarian who saves the temple herd earns eternal gratitude."*

## Overview

Animal husbandry in Eridu is a sophisticated science, not primitive herding. Sumerians maintained "stud books" (cuneiform records), practiced selective breeding, and developed veterinary medicine. This spec covers the Sipa (shepherd) profession, livestock management, breeding systems, veterinary care, and the legal contracts that govern flock management.

---

## Design Philosophy

### Core Principles

1. **Scientific Management**: Breeding records, lineage tracking, quality improvement
2. **High Stakes Contracts**: Shepherds are legally liable for flock health
3. **Supply Chain Integration**: Animals feed textiles, food, transport, sacrifice
4. **Skill Progression**: From basic herding to elite bloodline development
5. **Training Data Value**: Animal behavior prediction, disease recognition, breeding decisions

### Economic Integration

```yaml
animal_economy:
  wool_production:
    destination: "Textile industry (90% of economy)"
    cycle: "Annual spring plucking"

  meat_production:
    rule: "Only surplus males slaughtered"
    reason: "Breeding stock too valuable"

  dairy:
    products: "Milk, cheese, ghee"
    source: "Goats primarily, some cattle"

  transport:
    animals: "Donkeys, oxen"
    critical: "Trade, agriculture"

  sacrifice:
    demand: "Temple requires animals"
    premium: "Unblemished specimens"

  status:
    cattle: "Wealth symbol"
    fat_tailed_sheep: "Elite breeding"
```

---

## Livestock Types

### Sheep (Udu)

```yaml
sheep:
  importance: "Economic backbone"

  breeds:
    white_wool:
      value: "Highest (takes dye best)"
      breeding_goal: "Maximize white offspring"
      temple_demand: "Strong"

    carpet_wool:
      value: "Moderate"
      use: "Rugs, heavy textiles"
      fiber: "Coarse, long"

    fat_tailed:
      value: "High"
      product: "Tail fat for cooking, lamps"
      prestige: "Elite ownership"

  products:
    wool:
      harvest: "Spring plucking (not shearing)"
      yield: "3-5 pounds per sheep"

    meat:
      frequency: "Surplus males, old ewes"
      value: "Secondary to wool"

    milk:
      limited: "Sheep milk less common"

    hides:
      use: "Leather, parchment"

  herd_sizes:
    small: "10-30 (family operation)"
    medium: "50-200 (professional shepherd)"
    large: "500+ (temple flocks)"
```

### Goats (Uz)

```yaml
goats:
  role: "The commoner's animal"

  characteristics:
    hardiness: "Survives poor conditions"
    diet: "Eats what sheep won't"
    temperament: "Independent, clever"

  products:
    milk:
      importance: "Primary dairy animal"
      products: "Fresh milk, cheese, yogurt"

    meat:
      quality: "Lean, flavorful"
      frequency: "More often than sheep"

    hair:
      use: "Waterproof textiles, tents, bags"
      value: "Lower than wool"

    hides:
      use: "Water containers, leather goods"

  ownership:
    typical: "Commoners, small holders"
    reason: "Lower cost, easier care"
```

### Cattle (Gu)

```yaml
cattle:
  status: "Symbols of power and wealth"

  requirements:
    water: "Massive amounts"
    food: "Grain, quality pasture"
    expense: "Only temples/elites afford"

  uses:
    oxen:
      primary: "Plow power"
      importance: "Agriculture depends on them"
      value: "Extremely high"

    dairy:
      yield: "More than goats"
      products: "Milk, butter, ghee"

    sacrifice:
      prestige: "Highest temple offering"
      occasions: "Major festivals, emergencies"

    meat:
      rarity: "Only old or surplus"
      reason: "Too valuable alive"

  ownership:
    temple: "Primary owner"
    elite: "Status symbol"
    commoner: "Rarely affordable"
```

### Donkeys (Anshe)

```yaml
donkeys:
  role: "Primary transport before horses"

  uses:
    carrying:
      capacity: "100-150 pounds"
      terrain: "Any reasonable path"

    caravans:
      importance: "Long-distance trade"
      endurance: "Excellent"

    breeding:
      onagers: "Wild asses for crossbreeding"
      goal: "Stronger, docile hybrids"

  ownership:
    merchants: "Essential for trade"
    farmers: "Transport to market"
    temple: "Administrative logistics"
```

---

## The Shepherd Profession (Sipa)

### Role and Responsibility

```yaml
sipa_role:
  description: "Professional animal manager"

  responsibilities:
    daily_care:
      - "Lead to pasture"
      - "Ensure water access"
      - "Protect from predators"
      - "Monitor health"

    seasonal:
      - "Manage lambing (spring)"
      - "Coordinate wool harvest"
      - "Organize breeding"
      - "Prepare winter shelter"

    administrative:
      - "Keep accurate counts"
      - "Maintain lineage records"
      - "Report to owner"

  legal_status:
    liability: "Personally responsible for flock"
    contract: "Specific terms with owner"
    risk: "Pay for losses beyond natural"
```

### The Shepherd's Contract

```yaml
shepherds_contract:
  terms:
    base_flock: "X animals received"
    return_requirement: "100% of original count"
    growth_quota: "20-25% increase (lambs)"
    period: "Typically one year"

  proof_of_loss:
    natural_death: "Must produce hide and sinews"
    predator_kill: "Must show evidence"
    theft: "Oath before gods"
    failure_to_prove: "Charged for theft"

  compensation:
    success: "Percentage of surplus"
    bonus: "Quality improvement rewards"
    rations: "Food during contract"

  penalties:
    missing_animal: "Full replacement value"
    negligence: "Additional fines"
    fraud: "Severe legal consequences"

gameplay_implications:
  risk: "High personal liability"
  reward: "Independence, steady income"
  skill_value: "Better shepherds lose fewer animals"
```

### Shepherd Skill Tree

```yaml
shepherd_skills:
  tier_1_novice:
    skills:
      basic_herding:
        description: "Move animals safely"
        sila_reward: 15
        technique: "Voice commands, positioning"

      fold_construction:
        description: "Build nighttime enclosures"
        sila_reward: 20
        materials: "Reed, mud, available materials"

      predator_awareness:
        description: "Recognize threats"
        sila_reward: 15
        threats: "Lions, leopards, wolves"

    earnings: "Contract terms + rations"
    loss_rate: "5-10% (high)"

  tier_2_apprentice:
    requirements: "1 year herding"
    skills:
      breeding_selection:
        description: "Choose best mating pairs"
        sila_reward: 30
        impact: "Flock quality improvement"

      lambing_assistance:
        description: "Help difficult births"
        sila_reward: 35
        critical: "Save mother and lamb"

      pasture_rotation:
        description: "Manage grazing areas"
        sila_reward: 25
        benefit: "Sustainable land use"

    earnings: "Better contract terms"
    loss_rate: "3-5% (moderate)"

  tier_3_journeyman:
    requirements: "3 years + quality record"
    skills:
      lineage_records:
        description: "Track bloodlines for breeding"
        sila_reward: 50
        requires: "Basic literacy helps"

      seasonal_timing:
        description: "Optimize birth seasons"
        sila_reward: 40
        goal: "Spring lambs = best survival"

      disease_recognition:
        description: "Early illness detection"
        sila_reward: 50
        value: "Prevent epidemic loss"

    earnings: "Premium contracts, temple flocks"
    loss_rate: "1-3% (low)"

  tier_4_master:
    requirements: "10 years + reputation"
    skills:
      elite_bloodlines:
        description: "Develop superior animals"
        sila_reward: 100
        legacy: "Your lines become famous"

      veterinary_expertise:
        description: "Treat most conditions"
        sila_reward: 100
        income: "Consultation fees"

      large_flock_management:
        description: "Oversee 500+ animals"
        sila_reward: 100
        role: "Temple flock superintendent"

    earnings: "Elite status, significant wealth"
    loss_rate: "Under 1%"
```

---

## Breeding Systems

### Selective Breeding

```yaml
breeding_program:
  record_keeping:
    method: "Clay tablet lineage records"
    information:
      - "Parent animals"
      - "Birth date"
      - "Physical characteristics"
      - "Quality ratings"

  selection_criteria:
    wool_quality:
      traits: "Color, softness, density"
      goal: "Pure white, fine fiber"

    body_type:
      traits: "Size, conformation"
      goal: "Healthy, productive animals"

    temperament:
      traits: "Docility, flock behavior"
      goal: "Easy to manage"

    productivity:
      traits: "Milk yield, fertility"
      goal: "Maximum output"

  separation_protocol:
    rams_from_ewes: "Control breeding timing"
    purpose: "Spring lambs (best survival)"
    duration: "Separate except mating season"

  improvement_timeline:
    generation_1: "Select best parents"
    generation_2: "Improved offspring"
    generation_3: "Noticeable quality increase"
    generation_10: "Distinct superior line"

  sila_rewards:
    create_breeding_record: 30
    successful_breeding_season: 40
    develop_superior_line: 150
```

### Branding and Identification

```yaml
animal_identification:
  temple_flocks:
    method: "Clay tags on ears or horn marks"
    purpose: "Prove ownership"
    record: "Central temple registry"

  private_animals:
    method: "Owner's distinctive mark"
    registration: "Witnessed, recorded"
    disputes: "Mark is legal proof"

  stolen_animals:
    detection: "Wrong mark = theft evidence"
    penalty: "Severe (multiple replacement)"
```

---

## Veterinary Medicine

### Common Diseases

```yaml
livestock_diseases:
  anthrax:
    symptoms: "Sudden death, blood from orifices"
    cause: "Contaminated soil"
    treatment:
      prevention: "Avoid infected areas"
      response: "Quarantine, burn carcasses"
    risk: "Can destroy entire flock"

  foot_and_mouth:
    symptoms: "Mouth sores, lameness"
    cause: "Viral infection"
    treatment:
      isolation: "Move to distant marsh"
      care: "Rest, soft food"
    contagion: "Highly spreadable"

  parasites:
    symptoms: "Weight loss, dull coat, weakness"
    types: "Intestinal worms, liver flukes"
    cause: "Canal water, contaminated pasture"
    treatment:
      herbal_drench: "Worming medicines"
      pasture_rotation: "Break parasite cycle"

  mange:
    symptoms: "Hair loss, scratching, sores"
    cause: "Mites and ticks"
    treatment:
      dip: "Bitumen + sulfur in oil"
      application: "Full body treatment"
    prevention: "Regular inspections"

  bloat:
    symptoms: "Distended stomach, distress"
    cause: "Rich wet pasture"
    treatment:
      immediate: "Physical manipulation"
      prevention: "Gradual pasture changes"
    risk: "Can be fatal if untreated"
```

### Veterinary Profession

```yaml
veterinary_specialization:
  practitioner: "Asu specialized in animals"

  training_path:
    start: "Shepherd with medical interest"
    development: "Learn treatments"
    specialization: "Full veterinary focus"

  services:
    diagnosis: "Identify illness"
    treatment: "Administer cures"
    prevention: "Advise on herd health"
    emergency: "Difficult births, injuries"

  pricing:
    consultation: "10-30 SILA"
    treatment: "20-100 SILA (varies by complexity)"
    ongoing_contract: "Monthly retainer for large flocks"

  liability:
    success: "Payment + reputation"
    failure: "No payment, reputation risk"
    negligence: "Possible legal action"

  sila_rewards:
    learn_basic_treatment: 30
    cure_serious_illness: 50
    save_valuable_animal: 75
```

---

## Flock Management

### Daily Operations

```yaml
daily_routine:
  dawn:
    activity: "Count and inspect flock"
    purpose: "Detect overnight problems"

  morning:
    activity: "Lead to pasture"
    consideration: "Fresh grazing, water access"

  midday:
    activity: "Rest in shade"
    duty: "Watch for predators"

  afternoon:
    activity: "Continue grazing"
    preparation: "Move toward fold"

  evening:
    activity: "Return to fold"
    tasks: "Final count, close enclosure"

  night:
    duty: "Guard from predators"
    rotation: "Shared watch if multiple shepherds"
```

### Seasonal Calendar

```yaml
seasonal_cycle:
  spring:
    events:
      lambing:
        timing: "Early spring"
        intensity: "Busiest season"
        critical: "Lamb survival"

      wool_harvest:
        method: "Plucking during molt"
        timing: "After lambing"
        skill: "Maximize yield, minimize harm"

    focus: "Birth assistance, newborn care"

  summer:
    events:
      grazing:
        location: "Best pastures"
        management: "Rotation for sustainability"

      breeding_prep:
        activity: "Evaluate rams for fall"
        selection: "Choose mating pairs"

    focus: "Growth, health maintenance"

  autumn:
    events:
      breeding:
        timing: "Controlled mating"
        records: "Document pairings"
        goal: "Spring births"

      market:
        activity: "Sell surplus animals"
        evaluation: "End of year accounting"

    focus: "Reproduction, economics"

  winter:
    events:
      shelter:
        necessity: "Cold, wet conditions"
        feeding: "Stored fodder if needed"

      gestation:
        monitoring: "Pregnant ewes"
        preparation: "Spring lambing"

    focus: "Protection, preparation"
```

---

## Economic Structures

### Temple Flocks

```yaml
temple_flock_system:
  scale: "Thousands of animals"

  organization:
    superintendent:
      role: "Overall flock manager"
      status: "Temple official"

    shepherds:
      contract: "Standard shepherd terms"
      supervision: "Regular reporting"

  purposes:
    wool: "Temple textile production"
    sacrifice: "Ritual requirements"
    wealth: "Temple treasury"

  player_paths:
    shepherd:
      role: "Contract herder"
      income: "Stable, temple backing"

    supervisor:
      requirements: "Master shepherd skills"
      income: "Significant, elite status"
```

### Private Herding

```yaml
private_ownership:
  small_holder:
    flock_size: "5-20 animals"
    management: "Family operation"
    purpose: "Wool sale, household use"

  professional:
    flock_size: "50-200"
    contracts: "Multiple clients possible"
    income: "Primary livelihood"

  cooperative:
    structure: "Multiple families share herd"
    management: "Rotating responsibility"
    benefit: "Shared risk"
```

---

## Supply Chain Integration

### From Hoof to Product

```yaml
supply_chain:
  wool_path:
    step_1: "Shepherd raises sheep"
    step_2: "Spring plucking harvest"
    step_3: "Wool sold to temple or private"
    step_4: "Textile production"
    step_5: "Finished goods to market"

  meat_path:
    step_1: "Surplus males identified"
    step_2: "Sold to butcher or direct"
    step_3: "Slaughter and processing"
    step_4: "Fresh meat to market"

  dairy_path:
    step_1: "Daily milking (goats)"
    step_2: "Immediate consumption or processing"
    step_3: "Cheese, ghee production"
    step_4: "Products to market"

  transport_integration:
    donkeys: "Move goods to market"
    oxen: "Plow fields (agriculture link)"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  animal_behavior:
    - "Predicting flock movement"
    - "Reading animal health signs"
    - "Understanding herd dynamics"

  breeding_decisions:
    - "Selection criteria reasoning"
    - "Lineage optimization"
    - "Long-term planning"

  disease_management:
    - "Symptom recognition"
    - "Treatment selection"
    - "Prevention strategies"

  economic_reasoning:
    - "Contract negotiation"
    - "Risk assessment"
    - "Market timing"
```

---

## Implementation Notes

### Database Schema

```yaml
animal_records:
  animal_profile:
    animal_id: uuid
    species: enum
    breed: string
    birth_date: date
    parent_ids: array
    owner_id: uuid
    current_holder_id: uuid
    brand_mark: string
    quality_rating: integer
    health_status: object

  flock_record:
    flock_id: uuid
    owner_id: uuid
    shepherd_id: uuid
    contract_id: uuid
    animal_count: integer
    location: string

  contract_record:
    contract_id: uuid
    owner_id: uuid
    shepherd_id: uuid
    base_count: integer
    growth_quota: float
    start_date: date
    end_date: date
    status: enum
```

---

## Appendix: Sumerian Animal Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Sipa** | Shepherd | Primary profession |
| **Udu** | Sheep | Main livestock |
| **Uz** | Goat | Secondary livestock |
| **Gu** | Cattle | Prestige animals |
| **Anshe** | Donkey | Transport |
| **Sila** | Lamb | Young sheep |

---

*"A man's wealth walks on four legs. The shepherd who understands this truth, who tends with wisdom and breeds with foresight, builds fortune that outlasts kings."*
