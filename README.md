# Week 23 – Deterministic Learning Workflow Agent Prototype

This project implements a **Deterministic Learning Workflow Agent** that demonstrates
the core architecture of an AI learning agent:

- Agent architecture (goal → plan → execute → reflect)
- Workflow engine with multi-step planning
- Tool calling via local tool abstraction layer
- Memory persistence (per-user)
- Reflection with expected/actual comparison
- Security (heuristic demonstration only)
- Automated testing
- CI pipeline

**Important**: Decision policy is currently **rule-based (deterministic)**, not LLM-driven.
This prototype validates Agent architecture and workflow orchestration for Week23.
It does **not** implement autonomous LLM reasoning or dynamic planning from natural-language goals.

---

## Features

- Deterministic decision-making (rule-based policy)
- Local tool abstraction / simulated tool-calling layer (study plan, progress, questions, calculator)
- Multi-step planning (goal decomposition into ordered subtasks)
- Adaptive learning plan adjustment
- Per-user memory persistence
- Reflection with expected vs actual comparison
- Input validation & heuristic injection detection
- Full test suite
- GitHub Actions CI

---

## Architecture

```
User Input
    ↓
Input Validation (all fields)
    ↓
Injection Detection (heuristic)
    ↓
Planner (goal → ordered subtasks)
    ↓
Decision Engine (rule-based)
    ↓
Tool Selection
    ↓
Tool Execution (via registry)
    ↓
Reflection (expected vs actual)
    ↓
Memory Update (per-user)
    ↓
Output
```

See `project/docs/architecture.md` for full details.

---

## Project Structure

```
project/
├── agent/
│   ├── learning_agent.py
│   ├── decision_engine.py
│   ├── planner.py          # Multi-step planner
│   └── reflection.py
├── tools/
│   ├── registry.py
│   ├── progress_tool.py
│   ├── study_plan_tool.py
│   ├── question_tool.py
│   └── calculator_tool.py  # External tool with schema
├── memory/
│   └── memory_manager.py   # Per-user memory (<user_id>.json)
├── security/
│   ├── validator.py
│   └── injection_detector.py
├── tests/
├── docs/
└── main.py
```

---

## Testing

Run all tests:

```bash
python -m unittest discover -s project/tests
```

See `project/docs/testing_report.md` for full results.

---

## Security

- Empty input rejection
- Length validation
- Numeric range validation (hours, completed, total)
- Prompt injection detection (**heuristic demonstration only**, not a complete defense)
- Safe execution path

**Note**: The injection detector uses keyword matching and is for educational purposes only.
Real security boundaries rely on restricted tools, parameter validation, and permission checks.

---

## Memory

Stored per-user in `memory/<user_id>.json`:

- goal
- completed tasks
- total tasks
- progress
- previous plan
- weak topics
- previous reflection

---

## Reflection

The agent compares expected vs actual progress and records:
- Expected progress
- Actual progress
- Difference
- Previous decision
- Adjustment action

---

## CI Pipeline

GitHub Actions automatically runs tests on every push.

---

## Status

Meets the core educational architecture requirements for a local Week23 prototype;
not production-ready. Decision policy is deterministic (rule-based); no LLM integration.
