import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import json
import os

def map_interface():
    st.title("🗺️ Mapa Interativo — Plastic Busters")
    st.markdown("""
    ### 🌐 Monitoramento Ambiental em Tempo Real
    Visualize os pontos de coleta e análise de microplásticos e fungos em diferentes biomas e camadas ambientais.
    """)

    # Sidebar de controle
    with st.sidebar.expander("🎛️ Filtros do Mapa"):
        camada = st.multiselect(
            "Selecione as variáveis ambientais:",
            ["Temperatura", "Umidade", "Oxigênio", "pH", "Microplásticos", "Contaminação"],
            default=["Temperatura", "Umidade"]
        )

        tipo = st.radio(
            "Tipo de Ambiente",
            ["Aquático", "Terrestre", "Atmosférico"],
            horizontal=True
        )

        mostrar_pontos = st.checkbox("Exibir pontos de amostragem", True)

    # Criação do mapa base
    mapa = leafmap.Map(center=[-15.8, -47.9], zoom=4, tiles="CartoDB.DarkMatter")
    mapa.add_basemap("Esri.WorldImagery")

    # Carrega dados geográficos se existirem
    dados_geo_path = "./data/processed/pontos_geo.json"
    if os.path.exists(dados_geo_path):
        with open(dados_geo_path, "r", encoding="utf-8") as f:
            geo_data = json.load(f)
        df = pd.DataFrame(geo_data)
    else:
        df = pd.DataFrame({
            "latitude": [-23.5, -22.9, -3.1],
            "longitude": [-46.6, -43.2, -60.0],
            "temperatura": [26, 28, 31],
            "umidade": [70, 82, 88],
            "ph": [6.5, 7.1, 5.8],
            "oxigenio": [8.2, 7.5, 6.9],
            "tipo": ["Aquático", "Terrestre", "Aquático"]
        })

    # Exibe pontos se habilitado
    if mostrar_pontos:
        for _, row in df.iterrows():
            popup_text = f"""
            <b>Tipo:</b> {row['tipo']}<br>
            🌡️ <b>Temperatura:</b> {row['temperatura']} °C<br>
            💧 <b>Umidade:</b> {row['umidade']} %<br>
            🧪 <b>pH:</b> {row['ph']}<br>
            🌬️ <b>Oxigênio:</b> {row['oxigenio']} mg/L
            """
            mapa.add_marker(
                location=[row["latitude"], row["longitude"]],
                popup=popup_text,
                icon="info-sign"
            )

    # Camadas adicionais conforme filtro
    if "Microplásticos" in camada:
        mapa.add_heatmap(
            df[["latitude", "longitude"]].values.tolist(),
            name="Concentração de Microplásticos",
            radius=25
        )

    if "Contaminação" in camada:
        mapa.add_heatmap(
            df[["latitude", "longitude"]].values.tolist(),
            name="Níveis de Contaminação",
            radius=20,
            colors="Reds"
        )

    # Callback de clique
    st.markdown("---")
    st.markdown("🖱️ **Clique em qualquer ponto no mapa para consultar variáveis ambientais.**")

    clicked = mapa.user_interaction()
    if clicked:
        st.success(f"📍 Ponto clicado: {clicked}")
        # Aqui dá pra conectar com a IA e mostrar predições locais
        # Exemplo: modelo.predict([variáveis ambientais do ponto])

    mapa.to_streamlit(height=600)
