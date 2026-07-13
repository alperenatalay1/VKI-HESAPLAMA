import random
import streamlit as st

sehirler = {
    "Adana": "01", "Adıyaman": "02", "Afyonkarahisar": "03", "Ağrı": "04", "Amasya": "05",
    "Ankara": "06", "Antalya": "07", "Artvin": "08", "Aydın": "09", "Balıkesir": "10",
    "Bilecik": "11", "Bingöl": "12", "Bitlis": "13", "Bolu": "14", "Burdur": "15",
    "Bursa": "16", "Çanakkale": "17", "Çankırı": "18", "Çorum": "19", "Denizli": "20",
    "Diyarbakır": "21", "Edirne": "22", "Elazığ": "23", "Erzincan": "24", "Erzurum": "25",
    "Eskişehir": "26", "Gaziantep": "27", "Giresun": "28", "Gümüşhane": "29", "Hakkari": "30",
    "Hatay": "31", "Isparta": "32", "Mersin": "33", "İstanbul": "34", "İzmir": "35",
    "Kars": "36", "Kastamonu": "37", "Kayseri": "38", "Kırklareli": "39", "Kırşehir": "40",
    "Kocaeli": "41", "Konya": "42", "Kütahya": "43", "Malatya": "44", "Manisa": "45",
    "Kahramanmaraş": "46", "Mardin": "47", "Muğla": "48", "Muş": "49", "Nevşehir": "50",
    "Niğde": "51", "Ordu": "52", "Rize": "53", "Sakarya": "54", "Samsun": "55",
    "Siirt": "56", "Sinop": "57", "Sivas": "58", "Tekirdağ": "59", "Tokat": "60",
    "Trabzon": "61", "Tunceli": "62", "Şanlıurfa": "63", "Uşak": "64", "Van": "65",
    "Yozgat": "66", "Zonguldak": "67", "Aksaray": "68", "Bayburt": "69", "Karaman": "70",
    "Kırıkkale": "71", "Batman": "72", "Şırnak": "73", "Bartın": "74", "Ardahan": "75",
    "Iğdır": "76", "Yalova": "77", "Karabük": "78", "Kilis": "79", "Osmaniye": "80",
    "Düzce": "81"
}

if "sorulan_sehir" not in st.session_state:
    st.session_state["sorulan_sehir"] = random.choice(list(sehirler.keys()))
    st.session_state["dogru_cevap"] = sehirler[st.session_state["sorulan_sehir"]]
    
    tum_plakalar = list(sehirler.values())
    tum_plakalar.remove(st.session_state["dogru_cevap"])
    
    yanlis_siklar = random.sample(tum_plakalar, 3)
    yanlis_siklar.append(st.session_state["dogru_cevap"])
    random.shuffle(yanlis_siklar)
    st.session_state["siklar"] = yanlis_siklar

sorulan_sehir = st.session_state["sorulan_sehir"]
dogru_cevap = st.session_state["dogru_cevap"]
siklar = st.session_state["siklar"]

st.title(f"🤔 {sorulan_sehir} ilinin plakası nedir?")

secim = st.radio("Cevabınızı seçiniz:", siklar)

if st.button("Cevabı Kontrol Et"):
    if secim == dogru_cevap:
        st.success("🎉 Tebrikler! Doğru cevap.")
    else:
        st.error(f"❌ Yanlış cevap! Doğru cevap {dogru_cevap} olmalıydı.")

if st.button("Yeni Soru Getir ➡️"):
    del st.session_state["sorulan_sehir"]
    del st.session_state["dogru_cevap"]
    del st.session_state["siklar"]
    st.rerun()
