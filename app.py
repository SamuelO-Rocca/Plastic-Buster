import streamlit as st
from streamlit_option_menu import option_menu

# =====================
# IMPORTAÇÃO DOS MÓDULOS
# =====================
from modules.home import home
from modules.sobre import sobre
from modules.mapa import mapa
from modules.dashboard import dashboard_analitico
from modules.plasticoInsert import inserir_plastico
from modules.fungoInsert import inserir_fungo
from modules.simbiose import simbiose  # <-- Import simbiótico


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
# ESTILOS GLOBAIS
# =====================
def aplicar_tema(tema):
    """Aplica tema claro ou escuro dinamicamente."""
    if tema == "Escuro":
        st.markdown("""
            <style>
            body, .stApp {
                background-color: #0d1117;
                color: #e6edf3;
            }
            div[data-testid="stHeader"] {background: none;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body, .stApp {
                background-color: #f8f9fa;
                color: #212529;
            }
            div[data-testid="stHeader"] {background: none;}
            </style>
        """, unsafe_allow_html=True)


# =====================
# SIDEBAR — MENU LATERAL
# =====================
with st.sidebar:
    st.image("assets/logo.png", width=120)
    st.markdown("### Plastic Busters")
    st.markdown("IA • Biotecnologia • Remediação")

    # Menu principal (lado esquerdo)
    escolha = option_menu(
        menu_title="Navegação",
        options=[
            "Home",
            "Mapa",
            "Dashboard",
            "Inserir Plástico",
            "Inserir Fungo",
            "Simbiose",  # <--- NOVA ABA LATERAL
            "Sobre"
        ],
        icons=[
            "house",          # Home
            "map",            # Mapa
            "bar-chart",      # Dashboard
            "box-seam",       # Inserir Plástico
            "bug",            # Inserir Fungo
            "share",          # Simbiose (ícone de conexão)
            "info-circle"     # Sobre
        ],
        menu_icon="cast",
        default_index=0
    )

    st.markdown("---")
    tema = st.radio("Tema", ["Escuro", "Claro"], horizontal=True)
    aplicar_tema(tema)

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
