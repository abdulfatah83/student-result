import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# =========================
# إعداد الصفحة (Mobile Friendly)
# =========================
st.set_page_config(
    page_title="الاستعلام عن رقم الجلوس",
    layout="centered"
)

# =========================
# CSS احترافي + Responsive
# =========================
st.markdown("""
<style>
body {
    font-family: 'Cairo', sans-serif;
}
.container {
    max-width: 650px;
    margin: auto;
}
.header {
    text-align: center;
    color: #0b3c5d;
}
.sub-header {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}
.result-card {
    background-color: #f9fafb;
    padding: 22px;
    border-radius: 12px;
    border-right: 6px solid #0b5ed7;
    direction: rtl;
}
.result-item {
    font-size: 18px;
    margin-bottom: 10px;
}
.footer {
    text-align: center;
    margin-top: 35px;
    color: #555;
    font-size: 16px;
}
@media (max-width: 600px) {
    .result-item { font-size: 16px; }
    h1 { font-size: 22px; }
    h2 { font-size: 18px; }
    h3 { font-size: 16px; }
}
</style>
""", unsafe_allow_html=True)

# =========================
# دالة إنشاء PDF
# =========================
def generate_pdf(student):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "جامعة المرقب")
    c.setFont("Helvetica", 14)
    c.drawCentredString(
        width / 2, height - 80,
        "كلية العلوم الصحية – قسم المختبرات الطبية"
    )

    c.line(50, height - 100, width - 50, height - 100)

    c.setFont("Helvetica", 12)
    y = height - 150

    fields = [
        ("اسم الطالب", student["name"]),
        ("رقم القيد", student["reg"]),
        ("رقم الجلوس", student["seat"]),
        ("السنة الدراسية", student["year"]),
        ("القاعة الامتحانية", student["hall"]),
    ]

    for label, value in fields:
        c.drawRightString(width - 60, y, f"{label} : {value}")
        y -= 30

    c.line(50, y - 10, width - 50, y - 10)

    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(
        width / 2, 60,
        "إعداد: الأستاذ عبدالفتاح محمد البكوش"
    )

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# =========================
# واجهة التطبيق
# =========================
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>جامعة المرقب</h1>
    <h2>كلية العلوم الصحية</h2>
    <h3>قسم المختبرات الطبية</h3>
</div>
<div class="sub-header">
    الاستعلام عن رقم الجلوس
</div>
""", unsafe_allow_html=True)

reg_input = st.text_input("أدخل رقم القيد", max_chars=12)

if st.button("🔍 بحث"):
    # بيانات تجريبية (استبدلها لاحقًا بـ Excel)
    if reg_input == "222031353":
        student = {
            "name": "خالد جمال حسين البريدان",
            "reg": "222031353",
            "seat": "300",
            "year": "السنة الثانية",
            "hall": "القاعة الرئيسية"
        }

        st.success("✅ تم العثور على البيانات")

        st.markdown(f"""
        <div class="result-card">
            <div class="result-item"><strong>👤 اسم الطالب:</strong> {student["name"]}</div>
            <div class="result-item"><strong>🆔 رقم القيد:</strong> {student["reg"]}</div>
            <div class="result-item"><strong>🪑 رقم الجلوس:</strong> {student["seat"]}</div>
            <div class="result-item"><strong>📚 السنة الدراسية:</strong> {student["year"]}</div>
            <div class="result-item"><strong>🏫 القاعة الامتحانية:</strong> {student["hall"]}</div>
        </div>
        """, unsafe_allow_html=True)

        pdf = generate_pdf(student)

        st.download_button(
            label="🖨️ طباعة / تحميل PDF",
            data=pdf,
            file_name="رقم_الجلوس.pdf",
            mime="application/pdf"
        )
    else:
        st.error("❌ لم يتم العثور على رقم القيد")

st.markdown("""
<div class="footer">
    إعداد: الأستاذ عبدالفتاح محمد البكوش
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
