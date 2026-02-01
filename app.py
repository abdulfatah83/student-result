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
# CSS (ألوان + RTL + خط)
# ===============================
st.markdown("""
<style>
html, body {
    direction: rtl;
    font-family: Arial, sans-serif;
    background-color: #f5f7fb;
}

h1, h2, h3, label {
    font-weight: bold;
}

.block {
    background: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border-right: 6px solid #0D47A1;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}

.label {
    color: #0D47A1;
    font-weight: bold;
}

.value {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# العنوان
# ===============================
st.title("جامعة المرقب")
st.subheader("كلية العلوم الصحية")
st.markdown("### قسم المختبرات الطبية")
st.markdown("#### الاستعلام عن رقم الجلوس")
st.divider()

# ===============================
# إدخال رقم القيد
# ===============================
reg_input = st.text_input("🔢 رقم القيد")

# ===============================
# زر الاستعلام
# ===============================
if st.button("🔍 استعلام"):
    df = pd.read_excel("data.xlsx", dtype=str).fillna("")
    df.columns = df.columns.str.strip()

    reg_input = reg_input.strip()
    df["رقم القيد"] = df["رقم القيد"].str.strip()

    result = df[df["رقم القيد"] == reg_input]

    if not result.empty:
        row = result.iloc[0]

        hall = row.get("القاعة الامتحانية", "").strip()
        hall_display = hall if hall else "لم تُحدد بعد"

        st.success("تم العثور على بيانات الطالب")

        with st.container():
            st.markdown('<div class="block">', unsafe_allow_html=True)

            col1, col2 = st.columns([2, 3])
            col1.markdown("**اسم الطالب**")
            col2.markdown(row.get("اسم الطالب", ""))

            col1, col2 = st.columns([2, 3])
            col1.markdown("**رقم القيد**")
            col2.markdown(row.get("رقم القيد", ""))

            col1, col2 = st.columns([2, 3])
            col1.markdown("**رقم الجلوس**")
            col2.markdown(row.get("رقم الجلوس", ""))

            col1, col2 = st.columns([2, 3])
            col1.markdown("**السنة الدراسية**")
            col2.markdown(row.get("السنة الدراسية", ""))

            col1, col2 = st.columns([2, 3])
            col1.markdown("**القاعة الامتحانية**")
            col2.markdown(hall_display)

            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("❌ رقم القيد غير موجود")

# ===============================
# التذييل
# ===============================
st.divider()
st.markdown("**إعداد: الأستاذ عبدالفتاح محمد البكوش**")
st.markdown("© جامعة المرقب – كلية العلوم الصحية")
