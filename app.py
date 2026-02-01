import streamlit as st
import pandas as pd

# ===============================
# إعداد الصفحة
# ===============================
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    layout="centered"
)

# ===============================
# CSS (RTL + تنسيق احترافي)
# ===============================
st.markdown("""
<style>
html, body {
    direction: rtl;
    font-family: Arial, sans-serif;
    background-color: #f5f7fb;
}

.container {
    max-width: 700px;
    margin: auto;
}

.header {
    text-align: center;
    margin-bottom: 30px;
}
.header h1 {
    color: #0D47A1;
    font-weight: bold;
}
.header h2 {
    color: #2E7D32;
    font-weight: bold;
}
.header h3 {
    color: #444;
}

.card {
    background: #ffffff;
    padding: 25px;
    border-radius: 12px;
    border-right: 6px solid #0D47A1;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
}

.result-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}
.result-row:last-child {
    border-bottom: none;
}

.result-label {
    font-weight: bold;
    color: #0D47A1;
}

.result-value {
    font-weight: bold;
    color: #000;
}

.success {
    background-color: #E8F5E9;
    border-right: 5px solid #2E7D32;
    padding: 12px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: bold;
}

.error {
    background-color: #FDECEA;
    border-right: 5px solid #C62828;
    padding: 12px;
    border-radius: 8px;
    margin-top: 15px;
    font-weight: bold;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: #555;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# الواجهة
# ===============================
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>جامعة المرقب</h1>
    <h2>كلية العلوم الصحية</h2>
    <h3>قسم المختبرات الطبية</h3>
    <p><strong>الاستعلام عن رقم الجلوس</strong></p>
</div>
""", unsafe_allow_html=True)

# ===============================
# إدخال رقم القيد
# ===============================
reg_input = st.text_input("🔢 أدخل رقم القيد")

# ===============================
# زر الاستعلام
# ===============================
if st.button("🔍 استعلام"):
    try:
        # قراءة ملف Excel
        df = pd.read_excel("data.xlsx", dtype=str).fillna("")
        df.columns = df.columns.str.strip()

        reg_input = reg_input.strip()
        df["رقم القيد"] = df["رقم القيد"].str.strip()

        result = df[df["رقم القيد"] == reg_input]

        if not result.empty:
            row = result.iloc[0]
            hall = row.get("القاعة الامتحانية", "").strip()
            hall_display = hall if hall else "لم تُحدد بعد"

            st.markdown("""
            <div class="success">✅ تم العثور على بيانات الطالب</div>
            """, unsafe_allow_html=True)

            html_result = f"""
            <div class="card">

                <div class="result-row">
                    <div class="result-label">اسم الطالب</div>
                    <div class="result-value">{row.get('اسم الطالب','')}</div>
                </div>

                <div class="result-row">
                    <div class="result-label">رقم القيد</div>
                    <div class="result-value">{row.get('رقم القيد','')}</div>
                </div>

                <div class="result-row">
                    <div class="result-label">رقم الجلوس</div>
                    <div class="result-value">{row.get('رقم الجلوس','')}</div>
                </div>

                <div class="result-row">
                    <div class="result-label">السنة الدراسية</div>
                    <div class="result-value">{row.get('السنة الدراسية','')}</div>
                </div>

                <div class="result-row">
                    <div class="result-label">القاعة الامتحانية</div>
                    <div class="result-value">{hall_display}</div>
                </div>

            </div>
            """

            st.markdown(html_result, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="error">❌ رقم القيد غير موجود</div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"""
        <div class="error">⚠️ خطأ في قراءة البيانات<br>{e}</div>
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
