import streamlit as st
import google.generativeai as genai
from PIL import Image
import pandas as pd
import json
import time
from modules import styles # Import Style

def run_expense_tracker():
    styles.header("🧾 AI Expense Tracker", "Scan struk belanjaan dalam hitungan detik.")

    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("API Key Missing!")
        return

    c1, c2 = st.columns([1, 2])
    
    with c1:
        uploaded_file = st.file_uploader("Upload Struk", type=["jpg", "png"], label_visibility="collapsed")
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Preview Struk", use_container_width=True)
    
    with c2:
        if uploaded_file and st.button("🔍 Analisa Sekarang", use_container_width=True):
            with st.status("🤖 AI sedang bekerja...", expanded=True) as status:
                try:
                    st.write("Membaca gambar...")
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = """
                    Analisa struk ini. Output JSON murni:
                    { "toko": "...", "tanggal": "...", "total": 0, "kategori": "...", "items": [{"nama": "...", "harga": 0}] }
                    """
                    response = model.generate_content([prompt, image])
                    
                    st.write("Menyusun data...")
                    text = response.text.replace("```json", "").replace("```", "")
                    data = json.loads(text)
                    
                    status.update(label="✅ Selesai!", state="complete", expanded=False)
                    
                    # --- UI HASIL KEREN ---
                    st.success("Berhasil Mengekstrak Data!")
                    
                    # Kartu Ringkasan
                    with st.container(border=True):
                        col_a, col_b, col_c = st.columns(3)
                        col_a.metric("Toko", data.get('toko', '-'))
                        col_b.metric("Tanggal", data.get('tanggal', '-'))
                        col_c.metric("Total", f"Rp {data.get('total', 0):,}")
                    
                    # Tabel Detail
                    st.subheader("🛒 Item Belanja")
                    if "items" in data:
                        st.dataframe(
                            pd.DataFrame(data["items"]),
                            use_container_width=True,
                            hide_index=True
                        )

                except Exception as e:
                    status.update(label="❌ Gagal", state="error")
                    st.error(f"Error: {e}")
        elif not uploaded_file:
            st.info("👈 Silakan upload foto struk di sebelah kiri.")