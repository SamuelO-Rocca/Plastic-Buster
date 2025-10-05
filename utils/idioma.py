"""
Módulo: idioma.py
Descrição: Gerencia a seleção e carregamento de idiomas no projeto Plastic Buster.
Autor: Samuel
Data: 2025
"""

import json
import streamlit as st
import os

# Caminho do arquivo de tradução
LOCALES_PATH = os.path.join(os.path.dirname(__file__), "locales.json")

# ============================================================================

def carregar_traducoes():
    """
    Carrega o arquivo JSON de traduções.
    Retorna um dicionário com os idiomas disponíveis.
    """
    if not os.path.exists(LOCALES_PATH):
        st.error("Arquivo de tradução (locales.json) não encontrado.")
        return {}

    with open(LOCALES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def selecionar_idioma():
    """
    Exibe o seletor de idioma na interface e salva a escolha na sessão.
    """
    traducoes = carregar_traducoes()
    idiomas_disponiveis = list(traducoes.keys())

    if "idioma" not in st.session_state:
        st.session_state.idioma = "pt"  # Padrão: Português

    idioma_selecionado = st.sidebar.selectbox(
        "🌐 Idioma / Language",
        idiomas_disponiveis,
        index=idiomas_disponiveis.index(st.session_state.idioma)
        if st.session_state.idioma in idiomas_disponiveis else 0,
    )

    st.session_state.idioma = idioma_selecionado
    return idioma_selecionado


def t(chave: str) -> str:
    """
    Traduz uma chave com base no idioma atual.
    Exemplo: t("titulo_home") -> "Bem-vindo ao Plastic Buster"
    """
    traducoes = carregar_traducoes()
    idioma = st.session_state.get("idioma", "pt")

    if idioma not in traducoes:
        return chave

    return traducoes[idioma].get(chave, chave)
