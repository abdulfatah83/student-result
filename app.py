import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    page_icon="🎓",
    layout="centered"
)

# 2. تنسيق احترافي (CSS)
# هذا الجزء يجعل النصوص عربية بشكل صحيح ويجمل الأزرار والخلفيات
st.markdown("""
<style>
    /* اتجاه النص لليمين ونوع الخط */
    .main {
        direction: rtl; 
        text-align: right; 
        font-family: sans-serif;
    }
    
    /* تنسيق زر البحث */
    div.stButton > button:first-child {
        background-color: #0e4d92; /* لون أزرق رسمي */
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        width: 100%;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #09386d;
        color: white;
    }

    /* تنسيق مربعات عرض النتائج */
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        text-align: right;
    }
    
    /* إخفاء القائمة الجانبية والقوائم العلوية لتبدو كصفحة ويب عادية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. واجهة التطبيق
st.markdown("<h1 style='text-align: center; color: #0e4d92;'>الاستعلام عن رقم الجلوس 🎓</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>أدخل رقم القيد للحصول على بيانات الجلوس والقاعة</h5>", unsafe_allow_html=True)
st.write("---")

# 4. تحميل البيانات
try:
    df = pd.read_excel("data.xlsx", dtype=str)
    # تنظيف العناوين والبيانات من أي مسافات زائدة
    df.columns = df.columns.str.strip()
    for col in df.columns:
        df[col] = df[col].str.strip()
except Exception as e:
    st.error("⚠️ عذراً، حدثت مشكلة في قراءة ملف البيانات.")
    st.stop()

# 5. مربع البحث
col_search1, col_search2, col_search3 = st.columns([1, 2, 1])
with col_search2:
    student_id = st.text_input("رقم القيد:", placeholder="اكتب الرقم هنا...", label_visibility="collapsed")
    search_btn = st.button("🔍 بحث عن النتيجة")

# 6. منطق البحث والعرض
if search_btn:
    if student_id:
        # البحث
        result = df[df['رقم القيد'] == student_id]
        
        if not result.empty:
            st.success("✅ تم العثور على البيانات:")
            st.write("") # مسافة فارغة
            
            # جلب بيانات الطالب في متغير واحد لسهولة الاستخدام
            info = result.iloc[0]
            
            # عرض البيانات في عمودين متجاورين بشكل جميل
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="👤 اسم الطالب", value=info.get('اسم الطالب', '---'))
                st.metric(label="🆔 رقم القيد", value=info.get('رقم القيد', '---'))
            
            with col2:
                st.metric(label="🪑 رقم الجلوس", value=info.get('رقم الجلوس', '---'))
                st.metric(label="📅 السنة الدراسية", value=info.get('السنة الدراسية', '---'))
                
        else:
            st.warning("⚠️ رقم القيد هذا غير مسجل لدينا، يرجى التأكد والمحاولة مرة أخرى.")
    else:
        st.info("الرجاء كتابة رقم القيد في الخانة أعلاه.")

# تذييل بسيط
st.markdown("<br><br><hr><center><small>نظام شؤون الطلاب الإلكتروني © 2026</small></center>", unsafe_allow_html=True)
