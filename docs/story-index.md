# The Analog Economy: Documentation Index

> A comprehensive index of all project documentation, organized by category.

**Last Updated:** 2026-01-20
**Total Documents:** 56

---

## Table of Contents

1. [Project Overview & Setup](#1-project-overview--setup)
2. [Architecture & Development](#2-architecture--development)
3. [World Building & Setting](#3-world-building--setting)
4. [Core Gameplay Systems](#4-core-gameplay-systems)
5. [Economy & Trade](#5-economy--trade)
6. [Player Progression & Legacy](#6-player-progression--legacy)
7. [AI & Governance Systems](#7-ai--governance-systems)
8. [Knowledge & Innovation](#8-knowledge--innovation)
9. [Visual & Art Direction](#9-visual--art-direction)

---

## 1. Project Overview & Setup

| Document | Path | Description |
|----------|------|-------------|
| **README** | [README.md](../README.md) | Project introduction, structure overview, tech stack (UE5, Python/FastAPI, React/TS), getting started guide, and Gaian/Mault governance overview |
| **Claude Code Instructions** | [claude.md](../claude.md) | Project instructions for Claude Code AI assistant: story-first philosophy, documentation standards, index maintenance rules, era context, and pending documentation gaps |
| **Project Overview** | [docs/guides/concepts/project-overview.md](guides/concepts/project-overview.md) | Executive summary of The Analog Economy concept: Proof-of-Intelligence mining, the economic model, biome portfolio, technical architecture, Gaian governance, competitive landscape, and target customers |
| **Security** | [SECURITY.md](../SECURITY.md) | Security policies and vulnerability reporting procedures |

---

## 2. Architecture & Development

| Document | Path | Description |
|----------|------|-------------|
| **Directory Structure** | [docs/guides/architecture/directory-structure.md](guides/architecture/directory-structure.md) | Detailed breakdown of the codebase organization: core-governance, web-portal, admin-tools, client-simulation, economy-contracts, and ops-infra |
| **Mault AI Coder Guide** | [docs/guides/MAULT-AI-CODER-GUIDE.md](guides/MAULT-AI-CODER-GUIDE.md) | Guidelines for AI-assisted development using the Mault code governance system |
| **Guides README** | [docs/guides/README.md](guides/README.md) | Overview of available developer guides and documentation structure |
| **Multiplayer Architecture** | [docs/specs/multiplayer-architecture.md](specs/multiplayer-architecture.md) | Persistent shared world design, world layers (city, settlement, private), settlement formation and governance, structured PvP philosophy (declared war vs murder), cooperation mechanics, and technical infrastructure for massively multiplayer ancient Eridu |
| **Phase 1: Golden Spike** | [development/phase-1-golden-spike.md](../development/phase-1-golden-spike.md) | Implementation plan for the first development phase: UE5-to-Python pipeline validation, Spike 0 (Hello Gaian) and Spike 1 (The First SILA), technical architecture, file structure, and testing checklist |
| **Docker Compose** | [docker-compose.yml](../docker-compose.yml) | Container orchestration for local development: Gaian service with hot reload, commented-out PostgreSQL/Redis/Qdrant services ready to enable |
| **Gaian Dockerfile** | [core-governance/Dockerfile](../core-governance/Dockerfile) | Multi-stage Docker build for the Gaian Python service: builder stage, production stage with non-root user, and development stage with hot reload |

---

## 3. World Building & Setting

| Document | Path | Description |
|----------|------|-------------|
| **World Lore** | [docs/specs/world-lore.md](specs/world-lore.md) | Comprehensive lore document covering the Mesopotamian map system, city-states, fog of war, Sumerian pantheon, the Anunnaki mystery layer, the Seven Sages (Apkallu), Divine ME artifacts, sacred sites, and Witness system integration |
| **Eridu Setting** | [docs/specs/eridu-setting.md](specs/eridu-setting.md) | Complete guide to Eridu (4500 BCE), the starting city: visual identity, city layout, zones (Temple, Harbor, Artisan, Commoner quarters), landmarks, institutions, currency system, infrastructure, daily life, NPC population, and player starting experience |
| **Daily Life Simulation** | [docs/specs/daily-life-simulation.md](specs/daily-life-simulation.md) | Detailed simulation of daily routines, social interactions, seasonal cycles, food culture, and atmospheric elements that bring the ancient world to life |
| **Temple & Religion** | [docs/specs/temple-religion.md](specs/temple-religion.md) | Religious life in Eridu: daily temple practices, the god's schedule, offering system (do ut des), festival calendar (Akitu, Kispu, lunar feasts), priestly paths and hierarchy, sanity/karma restoration through service, and the neglect penalty system |
| **Medicine & Healing** | [docs/specs/medicine-healing.md](specs/medicine-healing.md) | Dual healing system: Asu (physician) for physical treatment with herbal pharmacopeia, Ashipu (exorcist) for spiritual diagnosis and ritual cure, synergy mechanics, common ailments, treatment economics, and the path to becoming a master healer |
| **Entertainment & Leisure** | [docs/specs/entertainment-leisure.md](specs/entertainment-leisure.md) | Music system with instruments and performance venues, the Royal Game of Ur and gambling mechanics, tavern culture and the Kar-kid, storytelling traditions, sport hunting and fishing, social gatherings, and earning through entertainment |

---

## 4. Core Gameplay Systems

| Document | Path | Description |
|----------|------|-------------|
| **Character Creation** | [docs/specs/character-creation.md](specs/character-creation.md) | The Cast of Eridu: entry paths (free, SILA, land purchase), social hierarchy from elite to marginalized, character backgrounds with Sumerian titles, starting conditions, physical customization, naming conventions, and the "first moments" experience |
| **Combat & Conflict** | [docs/specs/combat-conflict.md](specs/combat-conflict.md) | Warfare in ancient Eridu: causes of conflict (water rights, borders, divine will), phalanx formations, battle phases, siege warfare, personal combat mechanics, weapons and equipment, karma consequences, legal penalties, and the seasonal warfare calendar |
| **Skills & Abilities** | [docs/specs/skills-abilities.md](specs/skills-abilities.md) | The "Learn the Ways" system: knowledge tiers (novice to grandmaster), skill categories, learning mechanics, complete trade mastery trees for Simug (smith) and Engar (farmer), supply chain knowledge, tech tree structure, and SILA rewards for learning |
| **Survival & Progression** | [docs/specs/survival-and-progression.md](specs/survival-and-progression.md) | Core survival mechanics: starting state, survival variables (hunger, thirst, health, energy, temperature, morale), environmental threats, risk assessment, progression paths, and the invention framework |
| **Inventory System** | [docs/specs/inventory-system.md](specs/inventory-system.md) | Ancient Era item catalog: tools, weapons, containers, materials, fire starting equipment, crafting stations, shop inventories, production limits, metalworking processes, "Learn the Ways" crafting rewards, SILA Developer Store, farmers markets, and caravan events |
| **NPC Behavior** | [docs/specs/npc-behavior.md](specs/npc-behavior.md) | Living world NPCs: behavior modes, information and intelligence sharing, law enforcement and social order, NPC delegation system for business operations, relationships and memory, daily life simulation, and developer revenue from NPC services |
| **Quest Framework** | [docs/specs/quest-framework.md](specs/quest-framework.md) | Organic quest discovery (no markers), quest types (survival, economic, social, temple, innovation, mystery, conflict), the contract system using clay tablets, time pressure mechanics, rewards and consequences, and how failure creates new quests |
| **Constraints** | [docs/specs/constraints.md](specs/constraints.md) | Design constraints and limitations that shape gameplay, ensuring historical accuracy and meaningful challenge |
| **MVP Training Facility** | [docs/specs/mvp-training-facility.md](specs/mvp-training-facility.md) | Minimum viable product scope for the initial training facility, defining what features are included in the first playable version |
| **Housing & Building** | [docs/specs/housing-building.md](specs/housing-building.md) | Land ownership tiers (squatter to deed owner), building types by category, construction phases (planning to finishing), material requirements, maintenance and decay systems, NPC labor delegation, and the path from reed hut to estate |
| **Water & Infrastructure** | [docs/specs/water-infrastructure.md](specs/water-infrastructure.md) | The canal system and irrigation, corvée labor obligations, the Gugallu (Canal Inspector) role, water allocation and disputes, levee construction and maintenance, seasonal infrastructure calendar, and liability for negligence |
| **Player Engagement** | [docs/specs/player-engagement.md](specs/player-engagement.md) | Complete retention and engagement systems: the Cylinder Seal progression marker, dopamine loops (30-second to weekly), material hierarchy for visual status, seasonal festivals and live ops, votive statue achievements, Scribe's Tablet leaderboards, daily Temple Tribute hooks, caravan system with 99/1 economy model, and anti-dark-pattern design philosophy |

---

## 5. Economy & Trade

| Document | Path | Description |
|----------|------|-------------|
| **Blockchain Economy** | [docs/specs/blockchain-economy.md](specs/blockchain-economy.md) | Complete crypto-economic model: two-token system (SILA off-chain + ANALOG on-chain), NFT categories (Genesis, Ascension, Destination Tickets), token utility, minting mechanisms, anti-inflation measures, and developer revenue model |
| **Payments** | [docs/specs/payments.md](specs/payments.md) | Payment integration specification: supported payment methods (crypto, fiat, in-game), transaction flows, fee structures, refund policies, and security measures |
| **Professions & Economy** | [docs/specs/professions-economy.md](specs/professions-economy.md) | In-game professions, economic roles, trade mechanics, specialization paths, and how players participate in the ancient economy |
| **Textile Production** | [docs/specs/textile-production.md](specs/textile-production.md) | The wool economy and largest industry: complete supply chain from fleece to garment, spinning/weaving/dyeing skill trees, quality grades, temple workshop system, the Lukur manager role, independent production, and trade networks |
| **Animal Husbandry** | [docs/specs/animal-husbandry.md](specs/animal-husbandry.md) | The Sipa (shepherd) profession, livestock types (sheep, goats, cattle, donkeys), selective breeding and lineage records, the shepherd's contract and liability, veterinary medicine, flock management, and integration with textile/food supply chains |
| **Fishing & Sailing** | [docs/specs/fishing-sailing.md](specs/fishing-sailing.md) | The Shu-ku (fisherman) and Ma-lah (sailor) professions, fishing techniques (nets, hooks, spears, traps), boat types (reed boats, coracles, freighters), the Karum harbor district, navigation skills, maritime trade, and water-based hazards |
| **Merchant & Trade** | [docs/specs/merchant-trade.md](specs/merchant-trade.md) | The Damgar (merchant) profession, trade routes (Dilmun, Magan, Meluhha), the Tappu investment partnership system, contract law and clay envelope authentication, the Karum marketplace, pricing dynamics, weights and measures, and merchant skill trees |
| **Scribe & Administration** | [docs/specs/scribe-administration.md](specs/scribe-administration.md) | The Dubsar (scribe) profession, Edubba (scribal school) curriculum and discipline, literacy as power, career paths (temple admin, palace admin, notary, specialist), document types, cuneiform mastery, and the economics of scribal services |
| **Food Production** | [docs/specs/food-production.md](specs/food-production.md) | The Lunga (brewer) and Muhaldim (baker/cook) professions, beer brewing process (bappir creation, fermentation), bread types and baking, butchering, the tavern system and Kar-kid (tavern keeper), supply chains, and temple food production |
| **Woodworking** | [docs/specs/woodworking.md](specs/woodworking.md) | The Nagar (carpenter) profession in a timber-poor land, wood scarcity and imports, carpentry techniques, furniture making, boat construction and the shipwright specialization, tool production, temple/palace commissions, and workshop economics |
| **Pottery & Ceramics** | [docs/specs/pottery-ceramics.md](specs/pottery-ceramics.md) | The Bahar (potter) profession, clay processing and preparation, forming techniques (coiling, wheel throwing, molds), kiln technology and firing process, product lines (storage, cooking, tableware, specialty), decoration methods, and workshop economics |

---

## 6. Player Progression & Legacy

| Document | Path | Description |
|----------|------|-------------|
| **Legacy System** | [docs/specs/legacy-system.md](specs/legacy-system.md) | Bloodlines across time: how player progress persists across deaths and eras, inheritance mechanics, cross-era progression, Legacy Points, the Great Filter vetting system, and the Ancestor Hall |
| **Historical Progression** | [docs/specs/historical-progression.md](specs/historical-progression.md) | How players advance through historical eras from Ancient to AI Era, era transition requirements, and timeline mechanics |
| **Asset Protection & Karma** | [docs/specs/asset-protection-karma.md](specs/asset-protection-karma.md) | What can and cannot be stolen, the four asset tiers (Soul-bound, Heirloom, Deed, Common), karma system, animal reincarnation consequences, and conquest mechanics |
| **Governance System** | [docs/specs/governance-system.md](specs/governance-system.md) | In-game governance structures: temple hierarchy, council systems, player governance roles, voting mechanics, and political progression |
| **Legal & Justice** | [docs/specs/legal-justice.md](specs/legal-justice.md) | The three-tier court system (local assembly, temple court, royal court), evidence and procedures, divine oaths, the River Ordeal, the Code of Ur-Nammu (fines over mutilation), capital crimes, marriage law, and karma integration with legal actions |
| **Ascension & Karma** | [docs/specs/ascension-karma.md](specs/ascension-karma.md) | Era graduation requirements (Five Pillars: wealth, legacy, skill mastery, karma minimum, innovation quests), persistent karma system across all lifetimes, Hindu-inspired reincarnation mechanics (human/animal forms), the Witness role for data validation, the secret Anunnaki mystery quest, and the path to Moksha (liberation) |

---

## 7. AI & Governance Systems

| Document | Path | Description |
|----------|------|-------------|
| **Director AI** | [docs/specs/director-ai.md](specs/director-ai.md) | The invisible hand orchestrating gameplay: tension management, drama curve management, event orchestration, player state monitoring, era-specific behaviors, and training data optimization |
| **Knowledge Consolidation** | [docs/specs/knowledge-consolidation.md](specs/knowledge-consolidation.md) | How player knowledge is collected, verified, and consolidated into training data; the verification pipeline and data quality measures |
| **Training Data Architecture** | [docs/specs/training-data-architecture.md](specs/training-data-architecture.md) | Technical blueprint for training data extraction: high-value data taxonomy (ambiguity resolution, novel strategy, Theory of Mind), capture schemas (SFT, DPO, RLDS trajectories), anti-gaming validation (peer prediction, Schelling points, gold standards), quality scoring algorithms, data pipeline architecture, and Witness integration for human QA |
| **Ancient Era Events** | [docs/specs/ancient-era-events.md](specs/ancient-era-events.md) | Director AI playbook for Ancient Era: code-ready event definitions with trigger conditions, codex learning paths, and failure states. Covers onboarding (first hour), survival events (flood, drought, disease), innovation events (wheel, writing, irrigation, metallurgy), economic events, social events, and mystery events (Anunnaki clues) |

---

## 8. Knowledge & Innovation

| Document | Path | Description |
|----------|------|-------------|
| **The Codex** | [docs/specs/the-codex.md](specs/the-codex.md) | The in-game "Ark of Humanity" - a living archive for knowledge preservation, contribution workflows, verification systems, era-specific presentations, and how it differs from traditional wikis |
| **Ancient Innovations** | [docs/specs/ancient-innovations.md](specs/ancient-innovations.md) | Discoverable technologies and innovations for the Ancient Era: what can be invented, discovery mechanics, innovation trees, and historical accuracy requirements |

---

## 9. Visual & Art Direction

| Document | Path | Description |
|----------|------|-------------|
| **Art Direction** | [docs/specs/art-direction.md](specs/art-direction.md) | Visual style guide: color palettes, architectural styles, character design principles, UI/UX guidelines, environmental art direction, and era-specific visual identity |

---

## Quick Reference: Files by Type

### Specification Documents (43)
All located in `docs/specs/`:
- ancient-era-events.md
- ancient-innovations.md
- animal-husbandry.md
- art-direction.md
- ascension-karma.md
- asset-protection-karma.md
- blockchain-economy.md
- character-creation.md
- combat-conflict.md
- constraints.md
- daily-life-simulation.md
- director-ai.md
- entertainment-leisure.md
- eridu-setting.md
- fishing-sailing.md
- food-production.md
- governance-system.md
- historical-progression.md
- housing-building.md
- inventory-system.md
- knowledge-consolidation.md
- legacy-system.md
- legal-justice.md
- medicine-healing.md
- merchant-trade.md
- multiplayer-architecture.md
- mvp-training-facility.md
- npc-behavior.md
- payments.md
- player-engagement.md
- pottery-ceramics.md
- professions-economy.md
- quest-framework.md
- scribe-administration.md
- skills-abilities.md
- survival-and-progression.md
- temple-religion.md
- textile-production.md
- the-codex.md
- training-data-architecture.md
- water-infrastructure.md
- woodworking.md
- world-lore.md

### Guide Documents (7)
- docs/guides/README.md
- docs/guides/MAULT-AI-CODER-GUIDE.md
- docs/guides/concepts/project-overview.md
- docs/guides/architecture/directory-structure.md
- docs/guides/project setup/GIT-SETUP.md
- docs/guides/project setup/ENVIRONMENT.md
- docs/guides/project setup/CONTAINERIZATION.md

### Root Documents (3)
- README.md
- claude.md
- SECURITY.md

---

## Document Status Legend

| Status | Meaning |
|--------|---------|
| **Draft** | Initial creation, subject to major changes |
| **In Progress** | Actively being developed |
| **Review** | Ready for review and feedback |
| **Complete** | Finalized, minor updates only |

---

## Related Resources

- **Gaian Configuration**: `core-governance/gaian/config.yaml` - Runtime ethics and anti-cheat rules
- **Mault Configuration**: `docs/mault.yaml` - Code quality and governance rules

---

*"The best time to plant a tree was 20 years ago. The second best time is now. The best time to document your game was at the start. The second best time is also now."*
