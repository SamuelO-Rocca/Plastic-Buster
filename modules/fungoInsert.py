import streamlit as st
import json
import os

# ==========================
# CONFIGURAÇÕES GERAIS
# ==========================
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_PATH = os.path.join(DATA_DIR, "fungos.json")
IMAGES_DIR = os.path.join(DATA_DIR, "imagens_fungos")

os.makedirs(IMAGES_DIR, exist_ok=True)


def salvar_dados_fungo(dados):
    """Salva os dados do fungo no JSON central do sistema."""
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            existentes = json.load(f)
    else:
        existentes = []

    existentes.append(dados)

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(existentes, f, ensure_ascii=False, indent=4)


# ==========================
# INTERFACE PRINCIPAL
# ==========================
def inserir_fungo():
    """Interface de cadastro de novos fungos."""
    st.markdown("### 🧫 Ficha Técnica — **Fungos**")

    with st.form("form_fungo"):
        nome_cientifico = st.text_input("Nome Científico", placeholder="Ex: Ideafungus plasticae")
        taxonomia = st.text_input("Taxonomia", placeholder="Ex: Fungi > Basidiomycota")

        col1, col2 = st.columns(2)
        with col1:
            enzima = st.text_input("Enzima", placeholder="Ex: Plastase-A")
        with col2:
            degradacao = st.text_input("Degradação", placeholder="Ex: Alta")

        maturacao = st.text_input("Maturação", placeholder="Ex: 6 semanas")
        imagem = st.file_uploader("Imagem", type=["jpg", "png", "jpeg"])

        # === Botões lado a lado ===
        col1, col2 = st.columns(2)
        with col1:
            salvar_btn = st.form_submit_button("💾 Salvar", use_container_width=True)
        with col2:
            exportar_btn = st.form_submit_button("📦 Exportar", use_container_width=True)

    # ==========================
    # Ações dos botões
    # ==========================
    if salvar_btn:
        dados = {
            "nome_cientifico": nome_cientifico,
            "taxonomia": taxonomia,
            "enzima": enzima,
            "degradacao": degradacao,
            "maturacao": maturacao,
            "imagem": imagem.name if imagem else None,
        }

        salvar_dados_fungo(dados)
        st.success("✅ Dados do fungo salvos com sucesso!")

        if imagem:
            caminho_imagem = os.path.join(IMAGES_DIR, imagem.name)
            with open(caminho_imagem, "wb") as f:
                f.write(imagem.getbuffer())
            st.info(f"🖼️ Imagem salva em: {caminho_imagem}")

    if exportar_btn and os.path.exists(DATA_PATH):
        with open(DATA_PATH, "rb") as f:
            st.download_button(
                label="⬇️ Baixar JSON Gerado",
                data=f,
                file_name="fungos.json",
                mime="application/json"
            )