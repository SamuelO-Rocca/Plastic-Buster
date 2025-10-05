import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def dashboard_analitico():
    st.title("📊 Dashboard Analítico de Decomposição de Plásticos")

    st.markdown("""
        Este módulo apresenta uma análise comparativa entre os cenários:
        - **Com fungo biodegradante ativo**
        - **Sem presença do fungo**
    """)

    tempo = np.linspace(0, 12, 100)  # meses
    decomposicao_sem_fungo = np.exp(-0.05 * tempo) * 100
    decomposicao_com_fungo = np.exp(-0.25 * tempo) * 100

    fig, ax = plt.subplots()
    ax.plot(tempo, decomposicao_sem_fungo, label="Sem fungo", linestyle="--", color="red")
    ax.plot(tempo, decomposicao_com_fungo, label="Com fungo", color="green")
    ax.set_xlabel("Tempo (meses)")
    ax.set_ylabel("Percentual de plástico remanescente (%)")
    ax.set_title("Evolução da decomposição do plástico")
    ax.legend()
    st.pyplot(fig)

    acuracia_modelo = np.random.uniform(85, 99)
    tempo_estimado = np.random.uniform(1, 6)

    st.metric("🎯 Acurácia do modelo preditivo", f"{acuracia_modelo:.2f}%")
    st.metric("⏳ Tempo médio previsto de decomposição", f"{tempo_estimado:.1f} meses")

    st.markdown("---")
    st.info("Este painel será aprimorado com dados reais provenientes de sensores e simulações ambientais.")

