# System Architecture

```text
CLI input (with user_id)
    ↓
Input parsing (protected by try/except)
    ↓
Input validation (goal, subject, hours, completed, total)
    ↓
Injection detection (heuristic keyword matching)
    ↓
Memory load (per-user: memory/<user_id>.json)
    ↓
Progress calculation
    ↓
Decision engine (rule-based: intensive / normal / advance)
    ↓
Planner (goal → ordered subtasks with dependencies)
    ↓
Tool selection (rule-based)
    ↓
Tool execution via registry (progress, study_plan, question, calculator)
    ↓
Reflection (expected vs actual, with adjustment)
    ↓
Memory save (per-user)
    ↓
Output
```

## Key Design Decisions

- **Decision policy is deterministic (rule-based)**, not LLM-driven.
  This is intentional for the Week23 educational prototype.
- **Planner** decomposes goals into ordered subtasks with dependencies.
- **Tool layer** is a local abstraction with schema definitions.
  The calculator tool demonstrates the tool-calling pattern.
- **Memory** is per-user to prevent data leakage.
- **Reflection** records expected vs actual progress for auditability.
- **Security** uses heuristic keyword matching for injection detection.
  This is a demonstration only, not a complete defense.
- **Input validation** covers all fields at the system boundary.

## Limitations

- No LLM integration
- No remote API calls
- No concurrent write locking
- No production-grade security
- CLI-only interface
