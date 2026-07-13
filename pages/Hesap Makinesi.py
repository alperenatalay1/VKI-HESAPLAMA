import streamlit as st
st.markdown(
    """
    <style>
    /* Tüm sayfanın arka planı (Facebook Gri/Mavi Fonu) */
    .stApp {
        background-color: #f0f2f5 !important;
    }
    
    /* Başlıklar ve Yazı Renkleri (Facebook Koyu Lacivert/Siyah Yazı Tonu) */
    h1, h2, h3, p, span, label {
        color: #050505 !important;
        font-family: Segoe UI, Helvetica, Arial, sans-serif !important;
    }
    
    /* Butonların Tasarımı (Orijinal Facebook Mavisi) */
    div.stButton > button:first-child {
        background-color: #1877f2 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.5rem 1rem !important;
        border-radius: 6px !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Butonun üzerine fareyle gelindiğinde (Koyu Mavi Hover Efekti) */
    div.stButton > button:first-child:hover {
        background-color: #166fe5 !important;
        color: #ffffff !important;
    }
    
    /* Giriş kutularının beyaz fonu ve yuvarlak hatları */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        border-radius: 6px !important;
        border: 1px solid #ced4da !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def topla(a, b):
    return a + b
def çıkar(a, b):
    return a - b
def çarp(a, b):
    return a * b
def böl(a, b):
    if b == 0:
        return "Tanımsız (Sıfıra bölünemez!)"
    return a / b

st.title("🧮 Hesap Makinesine Hoş Geldiniz")

a = st.number_input("LÜTFEN BİR SAYI GİRİNİZ: ", value=0)
işlem = st.selectbox("BİR İŞLEM SEÇİNİZ: ", ["+", "-", "x", "/"])
# Düzeltilen satır:
b = st.number_input("LÜTFEN İKİNCİ SAYIYI GİRİNİZ: ", value=0)

if st.button("Hesapla"):
    if işlem == "+":
        st.success(f"SONUÇ: {topla(a, b)}")
    elif işlem == "-":
        st.success(f"SONUÇ: {çıkar(a, b)}")
    elif işlem == "x":
        st.success(f"SONUÇ: {çarp(a, b)}")
    elif işlem == "/":
        st.success(f"SONUÇ: {böl(a, b)}")
    else:
        st.error("Geçersiz bir işlem seçtiniz.")
