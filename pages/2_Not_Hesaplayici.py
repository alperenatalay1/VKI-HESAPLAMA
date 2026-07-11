import streamlit as st

# 1. Ortalamayı hesaplayan fonksiyon
def ortalama_hesaplama(vize1, vize2, final):
    return (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)

# 2. Sayfa Başlığı
st.title("🎓 Akademik Not Hesaplama Modülü")
st.write("Vize ve Final notlarınızı girerek ders geçme durumunuzu kontrol edebilirsiniz.")

# 3. Giriş Kutuları
vize1 = st.number_input("VİZE 1 Notunu Giriniz:", min_value=0.0, max_value=100.0, value=60.0)
vize2 = st.number_input("VİZE 2 Notunu Giriniz:", min_value=0.0, max_value=100.0, value=60.0)
final = st.number_input("FİNAL Notunu Giriniz:", min_value=0.0, max_value=100.0, value=60.0)

# 4. Hesaplama Butonu ve Sonuç
if st.button("Hesapla ve Kontrol Et"):
    sonuc = ortalama_hesaplama(vize1, vize2, final)
    st.write(f"### Ders Ortalamanız: **{sonuc:.2f}**")
    
    if final >= 60 and sonuc >= 60:
        st.success(f"🎉 Tebrikler! **{sonuc:.2f}** notu ile dersi başarıyla geçtiniz.")
    else:
        st.error("❌ Maalesef dersi geçebilmeniz için gerekli şartlar sağlanamadı (Final veya ortalama 60'ın altında).")
