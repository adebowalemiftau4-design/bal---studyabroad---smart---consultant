
import streamlit as st
import pandas as pd

st.set_page_config(page_title="BAL Study Abroad Smart-Consultant", layout="wide")

st.title("🎓 BAL Study Abroad Smart-Consultant")
st.write("Helping Nigerians and international students navigate scholarships, admissions, and visa processes — all in one place.")

menu = st.sidebar.radio("📌 Navigate", [
    "Home",
    "Scholarships & Funding",
    "University Application Guidance",
    "Visa Policy Updates",
    "Document Checklist & Tracking"
])

if menu == "Home":
    st.subheader("Welcome 👋")
    st.write("This platform helps you manage your entire study-abroad journey with AI-driven guidance and tools.")

elif menu == "Scholarships & Funding":
    st.subheader("💰 Scholarships & Funding Opportunities")
    scholarships = [
        {"name": "Chevening Scholarships (UK)", "link": "https://www.chevening.org/scholarships/"},
        {"name": "Erasmus+ (EU)", "link": "https://erasmus-plus.ec.europa.eu/"},
        {"name": "DAAD Scholarships (Germany)", "link": "https://www.daad.de/en/study-and-research-in-germany/scholarships/"},
        {"name": "MEXT Scholarships (Japan)", "link": "https://www.studyinjapan.go.jp/en/"},
        {"name": "Mastercard Foundation Scholars Program", "link": "https://mastercardfdn.org/all/scholars/"}
    ]
    for s in scholarships:
        st.markdown(f"- [{s['name']}]({s['link']})")

elif menu == "University Application Guidance":
    st.subheader("🏫 Direct University Application Guidance")
    st.markdown("""
    1. Research universities and check entry requirements.
    2. Prepare transcripts, certificates, and recommendation letters.
    3. Draft a strong personal statement (SOP).
    4. Apply directly via university portals.
    5. Track your application progress.
    """)

elif menu == "Visa Policy Updates":
    st.subheader("🛂 Real-Time Visa Policy Updates")
    updates = [
        "🇬🇧 UK: Graduate Route Visa available for post-study work.",
        "🇨🇦 Canada: New intake cap for international students (2025).",
        "🇺🇸 USA: F1 visa interview wait times reduced in Lagos & Abuja.",
        "🇩🇪 Germany: Proof of funds requirement updated."
    ]
    for u in updates:
        st.markdown(f"- {u}")

elif menu == "Document Checklist & Tracking":
    st.subheader("📂 Document Checklist & Progress Tracking")
    checklist = {
        "Passport": False,
        "Academic Transcripts": False,
        "Degree Certificates": False,
        "Recommendation Letters": False,
        "Personal Statement/SOP": False,
        "Proof of Funds": False,
        "English Proficiency Test (IELTS/TOEFL)": False,
        "CV/Resume": False,
        "Visa Application Form": False
    }

    completed = 0
    for doc in checklist:
        if st.checkbox(doc):
            completed += 1

    st.progress(completed / len(checklist))
    st.write(f"✅ {completed} of {len(checklist)} documents completed")
