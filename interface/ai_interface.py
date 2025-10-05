import streamlit as st
from core.data_loader import load_data
from core.preprocessing import preprocess_data
from core.ml_model import train_model

def ai_interface():
    st.title("🤖 IA Analítica — Plastic Busters")
    st.write("Envie seus dados e veja a inteligência artificial processar as informações ambientais.")

    uploaded_file = st.file_uploader(
        "Selecione um arquivo (CSV, JSON, DB, PDF)",
        type=["csv", "json", "db", "pdf"]
    )

    if uploaded_file:
        file_path = f"./data/uploads/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info("🔍 Carregando e estruturando os dados...")
        df = load_data(file_path)
        st.dataframe(df.head())

        st.divider()
        if st.button("🚀 Processar e Treinar IA"):
            with st.spinner("Processando dados..."):
                df_clean = preprocess_data(df)
                model, acc = train_model(df_clean)
            st.success(f"✅ Modelo treinado com acurácia de {acc:.2f}")
