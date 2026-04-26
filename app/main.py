import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import time
import hashlib

from backend.jd_parser import parse_jd
from backend.candidate_matcher import load_candidates, preprocess_candidates, score_all_candidates
from backend.resume_parser import parse_resume

CSV_PATH = "data/candidates_structured.csv"

st.set_page_config(page_title="AI Talent Scout", layout="wide")

st.markdown("""
<style>
body { background: #020617; color: white; }

.card {
    background: #0f172a;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.05);
}

.tag {
    display:inline-block;
    padding:6px 12px;
    margin:4px;
    border-radius:8px;
    font-size:12px;
}

.match { background:#064e3b; color:#34d399; }
.miss { background:#450a0a; color:#f87171; }

.hero {
    background: linear-gradient(135deg,#4f46e5,#9333ea);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
<h1>AI Talent Intelligence Platform</h1>
<p>Discover • Match • Engage • Rank candidates instantly</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
jd_input = st.text_area("📄 Job Description", height=150)
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
run_clicked = st.button("🚀 Run AI Agent")

def get_file_hash(file):
    return hashlib.md5(file.getvalue()).hexdigest()

if uploaded_file:

    file_hash = get_file_hash(uploaded_file)

    if "uploaded_hashes" not in st.session_state:
        st.session_state.uploaded_hashes = set()

    if file_hash not in st.session_state.uploaded_hashes:

        candidate = parse_resume(uploaded_file)

        if "error" not in candidate:

            new_row = pd.DataFrame([{
                "id": int(time.time()),
                "name": candidate.get("name", "Unknown"),
                "role": candidate.get("role", ""),
                "experience_years": candidate.get("experience_years", 0),
                "skills_required": ";".join(candidate.get("skills_required", [])),
                "skills_preferred": ";".join(candidate.get("skills_preferred", [])),
                "tools_technologies": ";".join(candidate.get("tools_technologies", [])),
                "soft_skills": ";".join(candidate.get("soft_skills", [])),
                "seniority_level": candidate.get("seniority_level", "")
            }])

            if not os.path.exists(CSV_PATH):
                new_row.to_csv(CSV_PATH, index=False)
            else:
                new_row.to_csv(CSV_PATH, mode="a", header=False, index=False)

            st.session_state.uploaded_hashes.add(file_hash)
            st.success("✅ Resume added to candidate pool")

        else:
            st.error("Resume parsing failed")

    else:
        st.info("⚠️ This resume is already added")

# ---------------- AI THINKING ----------------
def ai_thinking():
    steps = [
        "🔍 Parsing JD...",
        "🧠 Extracting skills...",
        "📊 Matching...",
        "💬 Evaluating interest...",
        "🏆 Ranking..."
    ]
    placeholder = st.empty()
    for s in steps:
        placeholder.info(s)
        time.sleep(0.5)
    placeholder.success("✅ Done!")

# ---------------- TAG RENDER ----------------
def render_tags(items, cls):
    if not items:
        return
    html = ""
    for i in items:
        html += f"<span class='tag {cls}'>{i}</span>"
    st.markdown(html, unsafe_allow_html=True)

# ---------------- MAIN ----------------
if run_clicked:

    if not jd_input:
        st.warning("Enter JD")
    else:
        ai_thinking()

        jd = parse_jd(jd_input)
        df = preprocess_candidates(load_candidates())
        results = score_all_candidates(jd, df)

        st.markdown("## 🏆 Top Candidates")

        for i, r in enumerate(results[:5]):

            st.markdown(f"""
            <div class="card">
            <h3>#{i+1} {r['name']}</h3>
            <p>{r.get('role','-')} • {r.get('experience_years','-')} yrs</p>
            <h2>{r.get('final_score',0)} | {r.get('recommendation','')}</h2>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            # -------- LEFT --------
            with col1:
                st.subheader("📊 Match Scores")

                st.progress(r.get("skill_score",0)/100)
                st.caption(f"Skills: {r.get('skill_score',0)}%")

                st.progress(r.get("tool_score",0)/100)
                st.caption(f"Tools: {r.get('tool_score',0)}%")

                st.progress(r.get("experience_score",0)/100)
                st.caption(f"Experience: {r.get('experience_score',0)}%")

            with col2:
                st.subheader("💬 Engagement")

                st.metric("Score", r.get("interest_score",0))

                for reason in r.get("engagement_reasons", []):
                    st.markdown(f"✔ {reason}")

            st.subheader("🧠 Match Analysis")

            st.write(r.get("match_explanation",""))

            colA, colB = st.columns(2)

            with colA:
                st.markdown("**✔ Matching Skills**")
                render_tags(r.get("matched_skills", []), "match")

            with colB:
                st.markdown("**❌ Missing Skills**")
                render_tags(r.get("missing_skills", []), "miss")