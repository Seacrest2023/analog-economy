# Analog Economy: Directory Structure Specification

> **Version:** 1.0
> **Last Updated:** 2026-01-19
> **Status:** Approved

## Overview

This document defines the canonical directory structure for The Analog Economy project. This structure is designed to:

1. **Separate concerns** - Clear boundaries between client, governance, contracts, and infrastructure
2. **Support Mault governance** - Python and TypeScript components follow Mault conventions
3. **Isolate proprietary IP** - Gaian governance layer is clearly separated for IP protection
4. **Scale with growth** - Biome-based organization allows adding new simulation environments
5. **Enable multi-team development** - Each top-level directory can be owned by different teams

---

## Root Structure

```
analog-economy/
│
├── docs/                         # Documentation & governance configs
├── shared/                       # Cross-component contracts & schemas
├── core-governance/              # THE BRAIN (Python/FastAPI + Gaian)
├── web-portal/                   # Player dashboard (TypeScript/React)
├── admin-tools/                  # Moderation & oversight tools
├── client-simulation/            # THE BODY (Unreal Engine 5)
├── economy-contracts/            # THE BANK (Solidity/Web3)
├── ops-infra/                    # THE WORLD (DevOps)
├── data/                         # Datasets & training outputs
├── tests/                        # E2E & integration tests
├── scripts/                      # Automation & governance scripts
├── .github/                      # CI/CD workflows
├── .governance/                  # Governance baselines (type-safety, mock-tax)
├── .pre-commit-config.yaml       # Pre-commit hook configuration
├── pyproject.toml                # Python tool configurations
├── .memory-layer/                # Mault local knowledge base (gitignored)
├── .gitignore
└── README.md
```

---

## Detailed Structure

### `/docs` - Documentation & Governance

```
docs/
├── mault.yaml                    # Code governance rulebook (Python/TS)
├── GDD_Master.md                 # Living Game Design Document
├── Architecture.md               # Tech stack definition
├── API_Contracts/                # Cross-component API specs
│   ├── game-to-governance.yaml   # UE5 → Python API contract
│   └── governance-to-chain.yaml  # Python → Solidity contract
├── gaian/                        # Gaian governance documentation
│   ├── philosophy.md             # The "why" of Gaian
│   ├── policies.md               # Rule definitions
│   └── biome-overrides.md        # Per-biome ethics rules
├── biomes/                       # Biome design documents
│   ├── the-abyss.md
│   ├── the-scorch.md
│   ├── the-ruins.md
│   ├── the-aqua.md
│   ├── the-botany.md
│   ├── the-theater.md
│   ├── the-exodus.md
│   ├── the-brink.md
│   ├── the-vector.md
│   └── the-uprising.md
└── guides/                       # Developer & user guides
    ├── architecture/             # Technical structure docs
    ├── concepts/                 # Project philosophy & vision
    ├── development/              # Setup, contributing, workflows
    ├── operations/               # Deployment, monitoring
    └── governance/               # Gaian & ethics documentation
```

### `/shared` - Cross-Component Contracts

**Purpose:** Single source of truth for data structures shared between components.

```
shared/
├── schemas/                      # Type definitions
│   ├── telemetry.py              # Python dataclasses (source of truth)
│   ├── telemetry.ts              # TypeScript interfaces (generated/synced)
│   └── telemetry.h               # C++ structs (manual sync required)
└── constants/
    ├── biome_ids.py              # Biome identifiers
    ├── biome_ids.ts              # TypeScript biome constants
    └── error_codes.py            # Standardized error codes
```

**Governance:** Changes to `shared/schemas/*.py` require updates to all language variants.

### `/core-governance` - The Brain

**Purpose:** Backend API, Gaian governance engine, and ML pipeline.

**Language:** Python 3.11+ (Mault governed)

```
core-governance/
├── app/                          # FastAPI application
│   ├── api/
│   │   ├── v1/                   # Versioned public endpoints
│   │   │   ├── telemetry.py      # Receives game telemetry
│   │   │   ├── payouts.py        # Token calculations
│   │   │   └── exports.py        # Buyer data access
│   │   └── internal/             # Admin-only endpoints
│   │       └── review.py         # Ethics review endpoints
│   ├── services/
│   │   ├── telemetry_service.py
│   │   ├── payout_calculator.py
│   │   └── export_service.py
│   ├── schemas/                  # Pydantic models
│   │   ├── telemetry_schema.py
│   │   └── payout_schema.py
│   ├── models/                   # Database models
│   │   └── player_session.py
│   ├── config/
│   │   └── settings.py
│   └── main.py                   # Application entrypoint
│
├── gaian/                        # PROPRIETARY GOVERNANCE (100% owned)
│   ├── __init__.py
│   ├── config.yaml               # Runtime policy configuration
│   ├── core/
│   │   ├── __init__.py
│   │   ├── policy_engine.py      # Rule evaluation engine
│   │   ├── ethics_filter.py      # Moral boundary enforcement
│   │   ├── novelty_scorer.py     # "Is this worth tokens?"
│   │   ├── anti_cheat.py         # "Is this real human behavior?"
│   │   ├── data_gate.py          # Final export checkpoint
│   │   ├── karma_tracker.py      # Karma accumulation and consequences
│   │   ├── animal_life.py        # Animal reincarnation mechanics
│   │   ├── checkpoint_manager.py # Save/restore for theft system
│   │   ├── theft_handler.py      # Theft mechanics, Shadow Marks
│   │   ├── conquest_manager.py   # Control vs ownership, Dominion Marks
│   │   └── director_ai.py        # Tension/pacing management
│   ├── biomes/                   # Biome-specific rule overrides
│   │   ├── __init__.py
│   │   ├── base_biome.py         # Base class for biome rules
│   │   ├── uprising.py           # Strictest ethics (man vs machine)
│   │   ├── theater.py            # Warfare abstraction rules
│   │   ├── vector.py             # Bio-warfare constraints
│   │   ├── brink.py              # Nuclear scenario rules
│   │   ├── exodus.py             # Migration sensitivity
│   │   ├── abyss.py              # Deep ocean rules
│   │   ├── scorch.py             # Mars/desert rules
│   │   ├── ruins.py              # Disaster SAR rules
│   │   ├── aqua.py               # Water scarcity rules
│   │   └── botany.py             # Agriculture rules
│   └── exports/
│       ├── __init__.py
│       └── buyer_packages.py     # Buyer-specific data packaging
│
├── ml_pipeline/
│   ├── ingest/
│   │   └── raw_receiver.py       # Initial telemetry landing
│   ├── processors/
│   │   ├── anonymizer.py         # PII removal
│   │   ├── feature_extractor.py  # Extract training features
│   │   └── quality_scorer.py     # Data quality assessment
│   └── exports/
│       └── dataset_builder.py    # Build buyer-ready datasets
│
├── tests/
│   ├── test_telemetry.py
│   ├── test_gaian_ethics.py
│   └── test_novelty_scorer.py
│
└── requirements.txt
```

**IP Note:** The `/gaian` directory contains proprietary algorithms. This code should have restricted access and is NOT part of Mault.

### `/web-portal` - Player Dashboard

**Purpose:** Player-facing web application for wallet, inventory, and earnings.

**Language:** TypeScript/React (Mault governed)

```
web-portal/
├── src/
│   ├── components/
│   │   ├── wallet/               # Wallet connection & display
│   │   ├── inventory/            # NFT inventory views
│   │   └── leaderboard/          # Player rankings
│   ├── pages/
│   │   ├── dashboard.tsx         # Main player dashboard
│   │   ├── profile.tsx           # Player profile
│   │   └── marketplace.tsx       # NFT marketplace
│   ├── services/
│   │   ├── api_client.ts         # Backend API client
│   │   └── wallet_service.ts     # Web3 wallet integration
│   ├── utils/
│   │   └── formatting.ts         # Display formatting helpers
│   └── types/
│       └── index.ts              # TypeScript type definitions
├── tests/
│   └── dashboard.test.ts
├── package.json
└── tsconfig.json
```

### `/admin-tools` - Moderation & Oversight

**Purpose:** Internal tools for ethics review, analytics, and buyer management.

**Language:** TypeScript (Mault governed)

```
admin-tools/
├── ethics-review/                # Human-in-the-loop interface
│   └── src/
├── analytics-dashboard/          # Usage metrics & biome performance
│   └── src/
├── buyer-portal/                 # Enterprise customer data access
│   └── src/
└── package.json
```

### `/client-simulation` - The Body

**Purpose:** Unreal Engine 5 game client.

**Language:** C++ (NOT Mault governed - requires custom tooling)

```
client-simulation/
├── Config/                       # UE5 configuration files
├── Content/
│   ├── Core/                     # Shared assets (UI, common materials)
│   └── Biomes/                   # Biome-specific content
│       ├── TheAbyss/
│       ├── TheScorch/
│       ├── TheRuins/
│       ├── TheAqua/
│       ├── TheBotany/
│       ├── TheTheater/
│       ├── TheExodus/
│       ├── TheBrink/
│       ├── TheVector/
│       └── TheUprising/
├── Source/
│   ├── AnalogEconomy/
│   │   ├── Public/               # Header files
│   │   └── Private/              # Implementation
│   └── GaianBridge/              # C++ plugin for Python/governance comms
├── Plugins/
│   └── PythonScripting/          # Unreal Python integration
└── Scripts/                      # Unreal automation scripts
```

**Tooling Note:** Use clang-tidy and Unreal Engine coding standards for C++ governance.

### `/economy-contracts` - The Bank

**Purpose:** Smart contracts for NFTs and Novelty Token.

**Language:** Solidity (NOT Mault governed - requires Solhint/Slither)

```
economy-contracts/
├── contracts/
│   ├── items/                    # ERC-1155 (Tools)
│   │   └── AnalogItems.sol
│   ├── land/                     # ERC-721 (Real Estate)
│   │   └── AnalogLand.sol
│   └── token/                    # ERC-20 (Novelty Token)
│       └── NoveltyToken.sol
├── scripts/
│   └── deploy.js                 # Deployment scripts
├── test/
│   └── NoveltyToken.test.js
├── hardhat.config.js
└── package.json
```

### `/ops-infra` - The World

**Purpose:** DevOps, infrastructure as code, monitoring.

```
ops-infra/
├── docker/
│   ├── governance.Dockerfile
│   └── web-portal.Dockerfile
├── terraform/
│   ├── aws/
│   └── modules/
├── k8s/
│   ├── governance-deployment.yaml
│   └── web-portal-deployment.yaml
└── monitoring/
    ├── prometheus/
    └── grafana/
```

### `/data` - Datasets

**Purpose:** Training data storage (mostly gitignored).

```
data/
├── raw/                          # Unprocessed telemetry (gitignored)
├── processed/                    # Cleaned, anonymized (gitignored)
└── exports/                      # Buyer-ready packages (gitignored)
```

### `/tests` - E2E & Integration

**Purpose:** Tests spanning multiple components.

```
tests/
├── e2e/
│   └── full_flow.test.ts
└── integration/
    └── governance_chain.test.py
```

### `/.github` - CI/CD

```
.github/
└── workflows/
    ├── governance-ci.yml
    ├── web-portal-ci.yml
    ├── contracts-audit.yml
    └── deploy.yml
```

### `/scripts/governance` - Pre-commit Governance Scripts

**Purpose:** Custom pre-commit hooks implementing Iron Dome, Rising Tide, and other governance policies.

**Strategy:** Native Governance - scripts are written in the language best suited to analyze the target code.

```
scripts/
└── governance/
    ├── python/                       # Python governance scripts
    │   ├── __init__.py
    │   ├── validate_config.py        # Layer 0: Config file validation
    │   ├── check_iron_dome.py        # Layer 2: Type safety ratchet
    │   ├── check_mock_tax.py         # Layer 3: Rising Tide (2x rule)
    │   ├── check_srp_size.py         # Layer 9: SRP size guardrails
    │   └── check_mock_conformance.py # Layer 10: create_autospec enforcement
    └── node/                         # Node.js governance scripts
        └── check_supply_chain.js     # Supply chain hallucination detector
```

| Script | Layer | Target | Purpose |
|--------|-------|--------|---------|
| `validate_config.py` | 0 | All | Prevent governance fail-open |
| `check_iron_dome.py` | 2 | Python | Type safety ratchet (only goes down) |
| `check_mock_tax.py` | 3 | Python | Tests cannot be >2x source |
| `check_srp_size.py` | 9 | Python | File/function size limits |
| `check_mock_conformance.py` | 10 | Python | Enforce create_autospec() |
| `check_supply_chain.js` | - | TypeScript | Detect hallucinated npm packages |

**Why Native Languages?**
- Python's `ast` module accurately counts type holes
- Node.js natively parses `package.json` and TypeScript configs
- Regex-based solutions are fragile and error-prone

See: [PRECOMMIT-SETUP.md](../project%20setup/PRECOMMIT-SETUP.md)

---

## Governance Coverage

| Directory | Language | Pre-commit Governed | Alternative Tooling |
|-----------|----------|---------------------|---------------------|
| `core-governance/` | Python | Yes (Layers 0-10) | - |
| `gaian/` | Python | Yes (structure only) | IP protection policies |
| `web-portal/` | TypeScript | Yes (Supply chain) | ESLint, tsc |
| `admin-tools/` | TypeScript | Yes (Supply chain) | ESLint, tsc |
| `client-simulation/` | C++ | Partial | clang-format, UE standards |
| `economy-contracts/` | Solidity | No | Solhint, Slither |
| `ops-infra/` | YAML/HCL | No | yamllint, tflint |
| `scripts/governance/` | Python/Node.js | N/A (is the governance) | - |

---

## Adding New Biomes

To add a new biome (e.g., "The Frontier"):

1. **Documentation:** Create `docs/biomes/the-frontier.md`
2. **Gaian rules:** Create `core-governance/gaian/biomes/frontier.py`
3. **Content:** Create `client-simulation/Content/Biomes/TheFrontier/`
4. **Update config:** Add biome to `core-governance/gaian/config.yaml`

---

## Related Documentation

- [Project Overview](../concepts/project-overview.md)
- [Gaian Philosophy](../../gaian/philosophy.md)
- [Mault Configuration](../../mault.yaml)
