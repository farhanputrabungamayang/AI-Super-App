import streamlit as st
import google.generativeai as genai
import os
import time
from modules import styles

def run_meeting_notetaker():
    styles.header("🎙️ AI Meeting Notetaker", "Ubah rekaman suara jadi notulen rapi.")

    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    upl = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a"])
    
    if upl:
        st.audio(upl)
        if st.button("📝 Proses Audio", use_container_width=True):
            # Menggunakan st.status untuk log proses yang keren
            with st.status("Sedang memproses...", expanded=True) as status:
                try:
                    st.write("📥 Menyimpan file sementara...")
                    temp_filename = "temp.mp3"
                    with open(temp_filename, "wb") as f:
                        f.write(upl.getbuffer())

                    st.write("☁️ Mengupload ke Brain AI...")
                    audio_file = genai.upload_file(path=temp_filename)
                    while audio_file.state.name == "PROCESSING":
                        time.sleep(1)
                        audio_file = genai.get_file(audio_file.name)

                    st.write("🧠 AI sedang mendengar & merangkum...")
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    response = model.generate_content(["Buat notulen rapat detail bahasa indonesia.", audio_file])
                    
                    status.update(label="✅ Selesai!", state="complete", expanded=False)
                    
                    st.divider()
                    st.markdown("### 📄 Hasil Notulen")
                    with st.container(border=True):
                        st.markdown(response.text)
                    
                    # Cleanup
                    genai.delete_file(audio_file.name)
                    os.remove(temp_filename)

                except Exception as e:
                    status.update(label="❌ Error", state="error")
                    st.error(f"Error: {e}")