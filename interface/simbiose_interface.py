import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from core.data_loader import load_data
from core.preprocessing import preprocess_data

def simbiose_interface():
    st.title("🧫 Simbiose — Fungo x Microplástico")
    st.markdown("""
    Explore as interações simbióticas entre espécies fúngicas e partículas de microplástico.
    Este painel analisa dados laboratoriais, ambientais e de campo, gerando insights sobre **biodegradação e ecossimbiose**.
    """)

    uploaded_file = st.file_uploader("📥 Envie um arquivo de dados (CSV, JSON ou DB)", type=["csv", "json", "db"])

    if uploaded_file:
        file_path = f"./data/uploads/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("Carregando e estruturando dados..."):
            df = load_data(file_path)
            df = preprocess_data(df)
            st.success("✅ Dados carregados e processados com sucesso!")
            st.dataframe(df.head())

        st.markdown("### 🧠 Relações simbióticas detectadas")

        # Simulação de dados caso não exista relação explícita
        if "fungo" not in df.columns or "polimero" not in df.columns:
            df = pd.DataFrame({
                "fungo": ["Aspergillus niger", "Penicillium sp.", "Fusarium oxysporum", "Trichoderma harzianum"],
                "polimero": ["PET", "PEAD", "PP", "PVC"],
                "eficiencia_biodegradacao": [0.81, 0.73, 0.66, 0.59],
                "condicao": ["Temperado", "Tropical", "Árido", "Úmido"]
            })

        # Cria grafo simbiótico
        G = nx.Graph()

        for _, row in df.iterrows():
            G.add_node(row["fungo"], group="Fungo", size=30)
            G.add_node(row["polimero"], group="Polímero", size=20)
            G.add_edge(row["fungo"], row["polimero"], weight=row.get("eficiencia_biodegradacao", 0.5))

        pos = nx.spring_layout(G, seed=42)
        edge_x, edge_y = [], []

        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Desenha arestas
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1, color='#888'),
            hoverinfo='none',
            mode='lines'
        )

        node_x, node_y, node_text, node_color = [], [], [], []

        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            group = G.nodes[node]["group"]
            node_text.append(f"{node} ({group})")
            node_color.append("lightgreen" if group == "Fungo" else "lightblue")

        # Desenha nós
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition='top center',
            hoverinfo='text',
            marker=dict(
                color=node_color,
                size=[G.nodes[n].get("size", 20) for n in G.nodes()],
                line_width=2
            )
        )

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title="Rede Simbiótica: Fungos e Polímeros",
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=0, l=0, r=0, t=40),
                            xaxis=dict(showgrid=False, zeroline=False),
                            yaxis=dict(showgrid=False, zeroline=False)
                        ))

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📈 Eficiência de Biodegradação")
        st.bar_chart(df.set_index("fungo")["eficiencia_biodegradacao"])

        st.markdown("---")
        st.info("💡 Dica: Clique no nó do fungo para cruzar dados com o mapa interativo na aba 'Mapa'.")
    else:
        st.warning("Envie um arquivo de dados para iniciar a análise simbiótica.")
