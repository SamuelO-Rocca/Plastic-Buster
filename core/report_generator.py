"""
Módulo: report_generator.py
Descrição: Gera relatórios inteligentes com base nos resultados do modelo, correlações e insights simbióticos.
Autor: Samuel
Data: 2025
"""

import os
import pandas as pd
from datetime import datetime
from fpdf import FPDF
from utils.logger import registrar_evento, registrar_erro
from utils.constants import REPORTS_PATH

# =============================================================================
# 🧠 Classe Principal — ReportGenerator
# =============================================================================

class ReportGenerator:
    """
    Classe responsável por consolidar e gerar relatórios automatizados (PDF/JSON/Dict)
    com análises preditivas, correlações e observações simbióticas.
    """

    def __init__(self, output_dir: str = REPORTS_PATH):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    # -------------------------------------------------------------------------
    # 📊 Geração de Relatório Geral
    # -------------------------------------------------------------------------
    def generate_report(self, df: pd.DataFrame, predictions=None, correlations=None, insights=None):
        """
        Gera relatório completo em PDF com dados, resultados do modelo e análises simbióticas.
        """
        try:
            registrar_evento("Iniciando geração de relatório inteligente...")

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(self.output_dir, f"Relatorio_PlasticBusters_{timestamp}.pdf")

            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            # Cabeçalho
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "🧬 Relatório Inteligente — Projeto Plastic Busters", ln=True, align="C")
            pdf.ln(5)

            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 10, f"Data de Geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True)
            pdf.ln(10)

            # Seção 1 — Dados
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 10, "1️⃣ Visão Geral dos Dados", ln=True)
            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, f"O dataset processado contém {df.shape[0]} registros e {df.shape[1]} variáveis.")
            pdf.ln(5)

            # Estatísticas descritivas
            try:
                stats = df.describe().round(2).to_string()
                pdf.multi_cell(0, 6, stats)
            except Exception:
                pdf.multi_cell(0, 6, "Não foi possível gerar estatísticas descritivas para este dataset.")

            pdf.ln(8)

            # Seção 2 — Predições
            if predictions is not None:
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, "2️⃣ Resultados Preditivos", ln=True)
                pdf.set_font("Arial", "", 11)

                pred_summary = pd.Series(predictions).value_counts(normalize=True).round(3) * 100
                pdf.multi_cell(0, 8, f"Distribuição das predições:\n{pred_summary.to_string()}")
                pdf.ln(8)

            # Seção 3 — Correlações
            if correlations is not None and not correlations.empty:
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, "3️⃣ Correlações Identificadas", ln=True)
                pdf.set_font("Arial", "", 11)

                top_corr = correlations.abs().unstack().sort_values(ascending=False).drop_duplicates().head(10)
                pdf.multi_cell(0, 8, f"Principais correlações detectadas:\n{top_corr.to_string()}")
                pdf.ln(8)

            # Seção 4 — Insights Simbióticos
            if insights:
                pdf.set_font("Arial", "B", 14)
                pdf.cell(0, 10, "4️⃣ Insights Simbióticos e Explicações", ln=True)
                pdf.set_font("Arial", "", 11)
                for i, insight in enumerate(insights, start=1):
                    pdf.multi_cell(0, 8, f"🔹 {i}. {insight}")
                pdf.ln(10)

            # Rodapé
            pdf.set_font("Arial", "I", 10)
            pdf.cell(0, 10, "Relatório gerado automaticamente pelo sistema Plastic Busters IA.", ln=True, align="C")

            pdf.output(file_path)
            registrar_evento(f"Relatório gerado com sucesso: {file_path}")

            return file_path

        except Exception as e:
            registrar_erro("ReportGenerator", e)
            return None

    # -------------------------------------------------------------------------
    # 📦 Exportação JSON
    # -------------------------------------------------------------------------
    def export_json(self, df: pd.DataFrame, predictions=None, correlations=None, insights=None):
        """
        Exporta relatório resumido em formato JSON.
        """
        try:
            data = {
                "meta": {"generated_at": datetime.now().isoformat()},
                "shape": {"rows": len(df), "columns": len(df.columns)},
                "predictions_summary": (
                    pd.Series(predictions).value_counts().to_dict() if predictions is not None else {}
                ),
                "insights": insights or [],
            }
            json_path = os.path.join(self.output_dir, f"Resumo_PlasticBusters.json")
            pd.Series(data).to_json(json_path, indent=4)
            registrar_evento(f"Resumo JSON exportado: {json_path}")
            return json_path
        except Exception as e:
            registrar_erro("ReportJSON", e)
            return None
