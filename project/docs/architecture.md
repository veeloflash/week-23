# System Architecture

## Key Design Decisions

- **Decision policy is deterministic (rule-based)**, not LLM-driven.
- **Planner** decomposes goals into ordered subtasks with dependencies.
- **Tool layer** is a local abstraction with schema definitions.
- **Memory** is per-user to prevent data leakage.
- **Reflection** records expected vs actual progress for auditability.
- **Security** uses heuristic keyword matching for injection detection.
- **Input validation** covers all fields at the system boundary.

## Limitations

- No LLM integration
- No remote API calls
- No concurrent write locking
- No production-grade security
- CLI-only interface