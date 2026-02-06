import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* CSS untuk Judul Gradient */
        .title-text {
            background: linear-gradient(to right, #00ADB5, #00FFF5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 3rem;
            padding-bottom: 20px;
        }
        
        /* CSS untuk Card/Container */
        .st-emotion-cache-1r6slb0, .st-emotion-cache-12w0qpk {
            border-radius: 15px;
            border: 1px solid #00ADB5;
            background-color: #393E46;
        }

        /* Tombol Biar Glowing */
        .stButton > button {
            background: linear-gradient(45deg, #00ADB5, #393E46);
            color: white;
            border-radius: 10px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 15px rgba(0, 173, 181, 0.4);
        }

        /* Metric Value */
        div[data-testid="stMetricValue"] {
            color: #00FFF5;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

def header(judul, subjudul):
    st.markdown(f'<h1 class="title-text">{judul}</h1>', unsafe_allow_html=True)
    st.markdown(f"##### {subjudul}")
    st.markdown("---")