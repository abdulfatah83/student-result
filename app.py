import streamlit as st
import pandas as pd

# ===============================
# إعدادات الصفحة
# ===============================
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    layout="centered"
)

# ===============================
# CSS احترافي (RTL + ألوان جامعية)
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    direction: rtl;
    font-family: 'Cairo', sans-serif;
    background-color: #F7F9FC;
}

/* الحاوية الرئيسية */
.app-container {
    max-width: 720px;
    margin: auto;
}

/* العناوين */
.header {
    text-align: center;
    margin-bottom: 30px;
}
.header h1 {
    color: #0B3C5D;
    font-weight: 700;
    margin-bottom: 5px;
}
.header h2 {
    color: #1B5E20;
    font-weight: 600;
    margin-bottom: 5px;
}
.header h3 {
    color: #555;
    font-weight: 500;
    margin-bottom: 20px;
}

/* كرت النتيجة */
.card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 28px;
    border-right: 5px solid #0B3C5D;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-top: 20px;
}

/* عناصر البيانات */
.item {
    font-size: 17px;
    margin-bottom: 14px;
    color: #222;
}

/* زر البحث */
div.stButton > button {
    background-color: #0B3C5D;
    color: white;
    padding: 10px 30px;
    font-size: 16px;
    border-radius: 8px;
    border: none;
}
div.stButton > button:hover {
    background-color: #124A73;
}

/* رسائل */
.success {
    background-color: #E8F5E9;
    border-right: 5px solid #2E7D32;
    padding: 14px;
    border-radius: 8px;
    margin-top: 15px;
}
.error {
    background-color: #FDECEA;
    border-right: 5px solid #B71C1C;
    padding: 14px;
    border-radius: 8px;
    margin-top: 15px;
}

/* التذييل */
.footer {
    text-align: center;
    margin-top: 45px;
    color: #666;
    font-size: 14px;
}

@media (max-width: 600px) {
    .item { font-size: 16px; }
}
</style>
""", unsafe_allow_html=True)

# ===============================
# واجهة العنوان
# ===============================
st.markdown('<div class="app-container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>جامعة المرقب</h1>
    <h2>كلية العلوم الصحية</h2>
    <h3>قسم المختبرات الطبية</h3>
    <p>الاستعلام عن رقم الجلوس</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# إدخال رقم القيد
# ===============================
reg_input = st.text_input(
    "🔢 أدخل رقم القيد",
    placeholder="مثال: 223030759"
)

# ===============================
# زر البحث والمنطق
# ===============================
if st.button("🔍 بحث"):
    try:
        # قراءة ملف Excel كنص (حل جذري)
        df = pd.read_excel("data.xlsx", dtype=str)

        # تنظيف رقم القيد
        df["رقم القيد"] = df["رقم القيد"].str.strip()
        reg_input = reg_input.strip()

        # البحث
        result = df[df["رقم القيد"] == reg_input]

        if not result.empty:
            row = result.iloc[0]

            st.markdown("""
            <div class="success">
                ✅ تم العثور على بيانات الطالب
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card">
                <div class="item"><strong>اسم الطالب:</strong> {row['اسم الطالب']}</div>
                <div class="item"><strong>رقم القيد:</strong> {row['رقم القيد']}</div>
                <div class="item"><strong>رقم الجلوس:</strong> {row['رقم الجلوس']}</div>
                <div class="item"><strong>السنة الدراسية:</strong> {row['السنة الدراسية']}</div>
                <div class="item"><strong>القاعة الامتحانية:</strong> {row['القاعة الامتحانية']}</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="error">
                ❌ لم يتم العثور على رقم القيد
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"""
        <div class="error">
            ⚠️ حدث خطأ أثناء قراءة البيانات<br>
            {e}
        </div>
        """, unsafe_allow_html=True)

# ===============================
# التذييل
# ===============================
st.markdown("""
<div class="footer">
    إعداد: الأستاذ عبدالفتاح محمد البكوش<br>
    © جامعة المرقب – كلية العلوم الصحية
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
