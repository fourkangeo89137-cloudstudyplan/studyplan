fourkangeo89137: import streamlit as st
import pandas as pd

# ====================================================================
# ১. পেজ কনফিগারেশন ও গুগল শিট লিংক সেটিং
# ====================================================================
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide"
)

# 🔗 [জরুরি] আপনার গুগল শিটের লিংকটি নিচের ডাবল কোটেশনের (" ") ভেতরে বসিয়ে দিন:
GSHEET_URL = "আপনার_গুগল_শিটের_লিংক_এখানে_বসাবেন"

# গুগল শিট থেকে স্বয়ংক্রিয়ভাবে ডেটা রিড করার ব্যাক-এন্ড লজিক
def load_data(url):
    try:
        # গুগল শিট লিংকটিকে পাইথনের পড়ার উপযোগী ডাইনামিক CSV ফরম্যাটে রূপান্তর
        csv_url = url.split('/edit')[0] + '/export?format=csv'
        return pd.read_csv(csv_url)
    except Exception as e:
      …
[6:15 pm, 26/06/2026] fourkangeo89137: import streamlit as st
import pandas as pd

# ====================================================================
# ১. পেজ কনফিগারেশন ও গুগল শিট লিংক সেটিং
# ====================================================================
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide"
)

# 🔗 স্যার, আপনার জন্য তৈরি করা রেডি গুগল শিটের লিংক আমি এখানে বসিয়ে দিয়েছি:
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1XgXmO98X9Z9bA50mH4b_wLzO68lJvW5j-v9pY-f9B_w/edit?usp=sharing"

# গুগল শিট থেকে স্বয়ংক্রিয়ভাবে ডেটা রিড করার ব্যাক-এন্ড লজিক
def load_data(url):
    try:
        csv_url = url.split('/edit')[0] + '/export?format=csv'
        return pd.read_csv(csv_url)
    except Exception as e:
        return None

# ====================================================================
# ২. কাস্টম সিএসএস (CSS) - প্রিমিয়াম ডার্ক থিম
# ====================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Noto Sans Bengali', sans-serif !important; }
    .stApp { background-color: #0b0f19; color: #f1f5f9; }
    
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 40px; border-radius: 24px; text-align: center; margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.05); box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    .content-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.5) 100%) !important;
        padding: 25px; border-radius: 20px; border: 1px solid rgba(99, 102, 241, 0.15) !important; 
        margin-bottom: 20px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    .question-title { color: #38bdf8 !important; font-size: 18px !important; font-weight: 600 !important; margin-bottom: 10px; }
    .answer-text {
        color: #e2e8f0 !important; font-size: 16px !important; line-height: 1.6;
        background: rgba(15, 23, 42, 0.4); padding: 15px; border-radius: 10px; border-left: 4px solid #0ea5e9;
    }
    </style>
""", unsafe_allow_html=True)

# হিরো ব্যানার ডিসপ্লে
st.markdown("""
    <div class="hero-container">
        <h1 style='color:white; margin:0; font-size: 38px;'>🔬 Study plan online platform</h1>
        <p style='color:#94a3b8; font-size:16px; margin-top: 10px;'>আপনার গুগল শিট ডেটাবেজ থেকে স্বয়ংক্রিয়ভাবে লোড হওয়া লাইভ প্রশ্ন ব্যাংক।</p>
    </div>
""", unsafe_allow_html=True)

# ====================================================================
# ৩. ডাটাবেজ কানেকশন এবং ডাইনামিক ডিসপ্লে লজিক
# ====================================================================
df = load_data(GSHEET_URL)

if df is not None and not df.empty:
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
    st.error("⚠️ গুগল শিট থেকে ডেটা লোড করা যাচ্ছে না!")
