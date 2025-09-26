import streamlit as st
import pandas as pd
# ========================
# BAL Study Abroad Smart-Consultant
# ========================

st.set_page_config(page_title="BAL Study Abroad Smart-Consultant", layout="wide")

st.title("🎓 BAL Study Abroad Smart-Consultant")
st.markdown("Helping Nigerians and international students navigate scholarships, admissions, and visa processes — all in one place.")

# Sidebar navigation
menu = st.sidebar.radio("📌 Navigate", [
    "Home",
    "Scholarships & Funding",
    "University Application Guidance",
    "Visa Policy Updates",
    "Document Checklist & Tracking"
])

# ========== HOME ==========
if menu == "Home":
    st.subheader("Welcome 👋")
    st.write("This platform helps you manage your entire study-abroad journey with AI-driven guidance and tools.")

# ========== SCHOLARSHIPS ==========
elif menu == "Scholarships & Funding":
    st.subheader("💰 Scholarships & Funding Opportunities")
    st.write("Here you’ll find curated scholarships and funding programs for Nigerians & international students.")
    scholarships = [
        {"name": "Chevening Scholarships (UK)", "link": "https://www.chevening.org/scholarships/"},
        {"name": "Erasmus+ (EU)", "link": "https://erasmus-plus.ec.europa.eu/"},
        {"name": "DAAD Scholarships (Germany)", "link": "https://www.daad.de/en/study-and-research-in-germany/scholarships/"},
        {"name": "MEXT Scholarships (Japan)", "link": "https://www.studyinjapan.go.jp/en/"},
        {"name": "Mastercard Foundation Scholars Program", "link": "https://mastercardfdn.org/all/scholars/"}
    ]
    for s in scholarships:
        st.markdown(f"- [{s['name']}]({s['link']})")

# ========== APPLICATION GUIDANCE ==========
elif menu == "University Application Guidance":
    st.subheader("🏫 Direct University Application Guidance")
    st.write("Step-by-step guide on preparing your applications:")
    st.markdown("""
    1. Research your preferred universities and confirm entry requirements.
    2. Prepare academic transcripts, certificates, and recommendation letters.
    3. Draft a strong personal statement/statement of purpose (use AI assistance if needed).
    4. Apply directly via the university’s online portal.
    5. Track your application and deadlines here.
    """)

# ========== VISA UPDATES ==========
elif menu == "Visa Policy Updates":
    st.subheader("🛂 Real-Time Visa Policy Updates")
    st.write("Stay updated with the latest visa rules and policies. (This section can later pull data from APIs.)")
    updates = [
        "🇬🇧 UK: Graduate Route Visa remains available for post-study work.",
        "🇨🇦 Canada: New cap announced for international student intake (2025).",
        "🇺🇸 USA: F1 visa interview wait times reduced in Lagos & Abuja.",
        "🇩🇪 Germany: Proof of funds requirement for blocked account updated."
    ]
    for u in updates:
        st.markdown(f"- {u}")

# ========== DOCUMENT CHECKLIST ==========
elif menu == "Document Checklist & Tracking":
    st.subheader("📂 Document Checklist & Progress Tracking")
    st.write("Mark your documents as complete to stay on track.")

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

    for doc in checklist:
        checklist[doc] = st.checkbox(doc)

    st.success(f"✅ You have completed {sum(checklist.values())}/{len(checklist)} documents!")
