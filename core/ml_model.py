"""
Módulo: ml_model.py
Descrição: Responsável por treinar, avaliar e fazer predições usando Machine Learning
Autor: Samuel
Data: 2025
"""

import os
import sys
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from utils.logger import registrar_evento, registrar_erro
from utils.constants import MODEL_PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# =============================================================================
# ⚙️ Classe Principal — MLModel
# =============================================================================

class MLModel:
    """
    Classe responsável por manipular o ciclo de vida de um modelo de Machine Learning:
    treinamento, predição e persistência.   
    """

    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()

    # -------------------------------------------------------------------------
    # 🧠 Treinamento
    # -------------------------------------------------------------------------
    def train(self, df: pd.DataFrame, target_col: str):
        """
        Treina o modelo de Machine Learning com base no DataFrame fornecido.
        """
        try:
            registrar_evento("Iniciando treinamento do modelo...")

            if target_col not in df.columns:
                raise ValueError(f"A coluna alvo '{target_col}' não foi encontrada no DataFrame.")

            X = df.drop(columns=[target_col])
            y = df[target_col]

            # Encoding de variáveis categóricas
            X = pd.get_dummies(X, drop_first=True)

            # Normalização
            X_scaled = self.scaler.fit_transform(X)
            y_encoded = self.label_encoder.fit_transform(y)

            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y_encoded, test_size=0.2, random_state=42
            )

            # Modelo base (pode ser substituído por IA customizada)
            self.model = RandomForestClassifier(
                n_estimators=200, max_depth=12, random_state=42
            )
            self.model.fit(X_train, y_train)

            y_pred = self.model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)

            registrar_evento(f"Modelo treinado com acurácia: {acc:.4f}")
            registrar_evento(f"Relatório:\n{classification_report(y_test, y_pred)}")

            # Persistência
            self._save_model()

            return acc

        except Exception as e:
            registrar_erro("ML_Training", e)
            return None

    # -------------------------------------------------------------------------
    # 🔮 Predição
    # -------------------------------------------------------------------------
    def predict(self, df: pd.DataFrame):
        """
        Realiza predição com base no modelo treinado.
        """
        try:
            if self.model is None:
                self._load_model()

            df_encoded = pd.get_dummies(df, drop_first=True)
            df_encoded = df_encoded.reindex(columns=self.model.feature_names_in_, fill_value=0)
            df_scaled = self.scaler.transform(df_encoded)

            preds = self.model.predict(df_scaled)
            preds_decoded = self.label_encoder.inverse_transform(preds)

            registrar_evento(f"Predição realizada com sucesso ({len(preds_decoded)} registros).")
            return preds_decoded

        except Exception as e:
            registrar_erro("ML_Prediction", e)
            return []

    # -------------------------------------------------------------------------
    # 💾 Persistência
    # -------------------------------------------------------------------------
    def _save_model(self):
        """
        Salva modelo e pré-processadores.
        """
        try:
            os.makedirs(self.model_path, exist_ok=True)
            joblib.dump(self.model, os.path.join(self.model_path, "model.pkl"))
            joblib.dump(self.scaler, os.path.join(self.model_path, "scaler.pkl"))
            joblib.dump(self.label_encoder, os.path.join(self.model_path, "encoder.pkl"))
            registrar_evento(f"Modelo salvo em: {self.model_path}")
        except Exception as e:
            registrar_erro("ML_SaveModel", e)

    def _load_model(self):
        """
        Carrega modelo treinado previamente.
        """
        try:
            self.model = joblib.load(os.path.join(self.model_path, "model.pkl"))
            self.scaler = joblib.load(os.path.join(self.model_path, "scaler.pkl"))
            self.label_encoder = joblib.load(os.path.join(self.model_path, "encoder.pkl"))
            registrar_evento("Modelo carregado com sucesso!")
        except Exception as e:
            registrar_erro("ML_LoadModel", e)
            raise RuntimeError("Falha ao carregar modelo.")

