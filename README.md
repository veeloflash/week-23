# Week 23 - Deterministic Learning Workflow Agent Prototype

This project implements a **Deterministic Learning Workflow Agent** that demonstrates
the core architecture of an AI learning agent:

- Agent architecture (goal -> plan -> execute -> reflect)
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
- Local tool abstraction / simulated tool-calling layer
- Multi-step planning (goal decomposition into ordered subtasks)
- Adaptive learning plan adjustment
- Per-user memory persistence
- Reflection with expected vs actual comparison
- Input validation & heuristic injection detection
- Full test suite
- GitHub Actions CI

---

## Testing

```bash
python -m unittest discover -s project/tests
```

---

## Security

- Empty input rejection
- Length validation
- Numeric range validation
- Prompt injection detection (**heuristic demonstration only**)
- Safe execution path

**Note**: The injection detector uses keyword matching for educational purposes only.

---

## Memory

Stored per-user in `memory/<user_id>.json`

---

## Status

Meets the core educational architecture requirements for a local Week23 prototype;
not production-ready. Decision policy is deterministic (rule-based); no LLM integration.