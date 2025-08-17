# Proyek Tugas Akhir: Aplikasi Prediksi Preferensi Karya Seni pada Bartele Gallery

## Ikhtisar Proyek

Aplikasi ini merupakan bagian dari proyek Tugas Akhir di jurusan Teknik Informatika. Tujuan utamanya adalah untuk mendemonstrasikan penerapan algoritma _Machine Learning_, khususnya K-Nearest Neighbors (KNN), dalam mengklasifikasikan preferensi karya seni.

Model yang dikembangkan berhasil mencapai akurasi **77.81%** dalam memprediksi kategori karya seni berdasarkan empat fitur utama: `Medium`, `Style`, `Color Palette`, dan `Mood/Atmosphere`. Aplikasi web ini dibuat menggunakan Streamlit untuk memvisualisasikan dan berinteraksi dengan model secara langsung.

## Metodologi

1.  **Pengumpulan Data:** Data mentah diperoleh dari Bartele Gallery, berisi atribut-atribut karya seni dan preferensi pengunjung.
2.  **Pra-pemrosesan Data:**
    * Data kategorikal dikonversi menjadi numerik menggunakan One-Hot Encoding.
    * Menggunakan **MinMaxScaler** untuk penskalaan fitur.
    * Menerapkan **Principal Component Analysis (PCA)** untuk mereduksi dimensi dan menghilangkan korelasi antar fitur.
    * Menggunakan teknik **SMOTE** untuk mengatasi masalah ketidakseimbangan kelas pada data.
3.  **Pelatihan Model:** Model KNN dilatih menggunakan data yang sudah diproses untuk mengklasifikasikan `Subject of Painting`.
4.  **Deployment:** Model yang sudah dilatih disimpan dalam format `.pkl` dan di-deploy ke aplikasi web Streamlit.

## Cara Menjalankan Aplikasi

### Persyaratan Lingkungan
Aplikasi ini membutuhkan Python 3.x. Pustaka yang diperlukan tercantum dalam `requirements.txt`.

### Langkah-langkah

1.  **Kloning Repositori:**
    ```bash
    git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
    cd your-repo
    ```

2.  **Instal Pustaka:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi Streamlit:**
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan terbuka secara otomatis di browser web Anda.

## Direktori Proyek

-   `app.py`: Kode sumber utama aplikasi Streamlit.
-   `model/`: Folder yang berisi file `.pkl` dari model dan objek preprocessor yang sudah dilatih.
-   `README.md`: Dokumen ini.
-   `requirements.txt`: Daftar semua pustaka yang dibutuhkan.

---
