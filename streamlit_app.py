import streamlit as st
import pandas as pd

# ১. পেজ কনফিগারেশন
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide"
)

# ২. রেডি গুগল শিট লিংক (সরাসরি বসিয়ে দেওয়া হয়েছে)
GSHEET_URL = "study_data.csv"

def load_data(url):
    try:
        
        return pd.read_csv(url)
    except:
        return None

# ৩. কাস্টম ডিজাইন (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Noto Sans Bengali', sans-serif !important; }
    .stApp { background-color: #0b0f19; color: #f1f5f9; }
    
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 40px; border-radius: 24px; text-align: center; margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .content-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.5) 100%) !important;
        padding: 25px; border-radius: 20px; border: 1px solid rgba(99, 102, 241, 0.15) !important; margin-bottom: 20px;
    }
    .question-title { color: #38bdf8 !important; font-size: 18px !important; font-weight: 600 !important; }
    .answer-text {
        color: #e2e8f0 !important; font-size: 16px !important;
        background: rgba(15, 23, 42, 0.4); padding: 15px; border-radius: 10px; border-left: 4px solid #0ea5e9;
    }
    </style>
""", unsafe_allow_html=True)

# হিরো ব্যানার
st.markdown("""
    <div class="hero-container">
        <h1 style='color:white; margin:0;'>🔬 Study plan online platform</h1>
        <p style='color:#94a3b8; font-size:16px;'>গুগল শিট ডেটাবেজ দ্বারা চালিত লাইভ প্ল্যাটফর্ম।</p>
    </div>
""", unsafe_allow_html=True)

# ৪. ডাটা ডিসপ্লে লজিক
df = load_data(GSHEET_URL)

if df is not None:
    st.markdown("### 🎯 রসায়ন ১ম অধ্যায়: গুরুত্বপূর্ণ ছোট প্রশ্নসমূহ")
    
    for index, row in df.iterrows():
        q_type = row.get('type', '💡 প্রশ্ন')
        q_text = row.get('question', 'প্রশ্ন পাওয়া যায়নি')
        a_text = row.get('answer', 'উত্তর পাওয়া যায়নি')
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f'<p class="question-title">{q_type}: {q_text}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="answer-text"><b>উত্তর:</b> {a_text}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error("⚠️ ডাটা লোড করা যাচ্ছে না।")
