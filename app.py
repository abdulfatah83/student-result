import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    page_icon="🏛️",
    layout="centered"
)

# 2. تنسيق CSS احترافي (الترويسة، التذييل، اتجاه النص)
st.markdown("""
<style>
    /* ضبط الخط والاتجاه العام */
    .main {
        direction: rtl; 
        text-align: right; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding-bottom: 100px; /* مسافة للتذييل */
    }
    
    /* تنسيق الترويسة (Header) */
    .header-container {
        text-align: center;
        margin-bottom: 20px;
        color: #1f2937;
    }
    .uni-name { font-size: 26px; font-weight: bold; color: #0e4d92; margin-bottom: 5px; }
    .faculty-name { font-size: 20px; font-weight: 600; color: #333; margin-bottom: 5px; }
    .dept-name { font-size: 18px; color: #555; }
    
    /* تنسيق بطاقة الاسم (مميزة) */
    .name-card {
        background-color: #e3f2fd;
        border-right: 5px solid #0e4d92;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* تنسيق مربعات البيانات الأخرى */
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #e9ecef;
        text-align: right;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* تنسيق زر البحث */
    div.stButton > button:first-child {
        background-color: #0e4d92;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
    }

    /* تنسيق التذييل (Footer) الثابت في الأسفل */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 15px;
        font-size: 14px;
        border-top: 3px solid #0e4d92;
        z-index: 999;
    }
    
    /* إخفاء عناصر Streamlit الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. عرض الترويسة الرسمية
st.markdown("""
<div class="header-container">
    <div class="uni-name">جامعة المرقب</div>
    <div class="faculty-name">كلية العلوم الصحية</div>
    <div class="dept-name">قسم المختبرات الطبية</div>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("<h3 style='text-align: center;'>الاستعلام عن رقم الجلوس</h3>", unsafe_allow_html=True)

# 4. تحميل البيانات
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data.xlsx", dtype=str)
        df.columns = df.columns.str.strip()
        for col in df.columns:
            df[col] = df[col].str.strip()
        return df
    except:
        return None

df = load_data()

# 5. واجهة البحث
if df is not None:
    # جعل مربع البحث في المنتصف
    col_spacer1, col_input, col_spacer2 = st.columns([1, 2, 1])
    with col_input:
        student_id = st.text_input("📝 أدخل رقم القيد:", placeholder="اكتب الرقم هنا...")
        search_btn = st.button("بحث")

    if search_btn and student_id:
        result = df[df['رقم القيد'] == student_id]
        
        if not result.empty:
            info = result.iloc[0]
            st.success("✅ تم العثور على البيانات:")
            
            # --- عرض النتائج بالترتيب المطلوب ---
            
            # 1. اسم الطالب (مميز في الأعلى)
            st.markdown(f"""
            <div class="name-card">
                <h4 style="margin:0; color:#333;">👤 اسم الطالب: <span style="color:#0e4d92;">{info.get('اسم الطالب', '---')}</span></h4>
            </div>
            """, unsafe_allow_html=True)
            
            # 2. باقي التفاصيل في شبكة (Grid)
            # الصف الأول: رقم القيد - رقم الجلوس
            c1, c2 = st.columns(2)
            with c1:
                st.metric("🆔 رقم القيد", info.get('رقم القيد', '---'))
            with c2:
                st.metric("🪑 رقم الجلوس", info.get('رقم الجلوس', '---'))
            
            # الصف الثاني: السنة الدراسية - القاعة الامتحانية
            c3, c4 = st.columns(2)
            with c3:
                st.metric("📅 السنة الدراسية", info.get('السنة الدراسية', '---'))
            with c4:
                # محاولة جلب القاعة، وإذا لم توجد يكتب غير محدد
                hall = info.get('القاعة الامتحانية', info.get('القاعة', 'غير محدد'))
                st.metric("🏫 القاعة الامتحانية", hall)
                
        else:
            st.error("❌ رقم القيد غير موجود، يرجى التأكد والمحاولة مرة أخرى.")
elif df is None:
    st.warning("⚠️ يرجى رفع ملف البيانات data.xlsx")

# 6. التذييل (Footer)
st.markdown("""
<div class="footer">
    إعداد الأستاذ: <b>عبدالفتاح محمد البكوش</b>
</div>
""", unsafe_allow_html=True)
