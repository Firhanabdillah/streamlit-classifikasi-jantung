import streamlit as st
from PIL import Image

def app():
    st.title("Aplikasi Prediksi Penyakit Jantung")
    st.write("Selamat datang di aplikasi prediksi penyakit jantung. Silakan gunakan navigasi di sebelah kiri untuk memilih halaman yang ingin Anda kunjungi.")
    image = Image.open("jantung.png")
    st.image(image, use_column_width=True)
