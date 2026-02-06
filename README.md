# ⚡ AI Super App

Aplikasi produktivitas All-in-One yang ditenagai oleh **Google Gemini 2.5 Flash**. Menggabungkan kemampuan Computer Vision, Audio Processing, dan Contextual AI dalam satu dashboard modern.

🔗 **Live Demo:** [Klik Disini Untuk Mencoba](https://ai-super-app-project.streamlit.app/)

## 🌟 Fitur Utama

### 1. 🧾 AI Expense Tracker (Dompet Pintar)
- **Teknologi:** OCR & Vision AI.
- **Fungsi:** Upload foto struk belanja, AI mengekstrak nama toko, tanggal, item, dan total harga ke dalam tabel rapi.

### 2. 🎙️ AI Meeting Notetaker (Notulen Otomatis)
- **Teknologi:** Audio Processing & Speech-to-Text.
- **Fungsi:** Upload rekaman rapat, AI membuat ringkasan, transkrip, dan *action items*.

### 3. 🩺 AI Health Companion
- **Teknologi:** Multimodal AI & Context Awareness.
- **Fungsi:** Analisa gejala medis awal dan deteksi nutrisi/kalori dari foto makanan.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **AI Model:** Google Gemini 2.5 Flash (via Google Gen AI SDK)
- **Data Processing:** Pandas & JSON
- **Styling:** Custom CSS (Glassmorphism & Dark Mode)

## 🚀 Cara Menjalankan di Lokal

1. Clone repository ini.
2. Install library:
   ```bash
   pip install -r requirements.txt
3. Buat file .streamlit/secrets.toml dan isi API Key.
   ```GOOGLE_API_KEY = "API_KEY_KAMU"
4. Jalankan aplikasi: streamlit run app.py

Created with ☕ by Farhan
