import streamlit as st
from PIL import Image

def sobre():
    # ========= Estilos personalizados =========
    st.markdown("""
        <style>
        .titulo-sobre {
            text-align: center;
            font-size: 2.3rem;
            font-weight: 800;
            color: #00e0a3;
            text-shadow: 0 0 15px rgba(0,255,180,0.4);
        }
        .subtitulo-sobre {
            text-align: center;
            font-size: 1.1rem;
            color: #b0b0b0;
            margin-bottom: 2rem;
        }
        .card {
            background: rgba(255, 255, 255, 0.05);
            padding: 1.2rem;
            border-radius: 20px;
            text-align: center;
            transition: 0.3s;
            box-shadow: 0 0 15px rgba(0,0,0,0.25);
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 25px rgba(0,255,180,0.3);
        }
        .emoji {
            font-size: 2rem;
        }
        .secao-titulo {
            font-size: 1.4rem;
            color: #00c896;
            font-weight: 700;
            margin-top: 1.5rem;
        }
        .texto {
            color: #bdbdbd;
            text-align: justify;
        }
        </style>
    """, unsafe_allow_html=True)

    # ========= Cabeçalho =========
    st.markdown("<h1 class='titulo-sobre'>Sobre o Projeto Plastic Busters</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo-sobre'>Conectando biotecnologia, IA e sustentabilidade para redefinir a relação entre o homem e o plástico.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # ========= Missão, Visão e Valores =========
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class='card'>
                <div class='emoji'>🎯</div>
                <h4>Missão</h4>
                <p class='texto'>Desenvolver soluções biotecnológicas e digitais capazes de eliminar resíduos plásticos do ambiente e acelerar a regeneração ecológica global.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class='card'>
                <div class='emoji'>🌍</div>
                <h4>Visão</h4>
                <p class='texto'>Ser referência mundial em biodegradação inteligente, aliando fungos e IA para transformar o problema do plástico em uma oportunidade de renascimento ambiental.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class='card'>
                <div class='emoji'>💎</div>
                <h4>Valores</h4>
                <p class='texto'>Sustentabilidade, ética científica, inovação contínua, colaboração global e responsabilidade socioambiental.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ========= Descrição institucional =========
    st.markdown("<h3 class='secao-titulo'>🔬 Nossa História</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p class='texto'>
        A <b>Plastic Busters</b> nasceu da convergência entre ciência de dados, biotecnologia e responsabilidade ambiental. 
        Nossa equipe multidisciplinar combina pesquisadores, engenheiros e cientistas de IA com um propósito único: 
        <b>restaurar o equilíbrio ecológico do planeta</b> através da inteligência aplicada à natureza.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='secao-titulo'>🤝 Parcerias Estratégicas</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p class='texto'>
        Firmamos colaborações com universidades, centros de pesquisa e startups verdes que compartilham 
        da mesma visão de um futuro limpo, tecnológico e regenerativo. 
        Juntos, mapeamos áreas críticas e implementamos soluções baseadas em dados reais e biotecnologia aplicada.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========= Equipe =========
    st.markdown("<h3 class='secao-titulo'>👥 Nossa Equipe</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6  = st.columns(6)

    membros = [
        ("assets/team1.png", "Gustavi Kim", "Dono do projeto"),
        ("assets/team2.png", "Samuel Rocca", "Desenvolvedor"),
        ("assets/team3.png", "João Pedro", "Desenvolvedor"),
        ("assets/team4.png", "Bibs", "Auxiliar de TI"),
        ("assets/team5.png", "Marim", "Biologo"),
        ("assets/team6.png", "Alex", "Desenvolvedor")
    ]

    for i, (img, nome, cargo) in enumerate(membros):
        with [col1, col2, col3, col4, col5, col6 ][i]:
            try:
                foto = Image.open(img)
                st.image(foto, use_container_width=True, caption=nome)
            except:
                st.markdown(f"#### {nome}")
            st.markdown(f"<p class='texto' style='text-align:center;'>{cargo}</p>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style='text-align:center; margin-top:30px;'>
            <h4 style='color:#00e0a3;'>Plastic Busters — IA a serviço do planeta 🌿</h4>
            <p style='color:#b0b0b0;'>Porque sustentabilidade não é tendência — é legado.</p>
        </div>
    """, unsafe_allow_html=True)