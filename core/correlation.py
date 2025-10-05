"""
Módulo: correlation.py
Descrição: Responsável por gerar e analisar correlações entre variáveis do projeto Plastic Buster.
Autor: Samuel
Data: 2025
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from utils.logger import registrar_evento, registrar_erro

# ============================================================================

def calcular_correlacoes(df: pd.DataFrame, metodo: str = "pearson"):
    """
    Calcula a matriz de correlação entre variáveis numéricas do dataset.
    Suporta Pearson (linear) e Spearman (não linear).
    """
    try:
        registrar_evento(f"Iniciando análise de correlação ({metodo}).")

        if df.empty:
            raise ValueError("DataFrame vazio. Nenhum dado disponível para análise de correlação.")

        if metodo not in ["pearson", "spearman"]:
            raise ValueError(f"Método '{metodo}' inválido. Use 'pearson' ou 'spearman'.")

        # Seleciona apenas colunas numéricas
        df_numerico = df.select_dtypes(include=[np.number])

        if df_numerico.shape[1] < 2:
            raise ValueError("Número insuficiente de colunas numéricas para correlação.")

        corr_matrix = df_numerico.corr(method=metodo)
        registrar_evento("Matriz de correlação gerada com sucesso.", "info")

        return corr_matrix

    except Exception as e:
        registrar_erro("Correlation", e)
        return pd.DataFrame()


# ============================================================================

def correlacao_personalizada(df: pd.DataFrame, col1: str, col2: str, metodo: str = "pearson"):
    """
    Calcula a correlação entre duas variáveis específicas.
    Retorna o coeficiente e o p-valor.
    """
    try:
        if col1 not in df.columns or col2 not in df.columns:
            raise KeyError(f"Colunas '{col1}' ou '{col2}' não encontradas no DataFrame.")

        x, y = df[col1].astype(float), df[col2].astype(float)

        if metodo == "pearson":
            coef, p_val = pearsonr(x, y)
        elif metodo == "spearman":
            coef, p_val = spearmanr(x, y)
        else:
            raise ValueError("Método inválido. Escolha entre 'pearson' ou 'spearman'.")

        registrar_evento(f"Correlação {metodo} entre {col1} e {col2}: coef={coef:.3f}, p={p_val:.3f}")
        return coef, p_val

    except Exception as e:
        registrar_erro("Correlation", e)
        return None, None


# ============================================================================

def gerar_relatorio_correlacao(df: pd.DataFrame, metodo: str = "pearson"):
    """
    Gera um relatório simples de correlações relevantes (coeficiente > 0.5 ou < -0.5).
    Retorna um DataFrame resumido com pares correlacionados.
    """
    try:
        corr_matrix = calcular_correlacoes(df, metodo)
        if corr_matrix.empty:
            return pd.DataFrame()

        resultados = []
        for col1 in corr_matrix.columns:
            for col2 in corr_matrix.columns:
                if col1 != col2:
                    coef = corr_matrix.loc[col1, col2]
                    if abs(coef) >= 0.5:
                        resultados.append({
                            "variavel_1": col1,
                            "variavel_2": col2,
                            "coeficiente": round(coef, 3),
                            "tipo": "positiva" if coef > 0 else "negativa"
                        })

        registrar_evento("Relatório de correlação gerado com sucesso.", "info")
        return pd.DataFrame(resultados).drop_duplicates(subset=["variavel_1", "variavel_2"])

    except Exception as e:
        registrar_erro("Correlation", e)
        return pd.DataFrame()
