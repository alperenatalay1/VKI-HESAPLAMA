import streamlit as st

# 1. Yazdığın Matematiksel Fonksiyon
def gereken_final_notu(v1, v2):
    vize = ((v1 + v2) / 2) * 0.4
    return (60 - vize) / 0.6

# 2. Web Sayfası Başlıkları
st.title("🎯 Hedef Final Notu Hesaplayıcı")
st.write("Dersi geçebilmek için final sınavından **en az kaç almanız gerektiğini** hesaplar.")
st.write("---")

# 3. Kullanıcıdan Notları Alan Web Kutuları
v1 = st.number_input("1. Vize Notunuzu Giriniz:", min_value=0.0, max_value=100.0, value=60.0, step=1.0)
v2 = st.number_input("2. Vize Notunuzu Giriniz:", min_value=0.0, max_value=100.0, value=60.0, step=1.0)

# 4. Hesaplama Butonu ve Senin Kurduğun Doğru Şart Sıralaması
if st.button("Gereken Final Notunu Hesapla"):
    f = gereken_final_notu(v1, v2)
    
    # Virgülden sonra tek basamağa yuvarlama (İstediğin özellik)
    temiz_f = round(f, 1)
    
    # IDLE'da kurduğun doğru if-elif-else mantığı:
    if f > 100:
        st.error(f"⚠️ Gereken not {temiz_f} olduğu için 100 alsanız bile dersi geçemiyorsunuz :(")
        
    elif f < 60:
        st.info("ℹ️ Finalden almanız gereken not üniversite kuralı gereği en az 60'tır.")
        
    else:
        st.success(f"🎉 Dersi geçebilmek için Final sınavından en az **{temiz_f}** almalısınız.")
