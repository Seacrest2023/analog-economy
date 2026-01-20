<!--
╔══════════════════════════════════════════════════════════════════════╗
║  MAULT PRO - Production-Readiness Kit                                ║
║  Copyright © 2025 Mault. All rights reserved.                        ║
║                                                                      ║
║  This document is licensed for use with the Mault VS Code Extension. ║
║  Redistribution or resale is prohibited.                             ║
║                                                                      ║
║  https://mault.dev | support@mault.dev                               ║
╚══════════════════════════════════════════════════════════════════════╝
-->

# TDD-GUIDE.md — Test-Driven Development Philosophy

> **The TDD Principle:** Write the test first. Watch it fail. Write code to make it pass. Refactor. The test is the specification.

---

## Official Pattern Files (THE NORTH STAR)

**CRITICAL:** When writing tests, always reference these pattern files. Do NOT copy patterns from existing test files — many are legacy and violate current standards.

| Pattern | Location | When to Use |
|---------|----------|-------------|
| **Pure Core Unit** | `extension/docs/patterns/pure-core-unit.ts` | NO I/O, NO vscode import, stub injection only. DELETE if Mock Tax >2x |
| **Gold Standard v3.0** | `extension/docs/patterns/gold-standard-integration.ts` | vscode API mocking OR Mock Tax escape hatch. Shared mock + patch in beforeEach |
| **Behavioral Detector** | `extension/docs/patterns/behavioral-detector.ts` | Detector perception: "Does it SEE the files?" Cross-language, negative cases |
| **Adapter Verification** | `extension/docs/patterns/adapter-verification.ts` | Real I/O in temp dirs (git, fs). Thin wrapper validation |
| **Event Flow** | `extension/docs/patterns/event-flow.ts` | Orchestration: "Does Save → Handler → Analysis?" Callback capture pattern |

### Quick Decision Tree

```
Is the code PURE (no I/O, no vscode)?
├── YES → Pure Core Unit Test (tests/unit/)
└── NO → What does it test?
    ├── vscode API interaction → Gold Standard Integration (tests/integration/)
    ├── Detector perception → Behavioral Detector (tests/behavioral/)
    ├── 3rd party I/O (git, fs) → Adapter Verification (tests/integration/adapters/)
    └── Event wiring → Event Flow (tests/integration/event-flows/)
```

> **CRITICAL CLARIFICATION:** Gold Standard v3.0 tests (which use `import * as vscode from 'vscode'`) go in `tests/integration/`, NOT `tests/unit/`. ESLint governance blocks ALL vscode imports in `tests/unit/` — this is intentional. Unit tests must be pure logic only.

---

## The Problem: Tests as Afterthoughts

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE AFTERTHOUGHT SPIRAL                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Day 1: Write feature code                                         │
│        ↓                                                            │
│   Day 2: "I'll add tests later"                                     │
│        ↓                                                            │
│   Day 5: Feature shipped, tests forgotten                           │
│        ↓                                                            │
│   Day 30: Bug found → No tests to catch it                          │
│        ↓                                                            │
│   Day 31: Write tests after the fact (low quality, tautological)    │
│        ↓                                                            │
│   TESTS VERIFY THE BUG, NOT THE INTENT                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The TDD Principle:** Tests written first capture intent. Tests written after capture implementation (bugs included).

---

## The Red-Green-Refactor Cycle

```
┌─────────────────────────────────────────────────────────────────────┐
│                    RED-GREEN-REFACTOR                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                    ┌──────────┐                                     │
│                    │   RED    │ ← Write failing test                │
│                    └────┬─────┘                                     │
│                         │                                           │
│              Write test first, watch it fail                        │
│                         │                                           │
│                         ▼                                           │
│                    ┌──────────┐                                     │
│                    │  GREEN   │ ← Write minimum code to pass        │
│                    └────┬─────┘                                     │
│                         │                                           │
│              Only enough code to make test green                    │
│                         │                                           │
│                         ▼                                           │
│                    ┌──────────┐                                     │
│                    │ REFACTOR │ ← Clean up while tests protect      │
│                    └────┬─────┘                                     │
│                         │                                           │
│              Improve design, tests catch regressions                │
│                         │                                           │
│                         └──────────────┐                            │
│                                        ▼                            │
│                              ┌─────────────────┐                    │
│                              │ REPEAT          │                    │
│                              └─────────────────┘                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Test Categories

### The Complete Testing Pyramid

The foundation of our testing strategy is a **Governance Layer** that validates the tests themselves. This eliminates the most common reason testing strategies fail: mocks that drift from reality over time.

```
                        ┌─────────────────────┐
                        │  Event Flow Tests   │  ← Full system behavior validation
                        │   (Integration)     │
                        └──────────┬──────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 │   Behavioral Detector Tests       │  ← Detector perception validation
                 │   (Input/Output Verification)     │
                 └─────────────────┬─────────────────┘
                                   │
                  ┌────────────────┴────────────────┐
                  │      Adapter Verification       │  ← 3rd party contracts
                  │        (Real I/O Tests)         │
                  └────────────────┬────────────────┘
                                   │
        ┌──────────────────────────┴──────────────────────────┐
        │                    Unit Tests                        │
        │  (Pure Core with Stub Injection - Gold Standard)    │
        └──────────────────────────┬──────────────────────────┘
                                   │
┌──────────────────────────────────┴──────────────────────────────┐
│                        Governance Layer                          │
│    Mock Integrity + Signature Validation + Type-Safe Helpers    │
│                      + Any Ratchet                               │
└─────────────────────────────────────────────────────────────────┘
```

**Why the Governance Layer?**

AI coders (Cursor, Copilot, Claude) have a unique failure mode:

> They write tests that **look correct** but test against **stale or incorrect mocks**.

The test passes. The AI reports success. Production crashes.

The Governance Layer guarantees that unit tests run against "fakes" that **mathematically match** the real APIs.

### Category Definitions

| Category | What It Tests | I/O Allowed? | Speed | Example |
|----------|---------------|--------------|-------|---------|
| **Unit** | Pure logic, single function | NO | Fast (ms) | `calculateTotal(items)` returns correct sum |
| **Integration** | Components wired together | Mocked I/O | Medium (s) | Detector → Publisher pipeline |
| **E2E** | Full user workflow | Real I/O | Slow (mins) | User opens app, clicks button, sees result |

### Directory Structure

```
tests/
├── unit/           # Pure logic ONLY — NO vscode imports (ESLint enforced)
│   ├── services/   # Business logic tests (pure functions)
│   ├── utils/      # Utility function tests
│   └── governance/ # Governance tests (meta-tests)
├── integration/    # Gold Standard v3.0 — vscode mocking allowed here
│   ├── commands/   # Command handler tests
│   ├── detectors/  # Detector pipeline tests
│   ├── adapters/   # Real I/O verification tests
│   └── event-flows/ # Event orchestration tests
├── behavioral/     # Detector perception tests (cross-language)
└── e2e/            # Full workflow tests
    └── stripe-checkout.e2e.test.ts
```

**Key distinction:** If your test needs `import * as vscode from 'vscode'`, it goes in `tests/integration/`, not `tests/unit/`. ESLint will block the commit otherwise.

---

## The Pure Core Pattern

### Why This Matters for TDD

Unit tests are easiest to write when code has **no I/O dependencies**. The Pure Core pattern separates:
- **Pure Core:** Business logic with no I/O imports (easy to test)
- **Adapters:** Thin wrappers for I/O (tested via integration tests)

### Example (Language-Agnostic)

**Before (Hard to Test):**
```
┌─────────────────────────────────────────────────────────────────────┐
│  function processOrder(order):                                      │
│    user = database.getUser(order.userId)     # I/O - hard to mock  │
│    if user.balance < order.total:                                   │
│      return Error("Insufficient funds")                             │
│    database.debitUser(user, order.total)     # I/O - hard to mock  │
│    email.send(user.email, "Order confirmed") # I/O - hard to mock  │
│    return Success                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

**After (Easy to Test):**
```
┌─────────────────────────────────────────────────────────────────────┐
│  PURE CORE (Unit Testable):                                         │
│  ─────────────────────────                                          │
│  function validateOrder(user, order):                               │
│    if user.balance < order.total:                                   │
│      return Error("Insufficient funds")                             │
│    return Success                                                   │
│                                                                     │
│  ADAPTERS (Integration Testable):                                   │
│  ────────────────────────────────                                   │
│  function processOrder(order):                                      │
│    user = userAdapter.getUser(order.userId)                         │
│    result = validateOrder(user, order)  # Pure call                 │
│    if result.ok:                                                    │
│      paymentAdapter.debit(user, order.total)                        │
│      emailAdapter.sendConfirmation(user)                            │
│    return result                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

**Unit Test (No Mocks Needed):**
```
test("rejects order when user has insufficient funds"):
  user = { balance: 50 }
  order = { total: 100 }
  result = validateOrder(user, order)
  assert result.error == "Insufficient funds"
```

---

## Language-Specific Frameworks

| Language | Unit Test Framework | Integration | Mutation Testing |
|----------|---------------------|-------------|------------------|
| **TypeScript/JS** | Jest, Vitest | Jest + mocks | StrykerJS |
| **Python** | pytest | pytest + fixtures | mutmut |

**Roadmap Languages:** Go (go test), Java (JUnit 5), Rust (cargo test), C# (xUnit) support is planned for future releases.

---

## The Gold Standard Pattern (Integration Tests)

### Core Principles (v3.0)

For VS Code extensions or any framework with global state:

1. **SHARED REALITY:** Use a shared mock file (e.g., `tests/mocks/vscode.ts`)
2. **PATCHING:** Use `beforeEach` to add missing capabilities to the shared mock
3. **NO DISK:** Mock filesystem. Never write to real `/tmp`
4. **PROCESS ISOLATION:** Each test file runs in its own process

### Anti-Patterns (DO NOT USE)

| Anti-Pattern | Why It's Bad |
|--------------|--------------|
| Inline mock factories | Collides with shared mock |
| `jest.isolateModules()` | Unnecessary with process isolation |
| `require()` inside tests | Use top-level imports |
| Real filesystem access | Flaky, non-deterministic |

### Template (TypeScript/Jest)

```typescript
/**
 * GOLD STANDARD (v3.0 - Process Isolation Era)
 */
import * as vscode from 'vscode'; // Uses tests/mocks/vscode.ts

describe('Feature Integration', () => {
  beforeEach(() => {
    // 1. CLEAN SLATE: Reset mock history
    jest.resetAllMocks();

    // 2. PATCH: Add specific capabilities
    (vscode.env as any).clipboard = {
      writeText: jest.fn().mockResolvedValue(undefined),
    };

    // 3. WORKSPACE: Set up context
    (vscode.workspace as any).workspaceFolders = [
      { uri: vscode.Uri.file('/test/workspace'), name: 'root' },
    ];
  });

  it('should execute feature flow', async () => {
    // ACT
    await MyFeature.execute();

    // ASSERT
    expect(vscode.window.showInformationMessage)
      .toHaveBeenCalledWith('Success');
  });
});
```

### Event Triggering (Testing Reactive Code)

The template above shows **state mocking** but not **event triggering**. Many features react to events (file save, editor change, config change). Here's how to test them:

```typescript
/**
 * GOLD STANDARD: Event-Driven Testing
 */
import * as vscode from 'vscode';

describe('Event-Driven Behavior', () => {
  let onDidSaveHandler: ((doc: vscode.TextDocument) => void) | undefined;
  let onDidChangeEditorHandler: ((editor: vscode.TextEditor | undefined) => void) | undefined;

  beforeEach(() => {
    jest.resetAllMocks();

    // Capture event handlers when registered
    (vscode.workspace.onDidSaveTextDocument as jest.Mock).mockImplementation(
      (handler) => {
        onDidSaveHandler = handler;
        return { dispose: jest.fn() };
      }
    );

    (vscode.window.onDidChangeActiveTextEditor as jest.Mock).mockImplementation(
      (handler) => {
        onDidChangeEditorHandler = handler;
        return { dispose: jest.fn() };
      }
    );
  });

  it('handles file save event', async () => {
    // ARRANGE: Initialize feature (registers event handlers)
    await MyFeature.activate();

    // ACT: Fire the event
    const mockDocument = {
      uri: vscode.Uri.file('/test/file.ts'),
      fileName: '/test/file.ts',
      languageId: 'typescript',
    } as vscode.TextDocument;

    onDidSaveHandler?.(mockDocument);

    // ASSERT: Feature reacted correctly
    expect(vscode.window.showInformationMessage)
      .toHaveBeenCalledWith('File saved: file.ts');
  });

  it('handles active editor change', async () => {
    // ARRANGE
    await MyFeature.activate();

    const mockEditor = {
      document: { uri: vscode.Uri.file('/test/new-file.ts') },
    } as vscode.TextEditor;

    // ACT
    onDidChangeEditorHandler?.(mockEditor);

    // ASSERT
    expect(someReactiveFunction).toHaveBeenCalledWith(mockEditor);
  });

  it('handles configuration change', async () => {
    let onDidChangeConfigHandler: ((e: vscode.ConfigurationChangeEvent) => void) | undefined;

    (vscode.workspace.onDidChangeConfiguration as jest.Mock).mockImplementation(
      (handler) => {
        onDidChangeConfigHandler = handler;
        return { dispose: jest.fn() };
      }
    );

    await MyFeature.activate();

    // ACT: Fire config change event
    onDidChangeConfigHandler?.({
      affectsConfiguration: (section: string) => section === 'mault.detectionLevel',
    } as vscode.ConfigurationChangeEvent);

    // ASSERT: Feature reloaded
    expect(MyFeature.isReloaded).toBe(true);
  });
});
```

### Event Flow Integration Tests

Event Flow tests validate that when components are wired together, the system behaves correctly end-to-end:

```
User Action → Framework Event → Extension Handler → Detection → Output
```

**Example Event Flows to Test:**

| Event | Test File | What It Validates |
|-------|-----------|-------------------|
| Config Change | `config-change-flow.test.ts` | Re-detection triggers on settings change |
| Document Save | `document-save-flow.test.ts` | File analysis runs on save |
| File Rename | `file-rename-flow.test.ts` | Naming violations update on rename |

**Event Flow Test Structure:**

```typescript
// tests/unit/event-flows/config-change-flow.test.ts
import * as vscode from '../../mocks/vscode';
import { setupEventCapture, fireConfigurationChange } from './event-flow-helpers';

beforeEach(() => {
  jest.clearAllMocks();  // Preserve mock implementations
  setupEventCapture();
});

describe('Configuration Change Event Flow', () => {
  it('should trigger re-detection when mault config changes', async () => {
    const redetectHandler = jest.fn();

    // 1. Register listener (simulating extension activation)
    vscode.workspace.onDidChangeConfiguration((e) => {
      if (e.affectsConfiguration('mault')) {
        redetectHandler();
      }
    });

    // 2. Fire config change event
    fireConfigurationChange(['mault.level']);

    // 3. Verify re-detection triggered
    expect(redetectHandler).toHaveBeenCalledTimes(1);
  });

  it('should NOT trigger for unrelated config changes', async () => {
    const redetectHandler = jest.fn();

    vscode.workspace.onDidChangeConfiguration((e) => {
      if (e.affectsConfiguration('mault')) {
        redetectHandler();
      }
    });

    // Fire unrelated config change
    fireConfigurationChange(['editor.fontSize']);

    // Should NOT trigger
    expect(redetectHandler).not.toHaveBeenCalled();
  });
});
```

**Event Flow Helpers:**

```typescript
// tests/unit/event-flows/event-flow-helpers.ts
import * as vscode from '../../mocks/vscode';

// Store captured listeners
const listeners = {
  configurationChange: [] as Array<(e: vscode.ConfigurationChangeEvent) => void>,
  documentSave: [] as Array<(doc: vscode.TextDocument) => void>,
  fileRename: [] as Array<(e: vscode.FileRenameEvent) => void>,
};

export function setupEventCapture() {
  // Capture configuration change listeners
  (vscode.workspace.onDidChangeConfiguration as jest.Mock).mockImplementation(
    (listener) => {
      listeners.configurationChange.push(listener);
      return { dispose: jest.fn() };
    }
  );

  // Capture document save listeners
  (vscode.workspace.onDidSaveTextDocument as jest.Mock).mockImplementation(
    (listener) => {
      listeners.documentSave.push(listener);
      return { dispose: jest.fn() };
    }
  );
}

export function fireConfigurationChange(sections: string[]) {
  const event = {
    affectsConfiguration: (section: string) =>
      sections.some((s) => s === section || s.startsWith(section + '.')),
  };
  listeners.configurationChange.forEach((listener) => listener(event));
}

export function fireDocumentSave(document: Partial<vscode.TextDocument>) {
  const doc = {
    uri: vscode.Uri.file('/test/file.ts'),
    fileName: '/test/file.ts',
    languageId: 'typescript',
    ...document,
  } as vscode.TextDocument;
  listeners.documentSave.forEach((listener) => listener(doc));
}
```

### Language-Agnostic Event Testing Patterns

| Language | Event Triggering Pattern |
|----------|--------------------------|
| **TypeScript** | Capture handler via `mockImplementation`, call directly |
| **Python** | Use `side_effect` to capture callback, invoke manually |

### Python Example (Event Testing)

```python
# tests/integration/test_event_handling.py
from unittest.mock import Mock, patch

class TestEventDrivenBehavior:
    def test_handles_file_save_event(self):
        # ARRANGE: Capture the event handler
        captured_handler = None

        def capture_handler(handler):
            nonlocal captured_handler
            captured_handler = handler
            return Mock()  # disposable

        with patch('vscode.workspace.onDidSaveTextDocument', side_effect=capture_handler):
            feature = MyFeature()
            feature.activate()

        # ACT: Fire the event
        mock_document = Mock(uri='/test/file.py', fileName='file.py')
        captured_handler(mock_document)

        # ASSERT
        assert feature.last_saved_file == 'file.py'
```

### Template (Python/pytest)

```python
"""
Gold Standard Integration Test (Python)
"""
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_database():
    """Shared mock for database adapter."""
    db = Mock()
    db.get_user.return_value = {"id": 1, "balance": 100}
    return db

@pytest.fixture
def mock_email():
    """Shared mock for email adapter."""
    return Mock()

class TestOrderProcessing:
    def test_successful_order(self, mock_database, mock_email):
        # ARRANGE
        order = {"user_id": 1, "total": 50}

        # ACT
        result = process_order(order, mock_database, mock_email)

        # ASSERT
        assert result.ok
        mock_email.send_confirmation.assert_called_once()
```

---

## Behavioral Detector Tests (Input/Output Verification)

### The Perception Gap

There's a critical blind spot in traditional testing pyramids:

| Layer | What It Tests | What It Misses |
|-------|---------------|----------------|
| **Unit Tests** | Logic works *if given data* | Whether the detector *perceives* the environment |
| **Event Flow** | The machine turns on when button pressed | Whether the diagnosis is correct |

**The Question No Test Answered:**
> "If I point this detector at a Python file in a nested folder, does it actually see it?"

This gap was discovered via production bugs where:
- Event Flow tests passed (system didn't crash) ✓
- Unit tests passed (logic works if given files) ✓
- **Feature failed** because glob patterns didn't match reality ✗

### The Solution: Behavioral Detector Tests

**Purpose:** Validate that detectors **perceive** the environment correctly and produce the expected diagnostics.

```
Unit Tests:  "Given these files, does the logic work?"     ← Assumes files are provided
Behavioral:  "Does the detector actually SEE these files?" ← Tests perception
Event Flow:  "Does the system wire together correctly?"    ← Tests orchestration
```

### Pattern: Cross-Language Test Workspaces

Use `describe.each` for cross-language coverage with realistic file structures:

```typescript
// tests/integration/detectors/naming-convention.behavioral.test.ts
describe.each(['typescript', 'python', 'go'])('NamingConventionDetector (%s)', (language) => {
  const testWorkspace = path.join(__dirname, `../../test-workspaces/naming-chaos/${language}`);

  describe('Files that SHOULD be flagged', () => {
    it('should detect camelCase file in snake_case directory', async () => {
      const diagnostics = await runDetector(testWorkspace);

      expect(diagnostics).toContainEqual(
        expect.objectContaining({
          file: expect.stringMatching(/badFileName\.(ts|py|go)$/),
          severity: DiagnosticSeverity.Warning
        })
      );
    });

    it('should detect files in deeply nested folders', async () => {
      // This catches glob pattern bugs — patterns must recurse correctly
      const diagnostics = await runDetector(testWorkspace);

      expect(diagnostics.map(d => d.file)).toContain(
        expect.stringMatching(/nested\/deep\/veryDeep\/violatingFile/)
      );
    });
  });

  describe('Files that SHOULD NOT be flagged', () => {
    it('should NOT flag validUserService file', async () => {
      const diagnostics = await runDetector(testWorkspace);

      expect(diagnostics.map(d => d.file)).not.toContain(
        expect.stringMatching(/valid_user_service/)
      );
    });

    it('should NOT flag files in excluded directories', async () => {
      const diagnostics = await runDetector(testWorkspace);

      expect(diagnostics.map(d => d.file)).not.toContain(
        expect.stringMatching(/node_modules|__pycache__|vendor/)
      );
    });
  });
});
```

### Three Critical Elements

| Element | Why It Matters | What It Prevents |
|---------|----------------|------------------|
| **Negative Case Testing** | Forces "SHOULD NOT be flagged" tests | False positive fatigue |
| **Cross-Language Iteration** | `describe.each(['typescript', 'python', 'go'])` | Glob pattern bugs |
| **Chaos Test Workspaces** | Nested folders, edge-case naming | Recursion bugs, pattern matching failures |

### Test Workspace Structure

```
test-workspaces/
├── naming-chaos/
│   ├── typescript/
│   │   ├── badFileName.ts           # SHOULD flag
│   │   ├── valid_user_service.ts    # SHOULD NOT flag
│   │   └── nested/
│   │       └── deep/
│   │           └── veryDeep/
│   │               └── violatingFile.ts  # SHOULD flag (tests recursion)
│   ├── python/
│   │   ├── BadFileName.py           # SHOULD flag
│   │   ├── valid_user_service.py    # SHOULD NOT flag
│   │   └── nested/deep/veryDeep/
│   │       └── violating_file.py    # SHOULD flag
│   └── go/
│       └── ...
```

### Cross-Platform Considerations

Behavioral tests should run on all target platforms in CI:

```yaml
# .github/workflows/ci.yml
jobs:
  behavioral-tests:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:behavioral
```

| Platform Issue | What It Catches | Example |
|----------------|-----------------|---------|
| Path separators | `\` vs `/` bugs | Windows paths in glob patterns |
| Case sensitivity | macOS/Windows case folding | `File.ts` vs `file.ts` |
| Line endings | CRLF vs LF | Text comparison failures |

### Python Example (Behavioral Testing)

```python
# tests/integration/detectors/test_naming_convention_behavioral.py
import pytest
from pathlib import Path

LANGUAGES = ['typescript', 'python', 'go']

@pytest.fixture(params=LANGUAGES)
def test_workspace(request):
    """Parameterized fixture for cross-language testing."""
    return Path(__file__).parent.parent / 'test-workspaces' / 'naming-chaos' / request.param

class TestNamingConventionBehavioral:
    def test_detects_camelcase_in_snake_case_directory(self, test_workspace, detector):
        """Files that SHOULD be flagged."""
        diagnostics = detector.run(test_workspace)

        flagged_files = [d.file for d in diagnostics]
        assert any('badFileName' in f or 'BadFileName' in f for f in flagged_files)

    def test_does_not_flag_valid_files(self, test_workspace, detector):
        """Files that SHOULD NOT be flagged."""
        diagnostics = detector.run(test_workspace)

        flagged_files = [d.file for d in diagnostics]
        assert not any('valid_user_service' in f for f in flagged_files)

    def test_detects_files_in_nested_folders(self, test_workspace, detector):
        """Catches glob pattern recursion bugs."""
        diagnostics = detector.run(test_workspace)

        flagged_files = [d.file for d in diagnostics]
        assert any('nested' in f and 'deep' in f for f in flagged_files)
```

---

## The Governance Layer (Foundation)

The Governance Layer validates that the tests themselves are reliable. It consists of four components:

| Component | What It Validates |
|-----------|-------------------|
| **Mock Integrity Test** | Mock implements all framework API methods |
| **Mock Signature Validation** | Mock signatures match framework TypeScript definitions |
| **Type-Safe Helpers** | Eliminates `as any` casts in test setup |
| **Any Ratchet** | `any` count can only decrease, never increase |

### Component 1: Mock Integrity Test

Validates that your mock implements all required methods of the real API.

```typescript
// tests/unit/governance/mock-integrity.test.ts
import * as MockVSCode from '../../mocks/vscode';

describe('Mock Integrity: VS Code API', () => {
  describe('vscode.window', () => {
    it('should have showInformationMessage', () => {
      expect(MockVSCode.window.showInformationMessage).toBeDefined();
      expect(typeof MockVSCode.window.showInformationMessage).toBe('function');
    });

    it('should have showQuickPick', () => {
      expect(MockVSCode.window.showQuickPick).toBeDefined();
      expect(typeof MockVSCode.window.showQuickPick).toBe('function');
    });

    // ... validate all methods used by your code
  });
});
```

### Component 2: Mock Signature Validation

Validates that mock function signatures match the real API signatures.

```typescript
// tests/unit/governance/mock-signature.test.ts
import * as MockVSCode from '../../mocks/vscode';

describe('Mock Signature Validation', () => {
  it('should match showQuickPick signature', () => {
    const mock = MockVSCode.window.showQuickPick;

    // Verify signature: accepts items, returns Thenable
    const result = mock(['item1', 'item2']);
    expect(result).toBeInstanceOf(Promise);
  });

  it('should match getConfiguration signature', () => {
    const mock = MockVSCode.workspace.getConfiguration;

    // Verify signature: accepts section, returns WorkspaceConfiguration
    const config = mock('mault');
    expect(config).toHaveProperty('get');
    expect(config).toHaveProperty('has');
    expect(config).toHaveProperty('update');
  });
});
```

### Component 3: Type-Safe Helpers

Eliminates `as any` casts in test setup by providing typed helper functions.

```typescript
// tests/mocks/helpers.ts
import * as vscode from './vscode';

/**
 * Type-safe clipboard mock
 */
export function mockClipboard(readText?: string) {
  const clipboard = {
    readText: jest.fn().mockResolvedValue(readText ?? ''),
    writeText: jest.fn().mockResolvedValue(undefined),
  };
  (vscode.env as { clipboard: typeof clipboard }).clipboard = clipboard;
  return clipboard;
}

/**
 * Type-safe configuration mock
 */
export function mockConfig(values: Record<string, unknown>) {
  const originalGet = vscode.workspace.getConfiguration;
  const mockGet = jest.fn((section?: string) => ({
    get: jest.fn((key: string, defaultValue?: unknown) => {
      const fullKey = section ? `${section}.${key}` : key;
      return values[fullKey] ?? defaultValue;
    }),
    has: jest.fn((key: string) => `${section}.${key}` in values),
    update: jest.fn(),
  }));

  (vscode.workspace as { getConfiguration: typeof mockGet }).getConfiguration = mockGet;
  return () => {
    (vscode.workspace as { getConfiguration: typeof originalGet }).getConfiguration = originalGet;
  };
}

/**
 * Type-safe QuickPick mock
 */
export function mockQuickPick<T extends vscode.QuickPickItem>(selectedItem: T | undefined) {
  (vscode.window.showQuickPick as jest.Mock).mockResolvedValue(selectedItem);
}
```

**Usage in Tests:**

```typescript
// Before (with `as any` - defeats TypeScript protection)
(vscode.env as any).clipboard = { readText: jest.fn() };

// After (type-safe - compiler enforces correct structure)
import { mockClipboard, mockConfig, mockQuickPick } from '../mocks/helpers';

beforeEach(() => {
  mockClipboard('copied text');
  mockConfig({ 'mault.level': 2 });
  mockQuickPick({ label: 'Option 1' });
});
```

---

## Mock Integrity Testing

### The Mock Drift Problem

When using shared mocks (e.g., `tests/mocks/vscode.ts`), the mock can diverge from the real API over time:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE MOCK DRIFT SPIRAL                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Month 1: Mock matches real API perfectly                          │
│        ↓                                                            │
│   Month 3: Real API adds new method `showInputBox`                  │
│        ↓                                                            │
│   Month 4: Mock unchanged — doesn't have `showInputBox`             │
│        ↓                                                            │
│   Month 5: Code uses `showInputBox`, tests pass (mock ignores it)   │
│        ↓                                                            │
│   RUNTIME CRASH IN PRODUCTION                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Problem:** Tests pass because the mock doesn't enforce the real API contract. Production crashes because the real API behaves differently.

### Defense: Mock Integrity Test

Create a dedicated test that validates your mock implements the real interface:

```typescript
// tests/unit/governance/mock-integrity.test.ts
import * as vscode from 'vscode';
import { mockVscode } from '../../mocks/vscode';

describe('Mock Integrity', () => {
  it('mock implements VS Code window API', () => {
    // TypeScript strict assignment check
    const _window: typeof vscode.window = mockVscode.window;
    expect(_window).toBeDefined();
  });

  it('mock implements VS Code workspace API', () => {
    const _workspace: typeof vscode.workspace = mockVscode.workspace;
    expect(_workspace).toBeDefined();
  });

  it('mock implements VS Code languages API', () => {
    const _languages: typeof vscode.languages = mockVscode.languages;
    expect(_languages).toBeDefined();
  });

  it('mock implements VS Code commands API', () => {
    const _commands: typeof vscode.commands = mockVscode.commands;
    expect(_commands).toBeDefined();
  });
});
```

**Why This Works:** TypeScript's strict assignment compatibility catches missing properties at compile time. If the real `vscode.window` adds a new method, the mock must implement it or the test fails.

### Language-Agnostic Patterns

| Language | Mock Integrity Pattern |
|----------|------------------------|
| **TypeScript** | Strict assignment compatibility (`const _x: RealType = mock`) |
| **Python** | Protocol/ABC conformance test (`isinstance(mock, Protocol)`) or `create_autospec` |

**Roadmap:** Go uses compile-time interface satisfaction (automatic). Java uses `@Override` annotation. Rust uses compile-time trait implementation.

### Python Example

```python
# tests/governance/test_mock_integrity.py
from typing import Protocol
from unittest.mock import Mock, create_autospec

class DatabaseProtocol(Protocol):
    def query(self, sql: str) -> list: ...
    def execute(self, sql: str) -> int: ...

def test_mock_implements_database_protocol():
    """Verify mock matches real interface using create_autospec."""
    # GOOD: create_autospec enforces interface conformance
    mock_db = create_autospec(DatabaseProtocol, instance=True)

    # These work - methods exist on the protocol
    mock_db.query("SELECT 1")
    mock_db.execute("INSERT INTO x VALUES (1)")

    # This raises AttributeError - method doesn't exist
    # mock_db.nonexistent_method()  # Fails!

def test_bare_mock_is_dangerous():
    """Demonstrate why bare Mock() is dangerous."""
    # BAD: bare Mock() accepts any method call (mock drift)
    mock_db = Mock()
    mock_db.nonexistent_method()  # Silently passes - BUG!
```

**Best Practice (Issue #1629):** Always use `create_autospec()` instead of bare `Mock()` to enforce interface conformance. This prevents mock drift where mocks accept methods that don't exist on the real service.

### When to Add Mock Integrity Tests

| Scenario | Add Mock Integrity Test? |
|----------|--------------------------|
| Mocking external framework (VS Code, React) | **Yes** — API changes frequently |
| Mocking internal interfaces | Optional — you control both sides |
| Mocking third-party libraries | **Yes** — library updates can break |
| Simple data mocks | No — no behavior to drift |

---

## Mutation Testing: Validating Test Quality

### The Problem with Coverage

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COVERAGE LIE                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   100% coverage ≠ Bug-free code                                     │
│                                                                     │
│   Example:                                                          │
│     function add(a, b) { return a + b; }                            │
│                                                                     │
│   Tautological test (100% coverage, catches nothing):               │
│     expect(add(1, 2)).toBe(add(1, 2));  // Always passes!           │
│                                                                     │
│   Mutation testing catches this:                                    │
│     Mutant: return a - b;  ← Test still passes? TEST IS WORTHLESS   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### How Mutation Testing Works

1. **Create Mutant:** Inject bug (e.g., change `+` to `-`)
2. **Run Tests:** Against mutated code
3. **Evaluate:**
   - Test fails → Mutant killed ✓ (test catches bugs)
   - Test passes → Mutant survives ✗ (test is weak)

### Mutation Score

| Score | Meaning | Action |
|-------|---------|--------|
| ≥ 70% | Tests catch most injected bugs | Good quality |
| 50-69% | Tests miss significant bugs | Improve tests |
| < 50% | Tests are nearly worthless | Rewrite tests |

### Tool Configuration

**StrykerJS (TypeScript/JavaScript):**
```json
{
  "mutate": ["src/**/*.ts", "!src/**/*.d.ts"],
  "testRunner": "jest",
  "reporters": ["html", "progress"],
  "thresholds": { "high": 80, "low": 60, "break": 50 }
}
```

**mutmut (Python):**
```ini
[mutmut]
paths_to_mutate=src/
tests_dir=tests/
runner=pytest
```

---

## The Disposable Test Principle

### AI-Generated Tests Are Scaffolding

In an AI-first development model, tests serve as **verification scaffolding**, not permanent artifacts.

**Rules:**
1. Do NOT "fix" broken AI tests during refactoring
2. DELETE the old test, regenerate for new logic
3. Tests that haven't caught a bug in 365 days are candidates for deletion
4. Governance validates test quality, not humans

### Why This Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TRADITIONAL vs. AI-FIRST                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   TRADITIONAL:                                                      │
│   • Tests are precious (human wrote them)                           │
│   • "Fix" tests when they break                                     │
│   • Maintain tests forever                                          │
│   • Test maintenance is 40% of dev time                             │
│                                                                     │
│   AI-FIRST:                                                         │
│   • Tests are cheap (AI regenerates in seconds)                     │
│   • Delete and regenerate when logic changes                        │
│   • Mutation testing validates quality automatically                │
│   • Human time spent on vision, not test maintenance                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Process Isolation (Non-Negotiable)

### Why This Matters

Without process isolation, tests can contaminate each other:
- Mock registry collisions
- Singleton state leakage
- Prototype pollution
- Heisenbugs that require human debugging

### The Rule

**ALL tests run in isolated processes. No `--runInBand` for unit tests.**

| Framework | Isolation Setting |
|-----------|-------------------|
| Jest | Default (parallel workers) |
| Vitest | Default (parallel workers) |
| pytest | `pytest-xdist` or default |

### Trade-off Accepted

| Metric | With Shared Process | With Isolation |
|--------|---------------------|----------------|
| Speed | ~45 seconds | ~2-3 minutes |
| Reliability | Flaky, requires debugging | Rock-solid |
| Human Required? | Yes (to debug) | **No** |

> **"Fast but wrong" is useless. We pay the speed cost for determinism.**

---

## TDD Setup Checklist

When setting up TDD for a new project (Step 5 of Production-Readiness):

### 1. Install Test Framework
```bash
# JavaScript/TypeScript
npm install --save-dev jest @types/jest ts-jest

# Python
pip install pytest pytest-cov
```

### 2. Create Directory Structure
```bash
mkdir -p tests/unit tests/integration tests/e2e
mkdir -p tests/mocks  # For shared mocks
```

### 3. Configure Coverage
```bash
# Add to package.json / pyproject.toml / Makefile
"test:coverage": "jest --coverage"
```

### 4. Add to CI/CD
```yaml
# .github/workflows/ci.yml
- name: Run Tests
  run: npm test

- name: Check Coverage
  run: npm run test:coverage
```

### 5. (Optional) Install Mutation Testing
```bash
# JavaScript/TypeScript
npm install --save-dev @stryker-mutator/core

# Python
pip install mutmut
```

---

## Behavioral Test Pairing Enforcement (#1666)

Issue #1666 adds **Layer 11** to the TypeScript pre-commit hooks, ensuring that perception-critical detector changes are always accompanied by behavioral tests.

### The Sentry Bug Lesson

The UC13 bug proved that unit tests and integration tests are not sufficient:

| Test Layer | Result | What It Missed |
|------------|--------|----------------|
| Unit Tests | ✅ Passed | Logic works *if given files* |
| Integration Tests | ✅ Passed | Components wire together |
| Production | ❌ Failed | Detector couldn't *see* nested Python files |

The glob pattern `**/*.py` was missing files in deeply nested directories. Behavioral tests would have caught this.

### Smart Scoping

The enforcement hook is **not black/white** — it targets perception-critical files only:

**Files that REQUIRE behavioral tests:**
```javascript
const PERCEPTION_CRITICAL = [
  '*Detector.ts',        // Core perception logic
  '*Analyzer.ts',        // File content analysis
  'globMatch.ts',        // Pattern matching (Sentry bug category)
];
```

**Files EXEMPT from requirement:**
```javascript
const EXEMPT = [
  'types.ts',            // Type definitions
  'constants.ts',        // Static values
  '*Throttler.ts',       // Timing, not perception
  '*Publisher.ts',       // Output, not perception
  '*Service.ts',         // Orchestration
];
```

### How It Works

```
Developer modifies src/services/detectors/NewDetector.ts
     ↓
Pre-commit Layer 11 runs (verify-behavioral-pairing.js)
     ↓
Is this a *Detector.ts file? → Yes, perception-critical
     ↓
Is it in behavioral-exemptions.json? → No, it's new
     ↓
Does tests/behavioral/ucXX-*.behavioral.test.ts exist? → No
     ↓
🚫 BLOCKED: "Perception-critical files require behavioral tests"
```

### Files

- `extension/scripts/governance/verify-behavioral-pairing.js` — Enforcement script
- `extension/behavioral-exemptions.json` — Legacy orphans (ratchet pattern)
- `extension/.pre-commit-config-ts.yaml` — Layer 11 hook

---

## Python Governance Layer (#1628, #1629)

The Python service has its own Governance Layer, achieving 10-layer pre-commit parity with TypeScript.

### Python Pre-commit Layers

| Layer | Hook | What It Validates |
|-------|------|-------------------|
| 1-4 | Style | trailing-whitespace, isort, black, flake8 |
| 5 | Logic | mypy (type checking) |
| 6 | Security | detect-secrets |
| 7 | Branch | branch-name-check |
| 8 | Architecture | SRP Size Guardrails (#1628) |
| 9 | Architecture | Duplicate Code Detection (#1628) |
| 10 | Testing | Mock Conformance (#1629) |

### Mock Conformance (#1629)

Python equivalent of TypeScript's Mock Integrity and Signature Validation:

```python
# BAD - bare Mock() accepts any method (mock drift)
mock = Mock()
mock.nonexistent_method()  # No error, silently passes

# GOOD - create_autospec enforces real interface
mock = create_autospec(UsageService, instance=True)
mock.nonexistent_method()  # Raises AttributeError
```

**Files:**
- `service/tests/conftest.py` — Uses `create_autospec` for all fixtures
- `service/tests/governance/test_mock_conformance.py` — Governance tests
- `service/scripts/ci/check_mock_conformance.py` — Pre-commit enforcement

---

## Summary

| Concept | Description |
|---------|-------------|
| **TDD** | Write test first, then code |
| **Red-Green-Refactor** | Fail → Pass → Clean |
| **Governance Layer** | Foundation that validates tests themselves (Mock Integrity + Signatures + Helpers) |
| **Pure Core** | Business logic with no I/O |
| **Gold Standard** | Integration test pattern with shared mocks |
| **Behavioral Detector Tests** | Validate detectors perceive the environment correctly (cross-language, cross-platform) |
| **Event Flow Tests** | Test full event → handler → output flows |
| **Mock Integrity** | Verify mocks implement all real API methods |
| **Mock Signature Validation** | Verify mock signatures match real API signatures |
| **Type-Safe Helpers** | Eliminate `as any` casts in test setup |
| **Mutation Testing** | Verify tests catch bugs, not just run code |
| **Disposable Tests** | Delete and regenerate, don't fix |
| **Process Isolation** | No shared state between test files |

---

## Related

- [RISING-TIDE.md](./RISING-TIDE.md) — Mock Tax philosophy (2x rule)
- [IRON-DOME.md](./IRON-DOME.md) — Type Safety philosophy
- [RATCHET-STRATEGY.md](./RATCHET-STRATEGY.md) — Quality baselines

---

*Part of the Mault Production-Readiness Kit*
