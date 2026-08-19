# Week 23 – Learning Workflow Agent (Full Product)

This project implements a complete Learning Workflow Agent with:

- AI Agent architecture  
- Workflow engine  
- Tool calling  
- Multi-step planning  
- Memory  
- Reflection  
- Security  
- Automated testing  
- CI pipeline  

It fully meets Week23 engineering requirements.

---

## 🚀 Features

- Dynamic decision-making  
- Real tool layer (study plan, progress, questions)  
- Adaptive learning plan adjustment  
- Memory persistence  
- Reflection-based improvement  
- Input validation & injection detection  
- Full test suite  
- GitHub Actions CI  

---

## 🧠 Architecture

User  
↓  
Input Validation  
↓  
Injection Detection  
↓  
Planner  
↓  
Decision Engine  
↓  
Tools  
↓  
Verification  
↓  
Memory Update  
↓  
Reflection  
↓  
Output

See `docs/architecture.md` for full details.

---

## 📂 Project Structure

```
project/
├── agent/
├── workflow/
├── tools/
├── memory/
├── security/
├── tests/
└── main.py
```

---

## 🧪 Testing

Run all tests:

```
python -m unittest discover -s project/tests
```

See `docs/testing_report.md` for full results.

---

## 🔐 Security

- Empty input rejection  
- Length validation  
- Prompt injection detection  
- Safe execution path  

---

## 💾 Memory

Stored in `memory/memory.json`:

- goal  
- completed tasks  
- total tasks  
- progress  
- previous plan  

---

## 🔄 Reflection

The agent evaluates previous performance and adjusts future plans.

---

## 🛠 CI Pipeline

GitHub Actions automatically runs tests on every push.

---

## 📈 Future Improvements

- Add web API  
- Add UI  
- Add more tools  
- Add advanced planning algorithms  

---

## ✔ Status

**Fully meets Week23 exit criteria.**