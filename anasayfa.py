import streamlit as st

# 1. Matematiksel hesaplama fonksiyonumuz (Aynen duruyor)
def vki(kilo, boy):
    return kilo / ((boy / 100) ** 2)

# 2. Web Sitesinin Başlığı ve İsmi
st.title("🦷 Dental & Sağlık Asistanım")
st.subheader("Vücut Kitle İndeksi (VKİ) Hesaplayıcı")

st.write("Lütfen aşağıdaki bilgileri doldurarak 'Hesapla' butonuna basınız.")

# 3. Web Sitesindeki Giriş Kutuları (input yerine st.number_input kullanıyoruz)
kilo = st.number_input("Kilonuzu giriniz (kg):", min_value=1.0, max_value=250.0, value=70.0)
boy = st.number_input("Boyunuzu cm cinsinden giriniz:", min_value=50.0, max_value=250.0, value=170.0)

# 4. Web Sitesindeki Buton ve Sonuç Ekranı
if st.button("Hesapla"):
    sonuc = vki(kilo, boy)
    
    # Sonucu ekrana kalın ve virgülden sonra 2 basamak olarak yazdırıyoruz
    st.write(f"### Sizin VKİ Sonucunuz: **{sonuc:.2f}**")
    
    # Koşullara göre renkli kutular içinde uyarılar veriyoruz
    if sonuc < 18.5:
        st.warning("Durum: Zayıfsınız. Beslenmenize dikkat etmelisiniz.")
    elif sonuc < 24.9:
        st.success("Durum: Harika! İdeal kilodasınız. :)")
    elif sonuc < 29.9:
        st.info("Durum: Kilolusunuz. Dengeli beslenmeye özen gösterin.")
    else:
        st.error("Durum: Obez sınıfındasınız. Bir uzmana danışmanız iyi olabilir.")
