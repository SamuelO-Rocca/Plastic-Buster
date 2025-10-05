import streamlit as st
from streamlit_option_menu import option_menu

# Importa os módulos de cada página
from modules.home import home
from modules.sobre import sobre
from modules.mapa import mapa as mapa
from modules.dashboard import dashboard_analitico


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
# SIDEBAR
# =====================
with st.sidebar:
    st.image("assets/logo.png", width=120)
    st.markdown("### Plastic Busters 🌱")
    st.markdown("IA • Biotecnologia • Remediação")

    # Tema visual
    tema = st.radio("🎨 Tema visual", ["Escuro", "Claro"], horizontal=True)
    aplicar_tema(tema)

    # Menu principal
    escolha = option_menu(
        menu_title="Navegação",
        options=["Home", "Sobre", "Mapa", "Dashboard"],
        icons=["house", "info-circle", "map", "bar-chart"],
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
elif escolha == "Sobre":
    sobre()
elif escolha == "Mapa":
    mapa()
elif escolha == "Dashboard":
    dashboard_analitico()
