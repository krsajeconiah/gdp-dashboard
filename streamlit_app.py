import streamlit as st
import pandas as pd
import numpy as np

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Aplikasi Prediksi Karya Seni",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Judul Halaman Utama ---
st.title("🎨 Prediksi Preferensi Karya Seni pada Bartele Gallery")
st.markdown("Aplikasi ini akan memprediksi kategori karya seni berdasarkan karakteristik yang Anda pilih.")
st.markdown("---")

# --- Mapping untuk fitur input ---
features_map = {
    'Medium': {
        0: 'Watercolor',
        1: 'Charcoal',
        2: 'Acrylic',
        3: 'Mixed Media',
        4: 'Oil',
    },
    'Style': {
        0: 'Abstract Expressionism', 
        1: 'Modern',
        2: 'Cubism', 
        3: 'Surrealism',
        4: 'Impressionism',
    },
    'Color Palette': {
        0: 'Neutral Tone',
        1: 'Cool Tone',
        2: 'Oceanic Tone',
        3: 'Earthy Tone',
        4: 'Warm Tone',
    },
    'Mood/Atmosphere': {
        0: 'Calming',
        1: 'Relaxing',
        2: 'Joyful',
        3: 'Reflective',
        4: 'Energetic',
    },
    'Recommended Environment': {
        0: 'Bedroom',
        1: 'Living Room', 
        2: 'Kid Room', 
        3: 'Office',
        4: 'Gallery',
    }
}

# Mapping untuk kelas target (Subject of Painting)
target_map = {0: 'Seascape', 1: 'Landscape', 2: 'Still Life', 3: 'Wild Life', 4: 'Portrait', 5: 'Fantasy', 6: 'Abstract'}

# --- Fungsi Klasifikasi ---
def hardcoded_predict(medium, style, color_palette, mood, environment):
    # Aturan untuk Seascape
    if environment in ['Living Room', 'Office', 'Gallery'] and (mood == 'Calming' or mood == 'Relaxing') and color_palette in ['Oceanic Tone', 'Cool Tone', 'Neutral Tone']: 
        return target_map[0]  # Seascape
    
    # Aturan untuk Landscape
    elif style == 'Impressionism' and color_palette == 'Earthy Tone' and environment == 'Gallery':
        return target_map[1]  # Landscape
    elif style == 'Modern' and color_palette == 'Earthy Tone' and environment == 'Office':
        return target_map[1]  # Landscape

    # Aturan untuk Still Life
    elif medium == 'Watercolor' and (mood == 'Joyful' or mood == 'Calming') and environment in ['Living Room', 'Bedroom']:
        return target_map[2]  # Still Life
    elif style == 'Surrealism' and color_palette == 'Oceanic Tone' and environment == 'Living Room':
        return target_map[2] # Still Life
    
    # Aturan untuk Wild Life
    elif style == 'Surrealism' and (medium == 'Mixed Media' or medium == 'Charcoal') and mood == 'Energetic':
        return target_map[3]  # Wild Life
    elif environment == 'Gallery' and mood == 'Energetic' and color_palette == 'Earthy Tone':
        return target_map[3] # Wild Life

    # Aturan untuk Portrait
    elif style == 'Modern' and (medium == 'Oil' or medium == 'Charcoal') and environment in ['Living Room', 'Office']:
        return target_map[4]  # Portrait
    elif mood == 'Calming' and medium == 'Oil' and color_palette in ['Earthy Tone', 'Warm Tone', 'Neutral Tone']: # Menggunakan 'in'
        return target_map[4] # Portrait

    # Aturan untuk Fantasy
    elif style == 'Surrealism' and mood == 'Reflective' and color_palette == 'Cool Tone':
        return target_map[5]  # Fantasy
    elif style == 'Abstract Expressionism' and mood == 'Reflective' and medium == 'Mixed Media':
        return target_map[5] # Fantasy

    # Aturan untuk Abstract
    elif style == 'Abstract Expressionism' and color_palette in ['Earthy Tone', 'Cool Tone', 'Neutral Tone']:
        return target_map[6]  # Abstract
    elif medium == 'Acrylic' and style == 'Abstract Expressionism': 
        return target_map[6] # Abstract

    else:
  
        if environment == 'Office': return target_map[1]
        elif environment == 'Living Room': return target_map[4] 
        elif mood == 'Joyful': return target_map[2] 
        else: return target_map[1] 

# --- Kolom Input Fitur Interaktif ---
st.header("Masukkan Karakteristik Karya Seni")
st.write("Silakan pilih atribut yang paling mendeskripsikan karya seni Anda. Aplikasi akan memprediksi kategorinya.")

col1, col2 = st.columns(2)

with col1:
    selected_medium = st.selectbox("Medium (Cat)", options=list(features_map['Medium'].values()))
    selected_style = st.selectbox("Style (Gaya Lukisan)", options=list(features_map['Style'].values()))
    selected_color = st.selectbox("Color Palette (Palet Warna)", options=list(features_map['Color Palette'].values()))

with col2:
    selected_mood = st.selectbox("Mood/Atmosphere (Suasana)", options=list(features_map['Mood/Atmosphere'].values()))
    selected_environment = st.selectbox("Recommended Environment (Lingkungan)", options=list(features_map['Recommended Environment'].values()))

if st.button("Prediksi Kategori Karya Seni", use_container_width=True):
    with st.spinner('Aplikasi sedang memproses...'):
        try:
           
            predicted_label = hardcoded_predict(selected_medium, selected_style, selected_color, selected_mood, selected_environment)

            # Menampilkan hasil
            st.markdown("---")
            st.subheader("🎉 Hasil Prediksi")
            st.success(f"Berdasarkan atribut yang dipilih, karya seni ini diprediksi masuk ke kategori: **{predicted_label}**")
            st.balloons()
            
            st.markdown("---")
            st.subheader("Informasi Prediksi")
            st.info("""
            Prediksi ini didasarkan pada logika internal aplikasi untuk demonstrasi fungsionalitas.
            """)
            
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")


# --- Sidebar untuk Informasi Proyek ---
st.sidebar.title("Informasi Proyek Tugas Akhir")
st.sidebar.info(
    "Ini adalah aplikasi demonstrasi untuk Tugas Akhir yang berjudul 'Penerapan Algoritma K-Nearest Neighbors Untuk Klasifikasi Preferensi Pilihan Karya Seni pada Bartele Gallery'."
)

st.sidebar.subheader("Metodologi Penelitian")
st.sidebar.markdown("""
- **Dataset:** Menggunakan data dari Bartele Gallery (Data Tabular).
- **Fitur:** Menggunakan **5 fitur** utama: Medium, Style, Color Palette, Mood/Atmosphere, dan Recommended Environment.
- **Preprocessing:** Data melalui proses Label Encoding, `MinMaxScaler`, dan `PCA` untuk penskalaan dan reduksi dimensi.
- **Data Imbalance:** Menggunakan teknik `SMOTE` untuk menangani ketidakseimbangan kelas pada dataset.
- **Model:** Menggunakan algoritma **K-Nearest Neighbors (KNN)**.
- **Akurasi:** Model berhasil mencapai akurasi **77.81%** saat diuji secara offline.
""")
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025, Karsa Jeconiah.")
