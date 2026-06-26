import streamlit as st

# ১. আপনার অফিশিয়াল ব্র্যান্ড নামে পেজ কনফিগারেশন
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ২. কাস্টম সিএসএস (CSS) - আল্ট্রা-মডার্ন লাক্সারি ডিজাইন
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
        padding: 50px 40px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 35px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
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
    
    /* আল্ট্রা-প্রফেশনাল গ্লাস কার্ড ডিজাইন */
    .content-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.5) 100%) !important;
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        backdrop-filter: blur(10px);
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .content-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(99, 102, 241, 0.1);
    }
    
    /* বিশ্বমানের সাইডবার মডিফিকেশন */
    section[data-testid="stSidebar"] {
        background-color: #090d16 !important;
        border-right: 1px solid rgba(99, 102, 241, 0.15);
    }
    
    div[data-testid="stSidebarUserContent"] {
        padding-top: 20px;
    }
    
    /* রেডিও বাটনের প্রিমিয়াম রূপান্তর */
    div[data-testid="stRadio"] > label {
        color: #6366f1 !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        margin-bottom: 12px;
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background: rgba(30, 41, 59, 0.3) !important;
        padding: 14px 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        border-color: #6366f1 !important;
        background: rgba(99, 102, 241, 0.1) !important;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.2) !important;
        transform: translateY(-2px);
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%) !important;
        border-color: #6366f1 !important;
        box-shadow: 0 4px 20px rgba(79, 70, 229, 0.4) !important;
    }
    
    /* ট্যাবের আধুনিক গ্লসি ডিজাইন */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: rgba(15, 23, 42, 0.6);
        padding: 8px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 14px 28px !important;
        border-radius: 12px !important;
        color: #94a3b8 !important;
        font-weight: 500 !important;
        font-size: 16px !important;
        transition: all 0.3s !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.03) !important;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* কুইজ ও অ্যালার্ট বক্সের প্রিমিয়াম ডিজাইন */
    .stAlert {
        background-color: rgba(30, 41, 59, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 14px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ৩. হিরো ব্যানার - আপনার চ্যানেলের ব্র্যান্ড নামসহ
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🔬 Study plan online platform</div>
        <div class="hero-subtitle">বিজ্ঞানকে গভীরভাবে অনুধাবন করার একটি আধুনিক ও বিশ্বমানের আঙিনা। এখানে কোনো মুখস্থ বিদ্যা নেই, শান্ত মাথায় আমরা শিখব প্রকৃতির আসল মেকানিজম।</div>
    </div>
""", unsafe_allow_html=True)

# ৪. সাইডবার লেআউট - অধ্যায় তালিকা
with st.sidebar:
    st.markdown("### 📚 অধ্যায় নির্দেশিকা")
    
    selected_chapter = st.radio(
        "পড়াশোনার টপিক বেছে নাও:",
        [
            "০১. রসায়নের ধারণা",
            "০২. পদার্থের অবস্থা",
            "০৩. পদার্থের গঠন",
            "০৪. পর্যায় সারণি",
            "০৫. রাসায়নিক বন্ধন",
            "০৬. মোলের ধারণা ও রাসায়নিক গণনা"
        ],
        label_visibility="visible"
    )
    
    st.markdown("---")
    st.caption("✨ Designed for Conceptual Excellence")

# ৫. মূল কন্টেন্ট এরিয়া
st.markdown(f"## 📖 {selected_chapter}")

tab1, tab2, tab3 = st.tabs(["🎯 মূল পাঠ্যবই ও কনসেপ্ট", "🎥 ভিডিও ও অ্যানিমেশন", "📝 সেলফ অ্যাসেสมেন্ট"])

with tab1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 কনসেপ্ট বুক")
    st.info("💡 এই আকর্ষণীয় গ্লাস প্যানেলে আপনার চমৎকার ক্লাস নোট ও বিজ্ঞানের গভীর কন্টেন্টগুলো সাজানো থাকবে।")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 🎬 ভিজ্যুয়াল লার্নিং সেকশন")
    st.caption("আপনার তৈরি করা পাইথন (Manim) অ্যানিমেশন ও হাই-কোয়ালিটি ভিডিওগুলো দেখার প্রিমিয়াম থিয়েটার উইন্ডো এটি।")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 📝 কুইজ ও রিয়েল-টাইম মূল্যায়ন")
    st.caption("শিক্ষার্থীদের মেধা যাচাইয়ের জন্য ইন্টারেক্টিভ ও আধুনিক প্রশ্নব্যাংক এখানে লোড হবে।")
    st.markdown('</div>', unsafe_allow_html=True)
