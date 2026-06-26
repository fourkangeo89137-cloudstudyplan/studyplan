import streamlit as st

# ১. বিশ্বমানের ও রেসপনসিভ পেজ কনফিগারেশন
st.set_page_config(
    page_title="Fourkan's Science Platform", 
    page_icon="🔬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ২. কাস্টম সিএসএস (CSS) - প্রিমিয়াম টাইপোগ্রাফি ও গ্লাস ইফেক্ট
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans Bengali', sans-serif !important;
    }
    
    /* মূল ব্যানার ডিজাইন */
    .hero-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        margin-bottom: 40px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        color: #ffffff !important;
        font-size: 38px !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #94a3b8 !important;
        font-size: 18px !important;
        font-weight: 300;
    }
    
    /* কার্ড এবং সেকশন ডিজাইন */
    .content-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# ৩. মডার্ন ও দৃষ্টিনন্দন হিরো ব্যানার
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🔬 ফিজিক্স ও কেমিস্ট্রি ডিজিটাল প্ল্যাটফর্ম</div>
        <div class="hero-subtitle">বিজ্ঞানকে গভীরভাবে অনুধাবন করার একটি আধুনিক ও বিশ্বমানের আঙিনা</div>
    </div>
""", unsafe_allow_html=True)

# ৪. সাইডবার লেআউট - অত্যন্ত ক্লিন নেভিগেশন
with st.sidebar:
    st.markdown("### 📚 পাঠ্যক্রম নির্দেশক")
    st.write("তোমার কাঙ্ক্ষিত অধ্যায়টি নির্বাচন করো:")
    
    # ১ম ৬টি অধ্যায় সম্পূর্ণ উন্মুক্ত ও বাণিজ্যিক লেবেল ছাড়া
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

# ৫. মূল কন্টেন্ট এরিয়া - ইন্টারফেস সাজানো
st.markdown(f"## 📖 {selected_chapter}")

# এখানে শিক্ষার্থীরা লেকচার, অ্যানিমেশন ও কন্টেন্ট দেখার জন্য মডার্ন ট্যাব লেআউট
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
