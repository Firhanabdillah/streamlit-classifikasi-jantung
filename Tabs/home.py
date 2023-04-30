import streamlit as st

def app():
    # judul halaman aplikasi 
    st.title("Aplikasi Prediksi Penyakit Jantung")
 # menambahkan gambar
    image = Image.open("jantung.png")
    st.image(image, caption="Gambar ilustrasi", use_column_width=True)
