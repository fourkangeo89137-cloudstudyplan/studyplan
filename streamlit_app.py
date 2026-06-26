import streamlit as st

# ১. বিশ্বমানের ও রেসপনসিভ পেজ কনফিগারেশন
st.set_page_config(
    page_title="Fourkan's Science Platform", 
    page_icon="🔬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ২. কাস্টম সিএসএস (CSS) - আন্তর্জাতিক মানের লাক্সারি ও আধুনিক ডিজাইন
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans Bengali', sans-serif !important;
    }
    
    /* ব্যাকগ্রাউন্ড ও গ্লোবাল স্টাইল */
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    
    /* গ্লাস-মরফিজম হিরো ব্যানার */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 60px 40px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 40px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        color: #ffffff !important;
        font-size: 42px !important;
        font-weight: 700 !important;
        margin-bottom: 15px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 19px !important;
        font-weight: 300;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* প্রফেশনাল কার্ড ডিজাইন */
    .content-card {
        background: rgba(30, 41, 59, 0.4);
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(8px);
        margin-top: 15px;
    }
    
    /* সাইডবার মডিফিকেশন */
    section[data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ৩. মডার্ন ও দৃষ্টিনন্দন হিরো ব্যানার
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🔬 ফিজিক্স ও কেমিস্ট্রি ডিজিটাল প্ল্যাটফর্ম</div>
        <div class="hero-subtitle">বিজ্ঞানকে গভীরভাবে অনুধাবন করার একটি আধুনিক ও বিশ্বমানের আঙিনা। এখানে কোনো মুখস্থ বিদ্যা নেই, শান্ত মাথায় আমরা শিখব প্রকৃতির আসল মেকানিজম।</div>
    </div>
""", unsafe_allow_html=True)

# ৪. সাইডবার লেআউট
with st.sidebar:
    st.markdown("### 📚 পাঠ্যক্রম নির্দেশক")
    st.write("তোমার কাঙ্ক্ষিত অধ্যায়টি নির্বাচন করো:")
    
    selected_chapter = st.radio(
        "",
        [
            "০১. রসায়নের ধারণা",
            "০২. পদার্থের অবস্থা",
            "০৩. পদার্থের গঠন",
            "০৪. পর্যায় সারণি",
            "০৫. রাসায়নিক বন্ধন",
            "০৬. মোলের ধারণা ও রাসায়নিক গণনা"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("✨ Designed for Conceptual Excellence")

# ৫. মূল কন্টেন্ট এরিয়া
st.markdown(f"## 📖 {selected_chapter}")

tab1, tab2, tab3 = st.tabs(["🎯 মূল পাঠ্যবই ও কনসেপ্ট", "🎥 ভিডিও ও অ্যানিমেশন", "📝 সেলফ অ্যাসেসমেন্ট"])

with tab1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.info("💡 এই সেকশনে আপনার নিজের কন্টেন্ট বা ক্লাস নোট সুন্দরভাবে ফুটে উঠবে। কোনো ডেমো টেক্সট রাখা হয়নি।")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("##### 🎬 ভিজ্যুয়াল লার্নিং সেকশন")
    st.caption("ভবিষ্যতে আপনার তৈরি করা পাইথন (Manim) অ্যানিমেশন ও ভিডিওগুলো এখানে যুক্ত হবে।")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("##### 📝 কুইজ ও মূল্যায়ন")
    st.caption("শিক্ষার্থীদের অনুশীলনের জন্য আধুনিক প্রশ্নব্যাংক এখানে সাজানো থাকবে।")
    st.markdown('</div>', unsafe_allow_html=True)
