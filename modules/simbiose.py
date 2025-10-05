import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

def simbiose():
    st.title("🧬 Simbiose — Fungo e Microrganismos Auxiliares")
    st.markdown(
        """
        ### 🌿 Interações simbióticas microbianas
        Explore as **parcerias simbióticas** entre fungos degradadores e microrganismos
        (bactérias, algas e actinomicetos) que **potencializam a decomposição de polímeros plásticos**.
        """
    )

    # ======================
    # BASE EXPERIMENTAL
    # ======================
    dados = pd.DataFrame({
        "Fungo": [
            "Aspergillus niger",
            "Trichoderma reesei",
            "Penicillium chrysogenum",
            "Fusarium solani",
            "Mucor racemosus"
        ],
        "Microrganismo Simbiótico": [
            "Pseudomonas putida",
            "Bacillus subtilis",
            "Rhodococcus ruber",
            "Chlorella vulgaris",
            "Streptomyces sp."
        ],
        "Tipo de Relação": [
            "Mutualismo Metabólico",
            "Comensalismo Produtivo",
            "Sinergia Enzimática",
            "Fotossimbiose",
            "Mutualismo de Superfície"
        ],
        "Eficiência da Degradação (%)": [78, 69, 85, 72, 80],
        "Expressão Enzimática (U/mL)": [320, 250, 410, 300, 360]
    })

    # ======================
    # VISUALIZAÇÃO 1: GRÁFICO DE BARRAS REFINADO
    # ======================
    st.markdown("### 📊 Eficiência simbiótica por par microbiano")

    fig = px.bar(
        dados,
        x="Eficiência da Degradação (%)",
        y="Fungo",
        color="Microrganismo Simbiótico",
        orientation="h",
        text_auto=".1f",
        color_discrete_sequence=px.colors.sequential.Tealgrn
    )

    fig.update_layout(
        height=400,  # reduzido (antes era ~700)
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0E0E0"),
        xaxis=dict(showgrid=False),
        yaxis=dict(title=""),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title=""
        )
    )
    st.plotly_chart(fig, use_container_width=True)


    # ======================
    # VISUALIZAÇÃO 3: TABELA DE DADOS
    # ======================
    st.markdown("### 📄 Dados simbióticos observados em laboratório")
    st.dataframe(dados, use_container_width=True)

    # ======================
    # INTERAÇÃO
    # ======================
    st.markdown("### 🔍 Analisar Par Específico")
    col1, col2 = st.columns(2)
    fungo = col1.selectbox("Selecione o Fungo:", dados["Fungo"].unique())
    micro = col2.selectbox("Selecione o Microrganismo:", dados["Microrganismo Simbiótico"].unique())

    if st.button("Analisar Relação Simbiótica"):
        filtro = dados[
            (dados["Fungo"] == fungo) &
            (dados["Microrganismo Simbiótico"] == micro)
        ]

        if not filtro.empty:
            linha = filtro.iloc[0]
            st.success(
                f"""
                🔬 **Relação:** {linha['Tipo de Relação']}  
                🧫 **Eficiência:** {linha['Eficiência da Degradação (%)']}%  
                ⚗️ **Expressão Enzimática:** {linha['Expressão Enzimática (U/mL)']} U/mL  
                """
            )
        else:
            st.warning("❌ Nenhum dado encontrado para esse par simbiótico.")

    st.caption("📘 Fonte: Plastic Busters Lab | EcoAI Division © 2025")