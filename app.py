import streamlit as st
from streamlit_option_menu import option_menu

# =====================
# CONFIGURAÇÃO INICIAL
# =====================
st.set_page_config(
    page_title="Plastic Busters | Plataforma de Remediação",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌍"
)

# =====================
# IMPORTAÇÃO DOS MÓDULOS
# =====================
from modules.home import home
from modules.sobre import sobre
from modules.mapa import mapa
from modules.dashboard import dashboard_analitico
from modules.plasticoInsert import inserir_plastico
from modules.fungoInsert import inserir_fungo
from modules.simbiose import simbiose

# =====================
# SIDEBAR — MENU LATERAL
# =====================
with st.sidebar:
    st.image("assets/logo.png", width=120)
    st.markdown("### Plastic Busters")
    st.markdown("IA • Biotecnologia • Remediação")

    escolha = option_menu(
        menu_title="Navegação",
        options=[
            "Home",
            "Mapa",
            "Dashboard",
            "Inserir Plástico",
            "Inserir Fungo",
            "Simbiose",
            "Sobre"
        ],
        icons=[
            "house",
            "map",
            "bar-chart",
            "box-seam",
            "bug",
            "share",
            "info-circle"
        ],
        menu_icon="cast",
        default_index=0
    )

    st.markdown("---")
    st.caption("© 2025 Plastic Busters | EcoAI Division")

# =====================
# CONTEÚDO PRINCIPAL
# =====================
if escolha == "Home":
    home()

elif escolha == "Mapa":
    mapa()

elif escolha == "Dashboard":
    dashboard_analitico()

elif escolha == "Inserir Plástico":
    inserir_plastico()

elif escolha == "Inserir Fungo":
    inserir_fungo()

elif escolha == "Simbiose":
    simbiose()

elif escolha == "Sobre":
    sobre()
