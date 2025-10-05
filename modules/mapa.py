import streamlit as st
from streamlit_folium import st_folium
import folium
import requests

def mapa():
    st.title("🌍 Mapa Ambiental Interativo — NASA GIBS + Open Data")
    st.markdown("Clique em qualquer ponto do mapa para visualizar o **nome do local e dados ambientais estimados**.")

    # Inicializa estado
    if 'clicked_lat' not in st.session_state:
        st.session_state['clicked_lat'] = None
        st.session_state['clicked_lon'] = None
        st.session_state['local_name'] = None

    # Função para obter o nome do local a partir das coordenadas
    def obter_nome_local(lat, lon):
        try:
            url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}"
            resp = requests.get(url, headers={"User-Agent": "streamlit-app"})
            data = resp.json()
            return data.get("display_name", "Local desconhecido")
        except:
            return "Local não identificado"

    # Função que monta o mapa
    def build_map(lat=None, lon=None):
        nasa_tiles = (
            "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/"
            "BlueMarble_ShadedRelief_Bathymetry/default/2013-12-01/"
            "GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg"
        )
        m = folium.Map(location=[0, 0], zoom_start=2, tiles=None)
        folium.TileLayer(tiles=nasa_tiles, attr="NASA GIBS BlueMarble", name="NASA Realista", overlay=False).add_to(m)
        
        if lat is not None and lon is not None:
            folium.Marker(
                [lat, lon],
                popup=f"<b>Coordenadas:</b> {lat:.4f}, {lon:.4f}",
                tooltip="Local selecionado"
            ).add_to(m)
            m.location = [lat, lon]
            m.zoom_start = 6
        return m

    # Layout de colunas
    col1, col2 = st.columns([2.5, 1])

    with col1:
        m = build_map(st.session_state['clicked_lat'], st.session_state['clicked_lon'])
        st_data = st_folium(m, width=850, height=550, key="map")

        # Captura clique no mapa
        if st_data and st_data.get("last_clicked"):
            lat = st_data["last_clicked"]["lat"]
            lon = st_data["last_clicked"]["lng"]

            if (st.session_state['clicked_lat'] != lat) or (st.session_state['clicked_lon'] != lon):
                st.session_state['clicked_lat'] = lat
                st.session_state['clicked_lon'] = lon
                st.session_state['local_name'] = obter_nome_local(lat, lon)
                st.rerun()

    with col2:
        st.markdown("### 📊 Dados Ambientais")

        if st.session_state['clicked_lat'] is None:
            st.info("🧭 Clique em um ponto do mapa para visualizar os dados ambientais.")
        else:
            lat = st.session_state['clicked_lat']
            lon = st.session_state['clicked_lon']
            local_name = st.session_state.get('local_name', "Local desconhecido")

            st.markdown(f"**📍 Local:** {local_name}")
            st.markdown(f"**🌐 Coordenadas:**  \nLatitude: `{lat:.4f}`  \nLongitude: `{lon:.4f}`")

            try:
                # API de dados climáticos
                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={lat}&longitude={lon}"
                    f"&current=temperature_2m,relative_humidity_2m"
                )
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                data = resp.json()
                current = data.get('current', {})

                temp = current.get('temperature_2m', "N/A")
                hum = current.get('relative_humidity_2m', "N/A")

                # Mock para dados complementares
                ph_solo = round(6.5 + (abs(lat) % 0.5), 2)
                ph_agua = round(7.0 + (abs(lon) % 0.3), 2)
                oxigenio = round(8 + ((abs(lat) + abs(lon)) % 1), 2)

                st.success("✅ Dados coletados com sucesso!")
                st.markdown(f"""
                - 🌡️ **Temperatura:** {temp} °C  
                - 💧 **Umidade:** {hum} %  
                - 🧪 **pH do Solo (estimado):** {ph_solo}  
                - 🌊 **pH da Água (estimado):** {ph_agua}  
                - 🫁 **Oxigênio dissolvido (estimado):** {oxigenio} mg/L
                """)

            except Exception as e:
                st.error(f"🚨 Erro ao buscar dados: {e}")

if __name__ == "__main__":
    mapa()
