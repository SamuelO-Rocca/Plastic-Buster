import streamlit as st
from streamlit_folium import st_folium
import folium
import requests

def mapa():
    st.title("🌍 Mapa Ambiental Interativo — NASA GIBS + Open Data")
    st.markdown("Clique em qualquer ponto do mapa para ver **temperatura, umidade, oxigênio e pH** estimados.")

    # Configuração do mapa base NASA GIBS (realista 2D)
    nasa_tiles = (
        "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/"
        "BlueMarble_ShadedRelief_Bathymetry/default/2013-12-01/"
        "GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg"
    )

    m = folium.Map(
        location=[0, 0],
        zoom_start=2,
        tiles=None
    )

    # Adiciona camada NASA
    folium.TileLayer(
        tiles=nasa_tiles,
        attr="NASA GIBS BlueMarble",
        name="NASA Realista",
        overlay=False,
        control=True
    ).add_to(m)

    folium.LayerControl().add_to(m)

    st.markdown("🛰️ Clique em qualquer ponto para ver as variáveis ambientais.")
    st_data = st_folium(m, width=900, height=550)

    # Se o usuário clicou no mapa
    if st_data and st_data.get("last_clicked"):
        lat = st_data["last_clicked"]["lat"]
        lon = st_data["last_clicked"]["lng"]

        st.subheader(f"📍 Coordenadas Selecionadas: {lat:.4f}, {lon:.4f}")

        try:
            # Chamada à API Open-Meteo
            url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m"
            )
            resp = requests.get(url, timeout=10).json()
            temp = resp["current"]["temperature_2m"]
            hum = resp["current"]["relative_humidity_2m"]

            # Mock das variáveis ainda não disponíveis via API
            ph_solo = round(6.5 + (lat % 0.5), 2)
            ph_agua = round(7.0 + (lon % 0.3), 2)
            oxigenio = round(8 + ((lat + lon) % 1), 2)

            st.success("✅ Dados ambientais obtidos com sucesso!")
            st.write(f"🌡️ **Temperatura:** {temp} °C")
            st.write(f"💧 **Umidade:** {hum} %")
            st.write(f"🧪 **pH do Solo:** {ph_solo}")
            st.write(f"🌊 **pH da Água:** {ph_agua}")
            st.write(f"🫁 **Oxigênio dissolvido:** {oxigenio} mg/L")

            # Exibe marcador dinâmico
            folium.Marker(
                [lat, lon],
                popup=(f"<b>Temperatura:</b> {temp}°C<br>"
                       f"<b>Umidade:</b> {hum}%<br>"
                       f"<b>pH Solo:</b> {ph_solo}<br>"
                       f"<b>pH Água:</b> {ph_agua}<br>"
                       f"<b>O₂:</b> {oxigenio} mg/L"),
                tooltip="Clique para detalhes"
            ).add_to(m)

        except Exception as e:
            st.error(f"Erro ao obter dados meteorológicos: {e}")