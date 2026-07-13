import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fafafa !important;
    }
    h1, h2, h3 {
        color: #a9043a !important;
    }
    div.stButton > button:first-child {
        background-color: #fdb912 !important;
        color: #a9043a !important;
        border: 2px solid #a9043a !important;
        font-weight: bold !important;
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
