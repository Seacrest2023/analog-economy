#!/usr/bin/env node
/**
 * Supply Chain Security: AI Hallucination/Typosquat Detector
 *
 * Detects potentially malicious packages BEFORE npm ci runs.
 * This runs in CI before installation, preventing postinstall
 * script execution from potentially malicious packages.
 *
 * Detection criteria:
 *   - Package doesn't exist in npm registry (true hallucination)
 *   - Package is < 30 days old (AI hallucinations are brand new)
 *
 * Usage:
 *   node scripts/governance/check_supply_chain.js
 *   node scripts/governance/check_supply_chain.js --verbose
 *
 * Exit codes:
 *   0 - All packages passed validation
 *   1 - Suspicious packages detected (BLOCKED)
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const MIN_DAYS_OLD = 30;
const EXEMPTIONS_FILE = '.supply-chain-exemptions.json';

// Well-known packages that don't need checking
const TRUSTED_PACKAGES = new Set([
  // TypeScript/JavaScript core
  'typescript', 'esbuild', 'webpack', 'vite', 'rollup',
  // Testing
  'jest', '@jest/globals', 'vitest', 'mocha', 'chai',
  // React ecosystem
  'react', 'react-dom', 'next',
  // Build tools
  'eslint', 'prettier', 'husky', 'lint-staged',
  // Common utilities
  'lodash', 'axios', 'express', 'fastify',
]);

// Trusted scopes
const TRUSTED_SCOPES = [
  '@types/',
  '@typescript-eslint/',
  '@babel/',
  '@eslint/',
  '@jest/',
  '@testing-library/',
];

/**
 * Load exemptions from file
 */
function loadExemptions(workingDir) {
  const exemptionsPath = path.join(workingDir, EXEMPTIONS_FILE);
  if (!fs.existsSync(exemptionsPath)) {
    return [];
  }
  try {
    const content = fs.readFileSync(exemptionsPath, 'utf8');
    const exemptions = JSON.parse(content);
    return Array.isArray(exemptions) ? exemptions : [];
  } catch {
    console.warn(`Warning: Could not parse ${EXEMPTIONS_FILE}`);
    return [];
  }
}

/**
 * Query npm registry for package metadata
 */
function getPackageInfo(packageName) {
  try {
    const result = execSync(`npm view ${packageName} time.created --json`, {
      encoding: 'utf-8',
      timeout: 10000,
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    const createdDate = JSON.parse(result.trim());
    const createdAt = new Date(createdDate);
    const ageInDays = Math.floor(
      (Date.now() - createdAt.getTime()) / (1000 * 60 * 60 * 24)
    );

    return { exists: true, createdAt: createdDate, ageInDays };
  } catch {
    return { exists: false, createdAt: null, ageInDays: null };
  }
}

/**
 * Parse package.json and extract all dependencies
 */
function getAllDependencies(packageJsonPath) {
  const content = fs.readFileSync(packageJsonPath, 'utf8');
  const packageJson = JSON.parse(content);
  const deps = new Set();

  const depFields = [
    'dependencies',
    'devDependencies',
    'peerDependencies',
    'optionalDependencies',
  ];

  for (const field of depFields) {
    if (packageJson[field]) {
      for (const name of Object.keys(packageJson[field])) {
        deps.add(name);
      }
    }
  }

  return Array.from(deps);
}

/**
 * Check if package should be skipped
 */
function shouldSkip(packageName, exemptions) {
  // Trusted packages
  if (TRUSTED_PACKAGES.has(packageName)) return true;

  // Trusted scopes
  for (const scope of TRUSTED_SCOPES) {
    if (packageName.startsWith(scope)) return true;
  }

  // Exempted packages
  return exemptions.some((e) => e.package === packageName);
}

/**
 * Main function
 */
function main() {
  const args = process.argv.slice(2);
  const verbose = args.includes('--verbose') || args.includes('-v');

  console.log('='.repeat(60));
  console.log('SUPPLY CHAIN SECURITY: Hallucination Detector');
  console.log('='.repeat(60) + '\n');

  // Find package.json (check web-portal first, then root)
  const possiblePaths = [
    path.join(process.cwd(), 'web-portal', 'package.json'),
    path.join(process.cwd(), 'package.json'),
  ];

  let packageJsonPath = null;
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) {
      packageJsonPath = p;
      break;
    }
  }

  if (!packageJsonPath) {
    console.log('No package.json found. Skipping check.\n');
    process.exit(0);
  }

  const workingDir = path.dirname(packageJsonPath);
  const exemptions = loadExemptions(workingDir);
  const allDeps = getAllDependencies(packageJsonPath);

  console.log(`Package.json: ${packageJsonPath}`);
  console.log(`Total dependencies: ${allDeps.length}`);

  const depsToCheck = allDeps.filter((dep) => !shouldSkip(dep, exemptions));
  console.log(`Dependencies to validate: ${depsToCheck.length}\n`);

  if (depsToCheck.length === 0) {
    console.log('All dependencies are trusted. No validation needed.\n');
    process.exit(0);
  }

  console.log('Validating packages...\n');

  const violations = [];

  for (const dep of depsToCheck) {
    const info = getPackageInfo(dep);

    if (!info.exists) {
      violations.push({
        package: dep,
        reason: 'Package does not exist in npm registry',
        severity: 'critical',
      });
      console.log(`  [CRITICAL] ${dep} - NOT FOUND`);
    } else if (info.ageInDays !== null && info.ageInDays < MIN_DAYS_OLD) {
      violations.push({
        package: dep,
        reason: `Package is only ${info.ageInDays} days old`,
        severity: 'high',
        createdAt: info.createdAt,
      });
      console.log(`  [HIGH] ${dep} - Only ${info.ageInDays} days old`);
    } else if (verbose) {
      console.log(`  [OK] ${dep} (${info.ageInDays} days old)`);
    }
  }

  console.log('');

  if (violations.length === 0) {
    console.log('All packages passed supply chain validation.\n');
    console.log('='.repeat(60));
    process.exit(0);
  }

  // BLOCKED
  console.log('-'.repeat(60));
  console.log(`\nBLOCKED: ${violations.length} suspicious package(s) detected.\n`);

  console.log('VIOLATIONS:\n');
  for (const v of violations) {
    console.log(`  Package: ${v.package}`);
    console.log(`  Reason: ${v.reason}`);
    console.log(`  Severity: ${v.severity.toUpperCase()}`);
    if (v.createdAt) {
      console.log(`  Created: ${v.createdAt}`);
    }
    console.log('');
  }

  console.log('FIX OPTIONS:');
  console.log('  1. Remove the suspicious package');
  console.log('  2. Use a well-known alternative');
  console.log('  3. If legitimate, add to .supply-chain-exemptions.json:\n');
  console.log('     [{"package": "name", "reason": "Verified by human",');
  console.log('       "addedBy": "your-name", "date": "YYYY-MM-DD"}]\n');
  console.log('-'.repeat(60));
  console.log('');
  console.log('='.repeat(60));

  process.exit(1);
}

main();
