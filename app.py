import streamlit as st
import pandas as pd

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    layout="centered"
)

# =====================================
# CSS احترافي (RTL + خلفية + ألوان + خط)
# =====================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&display=swap');

html, body, [class*="css"] {
    direction: rtl;
    font-family: 'Cairo', sans-serif;
    background: linear-gradient(135deg, #e3f2fd, #e8f5e9);
}

/* الحاوية العامة */
.app-container {
    max-width: 780px;
    margin: auto;
    padding: 30px;
}

/* العنوان */
.header {
    text-align: center;
    margin-bottom: 35px;
}
.header h1 {
    color: #0D47A1;
    font-weight: 800;
}
.header h2 {
    color: #2E7D32;
    font-weight: 700;
}
.header h3 {
    color: #333;
    font-weight: 600;
}

/* زر البحث */
div.stButton > button {
    background: linear-gradient(135deg, #1976D2, #42A5F5);
    color: white;
    padding: 12px 36px;
    font-size: 17px;
    font-weight: 700;
    border-radius: 10px;
    border: none;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #1565C0, #1E88E5);
}

/* رسائل */
.success {
    background-color: #E8F5E9;
    border-right: 6px solid #2E7D32;
    padding: 16px;
    border-radius: 10px;
    font-weight: 700;
    margin-top: 20px;
}
.error {
    background-color: #FDECEA;
    border-right: 6px solid #C62828;
    padding: 16px;
    border-radius: 10px;
    font-weight: 700;
    margin-top: 20px;
}

/* بطاقة النتيجة */
.card {
    background: #ffffff;
    border-radius: 18px;
    padding: 32px 36px;
    border-right: 7px solid #0D47A1;
    box-shadow: 0 12px 32px rgba(0,0,0,0.08);
    margin-top: 25px;
    text-align: right;
}

/* صفوف النتيجة */
.result-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0;
    border-bottom: 1px solid #eee;
}
.result-row:last-child {
    border-bottom: none;
}

/* العنوان */
.result-label {
    font-size: 16px;
    font-weight: 700;
    color: #0B3C5D;
}

/* القيمة */
.result-value {
    font-size: 17px;
    font-weight: 800;
    color: #222;
}

/* التذييل */
.footer {
    text-align: center;
    margin-top: 50px;
    color: #444;
    font-size: 15px;
    font-weight: 600;
}

@media (max-width: 600px) {
    .result-row {
        flex-direction: column;
        align-items: flex-start;
    }
    .result-value {
        margin-top: 4px;
    }
}
</style>
""", unsafe_allow_html=True)

# =====================================
# واجهة العنوان
# =====================================
st.markdown('<div class="app-container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>جامعة المرقب</h1>
    <h2>كلية العلوم الصحية</h2>
    <h3>قسم المختبرات الطبية</h3>
    <p><strong>الاستعلام عن رقم الجلوس</strong></p>
</div>
""", unsafe_allow_html=True)

# =====================================
# إدخال رقم القيد
# =====================================
reg_input = st.text_input(
    "🔢 رقم القيد",
    placeholder="أدخل رقم القيد هنا"
)

# =====================================
# منطق البحث
# =====================================
if st.button("🔍 استعلام"):
    try:
        df = pd.read_excel("data.xlsx", dtype=str)
        df = df.fillna("")

        df["رقم القيد"] = df["رقم القيد"].str.strip()
        reg_input = reg_input.strip()

        result = df[df["رقم القيد"] == reg_input]

        if not result.empty:
            row = result.iloc[0]

            st.markdown("""
            <div class="success">
                ✅ تم العثور على بيانات الطالب
            </div>
            """, unsafe_allow_html=True)

            hall = row.get("القاعة الامتحانية", "").strip()
            hall_display = hall if hall else "لم تُحدد بعد"

            st.markdown(f"""
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
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="error">
                ❌ رقم القيد غير موجود ضمن البيانات
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"""
        <div class="error">
            ⚠️ خطأ أثناء قراءة البيانات<br>{e}
        </div>
        """, unsafe_allow_html=True)

# =====================================
# التذييل
# =====================================
st.markdown("""
<div class="footer">
    إعداد: الأستاذ عبدالفتاح محمد البكوش<br>
    © جامعة المرقب – كلية العلوم الصحية
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
