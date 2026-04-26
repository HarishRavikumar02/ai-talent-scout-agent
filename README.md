# 🚀 AI-Powered Talent Scouting & Engagement Agent

An end-to-end AI recruiting system that automates candidate discovery, matching, engagement estimation, and ranking — enabling recruiters to make faster, data-driven hiring decisions with full transparency.

---

## 🎯 Problem

Recruiters spend significant time:
- Manually screening resumes  
- Comparing inconsistent skill formats  
- Evaluating candidate fit  
- Following up to assess interest  

This leads to:
- Slow hiring cycles  
- Missed qualified candidates  
- Lack of explainability in decisions  

---

## 💡 Solution

This project builds an AI agent that:

1. Parses job descriptions into structured data  
2. Ingests resumes and converts them into structured profiles  
3. Normalizes skills across inconsistent representations  
4. Matches candidates using multi-dimensional scoring  
5. Simulates engagement to estimate candidate interest  
6. Produces a ranked shortlist with clear explanations  

---

## ⚙️ Core Features

### 🧠 Job Description Parsing
- Extracts role, skills, tools, experience, and seniority  
- Converts unstructured text into structured format  

---

### 📄 Resume Parsing
- Upload PDF resumes  
- Extract structured candidate information using AI  
- Automatically adds candidates to the database  

---

### 🔄 Skill Normalization Engine (Key Innovation)

Handles real-world inconsistencies:

| Input | Normalized |
|------|-----------|
| ReactJS | react |
| CSS3 | css |
| ML | machine learning |
| NLP | natural language processing |

**Techniques used:**
- Canonical mapping  
- Rule-based cleaning  
- Fuzzy matching  

---

### 🎯 Multi-Dimensional Matching

Each candidate is evaluated across:

- Skill match  
- Tool alignment  
- Soft skills  
- Experience fit  
- Role similarity  

---

### 💬 Engagement Simulation

- Simulates candidate responses  
- Generates **Interest Score**  
- Captures response quality and availability  

---

### 🧠 Explainable AI

For every candidate:

- ✔ Matching skills  
- ❌ Missing skills  
- 📊 Score breakdown  
- 🧠 Human-readable explanation  

---

### 🏆 Ranking & Recommendation

Final score combines:
- Match Score  
- Engagement Score  

Recommendations:
- 🟢 Strong Hire  
- 🟡 Consider  
- 🔴 Reject  

---

## 🧱 Architecture
```
Job Description → JD Parser (LLM)
            ↓
Resume Upload → Resume Parser (LLM)
            ↓
  Skill Normalization Engine
            ↓
  Matching & Scoring Engine
            ↓
  Engagement Simulation
            ↓
  Ranking + Explanation
            ↓
      Streamlit UI
```
The system follows a modular pipeline architecture with independent components for parsing, normalization, scoring, and explainability.

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- LLM API (OpenAI / Grok)  
- Pandas  
- PyMuPDF  
- Difflib (fuzzy matching)  


---

## ▶️ How to Run

### 1. Clone repo
```
git clone <your-repo-url>
cd ai-talent-scout-agent
```

---

### 2. Create virtual environment
```
python -m venv venv
source venv/bin/activate # Mac/Linux
```
---

### 3. Install dependencies
```
pip install -r requirements.txt
```
---

### 4. Setup API key

Create a `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the app
```
streamlit run app/main.py
```

---

## 📊 Example Workflow

1. Paste a Job Description  
2. Upload a Resume  
3. Click **Run AI Agent**  
4. View:
   - Ranked candidates  
   - Match scores  
   - Engagement score  
   - Skill gap analysis  
   - Hiring recommendation  

---

## 🧠 Key Innovations

- Unified schema for JD and resume  
- Skill normalization across domains  
- Explainable AI for hiring decisions  
- Engagement-aware ranking  
- End-to-end automated pipeline  

---

## 🚀 Future Improvements

- Semantic matching using embeddings  
- Real-time candidate outreach  
- ATS integrations  
- Feedback learning loop  
- Candidate comparison dashboard  

---

## 👤 Author

**Harish Ravikumar**

---

## 📌 Note

For security, API keys are not included.  
Use `.env` file to configure your own API key.
