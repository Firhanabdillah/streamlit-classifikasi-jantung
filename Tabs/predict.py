from web_functions import predict
import streamlit as st

def app(df, x, y):
    st.title("Halaman Prediksi")
    col1, col2 = st.columns(2)
    with col1:
        sex = st.text_input("Input Nilai sex")
        cp = st.text_input("Input Nilai cp")
        trestbps = st.text_input("Input Nilai trestbps")
        chol = st.text_input("Input Nilai cho")
        fbs = st.text_input("Input Nilai fbs")
        restecg = st.text_input("Input Nilai restecg")
    with col2:
        thalach = st.text_input("Input Nilai thalach")
        exang = st.text_input("Input Nilai exang")
        oldpeak = st.text_input("Input Nilai oldpeak")
        slope = st.text_input("Input Nilai slope")
        ca = st.text_input("Input Nilai sod")
        thal = st.text_input("Input Nilai thal")

    features = [sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    # tombol Prediksi
    if st.button("Prediksi"):
        Prediction, score = predict(x, y, features)
        score = score
        st.info("prediksi sukses...")

        if (Prediction == 1):
            st.warning("orang tersebut rentan terkena penyakit Jantung")
        else:
            st.success("orang tersebut relatif aman dari penyakit Jantung")
            st.write("Model yang digunakan memiliki tingkat akurasi", (score*100),"%")
