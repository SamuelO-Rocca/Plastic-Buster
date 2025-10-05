import streamlit as st
import json
import os

# ==========================
# CONFIGURAÇÕES GERAIS
# ==========================
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_PATH = os.path.join(DATA_DIR, "plasticos.json")
IMAGES_DIR = os.path.join(DATA_DIR, "imagens_plasticos")

os.makedirs(IMAGES_DIR, exist_ok=True)


def salvar_dados(dados):
    """Salva os dados do plástico no JSON central do sistema."""
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
def inserir_plastico():
    """Interface de cadastro de novos plásticos."""
    st.markdown("### 🧾 Ficha Técnica — **Plástico**")

    with st.form("form_plastico"):
        nome_cientifico = st.text_input("Nome Científico / Técnico", placeholder="Ex: PET (polietileno tereftalato)")
        nome_popular = st.text_input("Nome Popular", placeholder="Ex: PET")
        estrutura_molecular = st.text_area("Estrutura Molecular", placeholder="Ex: —(O-CH2-CH2-O-CO-C6H4-CO)—")
        formula = st.text_input("Fórmula", placeholder="Ex: C10H8O4")
        aplicacao = st.text_input("Aplicação", placeholder="Ex: Garrafas, embalagens")
        tempo_deterioracao = st.text_input("Tempo de Deteriorização", placeholder="Ex: ≈ 450 anos")
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
            "nome_popular": nome_popular,
            "estrutura_molecular": estrutura_molecular,
            "formula": formula,
            "aplicacao": aplicacao,
            "tempo_deterioracao": tempo_deterioracao,
            "imagem": imagem.name if imagem else None,
        }

        salvar_dados(dados)
        st.success("✅ Dados salvos com sucesso!")

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
                file_name="plasticos.json",
                mime="application/json"
            )
        st.success("✅ Arquivo JSON pronto para download!")
    elif exportar_btn:
        st.warning("⚠️ Nenhum dado para exportar. Por favor, salve algum plástico primeiro.")