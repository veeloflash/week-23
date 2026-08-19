# Week 23 – System Architecture

This document describes the architecture of the Learning Workflow Agent.

---

## 🧠 High-Level Architecture

User  
↓  
Input Validation  
↓  
Injection Detection  
↓  
Goal Interpreter  
↓  
Planner  
↓  
Decision Engine  
↓  
Tool Layer  
├─ StudyPlanTool  
├─ ProgressTool  
└─ QuestionTool  
↓  
Verification  
↓  
Memory Update  
↓  
Reflection  
↓  
Output

---

## 📂 Directory Structure

```
project/
├── agent/
│   ├── decision_engine.py
│   ├── learning_agent.py
│   └── reflection.py
│
├── workflow/
│   ├── planner.py
│   ├── workflow_engine.py
│   └── verifier.py
│
├── tools/
│   ├── progress_tool.py
│   ├── study_plan_tool.py
│   └── question_tool.py
│
├── memory/
│   ├── memory_manager.py
│   └── memory.json
│
├── security/
│   ├── validator.py
│   └── injection_detector.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_tool_selection.py
│   ├── test_workflow.py
│   ├── test_memory.py
│   ├── test_plan_adjustment.py
│   └── test_security.py
│
└── main.py
```

---

## 🔧 Component Responsibilities

### **1. Input Validation**
Rejects empty or overly long input.

### **2. Injection Detection**
Blocks prompt injection attempts.

### **3. Planner**
Breaks goal into tasks.

### **4. Decision Engine**
Chooses workflow based on progress.

### **5. Tools**
- ProgressTool → calculates progress  
- StudyPlanTool → generates plan  
- QuestionTool → provides questions  

### **6. Memory**
Stores previous plan, progress, tasks.

### **7. Reflection**
Evaluates previous performance and adjusts.

---

## 📌 Architecture Notes

- Fully modular  
- Testable  
- Extensible  
- Follows Week23 requirements  
- Supports adaptive planning  
- Includes security and memory  