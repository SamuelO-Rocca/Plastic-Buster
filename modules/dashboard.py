import streamlit as st
import plotly.graph_objects as go
import numpy as np

def dashboard_analitico():
    # =====================
    # TÍTULO E CONTEXTO
    # =====================
    st.title("🧬 Dashboard Analítico — Projeto Plastic Busters")
    st.markdown("""
        <div style="font-size:17px; line-height:1.6; color:#A9B2C3;">
            Este painel monitora os índices de **biodegradação de plásticos** em ambiente controlado, 
            com foco no desempenho do <b>fungo simbiótico de degradação</b> sob parâmetros simulados pela IA.
        </div>
    """, unsafe_allow_html=True)

    # =====================
    # GRÁFICO INTERATIVO
    # =====================
    tempo = np.linspace(0, 12, 100)
    decomposicao_sem_fungo = np.exp(-0.05 * tempo) * 100
    decomposicao_com_fungo = np.exp(-0.25 * tempo) * 100

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tempo, y=decomposicao_sem_fungo,
        mode="lines",
        name="Sem Fungo",
        line=dict(dash="dot", color="#FF6B6B", width=3)
    ))

    fig.add_trace(go.Scatter(
        x=tempo, y=decomposicao_com_fungo,
        mode="lines",
        name="Com Fungo",
        line=dict(color="#00C853", width=4)
    ))

    fig.update_layout(
        title="📉 Curva de Decomposição de Polímeros",
        xaxis_title="Tempo (meses)",
        yaxis_title="Plástico remanescente (%)",
        template="plotly_dark",
        hovermode="x unified",
        height=450,
        margin=dict(l=40, r=40, t=60, b=40),
        font=dict(size=13, color="#E6EDF3"),
        plot_bgcolor="rgba(10, 12, 16, 0.85)",
        paper_bgcolor="rgba(10, 12, 16, 0.0)",
    )

    st.plotly_chart(fig, use_container_width=True)

    # =====================
    # MÉTRICAS CORPORATIVAS
    # =====================
    st.markdown("### 📈 Indicadores Operacionais")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Acurácia do Modelo", "96.8%", "Alta Confiabilidade")
    with col2:
        st.metric("⏳ Tempo Médio de Decomposição", "2.4 meses", "-60% vs. controle")
    with col3:
        st.metric("🌱 Eficiência Biológica", "88.5%", "+15% em relação ao baseline")

    # =====================
    # INSIGHTS ESTRATÉGICOS
    # =====================
    st.markdown("---")
    st.subheader("🧠 Insights Estratégicos da IA Symbiose Neural Engine")
    st.markdown("""
        - 🔍 **Correlação direta** entre temperatura e aceleração da decomposição após 28 dias.  
        - 🌡️ Ambientes acima de **32 °C** apresentaram um **aumento de 22%** na eficiência simbiótica.  
        - 🧫 Cepas mistas (fungo + bactéria auxiliar) atingiram **estabilidade microbiana 1.4x maior**.  
        - ⚙️ Recomenda-se ampliar o escopo para plásticos com matriz de PET e PEAD em campo real.
    """)

    # =====================
    # FOOTER VISUAL
    # =====================
    st.markdown("""
        <hr style="border: 1px solid rgba(100, 255, 218, 0.3);">
        <div style="text-align:center; color:#6F8093; font-size:13px;">
            © 2025 Plastic Busters | Division of BioSpace Research — Sistema Integrado de IA e Biotecnologia Aplicada
        </div>
    """, unsafe_allow_html=True)
