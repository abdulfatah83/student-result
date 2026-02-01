import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="نتيجة الطالب", layout="centered")

# تصميم الصفحة لتكون من اليمين لليسار
st.markdown("""
<style>
    .main {direction: rtl; text-align: right;}
    div.stButton > button:first-child {background-color: #0068c9; color: white; width: 100%;}
</style>
""", unsafe_allow_html=True)

st.title("🎓 نظام الاستعلام عن النتائج")
st.write("أدخل رقم القيد في الأسفل لعرض النتيجة")

# قراءة ملف الإكسل
try:
    df = pd.read_excel("data.xlsx", dtype=str)
    # تنظيف أسماء الأعمدة من المسافات الزائدة
    df.columns = df.columns.str.strip()
except:
    st.error("خطأ: ملف البيانات data.xlsx غير موجود")
    st.stop()

# خانة البحث
student_id = st.text_input("رقم القيد:", "")

if st.button("بحث"):
    if student_id:
        # البحث داخل الملف
        result = df[df['رقم القيد'] == student_id]
        
        if not result.empty:
            st.success("✅ بيانات الطالب:")
            st.table(result)
        else:
            st.error("❌ رقم القيد غير موجود")
    else:
        st.warning("الرجاء كتابة رقم القيد")
