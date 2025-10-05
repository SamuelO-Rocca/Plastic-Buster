"""
Módulo: symbiose_model.py
Descrição: Modelagem simbiótica entre fungos, microplásticos e variáveis ambientais.
Autor: Samuel
Data: 2025
"""

import numpy as np
import pandas as pd
from core.correlation import gerar_correlacoes
from utils.logger import registrar_evento, registrar_erro

# =============================================================================
# 🧬 Classe Principal — SymbioseModel
# =============================================================================

class SymbioseModel:
    """
    Modelo simbiótico: analisa interações entre fungos e microplásticos com base em variáveis ambientais.
    Gera métricas de simbiose, degradação e sinergia microbiana.
    """

    def __init__(self):
        self.symbiose_index = None
        self.degradation_rate = None
        self.eco_risk = None

    # -------------------------------------------------------------------------
    # 🔍 Função principal — Análise simbiótica
    # -------------------------------------------------------------------------
    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analisa o dataset e gera índices de simbiose, degradação e risco ecológico.
        Retorna um DataFrame enriquecido.
        """
        try:
            registrar_evento("Iniciando análise simbiótica dos dados ambientais.")

            df = df.copy()
            df = df.select_dtypes(include=[np.number]).dropna()

            if df.empty:
                raise ValueError("O dataset não contém dados numéricos suficientes para análise simbiótica.")

            # Correlações internas
            corr = gerar_correlacoes(df)

            # Índice simbiótico — combinação ponderada de variáveis ambientais
            temp_factor = df["temperatura"].mean() if "temperatura" in df else 0
            ph_factor = df["ph"].mean() if "ph" in df else 7
            ox_factor = df["oxigenio"].mean() if "oxigenio" in df else 0
            hum_factor = df["umidade"].mean() if "umidade" in df else 0

            # Cálculo simbiótico
            self.symbiose_index = round(
                (ox_factor * 0.4 + hum_factor * 0.3 + (7 - abs(7 - ph_factor)) * 0.2 + (temp_factor / 30) * 0.1), 3
            )

            # Taxa de degradação prevista (proxy para eficiência fúngica)
            self.degradation_rate = round(self.symbiose_index * np.random.uniform(0.8, 1.2), 3)

            # Risco ecológico — inverso do equilíbrio simbiótico
            self.eco_risk = round(1 - min(self.symbiose_index, 1), 3)

            # Aplica resultados no DataFrame
            df["índice_simbiose"] = self.symbiose_index
            df["taxa_degradacao"] = self.degradation_rate
            df["risco_ecologico"] = self.eco_risk

            registrar_evento(f"Análise simbiótica concluída — Índice: {self.symbiose_index}")

            return df

        except Exception as e:
            registrar_erro("Symbiose_Analysis", e)
            return pd.DataFrame()

    # -------------------------------------------------------------------------
    # 📈 Geração de insights textuais
    # -------------------------------------------------------------------------
    def generate_insights(self) -> list:
        """
        Gera interpretações simbióticas em linguagem natural (IA interpretativa).
        """
        try:
            insights = []

            if self.symbiose_index is None:
                insights.append("Nenhuma análise simbiótica foi realizada ainda.")
                return insights

            # Interpretações qualitativas
            if self.symbiose_index >= 0.8:
                insights.append("🟢 Alto potencial simbiótico: fungos adaptados ao ambiente e degradação eficiente.")
            elif 0.5 <= self.symbiose_index < 0.8:
                insights.append("🟡 Simbiose moderada: há interação, mas fatores ambientais limitam a eficiência.")
            else:
                insights.append("🔴 Baixo potencial simbiótico: ambiente hostil à ação microbiana degradadora.")

            if self.degradation_rate > 0.9:
                insights.append("🔬 A taxa de degradação é considerada alta, indicando forte ação enzimática fúngica.")
            elif self.degradation_rate > 0.6:
                insights.append("🧪 Taxa de degradação intermediária, dependente da umidade e do oxigênio disponível.")
            else:
                insights.append("⚠️ Baixa taxa de degradação — possível inibição por temperatura ou pH fora do ideal.")

            if self.eco_risk > 0.5:
                insights.append("🚨 Alto risco ecológico: desequilíbrio simbiótico pode impactar a regeneração ambiental.")
            else:
                insights.append("🌱 Risco ecológico controlado: equilíbrio simbiótico estável no ecossistema.")

            return insights

        except Exception as e:
            registrar_erro("Symbiose_Insights", e)
            return ["Falha ao gerar insights simbióticos."]

