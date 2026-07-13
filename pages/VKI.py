import streamlit as st
def vki(kilo, boy):
    return kilo / ((boy / 100) ** 2)
st.title("VKİ HESAPLAMA")
st.subheader("Vücut Kitle İndeksi (VKİ) Hesaplayıcı")
st.write("Lütfen aşağıdaki bilgileri doldurarak 'Hesapla' butonuna basınız.")
kilo = st.number_input("Kilonuzu giriniz (kg):", min_value=1.0, max_value=250.0, value=70.0)
boy = st.number_input("Boyunuzu cm cinsinden giriniz:", min_value=50.0, max_value=250.0, value=170.0)
if st.button("Hesapla"):
    sonuc = vki(kilo, boy)
    st.write(f"### Sizin VKİ Sonucunuz: **{sonuc:.2f}**")
    if sonuc < 18.5:
        st.warning("Durum: Zayıfsınız. Beslenmenize dikkat etmelisiniz.")
    elif sonuc < 24.9:
        st.success("Durum: Harika! İdeal kilodasınız. :)")
    elif sonuc < 29.9:
        st.info("Durum: Kilolusunuz. Dengeli beslenmeye özen gösterin.")
    else:
        st.error("Durum: Obez sınıfındasınız. Bir uzmana danışmanız iyi olabilir.")
        st.set_page_config()
st.sidebar.markdown("# 🏠 VKİ")
