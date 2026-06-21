import streamlit as st

# ওয়েবসাইটের টাইটেল ও কনফিগারেশন
st.set_page_config(page_title="Fourkan's Science Platform", layout="wide")

st.title("🔬 ফিজিক্স ও কেমিস্ট্রি ডিজিটাল প্ল্যাটফর্ম")
st.subheader("শিক্ষক: মো: ফোরকান")
st.write("---")

# সাইডবারে নোটিশ বা পরিচিতি
st.sidebar.header("📢 সর্বশেষ নোটিশ")
st.sidebar.info("৯ম শ্রেণীর সকল ক্লাস সম্পূর্ণ ফ্রি! ১০ম শ্রেণীর প্রিমিয়াম মিশনটি শীঘ্রই শুরু হতে যাচ্ছে।")

# প্রধান দুটি উইং বা পার্ট (জেনারেল এবং কারিগরি)
col1, col2 = st.columns(2)

with col1:
    st.header("🏛️ জেনারেল পার্ট")
    st.write("সাধারণ স্কুল ও মাদ্রাসার ৯ম-১০ম শ্রেণীর বিজ্ঞান শাখা।")
    
    subject_gen = st.selectbox("বিষয় নির্বাচন করুন (জেনারেল):", ["পদার্থবিজ্ঞান", "রসায়ন"])
    
    if subject_gen == "পদার্থবিজ্ঞান":
        st.markdown("### 📚 অধ্যায়সমূহ (Physics)")
        st.success("🔓 ১ম অধ্যায়: ভৌত রাশি ও পরিমাপ (FREE Class)")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # এখানে আপনার ইউটিউব ভিডিওর লিংক বসাবেন
        
        st.warning("🔒 ২য় অধ্যায়: গতি (Premium)")
        st.warning("🔒 ৩য় অধ্যায়: বল (Premium)")
        
    elif subject_gen == "রসায়ন":
        st.markdown("### 📚 অধ্যায়সমূহ (Chemistry)")
        st.success("🔓 ১ম অধ্যায়: রসায়নের ধারণা (FREE Class)")
        st.warning("🔒 ২য় অধ্যায়: পদার্থের অবস্থা (Premium)")

    if st.button("জেনারেল ফুল কোর্সে এনরোল করুন", key="gen_enroll"):
        st.success("ভর্তির ফরমটি শীঘ্রই যুক্ত করা হবে!")


with col2:
    st.header("🛠️ কারিগরি (ভোকেশনাল) পার্ট")
    st.write("ভোকেশনাল ও টেকনিক্যাল শাখার জন্য বিশেষায়িত ৬০ মার্কের কমপ্লিট মিশন।")
    
    # ৯ম ও ১০ম শ্রেণীর বিভাজন
    class_option = st.radio("শ্রেণী নির্বাচন করুন:", ["৯ম শ্রেণী (বোর্ড ফাইনাল - FREE)", "১০ম শ্রেণী (এসএসসি ফাইনাল - Premium)"])
    
    if class_option == "৯ম শ্রেণী (বোর্ড ফাইনাল - FREE)":
        st.markdown("### 🎁 ৯ম শ্রেণীর ফ্রি কন্টেন্ট")
        subject_voc9 = st.selectbox("বিষয় (৯ম):", ["পদার্থবিজ্ঞান-১", "রসায়ন-১"])
        
        if subject_voc9 == "পদার্থবিজ্ঞান-১":
            st.write("✨ *অধ্যায়: কাজ, ক্ষমতা ও শক্তি*")
            st.caption("লেকচার ভিডিও নিচে দেখুন:")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # আপনার ক্লাস লিংক
            st.button("📥 লেকচার শিট ডাউনলোড করুন (PDF)", key="pdf_p1")
            
    elif class_option == "১০ম শ্রেণী (এসএসসি ফাইনাল - Premium)":
        st.markdown("### 💎 ১০ম শ্রেণীর এসএসসি প্রিমিয়াম মিশন")
        st.error("🔒 এই সেকশনের ক্লাসগুলো দেখতে সাবস্ক্রিপশন প্রয়োজন।")
        
        subject_voc10 = st.selectbox("বিষয় (১০ম):", ["পদার্থবিজ্ঞান-২", "রসায়ন-২"])
        
        if st.button("💳 প্রিমিয়াম এক্সেস কিনুন (বিকাশ/নগদ)", key="pay_voc"):
            st.info("পেমেন্ট গেটওয়ে খুব শীঘ্রই সচল করা হচ্ছে। সাথে থাকার জন্য ধন্যবাদ!")
