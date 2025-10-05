"""
Módulo: constants.py
Descrição: Central de constantes e parâmetros fixos do projeto Plastic Buster.
Autor: Samuel
Data: 2025
"""

import os

# === PATHS GLOBAIS ===========================================================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
MODEL_DIR = os.path.join(BASE_DIR, "models")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

for path in [UPLOAD_DIR, MODEL_DIR, REPORT_DIR]:
    os.makedirs(path, exist_ok=True)

# === CONFIGURAÇÕES DE BANCO DE DADOS ========================================

DEFAULT_DB_PATH = os.path.join(DATA_DIR, "plastic_buster.db")
DB_TABLES = {
    "fungos": "tb_fungos",
    "polimeros": "tb_polimeros",
    "interacoes": "tb_interacoes"
}

# === CONFIGURAÇÕES DE INTERFACE =============================================

APP_TITLE = "🌍 Plastic Buster — Sistema de Análise Biotecnológica"
APP_DESCRIPTION = (
    "Plataforma integrada para análise de **microplásticos**, "
    "interações fúngicas e correlação ambiental com **IA e Machine Learning**."
)

THEME = {
    "background_color": "#0E1117",
    "text_color": "#FAFAFA",
    "accent_color": "#1DB954",
    "warning_color": "#FFCC00",
    "error_color": "#FF4B4B"
}

# === PARÂMETROS DE IA E MACHINE LEARNING =====================================

ML_CONFIG = {
    "modelo_principal": os.path.join(MODEL_DIR, "eco_simbiose.pkl"),
    "taxa_treinamento": 0.8,
    "random_state": 42,
    "features_padrao": ["ph", "temperatura", "umidade", "oxigenio", "polimero", "fungo"],
    "target": "eficiencia_biodegradacao"
}

# === SUPORTE A FORMATOS DE DADOS ============================================

SUPPORTED_FORMATS = ["csv", "json", "pdf", "db"]
DEFAULT_ENCODING = "utf-8"

# === VARIÁVEIS AMBIENTAIS RELEVANTES ========================================

ENV_VARS = {
    "TEMPERATURA": "°C",
    "UMIDADE": "%",
    "OXIGENIO": "%",
    "PH": "",
    "CONDICAO_SOLO": ["Árido", "Tropical", "Temperado", "Úmido"]
}

# === MAPEAMENTO VISUAL ======================================================

COLOR_MAPS = {
    "Fungo": "#7FFFD4",
    "Polímero": "#ADD8E6",
    "Alta Eficiência": "#4CAF50",
    "Média Eficiência": "#FFC107",
    "Baixa Eficiência": "#F44336"
}

# === LOGS E DEBUG ===========================================================

LOG_FILE = os.path.join(BASE_DIR, "logs", "system.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# === CHAVES E CÓDIGOS =======================================================

VERSION = "1.0.0"
AUTHOR = "Equipe Plastic Buster"
LICENSE = "MIT"

# === FUNÇÕES DE SUPORTE =====================================================

def get_version():
    """Retorna a versão atual do sistema."""
    return VERSION

def get_theme():
    """Retorna o dicionário de tema da interface."""
    return THEME

def get_ml_config():
    """Retorna as configurações padrão de IA."""
    return ML_CONFIG
