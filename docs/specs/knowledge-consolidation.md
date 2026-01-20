# The Analog Economy: Knowledge Consolidation System

> **Version:** 1.0
> **Last Updated:** 2026-01-19
> **Status:** Vision Draft

---

## Executive Summary

The Analog Economy doesn't just generate behavioral training data—it **consolidates humanity's fragmented knowledge** into structured, verified datasets. Players become researchers, documenting traditional knowledge that exists only in scattered sources: oral traditions, obscure academic papers, tribal records, and dying practices.

**The Insight:** AI systems struggle with domains where data is fragmented across languages, cultures, institutions, and formats. By gamifying research and verification, we create datasets that don't exist anywhere else.

**The Model:** Players earn NVT by contributing verified knowledge. The more complete, accurate, and novel the contribution, the higher the reward.

---

## Table of Contents

1. [The Fragmentation Problem](#the-fragmentation-problem)
2. [Notoriously Fragmented Datasets](#notoriously-fragmented-datasets)
3. [The Research-to-Reward Pipeline](#the-research-to-reward-pipeline)
4. [Era-Specific Knowledge Domains](#era-specific-knowledge-domains)
5. [Verification & Quality Control](#verification--quality-control)
6. [Data Schema & Requirements](#data-schema--requirements)
7. [Example: Ethnobotanical Knowledge](#example-ethnobotanical-knowledge)
8. [Enterprise Value](#enterprise-value)
9. [Ethical Considerations](#ethical-considerations)

---

## The Fragmentation Problem

### Why AI Struggles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE FRAGMENTATION PROBLEM                                 │
│            "The knowledge exists. Just not in one place."                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EXAMPLE: Medicinal Plants of the Sonoran Desert                            │
│                                                                             │
│  Where the knowledge lives TODAY:                                           │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Hopi Elders   │  │  Academic Papers │  │  Mexican Curan- │             │
│  │   (Oral Only)   │  │  (Scattered,     │  │  deros (Spanish │             │
│  │                 │  │   Paywalled)     │  │   Oral Tradition)│             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           ▼                    ▼                    ▼                       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  Museum         │  │  Herbarium      │  │  FDA/USDA       │             │
│  │  Collections    │  │  Specimens      │  │  Databases      │             │
│  │  (Physical)     │  │  (Partial)      │  │  (Modern Only)  │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           └────────────────────┼────────────────────┘                       │
│                                │                                            │
│                                ▼                                            │
│                    ┌───────────────────────┐                               │
│                    │     NO UNIFIED        │                               │
│                    │     DATABASE          │                               │
│                    │                       │                               │
│                    │  • No standard schema │                               │
│                    │  • Multiple languages │                               │
│                    │  • Conflicting names  │                               │
│                    │  • Unverified claims  │                               │
│                    │  • Dying knowledge    │                               │
│                    └───────────────────────┘                               │
│                                                                             │
│  WHAT WE BUILD: A unified, verified, structured dataset                     │
│                 through gamified crowdsourced research                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Opportunity

| Problem | Our Solution |
|---------|--------------|
| Knowledge scattered across languages | Multi-lingual player base researches in native sources |
| Oral traditions dying with elders | Players interview, record, and structure knowledge |
| Academic papers paywalled | Players synthesize publicly available information |
| No standard schema | We define structured data requirements |
| Unverified claims | Community verification + expert review |
| Knowledge not machine-readable | Players translate to structured formats |

---

## Notoriously Fragmented Datasets

### Tier 1: High Value, Extremely Fragmented

```yaml
tier_1_datasets:
  ethnobotanical_knowledge:
    description: "Traditional plant uses across cultures"
    fragmentation_sources:
      - "Oral traditions (hundreds of tribes/cultures)"
      - "Academic ethnobotany papers (scattered journals)"
      - "Colonial-era records (biased, incomplete)"
      - "Modern pharmaceutical research (proprietary)"
      - "Folk medicine traditions (unwritten)"
    current_state: "No unified global database"
    enterprise_value: "Pharmaceutical, supplement, cosmetic industries"
    game_integration: "Herbalism, medicine crafting, agriculture"

  traditional_agriculture:
    description: "Pre-industrial farming techniques"
    fragmentation_sources:
      - "Archaeological records"
      - "Regional farming traditions"
      - "Seed bank documentation"
      - "Historical crop yield records"
      - "Indigenous land management"
    current_state: "Climate adaptation research desperately needs this"
    enterprise_value: "AgTech, climate adaptation, food security"
    game_integration: "Farming mechanics, crop selection, irrigation"

  historical_climate_patterns:
    description: "Pre-industrial weather and climate data"
    fragmentation_sources:
      - "Ship logs (scattered archives)"
      - "Monastery records (Latin, various languages)"
      - "Tree ring data (academic)"
      - "Ice core correlations (specialized)"
      - "Oral histories of droughts/floods"
    current_state: "Climate models need historical baselines"
    enterprise_value: "Climate science, insurance, agriculture"
    game_integration: "Weather prediction, seasonal planning, catastrophes"

  traditional_craft_techniques:
    description: "Pre-industrial manufacturing methods"
    fragmentation_sources:
      - "Guild records (often destroyed/scattered)"
      - "Archaeological artifacts"
      - "Living craftspeople (aging)"
      - "Museum documentation"
      - "Apprenticeship traditions"
    current_state: "Many techniques being lost"
    enterprise_value: "Manufacturing, materials science, artisan markets"
    game_integration: "Crafting systems, workshop mechanics"

  historical_disease_patterns:
    description: "Pre-modern epidemiology"
    fragmentation_sources:
      - "Parish death records"
      - "Medical treatises (various languages)"
      - "Archaeological pathology"
      - "Oral histories of plagues"
      - "Quarantine records"
    current_state: "Pandemic modeling needs historical data"
    enterprise_value: "Public health, epidemiology, pharmaceutical"
    game_integration: "Disease mechanics, quarantine decisions, medicine"
```

### Tier 2: High Value, Moderately Fragmented

```yaml
tier_2_datasets:
  traditional_navigation:
    description: "Pre-GPS wayfinding techniques"
    examples:
      - "Polynesian star navigation"
      - "Desert caravan routes"
      - "Arctic Inuit ice reading"
      - "Mediterranean sailing knowledge"
    enterprise_value: "Autonomous systems, backup navigation, education"
    game_integration: "Exploration, trade routes, discovery"

  historical_metallurgy:
    description: "Pre-industrial metal processing"
    examples:
      - "Damascus steel techniques"
      - "Bronze Age alloy recipes"
      - "Japanese sword-making"
      - "African iron smelting"
    enterprise_value: "Materials science, metallurgy research"
    game_integration: "Smithing, tool crafting, weapons"

  traditional_food_preservation:
    description: "Pre-refrigeration food storage"
    examples:
      - "Fermentation traditions (global)"
      - "Smoking/curing techniques"
      - "Root cellaring methods"
      - "Salt preservation ratios"
    enterprise_value: "Food science, emergency preparedness"
    game_integration: "Food storage, survival, trade goods"

  historical_water_management:
    description: "Pre-modern hydraulic engineering"
    examples:
      - "Qanat systems (Persian)"
      - "Roman aqueduct engineering"
      - "Inca irrigation terraces"
      - "Dutch water management"
    enterprise_value: "Civil engineering, water scarcity solutions"
    game_integration: "Irrigation, city building, flood management"

  traditional_medicine_practices:
    description: "Non-plant medical techniques"
    examples:
      - "Bone setting traditions"
      - "Acupuncture point mapping"
      - "Ayurvedic treatments"
      - "Surgical techniques (trepanning, cauterization)"
    enterprise_value: "Medical research, alternative medicine validation"
    game_integration: "Healing, injury treatment, hospital mechanics"
```

### Tier 3: Moderate Value, Highly Fragmented

```yaml
tier_3_datasets:
  traditional_textiles:
    description: "Pre-industrial fabric production"
    examples:
      - "Natural dye recipes (region-specific)"
      - "Weaving patterns and techniques"
      - "Fiber processing methods"
      - "Embroidery traditions"
    enterprise_value: "Sustainable fashion, cultural preservation"
    game_integration: "Clothing crafting, trade goods, cultural items"

  historical_architecture:
    description: "Pre-modern building techniques"
    examples:
      - "Adobe construction (regional variants)"
      - "Timber framing traditions"
      - "Stone masonry techniques"
      - "Thatch roofing methods"
    enterprise_value: "Sustainable building, historic preservation"
    game_integration: "Structure building, community development"

  oral_histories_folklore:
    description: "Stories encoding practical knowledge"
    examples:
      - "Flood myths (often encode real events)"
      - "Monster legends (often describe real dangers)"
      - "Origin stories (migration patterns)"
      - "Trickster tales (social norms)"
    enterprise_value: "Cultural AI, storytelling, anthropology"
    game_integration: "Quest content, cultural context, religion system"

  traditional_animal_husbandry:
    description: "Pre-modern livestock management"
    examples:
      - "Heritage breed characteristics"
      - "Traditional veterinary medicine"
      - "Breeding selection criteria"
      - "Grazing rotation patterns"
    enterprise_value: "Sustainable agriculture, livestock genetics"
    game_integration: "Animal raising, dairy/meat production"

  historical_linguistics:
    description: "Dead and dying languages"
    examples:
      - "Sumerian vocabulary"
      - "Regional dialects (disappearing)"
      - "Technical terminology (guilds, trades)"
      - "Place name etymologies"
    enterprise_value: "NLP training, cultural preservation, translation"
    game_integration: "Communication, trade, cultural interactions"
```

---

## The Research-to-Reward Pipeline

### How Players Contribute Knowledge

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESEARCH-TO-REWARD PIPELINE                               │
│              "Play the game. Contribute real knowledge. Get paid."           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. ENCOUNTER                                                               │
│     Player encounters unknown plant/technique/knowledge in game             │
│     Example: "You find an unfamiliar desert plant. The Hopi elder           │
│              mentions it has medicinal properties, but details are lost."   │
│                                                                             │
│  2. RESEARCH QUEST                                                          │
│     Game assigns structured research requirements                           │
│     Example: "To unlock this plant's full benefits, document:               │
│              □ Full taxonomy (scientific name, family)                      │
│              □ Traditional names (Hopi, Spanish, English)                   │
│              □ Chemical composition (if known)                              │
│              □ Traditional uses (with sources)                              │
│              □ Preparation methods                                          │
│              □ Contraindications/dangers"                                   │
│                                                                             │
│  3. EXTERNAL RESEARCH                                                       │
│     Player researches outside the game                                      │
│     Sources: Academic papers, interviews, books, databases                  │
│     Tools: We provide research guides, citation templates                   │
│                                                                             │
│  4. SUBMISSION                                                              │
│     Player submits structured data through in-game interface                │
│     Required: Sources, citations, confidence level                          │
│                                                                             │
│  5. VERIFICATION                                                            │
│     ├── Automated: Cross-reference known databases                          │
│     ├── Community: Other players verify/challenge                           │
│     └── Expert: Specialists review high-value submissions                   │
│                                                                             │
│  6. REWARD                                                                  │
│     ├── Base NVT: For completing submission                                 │
│     ├── Novelty bonus: New information not in existing databases            │
│     ├── Quality bonus: Well-sourced, detailed contribution                  │
│     ├── Verification bonus: Confirming others' submissions                  │
│     └── In-game unlock: Full benefits of the plant/technique                │
│                                                                             │
│  7. DATASET                                                                 │
│     Verified knowledge enters the consolidated database                     │
│     Available for: AI training, enterprise licensing, open research         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Reward Structure

```yaml
knowledge_rewards:
  submission_tiers:
    basic:
      requirements: ["name", "basic_description", "one_source"]
      nvt_reward: 5
      novelty_multiplier: 1.0

    standard:
      requirements: ["full_taxonomy", "multiple_names", "three_sources", "uses"]
      nvt_reward: 25
      novelty_multiplier: 1.5

    comprehensive:
      requirements: ["all_fields", "five_sources", "chemical_data", "preparation"]
      nvt_reward: 100
      novelty_multiplier: 2.0

    expert:
      requirements: ["comprehensive", "original_research", "interview_data", "expert_review"]
      nvt_reward: 500
      novelty_multiplier: 3.0

  novelty_detection:
    existing_in_database: 0.1x         # Already documented
    partial_overlap: 0.5x              # Adds to existing entry
    new_entry: 1.0x                    # First documentation
    rare_source: 2.0x                  # From oral tradition or rare text
    first_ever_digital: 5.0x           # Never before digitized

  verification_rewards:
    confirm_accurate: 2                # Confirming good submission
    flag_inaccurate: 5                 # Catching errors
    provide_correction: 10             # Fixing with sources
    expert_review: 50                  # Qualified expert verification
```

---

## Era-Specific Knowledge Domains

### What Players Research in Each Era

```yaml
era_knowledge_domains:
  ancient:
    primary_domains:
      - domain: "Early Agriculture"
        examples: ["Irrigation techniques", "Crop domestication", "Soil management"]
        data_needed: ["Crop varieties", "Yield estimates", "Tool designs"]

      - domain: "Bronze Age Metallurgy"
        examples: ["Copper sources", "Tin trade routes", "Alloy ratios"]
        data_needed: ["Ore processing", "Temperature requirements", "Tool types"]

      - domain: "Early Medicine"
        examples: ["Sumerian remedies", "Egyptian treatments", "Trepanning"]
        data_needed: ["Plant ingredients", "Preparation methods", "Efficacy records"]

      - domain: "River Management"
        examples: ["Flood prediction", "Canal systems", "Water rights"]
        data_needed: ["Seasonal patterns", "Engineering techniques", "Social organization"]

    research_unlock: "Deeper knowledge = better gameplay outcomes"

  classical:
    primary_domains:
      - domain: "Imperial Administration"
        examples: ["Roman road standards", "Persian postal system", "Han bureaucracy"]
        data_needed: ["Construction specs", "Organizational charts", "Cost records"]

      - domain: "Classical Medicine"
        examples: ["Hippocratic treatments", "Chinese medicine", "Ayurveda origins"]
        data_needed: ["Diagnostic methods", "Treatment protocols", "Drug preparations"]

      - domain: "Military Engineering"
        examples: ["Siege warfare", "Fortification design", "Supply logistics"]
        data_needed: ["Equipment specs", "Tactical manuals", "Campaign records"]

      - domain: "Philosophy & Science"
        examples: ["Aristotelian biology", "Astronomical observations", "Mathematical texts"]
        data_needed: ["Original sources", "Experimental methods", "Knowledge transmission"]

  medieval:
    primary_domains:
      - domain: "Guild Craft Secrets"
        examples: ["Steel tempering", "Glass making", "Textile dyeing"]
        data_needed: ["Process steps", "Material sources", "Quality standards"]

      - domain: "Monastic Agriculture"
        examples: ["Crop rotation systems", "Vineyard management", "Beekeeping"]
        data_needed: ["Seasonal calendars", "Yield records", "Preservation methods"]

      - domain: "Plague Medicine"
        examples: ["Quarantine practices", "Herbal treatments", "Miasma theory applications"]
        data_needed: ["What worked (accidentally)", "Mortality patterns", "Social responses"]

      - domain: "Manuscript Preservation"
        examples: ["Ink recipes", "Parchment making", "Binding techniques"]
        data_needed: ["Material formulas", "Process documentation", "Preservation methods"]

  renaissance:
    primary_domains:
      - domain: "Navigation & Cartography"
        examples: ["Star charts", "Current maps", "Longitude methods"]
        data_needed: ["Instrument designs", "Calculation methods", "Route documentation"]

      - domain: "New World Botany"
        examples: ["Tobacco", "Chocolate", "Potato", "Tomato introduction"]
        data_needed: ["Indigenous uses", "European adaptation", "Cultivation changes"]

      - domain: "Early Chemistry"
        examples: ["Alchemy to chemistry", "Gunpowder formulas", "Dye chemistry"]
        data_needed: ["Experimental records", "Process documentation", "Safety data"]

      - domain: "Printing & Knowledge"
        examples: ["Movable type", "Ink formulas", "Paper making"]
        data_needed: ["Technical specifications", "Cost structures", "Distribution networks"]

  industrial:
    primary_domains:
      - domain: "Factory Processes"
        examples: ["Steam engine efficiency", "Textile machinery", "Steel production"]
        data_needed: ["Engineering specs", "Efficiency data", "Worker conditions"]

      - domain: "Urban Health"
        examples: ["Cholera mapping", "Sanitation engineering", "Hospital design"]
        data_needed: ["Disease patterns", "Infrastructure solutions", "Mortality data"]

      - domain: "Labor Organization"
        examples: ["Union formation", "Strike records", "Wage data"]
        data_needed: ["Organizational methods", "Negotiation records", "Outcomes"]

      - domain: "Agricultural Revolution"
        examples: ["Crop rotation advances", "Machinery introduction", "Land enclosure"]
        data_needed: ["Yield improvements", "Social disruption", "Migration patterns"]

  modern:
    primary_domains:
      - domain: "World War Logistics"
        examples: ["Supply chain management", "Production scaling", "Resource allocation"]
        data_needed: ["Organization methods", "Efficiency data", "Innovation records"]

      - domain: "Nuclear Era Documentation"
        examples: ["Civil defense", "Fallout patterns", "Shelter design"]
        data_needed: ["Survival strategies", "Psychological responses", "Community organization"]

      - domain: "Digital Transition"
        examples: ["Early computing", "Network development", "Information management"]
        data_needed: ["Technical evolution", "Adoption patterns", "Disruption effects"]

      - domain: "Climate Observation"
        examples: ["Weather records", "Ecosystem changes", "Disaster patterns"]
        data_needed: ["Measurement data", "Impact documentation", "Adaptation strategies"]
```

---

## Verification & Quality Control

### Multi-Layer Verification System

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VERIFICATION LAYERS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER 1: AUTOMATED CHECKS                                                  │
│  ├── Cross-reference against known databases                                │
│  │   • Wikipedia, Wikidata                                                  │
│  │   • USDA PLANTS Database                                                 │
│  │   • PubMed / academic databases                                          │
│  │   • Historical archives (digitized)                                      │
│  │                                                                          │
│  ├── Format validation                                                      │
│  │   • Required fields present                                              │
│  │   • Scientific names valid (ITIS, GBIF)                                  │
│  │   • Geographic coordinates plausible                                     │
│  │   • Dates consistent                                                     │
│  │                                                                          │
│  └── Plagiarism / duplication detection                                     │
│      • Not copied from existing sources verbatim                            │
│      • Not duplicate of existing database entry                             │
│                                                                             │
│  LAYER 2: COMMUNITY VERIFICATION                                            │
│  ├── Peer review by other players                                           │
│  │   • 3+ confirmations required for standard entries                       │
│  │   • Reputation-weighted voting                                           │
│  │   • Challenge/dispute mechanism                                          │
│  │                                                                          │
│  ├── Regional expertise matching                                            │
│  │   • Route to players with relevant cultural/geographic background        │
│  │   • Language-appropriate verification                                    │
│  │                                                                          │
│  └── Bounty for corrections                                                 │
│      • Rewards for finding errors                                           │
│      • Appeals process for disputed entries                                 │
│                                                                             │
│  LAYER 3: EXPERT REVIEW                                                     │
│  ├── Specialist verification for high-value submissions                     │
│  │   • Ethnobotanists for plant knowledge                                   │
│  │   • Historians for historical claims                                     │
│  │   • Scientists for technical data                                        │
│  │                                                                          │
│  ├── Partner institution review                                             │
│  │   • University partnerships                                              │
│  │   • Museum collaborations                                                │
│  │   • Indigenous community validation                                      │
│  │                                                                          │
│  └── Periodic audits                                                        │
│      • Random sampling of database                                          │
│      • Quality score tracking                                               │
│      • Contributor reputation adjustment                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Contributor Reputation System

```yaml
contributor_reputation:
  factors:
    accuracy_rate:
      description: "% of submissions verified as accurate"
      weight: 0.40

    novelty_rate:
      description: "% of submissions containing new information"
      weight: 0.25

    citation_quality:
      description: "Quality and verifiability of sources"
      weight: 0.20

    peer_ratings:
      description: "How other contributors rate your work"
      weight: 0.15

  levels:
    novice:
      threshold: 0
      max_submissions_per_week: 5
      verification_required: "full_community"
      nvt_multiplier: 1.0

    contributor:
      threshold: 50
      max_submissions_per_week: 15
      verification_required: "partial_community"
      nvt_multiplier: 1.25

    researcher:
      threshold: 200
      max_submissions_per_week: 30
      verification_required: "spot_check"
      nvt_multiplier: 1.5

    expert:
      threshold: 500
      max_submissions_per_week: 50
      verification_required: "minimal"
      nvt_multiplier: 2.0
      special: "Can verify others' submissions"

    scholar:
      threshold: 1000
      max_submissions_per_week: "unlimited"
      verification_required: "audit_only"
      nvt_multiplier: 3.0
      special: "Expert review authority"
```

---

## Data Schema & Requirements

### Universal Entry Structure

```yaml
knowledge_entry_schema:
  # Core identification
  id: "string (UUID)"
  type: "enum [plant, technique, practice, material, tool, recipe, tradition]"
  domain: "string (ethnobotany, metallurgy, agriculture, etc.)"
  era_relevance: "array [ancient, classical, medieval, renaissance, industrial, modern]"

  # Naming
  names:
    scientific: "string (if applicable)"
    common_english: "string"
    traditional_names:
      - language: "string"
        name: "string"
        source: "citation"
        romanization: "string (if non-Latin script)"

  # Taxonomy (for biological entries)
  taxonomy:
    kingdom: "string"
    phylum: "string"
    class: "string"
    order: "string"
    family: "string"
    genus: "string"
    species: "string"
    subspecies: "string (optional)"

  # Geographic context
  geography:
    native_range: "array of regions"
    historical_distribution: "array of regions by era"
    current_distribution: "array of regions"
    climate_requirements: "object"

  # Traditional knowledge
  traditional_uses:
    - use_type: "enum [medicinal, food, material, ritual, other]"
      culture: "string"
      description: "string"
      preparation: "string (detailed steps)"
      dosage: "string (if applicable)"
      efficacy: "enum [verified, plausible, unverified, disproven]"
      sources: "array of citations"
      confidence: "float 0-1"

  # Scientific data (if available)
  scientific_data:
    chemical_composition:
      - compound: "string"
        concentration: "string"
        source: "citation"

    pharmacological_activity:
      - activity: "string"
        mechanism: "string (if known)"
        evidence_level: "enum [in_vitro, animal, human_observational, clinical_trial]"
        source: "citation"

    toxicity:
      ld50: "string (if known)"
      contraindications: "array"
      interactions: "array"
      sources: "array of citations"

  # Provenance
  provenance:
    contributor_id: "string"
    submission_date: "datetime"
    verification_status: "enum [pending, community_verified, expert_verified, disputed]"
    verification_history: "array of verification events"
    last_updated: "datetime"

  # Citations
  citations:
    - id: "string"
      type: "enum [academic, book, interview, archive, database, oral]"
      authors: "array"
      title: "string"
      publication: "string"
      year: "integer"
      doi: "string (if available)"
      url: "string (if available)"
      accessed_date: "date"
      quote: "string (relevant excerpt)"
      page: "string"

  # Metadata
  metadata:
    completeness_score: "float 0-1"
    novelty_score: "float 0-1"
    quality_score: "float 0-1"
    usage_in_game: "array of game mechanics"
```

---

## Example: Ethnobotanical Knowledge

### Complete Entry Example

```yaml
# Example: Creosote Bush (Larrea tridentata)
# A real fragmented knowledge case

entry:
  id: "ETHNO-PLANT-00142"
  type: "plant"
  domain: "ethnobotany"
  era_relevance: ["ancient", "classical", "medieval", "renaissance", "industrial", "modern"]

  names:
    scientific: "Larrea tridentata"
    common_english: "Creosote bush"
    traditional_names:
      - language: "O'odham (Pima)"
        name: "segai"
        source: "Castetter & Underhill 1935"
        romanization: "segai"

      - language: "Spanish (Sonoran)"
        name: "gobernadora"
        source: "Martinez 1979"
        romanization: "gobernadora"

      - language: "Hopi"
        name: "aata'a"
        source: "Whiting 1939"
        romanization: "aata'a"

      - language: "Navajo"
        name: "azee' naadą́ą́'"
        source: "Wyman & Harris 1941"
        romanization: "azee' naadaa'"

  taxonomy:
    kingdom: "Plantae"
    phylum: "Tracheophyta"
    class: "Magnoliopsida"
    order: "Zygophyllales"
    family: "Zygophyllaceae"
    genus: "Larrea"
    species: "tridentata"

  geography:
    native_range: ["Sonoran Desert", "Mojave Desert", "Chihuahuan Desert"]
    historical_distribution:
      ancient: ["Southwest North America"]
      modern: ["California", "Arizona", "Nevada", "Utah", "New Mexico", "Texas", "Northern Mexico"]
    climate_requirements:
      temperature_range: "-8°C to 50°C"
      precipitation: "75-350mm annual"
      soil: "Well-drained, alkaline"

  traditional_uses:
    - use_type: "medicinal"
      culture: "O'odham (Pima)"
      description: "Treatment for respiratory ailments, colds, and chest congestion"
      preparation: "Leaves boiled in water to make tea; steam inhaled"
      dosage: "1-2 cups daily for acute illness"
      efficacy: "plausible"
      sources:
        - "Castetter & Underhill 1935, p. 47"
        - "Curtin 1949, p. 89"
      confidence: 0.75

    - use_type: "medicinal"
      culture: "O'odham (Pima)"
      description: "Wound treatment and skin infections"
      preparation: "Leaves crushed and applied as poultice; or resin applied directly"
      dosage: "Applied 2-3 times daily"
      efficacy: "verified"
      sources:
        - "Castetter & Underhill 1935, p. 48"
        - "Kay 1996, p. 234"
      confidence: 0.85

    - use_type: "medicinal"
      culture: "Mexican folk medicine"
      description: "Treatment for arthritis and rheumatism"
      preparation: "Leaves heated and applied as compress to affected joints"
      dosage: "As needed for pain"
      efficacy: "plausible"
      sources:
        - "Martinez 1979, p. 156"
        - "Ford 1975, p. 89"
      confidence: 0.65

    - use_type: "material"
      culture: "Multiple Southwest tribes"
      description: "Lac (resin) used as adhesive and waterproofing"
      preparation: "Resin collected from stems, heated to liquefy"
      dosage: "N/A"
      efficacy: "verified"
      sources:
        - "Hrdlicka 1908, p. 234"
      confidence: 0.90

    - use_type: "ritual"
      culture: "O'odham"
      description: "Purification ceremonies; smoke used to cleanse"
      preparation: "Dried branches burned"
      dosage: "N/A"
      efficacy: "N/A (spiritual use)"
      sources:
        - "Underhill 1946, p. 78"
      confidence: 0.80

  scientific_data:
    chemical_composition:
      - compound: "Nordihydroguaiaretic acid (NDGA)"
        concentration: "5-10% dry weight of leaves"
        source: "Arteaga et al. 2005"

      - compound: "Flavonoids (various)"
        concentration: "Present"
        source: "Sakakibara et al. 1976"

      - compound: "Lignans"
        concentration: "Present"
        source: "Konno et al. 1989"

    pharmacological_activity:
      - activity: "Antioxidant"
        mechanism: "NDGA scavenges free radicals"
        evidence_level: "in_vitro"
        source: "Grice et al. 1968"

      - activity: "Antimicrobial"
        mechanism: "Disrupts bacterial cell membranes"
        evidence_level: "in_vitro"
        source: "Verástegui et al. 1996"

      - activity: "Anti-inflammatory"
        mechanism: "Inhibits lipoxygenase"
        evidence_level: "animal"
        source: "Gnabre et al. 1995"

    toxicity:
      ld50: "Not established in humans"
      contraindications:
        - "Liver disease (NDGA hepatotoxicity reported)"
        - "Pregnancy"
        - "Kidney disease"
      interactions:
        - "May interact with anticoagulants"
        - "May affect liver enzyme metabolism"
      sources:
        - "Sheikh et al. 1997"
        - "FDA 1970 (GRAS status revoked for NDGA)"

  provenance:
    contributor_id: "player_0x7a3f9b..."
    submission_date: "2026-01-15T14:30:00Z"
    verification_status: "expert_verified"
    verification_history:
      - date: "2026-01-16"
        type: "community"
        result: "passed"
        verifiers: 5

      - date: "2026-01-18"
        type: "expert"
        reviewer: "Dr. Sarah Chen, Ethnobotanist"
        result: "verified with minor corrections"
        notes: "Added O'odham pronunciation guidance"

  metadata:
    completeness_score: 0.85
    novelty_score: 0.60          # Good compilation, some new traditional names
    quality_score: 0.90
    usage_in_game:
      - "Herbalism crafting"
      - "Medicine preparation"
      - "Trade goods"
      - "Ritual items"
```

### In-Game Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CREOSOTE BUSH IN GAMEPLAY                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DISCOVERY:                                                                 │
│  Player finds creosote bush in desert biome (Ancient Sonoran setting)       │
│                                                                             │
│  INITIAL STATE:                                                             │
│  "You find a pungent desert shrub. The elder mentions it has many uses,     │
│  but the knowledge was fragmented when the old healer passed."              │
│                                                                             │
│  UNLOCKABLE BENEFITS (based on research completion):                        │
│                                                                             │
│  □ Basic identification ─────────────── Can harvest leaves                  │
│  □ Traditional names (3+) ───────────── Trade value +25%                    │
│  □ Respiratory medicine recipe ──────── Craft "Breathing Tea"               │
│  □ Wound treatment method ───────────── Craft "Healing Poultice"            │
│  □ Resin collection technique ───────── Craft "Desert Glue"                 │
│  □ Full chemical data ───────────────── Unlock "Potent Extract" recipe      │
│  □ Toxicity warnings ────────────────── Avoid crafting failures             │
│                                                                             │
│  RESEARCH QUEST REWARDS:                                                    │
│  • 25 NVT for standard completion                                           │
│  • +50 NVT novelty bonus (first to document O'odham preparation)            │
│  • +25 NVT quality bonus (5+ sources with confidence >0.7)                  │
│  • Unlock: "Desert Herbalist" achievement                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Enterprise Value

### Who Buys This Data?

```yaml
enterprise_buyers:
  pharmaceutical_industry:
    interest:
      - "Lead compounds from traditional medicines"
      - "Ethnobotanical validation for drug development"
      - "Traditional preparation methods (bioavailability insights)"
    data_products:
      - "Ethnopharmacology database"
      - "Traditional use reports by compound class"
      - "Preparation method analysis"
    pricing: "$10,000-100,000 per focused dataset"

  agricultural_technology:
    interest:
      - "Climate-resilient crop varieties"
      - "Traditional irrigation techniques"
      - "Soil management practices"
      - "Pest control without chemicals"
    data_products:
      - "Historical agriculture database"
      - "Drought-resistant crop records"
      - "Traditional farming technique guides"
    pricing: "$5,000-50,000 per regional dataset"

  climate_research:
    interest:
      - "Pre-industrial climate baselines"
      - "Historical weather patterns"
      - "Traditional climate prediction methods"
      - "Adaptation strategies"
    data_products:
      - "Historical climate reconstruction data"
      - "Traditional weather prediction knowledge"
      - "Catastrophe response patterns"
    pricing: "$20,000-200,000 for comprehensive datasets"

  cultural_preservation:
    interest:
      - "Endangered language documentation"
      - "Traditional practice preservation"
      - "Indigenous knowledge systems"
    data_products:
      - "Linguistic databases"
      - "Cultural practice documentation"
      - "Oral history archives"
    pricing: "Often grant-funded; $10,000-100,000"

  materials_science:
    interest:
      - "Traditional metallurgy techniques"
      - "Natural material properties"
      - "Historical manufacturing methods"
    data_products:
      - "Traditional technique databases"
      - "Material property compilations"
      - "Process reconstruction guides"
    pricing: "$5,000-50,000 per domain"

  ai_training:
    interest:
      - "Structured knowledge graphs"
      - "Multi-lingual terminology"
      - "Domain-specific training data"
    data_products:
      - "Knowledge graph exports"
      - "Terminology databases"
      - "Question-answer pairs"
    pricing: "Per-token or subscription model"
```

### Revenue Model

```yaml
knowledge_data_revenue:
  licensing_tiers:
    research_access:
      description: "Academic and non-profit research"
      pricing: "Free or nominal"
      restrictions: "Non-commercial use, attribution required"

    commercial_exploration:
      description: "Initial R&D access"
      pricing: "$5,000/year per domain"
      restrictions: "Internal use only"

    commercial_license:
      description: "Full commercial use rights"
      pricing: "$25,000-250,000 per dataset"
      restrictions: "Defined use case, annual renewal"

    enterprise_integration:
      description: "API access, bulk data, custom exports"
      pricing: "Negotiated, typically $100,000+/year"
      restrictions: "None within license scope"

  revenue_sharing:
    contributors: 0.20             # 20% to original researchers
    verification_pool: 0.05       # 5% to verifiers
    community_treasury: 0.10      # 10% to governance
    platform: 0.65                # 65% to operations
```

---

## Ethical Considerations

### Indigenous Knowledge Protection

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INDIGENOUS KNOWLEDGE ETHICS                               │
│              "We consolidate knowledge. We don't exploit it."                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRINCIPLES:                                                                │
│                                                                             │
│  1. ATTRIBUTION                                                             │
│     • All traditional knowledge attributed to source culture                │
│     • Individual knowledge holders credited where appropriate               │
│     • No anonymization of cultural origin                                   │
│                                                                             │
│  2. BENEFIT SHARING                                                         │
│     • Revenue from indigenous knowledge shared with source communities      │
│     • Partnership agreements with tribal authorities                        │
│     • Community veto on sensitive knowledge publication                     │
│                                                                             │
│  3. CONSENT                                                                 │
│     • Prior informed consent for sensitive cultural knowledge               │
│     • Community review before publication                                   │
│     • Right to restrict commercial use                                      │
│                                                                             │
│  4. SACRED KNOWLEDGE PROTECTION                                             │
│     • Some knowledge should NOT be consolidated                             │
│     • Ritual secrets, sacred practices, initiation knowledge                │
│     • Players guided to respect these boundaries                            │
│                                                                             │
│  5. REPATRIATION                                                            │
│     • Knowledge databases shared back to source communities                 │
│     • Free access for indigenous researchers                                │
│     • Support for community-led documentation                               │
│                                                                             │
│  IMPLEMENTATION:                                                            │
│  • Indigenous Advisory Board reviews sensitive submissions                  │
│  • Cultural liaison officers for major knowledge domains                    │
│  • Automatic flagging of potentially sacred content                         │
│  • Community partnership agreements before commercialization                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quality Over Quantity

```yaml
quality_ethics:
  anti_gaming:
    - "No rewards for low-quality bulk submissions"
    - "Verification costs reduce spam incentive"
    - "Reputation loss for inaccurate submissions"

  accuracy_priority:
    - "Flagged errors reduce contributor standing"
    - "Corrections rewarded more than new entries"
    - "Expert review for all high-value claims"

  source_integrity:
    - "Primary sources preferred over secondary"
    - "Oral history methodology guidelines"
    - "Clear distinction between verified and unverified"

  uncertainty_honesty:
    - "Confidence scores required"
    - "Acknowledge gaps and unknowns"
    - "No incentive to fabricate"
```

---

## Summary

The Knowledge Consolidation System transforms The Analog Economy from a behavioral data platform into a **comprehensive knowledge preservation engine**.

**Key Insights:**

1. **Fragmented knowledge is AI's blind spot** - We fill that gap through gamified research
2. **Players become researchers** - Earning NVT for verified contributions
3. **Multi-layer verification** - Automated, community, and expert review ensures quality
4. **Enterprise value is real** - Pharma, AgTech, climate science all need this data
5. **Ethics-first approach** - Indigenous knowledge protection built in from the start

**The Vision:**
> "Play through history. Research what you find. Preserve knowledge that would otherwise be lost. Get paid for contributing to humanity's knowledge base."

---

## Related Documentation

- [Historical Progression](./historical-progression.md)
- [Survival & Progression](./survival-and-progression.md)
- [Payments Specification](./payments.md)
- [Gaian Configuration](../../core-governance/gaian/config.yaml)
