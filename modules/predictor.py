import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

def predictor():
    """
    Módulo de predição do tempo de degradação do plástico
    com base no tipo de polímero, fungo simbiótico e condições ambientais.
    """

    # =====================
    # CABEÇALHO
    # =====================
    st.title("🧬 Preditor de Tempo de Degradação do Plástico")
    st.markdown("""
        <div style="font-size:16px; line-height:1.6; color:#A9B2C3;">
            Este módulo utiliza <b>parâmetros heurísticos e ambientais</b> para simular a velocidade média
            de decomposição de polímeros sob ação simbiótica de fungos em condições específicas.
        </div>
    """, unsafe_allow_html=True)

    # =====================
    # ENTRADAS DO USUÁRIO
    # =====================
    col1, col2 = st.columns(2)

    with col1:
        tipo_plastico = st.selectbox(
            "🧱 Tipo de plástico",
            ["PET (Polietileno tereftalato)", "PEAD (Polietileno de alta densidade)",
             "PP (Polipropileno)", "PS (Poliestireno)"]
        )

        temperatura_ideal = st.radio(
            "🌡️ Temperatura agradável?",
            ["Sim", "Não"], horizontal=True
        )

        umidade_ideal = st.radio(
            "💧 Umidade agradável?",
            ["Sim", "Não"], horizontal=True
        )

    with col2:
        tipo_fungo = st.selectbox(
            "🍄 Espécie de fungo simbiótico",
            ["Aspergillus niger", "Penicillium chrysogenum",
             "Phanerochaete chrysosporium", "Trichoderma reesei"]
        )

        oxigenacao_ideal = st.radio(
            "🫧 Oxigenação a favor?",
            ["Sim", "Não"], horizontal=True
        )

    st.markdown("---")

    # =====================
    # BOTÃO DE PREDIÇÃO
    # =====================
    if st.button("🚀 Calcular previsão"):
        # =====================
        # PESOS HEURÍSTICOS
        # =====================
        pesos_plasticos = {
            "PET (Polietileno tereftalato)": 1.0,
            "PEAD (Polietileno de alta densidade)": 1.4,
            "PP (Polipropileno)": 1.2,
            "PS (Poliestireno)": 1.8
        }

        pesos_fungos = {
            "Aspergillus niger": 0.9,
            "Penicillium chrysogenum": 0.8,
            "Phanerochaete chrysosporium": 0.6,
            "Trichoderma reesei": 0.7
        }

        # =====================
        # FATORES AMBIENTAIS
        # =====================
        fatores_ambiente = 1.0
        if temperatura_ideal == "Sim":
            fatores_ambiente *= 0.9
        if umidade_ideal == "Sim":
            fatores_ambiente *= 0.9
        if oxigenacao_ideal == "Sim":
            fatores_ambiente *= 0.85

        # =====================
        # CÁLCULO DA PREVISÃO
        # =====================
        tempo_base = 12  # meses base para decomposição parcial
        tempo_estimado = (
            tempo_base
            * pesos_plasticos[tipo_plastico]
            * pesos_fungos[tipo_fungo]
            * fatores_ambiente
        )

        # =====================
        # RESULTADO E FEEDBACK
        # =====================
        st.success(f"🧬 Tempo estimado de degradação: **{tempo_estimado:.2f} meses**")

        if tempo_estimado < 3:
            nivel = "🚀 Degradação ultrarrápida — condições ideais!"
            cor = "#3FC380"
        elif tempo_estimado < 6:
            nivel = "⚙️ Degradação eficiente — simbionte ativo."
            cor = "#F5D76E"
        else:
            nivel = "🐢 Degradação lenta — otimização ambiental recomendada."
            cor = "#F64747"

        st.markdown(f"""
            <div style='padding:15px; background-color:{cor}; color:white; border-radius:10px;'>
                {nivel}
            </div>
        """, unsafe_allow_html=True)

        # =====================
        # GRÁFICO DE PIZZA — TEMPO DE DEGRADAÇÃO (Compacto)
        # =====================
        degradado = min(tempo_estimado * 0.3, tempo_estimado - 1)
        restante = tempo_estimado - degradado

        labels = ["Degradado", "Restante"]
        sizes = [degradado, restante]
        cores = ["#00E676", "#263238"]

        fig, ax = plt.subplots(figsize=(4, 4))
        fig.patch.set_facecolor("#0B0F19")
        ax.set_facecolor("#0B0F19")

        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct=lambda p: f"{p:.1f}%" if p > 5 else "",
            startangle=90,
            colors=cores,
            textprops={"color": "#E0F7FA", "fontsize": 10},
            wedgeprops={"linewidth": 2, "edgecolor": "#00BFA5"}
        )

        for autotext in autotexts:
            autotext.set_path_effects([
                path_effects.Stroke(linewidth=2, foreground="#00E5FF"),
                path_effects.Normal()
            ])

        ax.text(
            0, 0,
            f"{tempo_estimado:.1f}\nmeses",
            ha="center", va="center",
            fontsize=14, color="#A7FFEB", fontweight="bold"
        )

        ax.set_title(
            "🧬 Estimativa de Degradação",
            color="#A7FFEB",
            fontsize=13,
            pad=20,
            fontweight="bold"
        )

        plt.setp(ax, aspect="equal")
        st.pyplot(fig, use_container_width=False)

        # =====================
        # INSIGHT ADICIONAL
        # =====================
        st.markdown("---")
        st.info("""
            💡 *Nota técnica:* O modelo aplica parâmetros empíricos com ajuste
            ambiental dinâmico e será integrado a um sistema de machine learning
            preditivo na versão **Symbiose 2.0**.
        """)
