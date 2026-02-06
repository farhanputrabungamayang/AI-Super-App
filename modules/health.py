import streamlit as st
import google.generativeai as genai
from PIL import Image
from modules import styles

def run_health_companion():
    styles.header("🩺 AI Health Companion", "Asisten kesehatan pribadi dalam saku Anda.")
    
    # Alert Box yang lebih cantik
    st.info("👋 **Disclaimer:** AI ini hanya untuk informasi awal. Tetap konsultasi ke dokter untuk diagnosa medis.")

    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    tab1, tab2 = st.tabs(["🤒 Cek Gejala", "🥗 Cek Nutrisi"])

    with tab1:
        col_in, col_res = st.columns([1, 1])
        with col_in:
            st.subheader("Keluhan Anda")
            gejala = st.text_area("Deskripsikan gejala...", height=150)
            btn_analisa = st.button("🏥 Analisa Medis", use_container_width=True)

        with col_res:
            if btn_analisa and gejala:
                with st.spinner("Menganalisa basis data medis..."):
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        prompt = f"Analisa gejala: {gejala}. Format markdown rapi dengan emoji."
                        response = model.generate_content(prompt)
                        
                        with st.container(border=True):
                            st.markdown(response.text)
                    except Exception as e:
                        st.error(str(e))
            elif btn_analisa:
                st.warning("Mohon isi keluhan dulu.")

    with tab2:
        col_img, col_nut = st.columns([1, 1])
        with col_img:
            st.subheader("Foto Makanan")
            upl = st.file_uploader("Upload", type=['jpg','png'], label_visibility="collapsed")
            if upl:
                st.image(upl, use_container_width=True)
                btn_nutrisi = st.button("🥦 Hitung Kalori", use_container_width=True)
        
        with col_nut:
            if upl and btn_nutrisi:
                with st.spinner("Menghitung nutrisi..."):
                    try:
                        img = Image.open(upl)
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        prompt = "Tabel nutrisi lengkap (Kalori, Protein, Lemak, Karbo) dari makanan ini. Dan 1 tips singkat."
                        res = model.generate_content([prompt, img])
                        
                        with st.container(border=True):
                            st.markdown(res.text)
                    except Exception as e:
                        st.error(str(e))