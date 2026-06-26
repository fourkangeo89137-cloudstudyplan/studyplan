import streamlit as st

# ====================================================================
# ১. পেজ কনফিগারেশন ও ব্র্যান্ডিং (Study plan online platform)
# ====================================================================
st.set_page_config(
    page_title="Study plan online platform", 
    page_icon="🔬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ====================================================================
# ২. কন্টেন্ট ডেটাবেজ (এখানে আপনি আপনার মতো করে এডিট/যোগ করতে পারবেন)
# ====================================================================

# 📌 অতি গুরুত্বপূর্ণ ছোট প্রশ্ন (ক ও খ নম্বর) - এখান থেকে এডিট করুন
short_questions = [
    {
        "type": "💡 জ্ঞানমূলক (ক)",
        "question": "আল-কেমি (Al-chemy) শব্দটির উৎপত্তি কোন শব্দ থেকে?",
        "answer": "আরবি শব্দ 'আল-কমিয়া' (Al-kimiya) থেকে আল-কেমি শব্দটির উৎপত্তি হয়েছে, যার অর্থ মিশরীয় শিল্প।"
    },
    {
        "type": "💡 জ্ঞানমূলক (ক)",
        "question": "আধুনিক রসায়নের জনক কাকে বলা হয়?",
        "answer": "ফরাসি বিজ্ঞানী অ্যান্টনি ল্যাভয়সিয়ে (Antoine Lavoisier)-কে আধুনিক রসায়নের জনক বলা হয়।"
    },
    {
        "type": "🔥 অনুধাবনমূলক (খ)",
        "question": "মোมবাতির জ্বলনে ভৌত ও রাসায়নিক উভয় পরিবর্তনই ঘটে কেন? [বোর্ড ও শীর্ষ স্কুল টেস্টে বারবার আসা]",
        "answer": "মোমবাতি যখন জ্বলে, তখন আগুনের তাপে মোম গলে নিচের দিকে পড়তে থাকে এবং ঠান্ডা হয়ে পুনরায় কঠিন মোমে পরিণত হয়—এটি হলো ভৌত পরিবর্তন। অন্যদিকে, মোমের কিছু অংশ বাষ্পীভূত হয়ে বাতাসের অক্সিজেনের সাথে বিক্রিয়া করে কার্বন ডাই-অক্সাইড (CO₂), জলীয় বাষ্প (H₂O) এবং আলো-তাপ উৎপন্ন করে। যেহেতু এখানে নতুন पदार्थ তৈরি হচ্ছে, তাই এটি একটি রাসায়নিক পরিবর্তন। অতএব, মোমবাতির জ্বলনে উভয় পরিবর্তনই ঘটে।"
    },
    {
        "type": "🍏 অনুধাবনমূলক (খ)",
        "question": "কাঁচা আম টক কিন্তু পাকা আম মিষ্টি হয় কেন?",
        "answer": "কাঁচা আমে বিভিন্ন ধরনের জৈব অ্যাসিড (যেমন: ম্যালিক অ্যাসিড, টারটারিক অ্যাসিড) থাকে, যার কারণে কাঁচা আম টক লাগে। কিন্তু আম যখন পাকে, তখন রসায়নের নিয়মে এই অ্যাসিডগুলো রাসায়নিক বিক্রিয়ার মাধ্যমে মিষ্টি গ্লুকোজ এবং ফ্রুক্টোজে রূপান্তরিত হয়ে যায়। এই কারণেই পাকা আম মিষ্টি লাগে।"
    }
]

# 📌 টপ অবজেক্টিভস (MCQ) - এখান থেকে নতুন কুইজ যোগ বা পরিবর্তন করুন
mcq_questions = [
    {
        "id": "m1",
        "question": "১. অ্যান্টাসিড (Antacid) ওষুধের প্রধান রাসায়নিক উপাদান নিচের কোনটি?",
        "options": ["Al(OH)3 ও Mg(OH)2", "NaHCO3 ও HCl", "CaCO3", "NaOH"],
        "correct": "Al(OH)3 ও Mg(OH)2",
        "explanation": "🎉 সঠিক উত্তর! পেটের অতিরিক্ত হাইড্রোক্লোরিক অ্যাসিডকে প্রসমিত করতে অ্যান্টাসিডে ক্ষারীয় অ্যালুমিনিয়াম ও ম্যাগনেসিয়াম হাইড্রোক্সাইড ব্যবহৃত হয়।"
    },
    {
        "id": "m2",
        "question": "২. মরিচার (Rust) সঠিক রাসায়নিক সংকেত কোনটি? [বিগত ৫টি বোর্ডের প্রশ্ন]",
        "options": ["Fe3O4", "Fe2O3", "Fe2O3 . nH2O", "FeO"],
        "correct": "Fe2O3 . nH2O",
        "explanation": "🎉 সঠিক উত্তর! আর্দ্র ফেরিক অক্সাইডকেই মরিচা বলা হয়।"
    }
]


# ====================================================================
# ৩. কাস্টম সিএসএস (CSS) - আল্ট্রা-মডার্ন ডিজাইন (এটি পরিবর্তন করার প্রয়োজন নেই)
# ====================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Noto Sans Bengali', sans-serif !important; }
    .stApp { background-color: #0b0f19; color: #f1f5f9; }
    
    /* হিরো ব্যানার */
    .hero-container {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 45px 35px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 35px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
    }
    .hero-title { color: #ffffff !important; font-size: 40px !important; font-weight: 700 !important; margin-bottom: 12px; }
    .hero-subtitle { color: #94a3b8 !important; font-size: 17px !important; font-weight: 300; max-width: 800px; margin: 0 auto; }
    
    /* কন্টেন্ট কার্ড */
    .content-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.4) 0%, rgba(15, 23, 42, 0.5) 100%) !important;
        padding: 28px;
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        backdrop-filter: blur(10px);
        margin-bottom: 22px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }
    .question-title { color: #38bdf8 !important; font-size: 18px !important; font-weight: 600 !important; margin-bottom: 8px; }
    .answer-text {
        color: #e2e8f0 !important; font-size: 16px !important; line-height: 1.6;
        background: rgba(15, 23, 42, 0.4); padding: 15px; border-radius: 10px; border-left: 4px solid #0ea5e9;
    }
    
    /* সাইডবার ও ট্যাব */
    section[data-testid="stSidebar"] { background-color: #090d16 !important; border-right: 1px solid rgba(99, 102, 241, 0.15); }
    .stTabs [data-baseweb="tab-list"] { gap: 12px; background-color: rgba(15, 23, 42, 0.6); padding: 8px; border-radius: 16px; }
    .stTabs [data-baseweb="tab"] { padding: 12px 24px !important; border-radius: 12px !important; color: #94a3b8 !important; font-size: 16px !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important; color: #ffffff !important; }
    
    /* বাটন */
    .stButton>button {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%) !important;
        color: white !important; border: none !important; padding: 8px 22px !important; border-radius: 10px !important; font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ====================================================================
# ৪. অ্যাপ্লিকেশন লেআউট ও লজিক (স্বয়ংক্রিয়ভাবে ডেটা রেন্ডার হবে)
# ====================================================================

# হিরো ব্যানার প্রদর্শন
st.markdown(f"""
    <div class="hero-container">
        <div class="hero-title">🔬 Study plan online platform</div>
        <div class="hero-subtitle">বোর্ড পরীক্ষা ও শীর্ষস্থানীয় স্কুলের প্রশ্ন বিশ্লেষণ (Data Analysis) এর ওপর ভিত্তি করে তৈরি বিশেষ লার্নিং মডিউল।</div>
    </div>
""", unsafe_allow_html=True)

# সাইডবার
with st.sidebar:
    st.markdown("### 📚 অধ্যায় নির্দেশিকা")
    selected_chapter = st.radio("পড়াশোনার টপিক বেছে নাও:", ["০১. রসায়নের ধারণা", "০২. পদার্থের অবস্থা", "০৩. পদার্থের গঠন"])
    st.markdown("---")
    st.caption("✨ Designed for Conceptual Excellence")

st.markdown(f"## 📖 {selected_chapter}")

# ট্যাব বিভাজন
tab1, tab2, tab3 = st.tabs(["🎯 অতি গুরুত্বপূর্ণ ছোট প্রশ্ন (ক ও খ)", "📝 টপ অবজেক্টিভস (MCQ)", "📊 সাংকেতিক চিহ্ন (Hazard Symbols)"])

# ট্যাব ১: ছোট প্রশ্ন ডাইনামিক রেন্ডারিং
with tab1:
    st.markdown("### 📌 সর্বাধিক কমনোপযোগী জ্ঞান ও অনুধাবনমূলক প্রশ্ন")
    for q in short_questions:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f'<p class="question-title">{q["type"]}: {q["question"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="answer-text"><b>উত্তর:</b> {q["answer"]}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ট্যাব ২: অবজেক্টিভ বা MCQ ডাইনামিক লজিক
with tab2:
    st.markdown("### 📝 রিয়েল-টাইম MCQ প্র্যাকটিস উইন্ডো")
    for m in mcq_questions:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(f"##### *{m['question']}*")
        user_choice = st.radio("অপশনস:", m["options"], key=m["id"])
        
        if st.button("উত্তর চেক করো", key=f"btn_{m['id']}"):
            if user_choice == m["correct"]:
                st.success(m["explanation"])
            else:
                st.error(f"❌ ভুল উত্তর, সঠিক উত্তরটি হলো: {m['correct']}")
        st.markdown('</div>', unsafe_allow_html=True)

# ট্যাব ৩: সাংকেতিক চিহ্ন
with tab3:
    st.markdown("### ⚠️ ল্যাবরেটরি নিরাপত্তা ও সাংকেতিক চিহ্ন")
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("##### *১. ট্রিফয়েল (Trifoil) বা তেজস্ক্রিয় রশ্মি চিহ্ন*")
    st.warning("☢️ এই চিহ্নযুক্ত পদার্থ (যেমন: ইউরেনিয়াম, রেডিয়াম) থেকে ক্ষতিকর আলফা, বিটা ও গামা রশ্মি বের হয় যা ক্যানসার সৃষ্টি করতে পারে। এগুলোকে সীসার (Lead) পাত্রে সুরক্ষিত রাখতে হয়।")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("##### *২. দাহ্য পদার্থ (Flammable Substance)*")
    st.info("🔥 অ্যালকোহল বা ইথারের বোতলে এই চিহ্ন থাকে। এগুলোতে দ্রুত আগুন লাগতে পারে বলে এদের সবসময় আগুনের শিখা থেকে দূরে রাখতে হয়।")
    st.markdown('</div>', unsafe_allow_html=True)
