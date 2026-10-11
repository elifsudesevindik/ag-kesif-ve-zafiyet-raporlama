import streamlit as st
import pandas as pd
from main import main
from pdf import pdf_olustur
from servisler import servis_bilgileri

st.title("Ağ Güvenlik Analiz Sistemi")

# 1. VERİYİ ÇEK
@st.cache_data
def veri_yukle():
    return main()

data = veri_yukle()

# 2. GÖSTER
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Tarama Sonuçları")
with col2:
    if st.button("PDF Rapor Oluştur"):
        pdf_olustur(data)
        with open("rapor.pdf", "rb") as f:
            st.download_button(
                label="PDF indir",
                data=f,
                file_name="rapor.pdf",
             mime="application/pdf"
            )
        st.success("PDF başarıyla oluşturuldu!")


df = pd.DataFrame(data)[["service", "version", "cvss", "risk"]]
df.columns = ["Servis", "Versiyon", "CVSS", "Risk"]

tablo = []
for servis in data:
    tablo.append({
        "Port": servis.get("port", "—"),
        "Servis": servis["service"],
        "Versiyon": servis["version"] or "—",
        "CVSS": servis["cvss"],
        "Risk": servis["risk"],
    })
# DETAYLAR
st.dataframe(pd.DataFrame(tablo), use_container_width=True, hide_index=True, height=600)
st.subheader("Servis Detayları")
for servis in data:
    bilgi = servis_bilgileri.get(servis["service"], {})
    with st.expander(f"{servis['service']} — {servis['risk']}"):
        st.write("**Port:**", servis.get("port", "—"))
        st.write("**Tanım:**", bilgi.get("tanim", "—"))
        st.write("**Risk:**", bilgi.get("risk", "—"))
        st.write("**Öneri:**", bilgi.get("oneri", "—"))




# 4. İSTEĞE BAĞLI ÖZET
st.write("Toplam servis:", len(data))
