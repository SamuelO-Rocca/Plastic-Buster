import streamlit as st
import json
import os

CONFIG_PATH = "./config.json"

def carregar_config():
    """Carrega configurações do sistema."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "idioma": "pt-BR",
            "tema": "dark",
            "modo_dev": False,
            "precisao_minima_ia": 0.80
        }

def salvar_config(config):
    """Salva as configurações no arquivo config.json."""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)


def settings_interface():
    st.title("⚙️ Configurações — Plastic Busters")
    st.markdown("Personalize o comportamento da plataforma conforme suas preferências e necessidades operacionais.")

    config = carregar_config()

    # Seções de configuração
    st.subheader("🌍 Idioma e Aparência")
    col1, col2 = st.columns(2)

    with col1:
        idioma = st.selectbox(
            "Idioma da Interface:",
            ["pt-BR", "en-US", "es-ES"],
            index=["pt-BR", "en-US", "es-ES"].index(config.get("idioma", "pt-BR"))
        )

    with col2:
        tema = st.radio(
            "Tema visual:",
            ["dark", "light"],
            index=0 if config.get("tema", "dark") == "dark" else 1,
            horizontal=True
        )

    st.subheader("🧠 Inteligência Artificial")
    precisao_min = st.slider(
        "Precisão mínima esperada do modelo (threshold):",
        0.5, 0.99,
        config.get("precisao_minima_ia", 0.80),
        step=0.01
    )

    modo_dev = st.checkbox(
        "Ativar modo desenvolvedor (logs detalhados, debug)",
        value=config.get("modo_dev", False)
    )

    st.subheader("💾 Persistência e Dados")
    st.write("Escolha como o sistema deve armazenar e recuperar as informações.")

    opcoes_storage = ["SQLite Local", "JSON", "Cloud Storage (futuro)"]
    storage = st.selectbox(
        "Tipo de armazenamento:",
        opcoes_storage,
        index=0
    )

    st.divider()

    if st.button("💾 Salvar Configurações"):
        config["idioma"] = idioma
        config["tema"] = tema
        config["modo_dev"] = modo_dev
        config["precisao_minima_ia"] = precisao_min
        config["armazenamento"] = storage
        salvar_config(config)
        st.success("✅ Configurações salvas com sucesso!")
        st.toast("As alterações serão aplicadas na próxima inicialização.", icon="🔄")

    # Exibir config atual (modo transparente)
    with st.expander("📋 Visualizar Configuração Atual"):
        st.json(config)
