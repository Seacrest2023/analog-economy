# Git Setup — The Analog Economy

> **Step 1 of 8:** Version control foundation for the monorepo architecture.

---

## Overview

The Analog Economy is a **monorepo** containing multiple services and components:

```
analog-economy/
├── core-governance/      # Python/FastAPI backend
├── client-simulation/    # Unreal Engine 5 client
├── web-portal/           # React/TypeScript frontend (future)
├── economy-contracts/    # Solidity smart contracts
├── admin-tools/          # Administrative utilities
├── ops-infra/            # Terraform, Kubernetes configs
├── docs/                 # Documentation (you are here)
├── shared/               # Cross-service schemas
└── tests/                # Integration tests
```

**Repository:** [github.com/Seacrest2023/analog-economy](https://github.com/Seacrest2023/analog-economy)

---

## Repository Status

The Analog Economy repository is already initialized with:

- [x] Git repository (`.git/`)
- [x] Comprehensive `.gitignore`
- [x] Branch protection (main)
- [x] Documentation structure
- [x] Development infrastructure

This guide serves as reference for:
- New contributors onboarding
- Understanding our Git workflow
- Troubleshooting common issues

---

## Our .gitignore Strategy

The Analog Economy `.gitignore` is comprehensive, covering all components:

```gitignore
# =============================================================================
# THE ANALOG ECONOMY - .GITIGNORE
# =============================================================================
# Covers: Python, Node.js, UE5, Solidity, Secrets, OS files
# =============================================================================

# -----------------------------------------------------------------------------
# Python (core-governance)
# -----------------------------------------------------------------------------
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
ENV/
.eggs/
*.egg-info/
.mypy_cache/
.pytest_cache/
.ruff_cache/
.coverage
htmlcov/

# -----------------------------------------------------------------------------
# Node.js / TypeScript (web-portal, admin-tools)
# -----------------------------------------------------------------------------
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.eslintcache
*.tsbuildinfo
.next/
out/

# -----------------------------------------------------------------------------
# Unreal Engine 5 (client-simulation)
# -----------------------------------------------------------------------------
client-simulation/Binaries/
client-simulation/DerivedDataCache/
client-simulation/Intermediate/
client-simulation/Saved/
client-simulation/*.sln
client-simulation/*.xcworkspace

# UE5 binary assets (tracked via Git LFS if needed)
# *.uasset
# *.umap

# -----------------------------------------------------------------------------
# Solidity / Hardhat (economy-contracts)
# -----------------------------------------------------------------------------
economy-contracts/artifacts/
economy-contracts/cache/
economy-contracts/typechain/
economy-contracts/typechain-types/

# -----------------------------------------------------------------------------
# Training Data (NEVER commit)
# -----------------------------------------------------------------------------
data/raw/
data/processed/
data/exports/

# Preserve directory structure
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/exports/.gitkeep

# -----------------------------------------------------------------------------
# Environment & Secrets (CRITICAL)
# -----------------------------------------------------------------------------
.env
.env.local
.env.*.local
.env.development
.env.staging
.env.production
*.env
secrets/
*.pem
*.key
*.crt
credentials.json

# Keep example file
!.env.example

# -----------------------------------------------------------------------------
# IDE & Editors
# -----------------------------------------------------------------------------
.idea/
.vscode/
*.swp
*.swo
*~
.project
.classpath
.settings/

# -----------------------------------------------------------------------------
# OS Files
# -----------------------------------------------------------------------------
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
desktop.ini

# -----------------------------------------------------------------------------
# Logs
# -----------------------------------------------------------------------------
logs/
*.log

# -----------------------------------------------------------------------------
# Docker
# -----------------------------------------------------------------------------
.docker/

# -----------------------------------------------------------------------------
# Terraform (ops-infra)
# -----------------------------------------------------------------------------
ops-infra/terraform/.terraform/
ops-infra/terraform/*.tfstate
ops-infra/terraform/*.tfstate.*
ops-infra/terraform/.terraform.lock.hcl

# -----------------------------------------------------------------------------
# Build Artifacts
# -----------------------------------------------------------------------------
dist/
build/
*.dll
*.exe
*.o
*.obj

# -----------------------------------------------------------------------------
# MAULT Memory Layer
# -----------------------------------------------------------------------------
.memory-layer/
```

---

## Branch Strategy

### Main Branches

| Branch | Purpose | Protection |
|--------|---------|------------|
| `main` | Production-ready code | Protected, requires PR |
| `develop` | Integration branch (optional) | Protected |

### Feature Branch Naming

```
type/description

Examples:
feat/gaian-health-endpoint
fix/docker-networking
docs/phase1-update
chore/update-dependencies
refactor/training-pipeline
test/action-scorer-unit
```

### Branch Workflow

```
main ────●─────────●─────────●─────────●────────
          \       / \       /
           \     /   \     /
            ●───●     ●───●
         feat/auth  fix/bug-123

Rules:
1. main is always deployable
2. All work in feature branches
3. Merge via Pull Request
4. Delete branch after merge
5. Squash commits for cleaner history
```

---

## Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

### Types

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(gaian): Add health endpoint` |
| `fix` | Bug fix | `fix(docker): Resolve networking issue` |
| `docs` | Documentation | `docs: Update phase-1 plan` |
| `chore` | Maintenance | `chore: Update Python dependencies` |
| `refactor` | Code restructure | `refactor(training): Extract scorer` |
| `test` | Test changes | `test: Add action validation tests` |
| `style` | Formatting | `style: Apply black formatting` |
| `perf` | Performance | `perf(qdrant): Optimize vector search` |
| `ci` | CI/CD changes | `ci: Add Docker build workflow` |

### Scopes (Project-Specific)

| Scope | Component |
|-------|-----------|
| `gaian` | Core governance service |
| `ue5` | Unreal Engine client |
| `docker` | Container infrastructure |
| `training` | Training data pipeline |
| `specs` | Game specifications |
| `db` | Database changes |

### Examples

```bash
# Good
git commit -m "feat(gaian): Add /api/v1/action endpoint"
git commit -m "fix(docker): Use service names in DATABASE_URL"
git commit -m "docs(specs): Add redemption mechanics to ascension-karma"
git commit -m "chore: Update FastAPI to 0.110.0"
git commit -m "test(training): Add novelty scorer unit tests"

# Bad
git commit -m "fix stuff"
git commit -m "WIP"
git commit -m "changes"
git commit -m "Update file"
```

---

## Daily Workflow

### Starting New Work

```powershell
# Ensure you're on main and up-to-date
git checkout main
git pull origin main

# Create feature branch
git checkout -b feat/my-feature

# Work, commit frequently
git add .
git commit -m "feat(gaian): Add initial endpoint structure"

# Push to remote
git push -u origin feat/my-feature
```

### Creating Pull Request

```powershell
# Using GitHub CLI (recommended)
gh pr create --title "Add Gaian health endpoint" --body "Implements /health endpoint for container health checks"

# Or via GitHub web UI
# 1. Go to https://github.com/Seacrest2023/analog-economy
# 2. Click "Compare & pull request"
# 3. Fill in description
# 4. Request review if needed
```

### After Merge

```powershell
# Switch back to main
git checkout main

# Pull latest (includes your merged PR)
git pull origin main

# Delete local feature branch
git branch -d feat/my-feature

# Delete remote feature branch (if not auto-deleted)
git push origin --delete feat/my-feature
```

---

## Large File Handling

### UE5 Assets

Unreal Engine generates large binary files. Our strategy:

1. **Intermediate/Build files:** Always gitignored
2. **Source assets (.uasset, .umap):** Currently gitignored, may use Git LFS later
3. **Source content (textures, meshes):** Store in cloud, download separately

### Git LFS (When Needed)

If we need to track large files:

```powershell
# Install Git LFS
git lfs install

# Track specific file types
git lfs track "*.psd"
git lfs track "*.mp4"
git lfs track "client-simulation/Content/**/*.uasset"

# Commit the .gitattributes
git add .gitattributes
git commit -m "chore: Configure Git LFS for large files"
```

### Training Data

Training data is **never committed**:
- Generated locally during gameplay
- Stored in `data/` directory (gitignored)
- Exported to cloud storage for production

---

## Troubleshooting

### Accidentally Committed Secrets

```powershell
# If you committed .env or secrets:

# 1. IMMEDIATELY remove from staging
git rm --cached .env
git commit -m "chore: Remove accidentally committed .env"

# 2. Add to .gitignore if missing
echo ".env" >> .gitignore

# 3. ROTATE ALL CREDENTIALS
# - Generate new API keys
# - Change passwords
# - Update .env with new values

# If already pushed, assume compromised. Rotate everything.
```

### Committed node_modules or venv

```powershell
# Remove from Git tracking (keeps local files)
git rm -r --cached node_modules/
# or
git rm -r --cached venv/

# Ensure in .gitignore
# (should already be there)

# Commit the fix
git add .gitignore
git commit -m "chore: Remove tracked dependencies"
```

### Merge Conflicts

```powershell
# During merge:
git merge main

# If conflicts occur:
# 1. Open conflicting files
# 2. Look for conflict markers:
#    <<<<<<< HEAD
#    your changes
#    =======
#    their changes
#    >>>>>>> main

# 3. Resolve by keeping correct code (remove markers)
# 4. Stage resolved files
git add path/to/resolved-file

# 5. Complete merge
git commit
```

### Detached HEAD

```powershell
# If you're in "detached HEAD" state:
git status
# Shows: HEAD detached at abc1234

# Create a branch to save your work
git checkout -b fix/save-my-work

# Or discard and return to main
git checkout main
```

---

## GitHub Repository Settings

### Recommended Settings

**Branch Protection (main):**
- [x] Require pull request before merging
- [x] Require status checks to pass
- [ ] Require signed commits (optional)
- [x] Include administrators

**Security:**
- [x] Dependabot alerts enabled
- [x] Secret scanning enabled
- [ ] Code scanning (future)

### Repository Secrets (For CI/CD)

When we add GitHub Actions, these secrets will be needed:

| Secret | Purpose |
|--------|---------|
| `DOCKERHUB_USERNAME` | Docker Hub login |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `AWS_ACCESS_KEY_ID` | AWS deployment |
| `AWS_SECRET_ACCESS_KEY` | AWS deployment |

---

## Cloning the Repository

### For New Contributors

```powershell
# Clone repository
git clone https://github.com/Seacrest2023/analog-economy.git
cd analog-economy

# Create local environment
copy .env.example .env
notepad .env  # Fill in your values

# Install Python dependencies
cd core-governance
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Start services
cd ..
docker compose up -d
```

### SSH vs HTTPS

```powershell
# HTTPS (prompted for credentials)
git clone https://github.com/Seacrest2023/analog-economy.git

# SSH (requires SSH key setup)
git clone git@github.com:Seacrest2023/analog-economy.git

# Change remote URL
git remote set-url origin git@github.com:Seacrest2023/analog-economy.git
```

---

## Quick Reference

```powershell
# Check status
git status

# See recent commits
git log --oneline -10

# See what changed
git diff

# Stage all changes
git add .

# Commit with message
git commit -m "type(scope): description"

# Push to remote
git push origin branch-name

# Pull latest
git pull origin main

# Create branch
git checkout -b feat/new-feature

# Switch branches
git checkout main

# Delete branch
git branch -d old-branch

# Stash changes temporarily
git stash
git stash pop

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all local changes
git checkout -- .
```

---

## Verification Checklist

For new contributors:

- [ ] Repository cloned successfully
- [ ] `.env` created from `.env.example`
- [ ] `.env` not showing in `git status`
- [ ] Can create and push feature branch
- [ ] Can create pull request
- [ ] Commit messages follow convention

---

## Next Steps

After Git setup:

1. **Configure environment:** See [ENVIRONMENT.md](./ENVIRONMENT.md)
2. **Set up Docker:** See [CONTAINERIZATION.md](./CONTAINERIZATION.md)
3. **Start development:** See [Phase 1: Golden Spike](../../development/phase-1-golden-spike.md)

---

*Part of The Analog Economy Production-Readiness Setup — Step 1 of 8*
