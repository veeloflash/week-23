# System Architecture

```text
CLI input -> validation and injection detection -> LearningAgent
	-> memory load -> progress -> decision and tool selection
	-> registry tool execution -> reflection -> memory save -> output
```

`DecisionEngine.decide()` retains the `intensive`, `normal`, and `advance` modes. `select_tools()` considers goal wording, current progress, previous plan, and weak topics. Progress is always selected; planning is selected for a new goal or missing plan; questions are selected for practice goals, low progress, or weak topics.

`ToolRegistry` maps names to tool instances and executes named methods. The progress, study-plan, and question tools receive runtime parameters. Optional tool failures are returned in `tool_errors`.

The agent loads prior progress, plan, weak topics, and reflection before selection. It reflects on current progress and saves the effective plan and feedback for the next run.

This is a local educational example. Decisions are deterministic, security detection is heuristic, memory is a JSON file without concurrent-write locking, and no remote authentication, retry, timeout, API, or UI exists.