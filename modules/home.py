import streamlit as st
from PIL import Image

def home():
    # ========= Layout principal =========
    st.markdown("""
        <style>
        .titulo-principal {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            color: #00c896;
            text-shadow: 0 0 15px rgba(0,200,150,0.4);
        }
        .subtitulo {
            text-align: center;
            color: #b0b0b0;
            font-size: 1.2rem;
            margin-top: -10px;
        }
        .bloco {
            background: rgba(255, 255, 255, 0.05);
            padding: 1.5rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .bloco:hover {
            transform: scale(1.03);
            box-shadow: 0 0 25px rgba(0,255,180,0.3);
        }
        .icone {
            font-size: 2.3rem;
            color: #00e0a3;
        }
        </style>
    """, unsafe_allow_html=True)

    # ========= Cabeçalho =========
    st.markdown("<h1 class='titulo-principal'>🌍 Projeto Plastic Busters</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitulo'>Inovação biotecnológica e inteligência artificial unidas para regenerar o planeta</p>", unsafe_allow_html=True)
    st.write("")

    # ========= Seção de pilares =========
    st.markdown("### 🚀 Nossos Pilares Estratégicos")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='bloco'><div class='icone'>🧬</div><h4>Biotecnologia Sustentável</h4><p>Pesquisa aplicada em micro-organismos capazes de degradar polímeros e restaurar ecossistemas contaminados.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='bloco'><div class='icone'>🤖</div><h4>Inteligência Artificial</h4><p>Monitoramento automatizado do ambiente, mapeamento de hotspots de poluição e análise preditiva de eficiência biológica.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='bloco'><div class='icone'>🌱</div><h4>Impacto Ambiental Positivo</h4><p>Redução mensurável de microplásticos e recuperação da biodiversidade aquática e terrestre.</p></div>", unsafe_allow_html=True)

    st.markdown("---")

    # ========= CTA final =========
    st.markdown("""
        <div style='text-align:center; margin-top:30px;'>
            <h3 style='color:#00c896;'>Junte-se à revolução verde digital 🌎</h3>
            <p>Explore nossos dados no painel interativo e veja o impacto em tempo real.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("<div style='text-align:center;'>⬅️ Navegue pelo menu lateral para conhecer mais</div>", unsafe_allow_html=True)
