# 🩺 AI Based Patient Monitor (ICU Agentic AI System)

## 📌 Overview

AI Based Patient Monitor is a Streamlit-powered ICU monitoring prototype that analyzes patient vital signs using an LLM (GPT-4o) to:

- Detect abnormalities in real-time
- Diagnose patient condition
- Determine urgency level (Stable / Urgent / Emergency)
- Suggest ICU nurse actions
- Trigger emergency alerts
- Provide AI observability metrics (token usage + latency)

This project demonstrates Retrieval-Augmented Generation (RAG), Agentic AI behavior, and AI telemetry monitoring.

---

## 🧠 Key Features

### ✅ 1. RAG-Based Patient Monitoring
The application uses real ICU patient data in CSV format as the knowledge source (RAG).  
Each file contains 60 minutes of minute-by-minute vitals:

- patient_id
- timestamp
- ECG
- heart_rate_bpm
- temperature_c
- bp_systolic_mmHg
- bp_diastolic_mmHg
- spo2_percent

---

### ✅ 2. Patient Scenarios Included

| Patient | Condition Simulated | Abnormal Pattern |
|----------|--------------------|------------------|
| Patient 1 | Sepsis-like deterioration | Fever + Tachycardia + Hypotension + Mild Hypoxemia |
| Patient 2 | Arrhythmia episode | Suspected V-Tach segment |
| Patient 3 | Progressive respiratory failure | Declining SpO₂ trend |

Each dataset includes abnormal events requiring ICU nurse intervention.

---

### ✅ 3. Agentic AI Behavior

The system does NOT rely on hardcoded rules.

Instead, GPT-4o:
- Analyzes patient vitals
- Determines urgency
- Suggests real clinical actions
- Recommends:
  - Verify readings
  - Notify physician
  - Activate rapid response
  - Initiate CPR
  - Prepare life-saving drugs (as appropriate)

🚨 If Emergency is detected, flashing red alert is displayed.

---

### ✅ 4. AI Observability

The application tracks AI telemetry:

- Input/Output token usage
- Total tokens consumed
- LLM response latency

This enables transparency and monitoring of AI performance.

---

## 🏗 AI Architecture

### Workflow:

ICU Patient CSV Data
↓
Streamlit App (UI Layer)
↓
AI Agent (GPT-4o via OpenAI API)
↓
Diagnosis + Suggested Actions
↓
Emergency Alert + Observability Metrics


Architecture Diagram included in repository:
`architecture.png`

---

## 🚀 How to Run the App

### Step 1: Install Python 3

Check version:

```bash
python3 --version
```
Step 2: Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

Step 3: Install Dependencies
```bash
pip install streamlit openai pandas
```

Step 4: Set OpenAI API Key
Mac/Linux:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

Windows:

setx OPENAI_API_KEY "your_api_key_here"

Step 5: Run the App
```bash
python3 -m streamlit run streamlit_app.py
```

Open:

http://localhost:8501
Upload any patient CSV file to test diagnosis.

📊 AI Observability Example
When running, the app displays:

⏱ Latency (seconds)

🔢 Total Tokens Used

This demonstrates AI telemetry tracking.


## 🎥 Demo Video

Click below to watch the full working demo of the AI Based Patient Monitor:

[▶ Watch Demo Video on YouTube](https://www.youtube.com/watch?v=K_3IfPqq5Ec)

```
📂 Repository Structure
AI_Patient_Monitor/
│
├── patient1_sepsis.csv
├── patient2_arrhythmia.csv
├── patient3_respiratory_failure.csv
├── streamlit_app.py
├── architecture.png
└── README.md
```
