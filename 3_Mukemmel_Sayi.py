import streamlit as st

# 1. Mükemmel sayı kontrolü yapan fonksiyonun
def mukemmel(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi

# 2. Sayfa Başlığı ve Açıklaması
st.title("🔢 Mükemmel Sayı Bulucu")
st.write("Gireceğiniz sayıya kadar olan tüm mükemmel sayıları listeler.")
st.caption("Not: Mükemmel sayı, kendisi hariç pozitif bölenlerinin toplamına eşit olan sayıdır (Örn: 6 = 1 + 2 + 3).")

# 3. Web Giriş Kutusu (Kullanıcıdan sınır sayısını alıyoruz)
sinir_sayisi = st.number_input("Bir sınır sayısı giriniz:", min_value=2, max_value=10000000000000000000000000, value=100, step=1)

# 4. Hesaplama Butonu ve Sonuç Ekranı
if st.button("Mükemmel Sayıları Listele"):
    mukemmel_sayilar = []
    
    # Girdiğin sayıya kadar olan sayıları tarıyoruz
    for i in range(1, sinir_sayisi):
        if mukemmel(i):
            mukemmel_sayilar.append(i)
            
    # Sonuçları ekrana yazdırma
    if mukemmel_sayilar:
        st.success(f"**1 ile {sinir_sayisi} arasındaki mükemmel sayılar:**")
        # Sayıları yan yana şık bir şekilde listeliyoruz
        st.write(", ".join(map(str, mukemmel_sayilar)))
    else:
        st.info(f"1 ile {sinir_sayisi} arasında herhangi bir mükemmel sayı bulunamadı.")
