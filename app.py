import streamlit as st
from modules import expense, meeting, health, styles

# Config Page
st.set_page_config(page_title="AI Super App", page_icon="⚡", layout="wide")

# Load Custom CSS
styles.load_css()

# Sidebar yang lebih Clean
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80) # Icon Robot Placeholder
    st.title("⚡ AI Super App")
    st.caption("v2.5.0 | Powered by Gemini")
    
    st.markdown("---")
    
    menu = st.radio("Navigasi:", [
        "🏠 Home Dashboard",
        "🧾 Expense Tracker",
        "🎙️ Meeting Notetaker",
        "🩺 Health Companion"
    ])
    
    st.markdown("---")
    st.info("💡 **Tips:** Gunakan Dark Mode untuk pengalaman terbaik.")

# Logic Menu
if menu == "🏠 Home Dashboard":
    styles.header("Welcome, Masbro!", "Pilih AI Assistant yang kamu butuhkan hari ini.")
    
    # Grid Layout 3 Kolom
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.write("### 🧾 Keuangan")
            st.write("Malas catat pengeluaran? Foto struknya, biar AI yang input data.")
            if st.button("Buka Expense Tracker"):
                menu = "🧾 Expense Tracker" # (Hanya trigger visual, user harus klik sidebar manual di streamlit native)
                
    with col2:
        with st.container(border=True):
            st.write("### 🎙️ Produktivitas")
            st.write("Meeting panjang bikin ngantuk? AI akan mencatat & merangkumnya.")
            st.button("Buka Notetaker")

    with col3:
        with st.container(border=True):
            st.write("### 🩺 Kesehatan")
            st.write("Cek gejala sakit atau hitung kalori makananmu dalam sekejap.")
            st.button("Buka Health AI")

elif menu == "🧾 Expense Tracker":
    expense.run_expense_tracker()

elif menu == "🎙️ Meeting Notetaker":
    meeting.run_meeting_notetaker()

elif menu == "🩺 Health Companion":
    health.run_health_companion()