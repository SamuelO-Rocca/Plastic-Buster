"""
Módulo: data_loader.py
Descrição: Responsável por carregar dados de múltiplas fontes (CSV, JSON, PDF, DB) e padronizar para DataFrame.
Autor: Samuel
Data: 2025
"""

import os
import pandas as pd
import sqlite3
import pdfplumber
from utils.constants import SUPPORTED_FORMATS, DEFAULT_DB_PATH
from utils.logger import registrar_evento, registrar_erro

# =============================================================================
# 🔍 Função principal de carregamento
# =============================================================================

def load_data(file_path: str) -> pd.DataFrame:
    """
    Carrega dados a partir de CSV, JSON, PDF ou Banco de Dados (SQLite).
    Retorna um DataFrame padronizado.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        ext = os.path.splitext(file_path)[-1].lower().replace('.', '')

        registrar_evento(f"Iniciando leitura do arquivo: {file_path}")

        if ext == "csv":
            df = pd.read_csv(file_path, encoding="utf-8")

        elif ext == "json":
            df = pd.read_json(file_path, encoding="utf-8")

        elif ext == "pdf":
            df = _read_pdf_to_dataframe(file_path)

        elif ext == "db":
            df = _read_from_database(file_path)

        else:
            raise ValueError(f"Formato de arquivo não suportado: {ext}. Formatos aceitos: {SUPPORTED_FORMATS}")

        registrar_evento(f"Arquivo {file_path} carregado com sucesso! ({len(df)} registros)")
        return _normalize_dataframe(df)

    except Exception as e:
        registrar_erro("DataLoader", e)
        return pd.DataFrame()


# =============================================================================
# 🧩 Funções auxiliares
# =============================================================================

def _read_pdf_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Extrai tabelas de um arquivo PDF e converte em DataFrame.
    Utiliza pdfplumber.
    """
    try:
        registrar_evento(f"Lendo tabelas do PDF: {file_path}")
        tables = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    tables.append(pd.DataFrame(table[1:], columns=table[0]))

        if not tables:
            raise ValueError("Nenhuma tabela encontrada no PDF.")

        df = pd.concat(tables, ignore_index=True)
        registrar_evento(f"PDF processado com {len(df)} linhas extraídas.")
        return df

    except Exception as e:
        registrar_erro("PDF_Loader", e)
        return pd.DataFrame()


def _read_from_database(db_path: str) -> pd.DataFrame:
    """
    Lê dados do banco SQLite (tabela padrão ou detectada automaticamente).
    """
    try:
        registrar_evento(f"Conectando ao banco de dados: {db_path}")
        conn = sqlite3.connect(db_path)

        # Descobre tabelas disponíveis
        tabelas = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        if tabelas.empty:
            raise ValueError("Nenhuma tabela encontrada no banco de dados.")

        primeira_tabela = tabelas.iloc[0, 0]
        df = pd.read_sql_query(f"SELECT * FROM {primeira_tabela}", conn)
        conn.close()

        registrar_evento(f"Tabela '{primeira_tabela}' carregada com sucesso. Registros: {len(df)}")
        return df

    except Exception as e:
        registrar_erro("DB_Loader", e)
        return pd.DataFrame()


def _normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza colunas (nomes, espaços, tipos).
    """
    try:
        registrar_evento("Normalizando DataFrame.")
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        df = df.drop_duplicates().reset_index(drop=True)
        df = df.fillna(value=None)
        return df
    except Exception as e:
        registrar_erro("Normalizer", e)
        return df
