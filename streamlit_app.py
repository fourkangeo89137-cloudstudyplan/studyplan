import streamlit as st

# ১. পেজ কনফিগারেশন
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ২. কাস্টম সিএসএস (CSS) - আল্ট্রা-মডার্ন ডিজাইন ও বাটন ইফেক্ট
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans Bengali', sans-serif !important;
    }
    
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
        font-width: 300;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* গ্লাস কার্ড ডিজাইন */
    .content-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.5) 100%) !important;
        padding: 35px;
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        backdrop-filter: blur(10px);
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }
    
    /* সাইডবার ডিজাইন */
    section[data-testid="stSidebar"] {
        background-color: #090d16 !important;
        border-right: 1px solid rgba(99, 102, 241, 0.15);
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
    }
    
    div[data-testid="stRadio"] label[data-baseweb="radio"][aria-checked="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%) !important;
        border-color: #6366f1 !important;
    }
    
    /* ট্যাবের মডার্ন ডিজাইন */
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
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
    }
    
    /* সাবমিট বাটনের প্রিমিয়াম গ্লো স্টাইল */
    .stButton>button {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 30px !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ৩. হিরো ব্যানার
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🔬 Study plan online platform</div>
        <div class="hero-subtitle">বিজ্ঞানকে গভীরভাবে অনুধাবন করার একটি আধুনিক ও বিশ্বমানের আঙিনা। এখানে কোনো মুখস্থ বিদ্যা নেই, শান্ত মাথায় আমরা শিখব প্রকৃতির আসল মেকানিজম।</div>
    </div>
""", unsafe_allow_html=True)

# ৪. সাইডবার লেআউট
with st.sidebar:
    st.markdown("### 📚 অধ্যায় নির্দেশিকা")
    selected_chapter = st.radio(
        "পড়াশোনার টপিক বেছে নাও:",
        [
            "০১. রসায়নের ধারণা",
            "০২. পদার্থের অবস্থা",
            "০৩. পদার্থের গঠন",
            "০৪. পর্যায় സারণি",
            "০৫. রাসায়নিক বন্ধন",
            "০৬. মোলের ধারণা ও রাসায়নিক গণনা"
        ]
    )
    st.markdown("---")
    st.caption("✨ Designed for Conceptual Excellence")

# ৫. মূল কন্টেন্ট এরিয়া
st.markdown(f"## 📖 {selected_chapter}")

tab1, tab2, tab3 = st.tabs(["🎯 মূল পাঠ্যবই কনসেপ্ট", "🎥 ভিডিও ও অ্যানিমেশন", "📝 সেলফ অ্যাসেসমেন্ট"])

# মডিউল ১: কনসেপ্ট বুক
with tab1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 রসায়নের পরিচিতি ও পরিধি")
    st.write("আজ আমরা জানব রসায়নের মূল ভিত্তি নিয়ে। সৃষ্টির শুরু থেকেই মানুষ প্রকৃতির বিভিন্ন উপাদান এবং তাদের পরিবর্তন লক্ষ্য করে আসছে।")
    st.markdown('</div>', unsafe_allow_html=True)

# মডিউল ২: ভিডিও ল্যাব
with tab2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 🎬 ভিজ্যুয়াল লার্নিং সেকশন")
    st.caption("ভবিষ্যতে আপনার তৈরি করা পাইথন (Manim) অ্যানিমেশন ও ভিডিওগুলো এখানে যুক্ত হবে।")
    st.markdown('</div>', unsafe_allow_html=True)

# মডিউল ৩: সেলফ অ্যাসেসমেন্ট (ফ্রন্ট-এন্ড ও ব্যাক-এন্ড এর বাস্তব রূপ)
with tab3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("### 📝 কুইজ টাইম: নিজেকে যাচাই করো")
    
    # প্রশ্ন ১ (ফ্রন্ট-এন্ড ইন্টারফেস)
    st.markdown("##### *প্রশ্ন ১: নিচের কোনটিতে রাসায়নিক পরিবর্তন ঘটে?*")
    options = [
        "ক) বরফ গলে পানি হওয়া", 
        "খ) মোমবাতির দহন (জ্বলন)", 
        "গ) লোহাকে চুম্বকে পরিণত করা", 
        "ঘ) চিনি পানিতে দ্রবীভূত হওয়া"
    ]
    user_choice = st.radio("সঠিক উত্তরটি সিলেক্ট করো:", options, key="q1")
    
    submit_btn = st.button("উত্তর জমা দাও")
    
    # ব্যাক-এন্ড লজিক (পর্দার আড়ালের বুদ্ধিমত্তা)
    if submit_btn:
        if user_choice == "খ) মোমবাতির দহন (জ্বলন)":
            st.success("🎉 চমৎকার! তোমার উত্তরটি সঠিক হয়েছে। মোমবাতির দহনে কার্বন ডাই-অক্সাইড ও জলীয় বাষ্প তৈরি হয়, যা একটি রাসায়নিক পরিবর্তন।")
        else:
            st.error("❌ উত্তরটি সঠিক হয়নি, স্যার। আবার একটু ভেবে চেষ্টা করো! (হিন্টস: যেখানে নতুন পদার্থ তৈরি হয়, সেটিই রাসায়নিক পরিবর্তন)।")
            
    st.markdown('</div>', unsafe_allow_html=True)
