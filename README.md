# The Analog Economy

> A high-fidelity survival simulation game that functions as a "Proof-of-Intelligence" mining operation.

## Overview

The Analog Economy is a survival simulation game where players solve complex, physics-based problems across diverse biomes. Their gameplay data is harvested—with strict ethical governance—to train autonomous agents for enterprise and government customers.

**Core Thesis:** In a world where AI handles predictable work, the scarce resource becomes human improvisation, creativity, and edge-case problem-solving.

## Project Structure

```
analog-economy/
├── docs/                     # Documentation & governance configs
│   ├── mault.yaml            # Code governance (dev-time)
│   └── guides/               # Developer guides
├── shared/                   # Cross-component contracts
├── core-governance/          # Backend API + Gaian governance
├── web-portal/               # Player dashboard
├── admin-tools/              # Moderation & oversight
├── client-simulation/        # Unreal Engine 5 game client
├── economy-contracts/        # Smart contracts (Solidity)
├── ops-infra/                # DevOps & infrastructure
├── data/                     # Training datasets (gitignored)
└── tests/                    # E2E & integration tests
```

## Key Components

### Gaian Governance Engine

The proprietary governance layer that maintains balance between probabilistic AI systems and deterministic rules.

- **Ethics Filter** - Enforces moral boundaries on training data
- **Anti-Cheat** - Validates authentic human behavior
- **Novelty Scorer** - Evaluates solution creativity for token rewards
- **Data Gate** - Final checkpoint before data export

### The Biome Portfolio

| Biome | Theme | Target Customer |
|-------|-------|-----------------|
| The Abyss | Deep Ocean | Energy Sector |
| The Scorch | High Desert / Mars | Space / Mining |
| The Ruins | Disaster / Rubble | FEMA / NGOs |
| The Aqua | Water Scarcity | Utilities / Govt |
| The Botany | Food Security | Agri-Tech |
| The Theater | Geopolitics | DoD, NATO |
| The Exodus | Migration | UN, DHS |
| The Brink | Nuclear Escalation | State Dept |
| The Vector | Bio-Warfare | CDC, DARPA |
| The Uprising | Man vs. Machine | Big Tech, PMCs |

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Unreal Engine 5.3+

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-org/analog-economy.git
cd analog-economy

# Set up Python environment
cd core-governance
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Run the governance API
python -m uvicorn app.main:app --reload
```

## Documentation

- [Project Overview](docs/guides/concepts/project-overview.md)
- [Directory Structure](docs/guides/architecture/directory-structure.md)
- [Gaian Configuration](core-governance/gaian/config.yaml)
- [Mault Code Governance](docs/mault.yaml)

## Code Governance

This project uses **Mault** for code governance (Python & TypeScript) and **Gaian** for runtime data governance.

- **Mault** ensures code quality, directory structure, and naming conventions
- **Gaian** ensures ethical boundaries, anti-cheat, and data export rules

## License

Proprietary. All rights reserved.

## Contact

For inquiries about The Analog Economy project, contact the founding team.
