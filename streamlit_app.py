import streamlit as st

# ওয়েবসাইটের টাইটেল ও কনফিগারেশন
st.set_page_config(page_title="Fourkan's Science Platform", layout="wide")

st.title("🔬 ফিজিক্স ও কেমিস্ট্রি ডিজিটাল প্ল্যাটফর্ম")
st.subheader("শিক্ষক: মো: ফোরকান")
st.write("---")

# প্রধান দুটি উইং বা পার্ট
col1, col2 = st.columns(2)

with col1:
    st.header("🏛️ জেনারেল পার্ট")
    st.write("সাধারণ স্কুল ও মাদ্রাসার ৯ম-১০ম শ্রেণীর বিজ্ঞান শাখা।")
    if st.button("জেনারেল সেকশনে প্রবেশ করুন", key="general"):
        st.success("জেনারেল সেকশনটি শীঘ্রই চালু হচ্ছে!")

with col2:
    st.header("🛠️ কারিগরি (ভোকেশনাল) পার্ট")
    st.write("ভোকেশনাল ও টেকনিক্যাল শাখার জন্য বিশেষায়িত ৬০ মার্কের কমপ্লিট মিশন।")
    
    # ৯ম ও ১০ম শ্রেণীর বিভাজন
    class_option = st.radio("শ্রেণী নির্বাচন করুন:", ["৯ম শ্রেণী (বোর্ড ফাইনাল - FREE)", "১০ম শ্রেণী (এসএসসি ফাইনাল - Premium)"])
    
    if st.button("কারিগরি সেকশনে প্রবেশ করুন", key="vocational"):
        st.info(f"আপনি {class_option}-এ প্রবেশ করছেন...")
