# Merchant & Trade

> *"The Damgar risks everything—silver, reputation, life itself—on the chance that what is common here is rare there. This is not gambling. This is mathematics, courage, and the blessing of Enki combined."*

## Overview

The Damgar (merchant) is Eridu's gateway to the world. Unlike simple shopkeepers, these are international venture capitalists who organize expeditions to Dilmun, Magan, and Meluhha. They form partnerships, manage caravans, negotiate in foreign ports, and return with copper, lapis lazuli, and exotic luxuries. This spec covers trade routes, the partnership (Tappu) system, the Karum operations, pricing, and contract law.

---

## Design Philosophy

### Core Principles

1. **High Risk, High Reward**: International trade is dangerous but profitable
2. **Partnership System**: Capital and labor split between investors and traders
3. **Commodity-Based Pricing**: No coins—everything is ratios and weight
4. **Legal Framework**: Contracts, seals, and witnesses protect all parties
5. **Training Data Value**: Negotiation, risk assessment, logistics planning

### The Eridu Advantage

```yaml
eridu_trade_position:
  location: "Gateway to Persian Gulf"
  specialty: "Sacred goods monopoly"

  the_eridu_premium:
    description: "Temple ritual items command higher prices"
    products:
      - "Purified oils"
      - "Specific incenses"
      - "Holy metals"
      - "Ritual textiles"
    advantage: "Other cities must buy from Eridu"
```

---

## Trade Routes

### The Three Destinations

```yaml
trade_routes:
  dilmun:
    location: "Modern Bahrain"
    title: "Land of the Living"
    distance: "3-7 days by sea"
    role: "Central trade hub/emporium"

    imports_from:
      - "Copper (transshipped from Magan)"
      - "Pearls"
      - "Dates"
      - "Transshipped Indian goods"

    exports_to:
      - "Grain (barley, wheat)"
      - "Textiles (wool)"
      - "Sesame oil"
      - "Finished goods"

    trade_character: "Safe, regular, moderate profit"
    voyage_frequency: "Multiple per season"

  magan:
    location: "Modern Oman/UAE"
    distance: "7-14 days by sea"
    title: "Land of Copper"

    imports_from:
      - "Magan Copper (highest quality)"
      - "Diorite (black stone for statues)"
      - "Steatite (soapstone)"

    exports_to:
      - "Grain"
      - "Textiles"
      - "Silver"
      - "Manufactured goods"

    trade_character: "Longer voyage, higher profit"
    voyage_frequency: "Seasonal"

  meluhha:
    location: "Indus Valley (Modern Pakistan/India)"
    distance: "30-60 days by sea (monsoon dependent)"
    title: "The Farthest Land"

    imports_from:
      - "Carnelian beads"
      - "Ivory"
      - "Gold"
      - "Teak wood (wood of the sea)"
      - "Exotic animals"
      - "Indigo dye"

    exports_to:
      - "Silver"
      - "Wool textiles"
      - "Grain"

    trade_character: "Highest risk, highest reward"
    voyage_frequency: "Once per year (monsoon timing)"
    profit_potential: "200-500% markup"
```

### Land Routes

```yaml
land_routes:
  northern_routes:
    destinations:
      - "Assyria (metals, timber)"
      - "Anatolia (silver, copper)"
      - "Syria (cedar, wine)"
    transport: "Donkey caravans"
    speed: "15-20 miles per day"
    challenges:
      - "Tribal territory fees"
      - "Bandit risk"
      - "Water availability"

  eastern_routes:
    destinations:
      - "Elam (tin, timber)"
      - "Afghanistan (lapis lazuli)"
    transport: "Donkey caravans"
    special_goods: "Lapis = most valuable import"

  caravan_logistics:
    animals: "Donkeys (pre-camel era)"
    load: "100-150 pounds per donkey"
    caravan_size: "10-50 donkeys typical"
    personnel:
      drivers: "1 per 3-5 donkeys"
      guards: "Based on route danger"
      merchant: "1-2 leading trade"
```

---

## The Damgar (Merchant)

### Role and Status

```yaml
damgar_profession:
  title: "Damgar (Merchant)"
  social_class: "Commoner to Elite (based on success)"
  unique_status: "Temple-city representatives abroad"

  functions:
    trader: "Buy low, sell high"
    diplomat: "Represent Eridu in foreign ports"
    financier: "Manage investment partnerships"
    logistics: "Organize caravans and voyages"

  requirements:
    capital: "Significant starting investment or investor"
    literacy: "Basic numeracy essential, cuneiform helpful"
    languages: "Knowledge of trade languages"
    connections: "Temple, investor, or family backing"
```

### Merchant Skill Tree

```yaml
merchant_skills:
  tier_1_novice:
    skills:
      basic_haggling:
        description: "Negotiate simple transactions"
        sila_reward: 20

      commodity_knowledge:
        description: "Know standard exchange ratios"
        sila_reward: 25

      weight_measures:
        description: "Use standard weights accurately"
        sila_reward: 15

    earnings: "Small margins on local trade"
    role: "Market stall, small trades"

  tier_2_apprentice:
    requirements: "Successful trades + basic capital"
    skills:
      contract_drafting:
        description: "Write valid trade agreements"
        sila_reward: 40
        requires: "Basic literacy"

      quality_assessment:
        description: "Grade goods accurately"
        sila_reward: 35

      dilmun_trading:
        description: "Navigate Dilmun markets"
        sila_reward: 50
        requires: "Gulf voyage experience"

    earnings: "Moderate profits, Dilmun access"
    role: "Junior merchant, partnership participant"

  tier_3_journeyman:
    requirements: "3+ years + Magan voyage"
    skills:
      foreign_languages:
        description: "Communicate in Dilmun/Magan"
        sila_reward: 75

      partnership_management:
        description: "Organize Tappu investments"
        sila_reward: 60

      magan_trading:
        description: "Handle copper trade"
        sila_reward: 80

    earnings: "Significant profits, multiple routes"
    role: "Independent merchant"

  tier_4_master:
    requirements: "10+ years + Meluhha voyage"
    skills:
      meluhha_expertise:
        description: "Navigate Indus Valley trade"
        sila_reward: 150

      trade_network:
        description: "Permanent agents in foreign ports"
        sila_reward: 150

      temple_contracts:
        description: "Exclusive sacred goods trading"
        sila_reward: 100

    earnings: "Elite wealth"
    role: "Trade prince, dynasty founder"
```

---

## The Partnership System (Tappu)

### Structure

```yaml
tappu_partnership:
  description: "Investment structure for trade ventures"

  roles:
    investor:
      provides: "Capital (silver or goods)"
      takes: "Financial risk"
      receives: "Percentage of profits"
      examples: "Temple, priests, widows, wealthy citizens"

    traveling_partner:
      provides: "Labor, expertise, connections"
      takes: "Physical risk"
      receives: "Percentage of profits"
      examples: "Damgar, experienced traders"

  typical_split:
    standard: "50/50 after costs"
    high_risk: "60/40 favoring traveler"
    investor_advantage: "40/60 if investor provides all capital"

  legal_requirements:
    contract: "Written on clay tablet"
    witnesses: "2-3 named individuals"
    seal: "Cylinder seal impressions"
    terms: "Goods, destination, profit split, timeline"
```

### Partnership Mechanics

```yaml
partnership_process:
  formation:
    step_1: "Merchant proposes venture"
    step_2: "Investor agrees to capital amount"
    step_3: "Terms negotiated and agreed"
    step_4: "Contract written by scribe"
    step_5: "Both parties seal document"

  execution:
    step_6: "Capital provided to merchant"
    step_7: "Merchant organizes expedition"
    step_8: "Voyage/caravan proceeds"
    step_9: "Goods traded at destination"
    step_10: "Return with proceeds"

  settlement:
    step_11: "Accounting before witnesses"
    step_12: "Expenses deducted"
    step_13: "Profits divided per contract"
    step_14: "Settlement tablet created"

  dispute_resolution:
    minor: "Merchant court in Karum"
    major: "Temple court with oaths"
    fraud: "Severe legal penalties"
```

### Player Partnership Paths

```yaml
player_partnerships:
  as_investor:
    entry: "Have capital to invest"
    role: "Provide silver/goods"
    risk: "Lose investment if venture fails"
    reward: "Profit without travel"
    strategy: "Diversify across multiple ventures"

  as_merchant:
    entry: "Have trade skills"
    role: "Organize and execute trade"
    risk: "Physical danger, reputation"
    reward: "Profit share, experience, connections"
    strategy: "Build reputation for more investment"

  as_both:
    advanced: "Self-fund small ventures"
    benefit: "Keep all profits"
    risk: "Lose everything if it fails"
```

---

## The Karum (Trade District)

### Operations

```yaml
karum_operations:
  location: "Special zone outside city walls"

  facilities:
    warehouses:
      purpose: "Store goods in transit"
      security: "Sealed rooms, guards"
      fees: "Volume-based charges"

    trading_floors:
      purpose: "Conduct negotiations"
      customs: "Established trading hours"
      witnesses: "Available for contracts"

    foreign_quarters:
      residents: "Dilmun, Magan, Meluhha traders"
      law: "International merchant law"
      culture: "Foreign customs tolerated"

    administrative:
      records: "All transactions documented"
      weights: "Official standard weights"
      disputes: "Merchant court"
```

### Market Operations

```yaml
market_mechanics:
  trading_hours:
    morning: "Fresh goods, food"
    midday: "Bulk commodities"
    afternoon: "Negotiations, contracts"

  price_discovery:
    haggling: "Standard practice"
    benchmark: "Temple sets reference prices"
    quality: "Prices vary by grade"
    quantity: "Bulk discounts"

  transaction_types:
    spot: "Immediate exchange"
    forward: "Agree now, deliver later"
    consignment: "Sell on behalf of owner"
```

---

## Commodity Pricing

### The Ratio System

```yaml
pricing_system:
  base_unit: "Silver (shekel = ~8 grams)"

  standard_ratios:
    1_shekel_silver_equals:
      barley: "300 liters (1 gur)"
      gold: "2-3 grams"
      sheep: "1-2 healthy animals"
      wool: "3-5 minas"
      copper: "60-100 shekels by weight"

  quality_modifiers:
    premium: "+50% to +200%"
    standard: "Base price"
    low_grade: "-20% to -50%"

  seasonal_variation:
    harvest: "Grain cheap, everything else expensive"
    planting: "Grain expensive"
    trade_season: "Imported goods abundant"
```

### Trade Goods Valuation

```yaml
trade_goods:
  exports:
    textiles:
      standard_garment: "1-3 shekels silver"
      fine_garment: "5-15 shekels silver"
      dyed_garment: "10-30 shekels silver"

    grain:
      barley: "Base commodity"
      wheat: "2x barley value"

    oil:
      sesame_oil: "Premium export"

  imports:
    copper:
      magan_grade: "Premium pricing"
      standard: "Base metal price"
      processed: "Higher than ingot"

    lapis_lazuli:
      value: "Weight in silver (or more)"
      source: "Afghanistan via Elam"
      use: "Jewelry, temple decoration"

    ivory:
      value: "Very high"
      source: "Meluhha only"
      use: "Elite goods, inlay"

    carnelian:
      value: "High"
      source: "Indus Valley"
      use: "Beads, seals"
```

---

## Contract Law

### Trade Contracts

```yaml
contract_elements:
  required:
    parties: "Names of all involved"
    goods: "Exact quantities and qualities"
    prices: "Agreed exchange terms"
    timeline: "Delivery dates"
    witnesses: "2-3 named individuals"
    seals: "Cylinder seal impressions"

  optional:
    penalties: "For non-performance"
    guarantees: "Third-party backing"
    arbitration: "Dispute resolution terms"
```

### The Clay Envelope (Bullae)

```yaml
bullae_system:
  purpose: "Tamper-proof cargo verification"

  process:
    step_1: "Create tokens representing goods"
    step_2: "Place tokens inside clay ball"
    step_3: "Seal exterior with cylinder seal"
    step_4: "Ball travels with cargo"

  verification:
    arrival: "Break open bullae"
    compare: "Tokens vs actual goods"
    match: "Transaction complete"
    mismatch: "Damgar liable for difference"

  anti_fraud: "Cannot alter without breaking seal"
```

### Interest Rates

```yaml
lending_terms:
  standard_rates:
    silver: "20% annual"
    grain: "33.3% annual"

  rationale:
    grain_higher: "More perishable, storage risk"
    silver_lower: "Stable, easier to store"

  enforcement:
    contract: "Written terms"
    collateral: "Often required"
    default: "Legal action, debt slavery possible"
```

### Standardized Weights

```yaml
weight_standards:
  importance: "Trust in transactions"

  official_weights:
    shape: "Often polished stone ducks"
    verification: "Temple of Enki certifies"
    tampering: "Severe legal penalty"

  weight_units:
    shekel: "~8 grams"
    mina: "60 shekels (~500 grams)"
    talent: "60 minas (~30 kg)"

  player_use:
    purchase: "Need accurate weights for trade"
    verification: "Check against temple standards"
    status: "Quality weights = professional credibility"
```

---

## Trade Risks

### Voyage Risks

```yaml
maritime_risks:
  storms:
    frequency: "Seasonal"
    consequence: "Shipwreck, cargo loss"
    mitigation: "Proper timing, experienced crew"

  pirates:
    areas: "Gulf passages"
    consequence: "Cargo theft, crew harm"
    mitigation: "Convoy sailing, armed crew"

  foreign_politics:
    issue: "Port closures, tariffs, seizure"
    consequence: "Stranded, goods confiscated"
    mitigation: "Diplomatic relationships, local agents"
```

### Caravan Risks

```yaml
land_risks:
  bandits:
    frequency: "Route-dependent"
    consequence: "Goods stolen, injury"
    mitigation: "Armed guards, safe passage payments"

  tribal_fees:
    requirement: "Pay for passage through territory"
    consequence: "Refused passage if unpaid"
    mitigation: "Budget for fees, know rates"

  water_scarcity:
    issue: "Desert crossings"
    consequence: "Animal death, mission failure"
    mitigation: "Proper planning, local guides"

  animal_loss:
    causes: "Disease, exhaustion, theft"
    consequence: "Reduced cargo capacity"
    mitigation: "Spare animals, veterinary knowledge"
```

### Commercial Risks

```yaml
commercial_risks:
  market_shift:
    issue: "Prices change during voyage"
    consequence: "Lower profit or loss"
    mitigation: "Market intelligence, diversification"

  quality_disputes:
    issue: "Buyer claims goods substandard"
    consequence: "Price reduction, reputation damage"
    mitigation: "Quality documentation, witnesses"

  partner_fraud:
    issue: "Investor or merchant cheats"
    consequence: "Financial loss"
    mitigation: "Contracts, reputation research"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  negotiation:
    - "Haggling strategies"
    - "Reading counterparty"
    - "Finding mutual benefit"

  risk_assessment:
    - "Route selection reasoning"
    - "Partner evaluation"
    - "Cargo decisions"

  logistics:
    - "Voyage planning"
    - "Caravan organization"
    - "Timing optimization"

  legal_reasoning:
    - "Contract interpretation"
    - "Dispute resolution"
    - "Documentation practices"
```

---

## Implementation Notes

### Database Schema

```yaml
trade_records:
  merchant_profile:
    player_id: uuid
    skill_level: integer
    trade_history: array
    partnerships: array
    reputation: object  # by region
    capital: integer
    agents: array  # foreign port contacts

  partnership_record:
    partnership_id: uuid
    investor_id: uuid
    merchant_id: uuid
    capital: integer
    goods: array
    destination: string
    profit_split: object
    status: enum
    settlement: object

  voyage_record:
    voyage_id: uuid
    merchant_id: uuid
    route: string
    cargo_out: array
    cargo_return: array
    profit: integer
    incidents: array
```

---

## Appendix: Sumerian Trade Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Damgar** | Merchant | Trade profession |
| **Tappu** | Partnership | Investment structure |
| **Karum** | Harbor/trade district | Trade zone |
| **Shekel** | Weight unit (~8g) | Currency base |
| **Mina** | 60 shekels | Larger weight |
| **Bullae** | Clay envelope | Anti-fraud device |

---

*"The Damgar who returns empty-handed is a fool. The Damgar who returns with twice what he left with is competent. The Damgar who returns with goods the city has never seen—that one builds legacy."*
