"""
Módulo: preprocessing.py
Descrição: Responsável pela limpeza, padronização e engenharia de atributos dos dados.
Autor: Samuel
Data: 2025
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from utils.logger import registrar_evento, registrar_erro

# =============================================================================
# 🧠 Classe Principal — DataPreprocessor
# =============================================================================

class DataPreprocessor:
    """
    Classe para executar as etapas de pré-processamento dos dados antes do treinamento do modelo.
    """

    def __init__(self):
        self.scaler = MinMaxScaler()
        self.imputer = SimpleImputer(strategy="mean")
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

    # -------------------------------------------------------------------------
    # 🚿 Limpeza
    # -------------------------------------------------------------------------
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Realiza limpeza básica: remove duplicados, normaliza colunas, trata outliers.
        """
        try:
            registrar_evento("Iniciando limpeza de dados.")

            # Padroniza nomes das colunas
            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

            # Remove duplicados
            df = df.drop_duplicates()

            # Remove linhas completamente vazias
            df = df.dropna(how="all")

            # Substitui strings vazias por NaN
            df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

            # Conversão automática de tipos numéricos
            df = df.apply(self._convert_numeric, axis=0)

            registrar_evento(f"Limpeza concluída: {df.shape[0]} linhas, {df.shape[1]} colunas.")
            return df

        except Exception as e:
            registrar_erro("Preprocessing_Clean", e)
            return df

    # -------------------------------------------------------------------------
    # 🔧 Pré-processamento completo
    # -------------------------------------------------------------------------
    def transform(self, df: pd.DataFrame, target_col: str = None):
        """
        Executa normalização, imputação e codificação.
        Retorna X (features) e y (target, se existir).
        """
        try:
            registrar_evento("Iniciando transformação de dados.")

            X = df.copy()
            y = None

            if target_col and target_col in X.columns:
                y = X[target_col]
                X = X.drop(columns=[target_col])

            # Identifica colunas numéricas e categóricas
            numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
            categorical_cols = X.select_dtypes(include=["object", "category"]).columns

            # Imputação numérica
            X[numeric_cols] = self.imputer.fit_transform(X[numeric_cols])

            # Normalização
            X[numeric_cols] = self.scaler.fit_transform(X[numeric_cols])

            # Codificação de variáveis categóricas
            if len(categorical_cols) > 0:
                cat_encoded = self.encoder.fit_transform(X[categorical_cols])
                cat_df = pd.DataFrame(
                    cat_encoded, columns=self.encoder.get_feature_names_out(categorical_cols)
                )
                X = pd.concat([X.drop(columns=categorical_cols), cat_df], axis=1)

            registrar_evento(f"Transformação concluída. Shape final: {X.shape}")
            return (X, y) if y is not None else X

        except Exception as e:
            registrar_erro("Preprocessing_Transform", e)
            return (df, None)

    # -------------------------------------------------------------------------
    # 🧩 Função auxiliar interna
    # -------------------------------------------------------------------------
    @staticmethod
    def _convert_numeric(series: pd.Series):
        """
        Tenta converter colunas para numéricas sempre que possível.
        """
        try:
            return pd.to_numeric(series, errors="ignore")
        except Exception:
            return series
