# The Codex: Ark of Humanity

> "You are not filling out a database. You are preserving the last traces of knowledge before the flood."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Information Architecture](#3-information-architecture)
4. [User Interface](#4-user-interface)
5. [Contribution Workflows](#5-contribution-workflows)
6. [Verification & Rewards](#6-verification--rewards)
7. [Era-Specific Presentations](#7-era-specific-presentations)
8. [Social Features](#8-social-features)
9. [Implementation Notes](#9-implementation-notes)

---

## 1. Overview

The Codex is the in-game interface for the Knowledge Consolidation system. It is NOT a wiki, database, or encyclopedia. It is a **living archive** that players contribute to as an act of preservation - saving humanity's fragmented knowledge before it's lost forever.

### Core Identity

| What The Codex IS | What The Codex IS NOT |
|-------------------|----------------------|
| An ark preserving endangered knowledge | A Wikipedia clone |
| A sacred duty within the game fiction | A side-quest checklist |
| A collaborative archaeological dig | Solo data entry |
| A source of in-game power and status | External to gameplay |
| Beautiful, reverent, meaningful | Utilitarian forms |

### The Emotional Core

Players should feel:
- **Urgency**: This knowledge is being lost in the real world
- **Significance**: Their contributions matter beyond the game
- **Wonder**: Discovering connections across cultures and eras
- **Pride**: Becoming recognized experts and archivists
- **Community**: Part of a collective preservation effort

---

## 2. Design Philosophy

### 2.1 Diegetic Integration

The Codex exists within the game world, not as a menu overlay:

```
In Sumer:        Clay tablets in the temple archive
In Egypt:        Papyrus scrolls in the House of Life
In Rome:         Codices in the library
In Medieval:     Illuminated manuscripts in the scriptorium
In Industrial:   Encyclopedias and field journals
In AI Era:       Quantum-preserved data crystals
```

Players physically visit the Codex location in their settlement. The interface changes with the era, but the underlying system is consistent.

### 2.2 Anti-Wiki Principles

| Wiki Pattern | Codex Pattern |
|--------------|---------------|
| Anyone can edit anything | Expertise unlocks editing rights |
| Information is static | Knowledge must be "recovered" through gameplay |
| Neutral tone | Era-appropriate voice and framing |
| Complete from the start | Deliberately incomplete, fragments emerge |
| External research | Research happens in-world |
| Hyperlinks everywhere | Physical connections (trade routes, travelers) |

### 2.3 The Recovery Metaphor

Knowledge in The Codex is not "added" - it is **recovered**, **preserved**, or **transcribed**. This framing:
- Positions players as rescuers, not data entry clerks
- Implies the knowledge exists but was lost
- Creates narrative tension (will it be recovered in time?)
- Honors the real-world sources of the knowledge

---

## 3. Information Architecture

### 3.1 Knowledge Domains

```
THE CODEX
├── Living World
│   ├── Flora
│   │   ├── Cultivated Plants
│   │   ├── Wild Plants
│   │   ├── Medicinal Plants
│   │   └── Sacred Plants
│   ├── Fauna
│   │   ├── Domesticated Animals
│   │   ├── Wild Animals
│   │   ├── Useful Species
│   │   └── Dangerous Species
│   └── Ecosystems
│       ├── Biome Characteristics
│       ├── Climate Patterns
│       └── Resource Cycles
│
├── Material Arts
│   ├── Crafting
│   │   ├── Textiles
│   │   ├── Pottery
│   │   ├── Metallurgy
│   │   └── Construction
│   ├── Agriculture
│   │   ├── Cultivation Techniques
│   │   ├── Irrigation Systems
│   │   ├── Soil Management
│   │   └── Harvest Preservation
│   └── Medicine
│       ├── Remedies
│       ├── Surgical Techniques
│       └── Preventive Practices
│
├── Human Knowledge
│   ├── Languages
│   │   ├── Vocabulary
│   │   ├── Grammar Systems
│   │   └── Writing Systems
│   ├── Mathematics
│   │   ├── Number Systems
│   │   ├── Measurement Units
│   │   └── Calculation Methods
│   └── Astronomy
│       ├── Celestial Observations
│       ├── Calendar Systems
│       └── Navigation Methods
│
└── Cultural Memory
    ├── Traditions
    │   ├── Ceremonies
    │   ├── Oral Histories
    │   └── Social Customs
    ├── Beliefs
    │   ├── Cosmologies
    │   ├── Ethical Systems
    │   └── Sacred Narratives
    └── Governance
        ├── Legal Codes
        ├── Economic Systems
        └── Social Structures
```

### 3.2 Entry Structure

Each Codex entry has a consistent structure with era-appropriate presentation:

```yaml
codex_entry:
  # Identity
  entry_id: "FLORA-MED-001"
  domain: "Living World > Flora > Medicinal Plants"
  recovery_status: "partial"  # fragment | partial | substantial | complete

  # Names (multilingual, multicultural)
  names:
    scientific: "Larrea tridentata"
    common: "Creosote Bush"
    traditional:
      - culture: "O'odham (Pima)"
        name: "Segai"
        meaning: "The one that smells of rain"
      - culture: "Seri (Comcaac)"
        name: "Haat"
        meaning: null  # Unknown
      - culture: "Spanish Colonial"
        name: "Gobernadora"
        meaning: "The Governor (dominates its territory)"

  # Visual
  illustrations:
    - type: "botanical_drawing"
      contributor: "player_id_hash"
      era_recovered: "industrial"
    - type: "photograph"
      contributor: "player_id_hash"
      era_recovered: "modern"

  # Core Knowledge
  description:
    brief: "Desert shrub with waxy leaves and yellow flowers"
    detailed: "..." # Full botanical description
    traditional_context: "..." # How indigenous peoples understood it

  # Practical Knowledge
  uses:
    medicinal:
      - condition: "Respiratory infections"
        preparation: "Leaf tea"
        culture: "O'odham"
        efficacy: "verified"  # fragment | plausible | verified | scientific
    material:
      - purpose: "Preservative"
        method: "Resin extraction"
        culture: "Multiple"

  # Scientific Data
  science:
    chemistry:
      - compound: "NDGA"
        concentration: "5-10% dry weight"
        properties: ["antioxidant", "antimicrobial"]
    ecology:
      habitat: "Sonoran, Mojave, Chihuahuan deserts"
      range_km2: 140000
      climate: "Arid, <250mm annual rainfall"

  # Provenance
  sources:
    - type: "player_research"
      contributor: "player_id_hash"
      date_recovered: "2027-03-15"
      verification_status: "peer_reviewed"
    - type: "elder_consultation"
      contributor: "player_id_hash"
      culture: "O'odham"
      date_recovered: "2027-04-22"

  # Connections
  related_entries:
    - "FLORA-MED-015"  # Similar medicinal plants
    - "CRAFT-MED-003"  # Medicine preparation techniques
    - "CULTURE-OODHAM-001"  # O'odham cultural entry

  # Meta
  completeness_score: 0.72
  contribution_count: 47
  last_updated: "2027-06-10"
```

### 3.3 Recovery States

```
Fragment → Partial → Substantial → Complete

Fragment (0-25%):
- Name only, or single use mentioned
- No verification possible
- Displayed as "glimpse" or "rumor"

Partial (25-50%):
- Basic identification
- One or two uses documented
- Some cultural context
- Displayed as "recovering"

Substantial (50-75%):
- Multiple names and cultures
- Several uses with preparations
- Some scientific data
- Displayed as "preserved"

Complete (75-100%):
- Full multilingual names
- Comprehensive uses across cultures
- Scientific verification
- Full cultural context
- Displayed as "archived"
```

---

## 4. User Interface

### 4.1 Physical Space (In-World)

The Codex is accessed through a physical location in each settlement:

**Sumer - Temple Archive:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     │
│     ░░  TEMPLE OF KNOWLEDGE  ░░░░░░░░░░░░░░░░░░░░░░░░░     │
│     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     │
│                                                             │
│         ┌─────────────────────────────────────┐             │
│         │                                     │             │
│         │      [Clay Tablet Shelves]          │             │
│         │                                     │             │
│         │    ┌─────┐  ┌─────┐  ┌─────┐       │             │
│         │    │Flora│  │Craft│  │Stars│       │             │
│         │    └─────┘  └─────┘  └─────┘       │             │
│         │                                     │             │
│         │         [Scribe's Table]            │             │
│         │                                     │             │
│         └─────────────────────────────────────┘             │
│                                                             │
│     [Your Character]           [Temple Scribe NPC]          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Interaction Points:**
- **Browse shelves**: Read existing entries (era-appropriate UI opens)
- **Scribe's table**: Contribute new knowledge
- **Temple Scribe**: Quest giver, explains what knowledge is needed
- **Meditation alcove**: View your contribution history and standing

### 4.2 Browse Interface

When browsing, the interface is era-appropriate but functionally consistent:

**Sumer Era: Clay Tablet View**
```
┌─────────────────────────────────────────────────────────────┐
│  ╔══════════════════════════════════════════════════════╗   │
│  ║  𒀭 TABLET OF HEALING PLANTS 𒀭                       ║   │
│  ║                                                      ║   │
│  ║  ════════════════════════════════════════════════    ║   │
│  ║                                                      ║   │
│  ║  The plant called SEGAI by the desert dwellers      ║   │
│  ║                                                      ║   │
│  ║  It grows where the rains are scarce.               ║   │
│  ║  Its leaves smell of the storm approaching.         ║   │
│  ║                                                      ║   │
│  ║  KNOWN USES:                                        ║   │
│  ║  ▸ Breath ailments - brew leaves in water           ║   │
│  ║  ▸ Wounds - apply resin                             ║   │
│  ║  ▸ [Fragment - more uses lost]                      ║   │
│  ║                                                      ║   │
│  ║  RECOVERY: ████████░░░░░░░░░░░░ 42%                 ║   │
│  ║                                                      ║   │
│  ║  ────────────────────────────────────────────────    ║   │
│  ║  [Contribute Knowledge]  [Related Tablets]           ║   │
│  ╚══════════════════════════════════════════════════════╝   │
│                                                             │
│  [◀ Previous]              [Domain: Flora]     [Next ▶]     │
└─────────────────────────────────────────────────────────────┘
```

**Industrial Era: Encyclopedia View**
```
┌─────────────────────────────────────────────────────────────┐
│  ┌────────────────────────────────────────────────────────┐ │
│  │  THE UNIVERSAL COMPENDIUM OF NATURAL PHILOSOPHY        │ │
│  │  ══════════════════════════════════════════════════════│ │
│  │                                                        │ │
│  │  CREOSOTE BUSH                                         │ │
│  │  Larrea tridentata (DC.) Coville                       │ │
│  │                                                        │ │
│  │  ┌──────────────┐  Kingdom: Plantae                    │ │
│  │  │              │  Family: Zygophyllaceae              │ │
│  │  │  [Botanical  │  Distribution: North American       │ │
│  │  │  Illustration│              Deserts                 │ │
│  │  │              │                                      │ │
│  │  └──────────────┘  VERNACULAR NAMES                    │ │
│  │                    • Segai (O'odham)                   │ │
│  │  CHEMICAL          • Gobernadora (Spanish)             │ │
│  │  CONSTITUENTS:     • Haat (Seri)                       │ │
│  │  • NDGA (5-10%)                                        │ │
│  │  • Flavonoids      MEDICINAL APPLICATIONS              │ │
│  │  • Lignans         ├─ Respiratory: Tea infusion        │ │
│  │                    ├─ Topical: Resin application       │ │
│  │                    └─ [3 more recovering...]           │ │
│  │                                                        │ │
│  │  ARCHIVAL STATUS: ████████████░░░░░░░░ 62%            │ │
│  │                                                        │ │
│  │  [Contribute]  [Sources: 47]  [Related: 12]           │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  Volume: FLORA    Page: 247 of 1,892    [Index] [Search]   │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Search & Discovery

**Search is intentionally limited by era:**

| Era | Search Capability |
|-----|-------------------|
| Sumer | Browse by domain only, ask scribe for specific knowledge |
| Classical | Alphabetical index, categorical browse |
| Medieval | Cross-referenced index, marginalia hints |
| Industrial | Full-text search, taxonomic classification |
| AI Era | Semantic search, relationship graphs |

This progression reflects the advancement of information technology and creates incentive to progress through eras.

### 4.4 Mobile Companion (Out-of-Game)

A companion app allows research outside the game:

```
┌─────────────────────────────────────┐
│  THE CODEX COMPANION                │
│  ═══════════════════════════════════│
│                                     │
│  Your Archivist Status: SCHOLAR     │
│  Contributions: 147                 │
│  Verifications: 89                  │
│  Standing: Top 12%                  │
│                                     │
│  ─────────────────────────────────  │
│                                     │
│  RESEARCH QUEUE                     │
│  ┌───────────────────────────────┐  │
│  │ ◉ Creosote Bush               │  │
│  │   Needed: Seri preparation    │  │
│  │   methods                     │  │
│  │   Reward: 250 KC              │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │ ○ Mesquite                    │  │
│  │   Needed: Nutritional data    │  │
│  │   Reward: 180 KC              │  │
│  └───────────────────────────────┘  │
│                                     │
│  [Browse Codex]  [My Contributions] │
│                                     │
└─────────────────────────────────────┘
```

**Companion Features:**
- Browse all recovered knowledge
- See what's needed (research bounties)
- Draft contributions for later submission
- Track personal contribution history
- Cannot submit directly (must return to game)

---

## 5. Contribution Workflows

### 5.1 Contribution Types

```yaml
contribution_types:
  new_entry:
    description: "Create entry for previously unknown subject"
    difficulty: "High"
    base_reward: 500
    requirements:
      - Must not duplicate existing entry
      - Minimum 3 verifiable facts
      - At least one traditional source

  fragment_recovery:
    description: "Add single piece of information to existing entry"
    difficulty: "Low"
    base_reward: 50
    requirements:
      - Must cite source
      - Must not contradict verified info

  substantial_addition:
    description: "Add entire section (e.g., medicinal uses)"
    difficulty: "Medium"
    base_reward: 200
    requirements:
      - Section must be coherent
      - Multiple facts required
      - Sources cited

  verification:
    description: "Confirm or challenge existing information"
    difficulty: "Low-Medium"
    base_reward: 75
    requirements:
      - Independent source required
      - Clear verification reasoning

  cultural_context:
    description: "Add cultural/traditional knowledge layer"
    difficulty: "High"
    base_reward: 300
    requirements:
      - Specific culture identified
      - Respectful framing
      - Primary sources preferred

  illustration:
    description: "Add visual representation"
    difficulty: "Medium"
    base_reward: 150
    requirements:
      - Original or properly attributed
      - Accurate to subject
      - Era-appropriate style
```

### 5.2 Contribution Interface

**The Scribe's Table (Sumer Era Example):**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  THE SCRIBE'S TABLE                                         │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  "What knowledge do you bring to preserve, traveler?"       │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  CONTRIBUTION TYPE                                  │    │
│  │  ○ New Tablet (create entry)                        │    │
│  │  ● Add to Existing (fragment recovery)              │    │
│  │  ○ Challenge/Verify                                 │    │
│  │  ○ Illustration                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  SUBJECT: [Search existing tablets...]              │    │
│  │           Creosote Bush (FLORA-MED-001)             │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  WHAT KNOWLEDGE DO YOU OFFER?                       │    │
│  │                                                     │    │
│  │  The Seri people call this plant "Haat" and use    │    │
│  │  the leaves differently. They sun-dry the leaves   │    │
│  │  and grind them to powder, mixing with animal fat  │    │
│  │  for wound treatment...                            │    │
│  │                                                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  SOURCE OF THIS KNOWLEDGE                           │    │
│  │  ○ Personal research/field observation              │    │
│  │  ● Documented source (cite below)                   │    │
│  │  ○ Elder/Traditional knowledge holder               │    │
│  │                                                     │    │
│  │  Citation: Felger & Moser, "People of the Desert   │    │
│  │  and Sea", 1985, p. 247                            │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  [Submit for Review]                    [Save Draft]        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 In-Game Research Activities

Knowledge can be recovered through gameplay:

| Activity | Knowledge Type | Example |
|----------|---------------|---------|
| Cultivate plants | Growth conditions, cultivation techniques | "Creosote cuttings root in sandy soil after monsoon" |
| Prepare medicine | Preparation methods, dosages | "Leaf tea requires 20 min steep time" |
| Trade with NPCs | Traditional names, cultural uses | "The elder calls it segai and uses it for..." |
| Explore biomes | Ecological data, habitat | "Found at elevation 500-1500m" |
| Archaeological dig | Historical uses, ancient records | "Clay tablet describes similar plant..." |
| Experiment | Efficacy, interactions | "Combined with willow bark increases effect" |

**Research Integration:**

```
┌─────────────────────────────────────────────────────────────┐
│  FIELD OBSERVATION RECORDED                                 │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  While cultivating Creosote Bush, you observed:             │
│                                                             │
│  "This plant tolerates extreme drought. After 3 months      │
│   without water, the leaves curled but the plant survived.  │
│   Upon watering, new growth appeared within 7 days."        │
│                                                             │
│  This observation can be contributed to The Codex!          │
│                                                             │
│  [Contribute Now]  [Save for Later]  [Dismiss]              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Verification & Rewards

### 6.1 Verification Layers

```
Contribution → Auto-Check → Peer Review → Expert Review → Verified

Layer 1: Auto-Check
- Duplicate detection
- Format validation
- Source format check
- Language/content filters

Layer 2: Peer Review (required for all)
- 3 players must review
- Reviewers earn rewards
- Consensus required to proceed

Layer 3: Expert Review (for substantial/new)
- Players with domain expertise
- Unlocked by contribution history
- Can override peer consensus

Layer 4: External Verification (for scientific claims)
- Cross-reference with databases
- Flag for staff review if needed
- Adds "scientifically verified" badge
```

### 6.2 Review Interface

```
┌─────────────────────────────────────────────────────────────┐
│  PEER REVIEW REQUEST                                        │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  Subject: Creosote Bush (FLORA-MED-001)                     │
│  Contribution Type: Fragment Recovery                       │
│  Submitted: 2 hours ago                                     │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  EXISTING ENTRY EXCERPT:                                    │
│  "...the O'odham prepare a tea from the leaves..."          │
│                                                             │
│  PROPOSED ADDITION:                                         │
│  "The Seri people prepare the leaves differently,           │
│   sun-drying and grinding to powder, then mixing with       │
│   animal fat for topical wound treatment."                  │
│                                                             │
│  CITED SOURCE:                                              │
│  Felger & Moser, "People of the Desert and Sea", 1985      │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  YOUR ASSESSMENT:                                           │
│                                                             │
│  Accuracy:     [Accurate] [Uncertain] [Inaccurate]          │
│  Source:       [Verified] [Unable to Check] [Invalid]       │
│  Value:        [High] [Medium] [Low]                        │
│                                                             │
│  Optional notes: _______________________________________    │
│                                                             │
│  [Submit Review: +25 KC]                                    │
│                                                             │
│  Current Reviews: 1 Accurate, 0 Uncertain, 0 Inaccurate     │
│  Needs: 2 more reviews                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.3 Reward Structure

```yaml
rewards:
  base_currency: "Knowledge Credits (KC)"

  contribution_rewards:
    new_entry_accepted: 500
    substantial_addition: 200
    fragment_recovery: 50
    verification_submitted: 75
    illustration_accepted: 150
    cultural_context_added: 300

  review_rewards:
    peer_review_completed: 25
    expert_review_completed: 50
    consensus_achieved_bonus: 10

  quality_multipliers:
    first_to_document: 2.0x
    rare_knowledge: 1.5x
    fills_research_bounty: 1.5x
    exceptional_quality: 1.25x
    connects_multiple_entries: 1.25x

  standing_bonuses:
    apprentice_archivist: 1.0x
    journeyman_archivist: 1.1x
    master_archivist: 1.2x
    grand_archivist: 1.3x
    keeper_of_records: 1.5x

  uses_for_kc:
    - Reincarnation ticket discounts
    - Exclusive cosmetics
    - Research tool upgrades
    - Access to restricted Codex sections
    - Name immortalized in credits
```

### 6.4 Archivist Progression

```yaml
archivist_ranks:
  apprentice:
    requirement: "0 verified contributions"
    permissions: ["submit", "peer_review"]
    title_display: "Apprentice Archivist"

  journeyman:
    requirement: "10 verified contributions"
    permissions: ["submit", "peer_review", "fragment_disputes"]
    title_display: "Journeyman Archivist"

  scholar:
    requirement: "50 verified contributions + 90% accuracy"
    permissions: ["expert_review_flora", "mentor"]
    title_display: "Scholar of [Domain]"

  master:
    requirement: "200 contributions + domain expertise + community endorsement"
    permissions: ["expert_review_all", "resolve_disputes", "bounty_creation"]
    title_display: "Master Archivist"

  keeper:
    requirement: "500 contributions + exceptional impact + staff recognition"
    permissions: ["policy_input", "featured_contributor"]
    title_display: "Keeper of Records"
```

---

## 7. Era-Specific Presentations

### 7.1 Visual Language by Era

| Era | Interface Style | Contribution Feel |
|-----|-----------------|-------------------|
| Sumer | Cuneiform clay tablets, temple aesthetic | Inscribing sacred records |
| Egypt | Hieroglyphic scrolls, House of Life | Scribal tradition |
| Classical | Bound codices, columned library | Scholarship tradition |
| Medieval | Illuminated manuscripts, scriptorium | Monastic preservation |
| Renaissance | Printed books, cabinet of curiosities | Natural philosophy |
| Industrial | Encyclopedic volumes, field journals | Scientific documentation |
| Modern | Digital interfaces, databases | Information science |
| AI Era | Holographic crystals, neural archives | Post-human preservation |

### 7.2 Era-Specific Features

**Sumer Era:**
- Knowledge delivered through temple quests
- Scribe NPCs provide oral context
- Limited search (must explore shelves)
- Divine framing ("the gods revealed...")

**Medieval Era:**
- Marginalia system (annotate others' work)
- Illumination mini-game for illustrations
- Cross-referencing between manuscripts
- Monastic orders with specializations

**Industrial Era:**
- Citation system fully developed
- Peer review formalized
- Taxonomic organization
- Scientific method integration

**AI Era:**
- Full relationship graphs visible
- Cross-cultural synthesis tools
- Predictive gap analysis
- Legacy viewing (see all past contributions across history)

---

## 8. Social Features

### 8.1 Research Teams

Players can form research teams to tackle large knowledge gaps:

```yaml
research_team:
  name: "Desert Flora Collective"
  focus: "Sonoran Desert ethnobotany"
  members: 12
  active_projects:
    - "Complete Seri plant names"
    - "Verify O'odham medicinal preparations"
  total_contributions: 847
  rank: "Distinguished"
```

### 8.2 Research Bounties

Community-driven priorities:

```
┌─────────────────────────────────────────────────────────────┐
│  ACTIVE RESEARCH BOUNTIES                                   │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  URGENT: Traditional Irrigation Methods              │    │
│  │                                                     │    │
│  │  "Document pre-industrial irrigation techniques     │    │
│  │   from arid regions worldwide"                      │    │
│  │                                                     │    │
│  │  Reward Pool: 15,000 KC                             │    │
│  │  Progress: ███████░░░░░░░░░░░░░░ 35%               │    │
│  │  Contributors: 47                                   │    │
│  │  Deadline: 14 days                                  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Traditional Fermentation Techniques                 │    │
│  │  Reward: 8,000 KC | Progress: 62% | 28 days left   │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  [View All Bounties]  [Propose New Bounty]                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.3 Knowledge Lineage

Track how knowledge spreads:

```
"You contributed the Seri name 'Haat' for Creosote Bush.
 Since then:
 - 3 players added Seri-related knowledge citing your entry
 - 12 players used this knowledge in crafting
 - The entry has been viewed 1,247 times

 Your contribution has branched into 8 related entries."
```

### 8.4 The Archive Wall

Public recognition in each era's Codex location:

```
THE ARCHIVE WALL
═════════════════

This season's most valued archivists:

🏆 "DesertScholar_42" - 847 contributions
   Specialty: Sonoran ethnobotany

🥈 "ScrollKeeper" - 623 contributions
   Specialty: Ancient mathematics

🥉 "RootSeeker" - 591 contributions
   Specialty: Medicinal preparations

[View Full Rankings]
```

---

## 9. Implementation Notes

### 9.1 Technical Architecture

```yaml
codex_services:
  entry_service:
    responsibility: "CRUD for knowledge entries"
    storage: "PostgreSQL with full-text search"
    caching: "Redis for frequently accessed entries"

  contribution_service:
    responsibility: "Submission and workflow management"
    queue: "Async processing for verification"

  verification_service:
    responsibility: "Multi-layer review pipeline"
    components:
      - auto_checker
      - peer_review_matcher
      - expert_router
      - external_verifier

  search_service:
    responsibility: "Era-appropriate search capabilities"
    backends:
      - basic_filter (ancient eras)
      - full_text (industrial+)
      - semantic (AI era)

  reward_service:
    responsibility: "Calculate and distribute KC"
    integration: "Game economy system"

  social_service:
    responsibility: "Teams, bounties, lineage tracking"
```

### 9.2 MVP Scope

For MVP, implement:

```yaml
mvp_features:
  included:
    - Single domain (Flora - Medicinal Plants)
    - 2 eras (Sumer, Industrial)
    - Basic contribution workflow
    - Peer review only (no expert tier)
    - Fragment recovery and verification
    - Basic rewards
    - Individual contributions (no teams)

  excluded:
    - All domains
    - All eras
    - Illustrations
    - Research teams
    - Bounty system
    - Mobile companion
    - Complex search
    - Lineage tracking

  metrics_to_prove:
    - Players willingly contribute
    - Verification catches errors
    - Knowledge quality is high
    - Rewards feel meaningful
    - Interface is engaging (not tedious)
```

### 9.3 Content Seeding

The Codex starts partially filled:

```yaml
initial_seeding:
  purpose: "Show what 'complete' looks like, create recovery targets"

  seeded_entries:
    complete: 5%      # Gold standard examples
    substantial: 15%  # Show what's possible
    partial: 30%      # Primary targets
    fragment: 50%     # Easy wins for new players

  sources:
    - Public domain ethnobotanical databases
    - Wikipedia (restructured, gaps added)
    - Partner institution data
    - Staff-created exemplars
```

---

## Appendix: Data Schema

```python
@dataclass
class CodexEntry:
    entry_id: str
    domain_path: str  # "Living World > Flora > Medicinal"
    recovery_status: RecoveryStatus

    # Names
    scientific_name: str | None
    common_names: list[str]
    traditional_names: list[TraditionalName]

    # Content
    description_brief: str
    description_full: str | None
    traditional_context: str | None

    # Structured knowledge
    uses: list[UseRecord]
    scientific_data: dict[str, Any]

    # Media
    illustrations: list[Illustration]

    # Provenance
    contributions: list[Contribution]
    sources: list[Source]

    # Relationships
    related_entries: list[str]

    # Meta
    completeness_score: float
    last_updated: DateTime
    view_count: int


@dataclass
class Contribution:
    contribution_id: str
    entry_id: str
    contributor_id: str  # Hashed player ID
    contribution_type: ContributionType
    content: dict[str, Any]
    source_citation: str | None

    # Workflow
    status: ContributionStatus
    submitted_at: DateTime
    reviews: list[Review]
    verified_at: DateTime | None

    # Rewards
    base_reward: int
    final_reward: int | None
    multipliers_applied: list[str]


@dataclass
class Review:
    reviewer_id: str
    accuracy_rating: Literal["accurate", "uncertain", "inaccurate"]
    source_check: Literal["verified", "unable", "invalid"]
    value_rating: Literal["high", "medium", "low"]
    notes: str | None
    reviewed_at: DateTime
```

---

*The Codex is not a database. It is humanity's memory, entrusted to those who play as preservers, not just players.*
