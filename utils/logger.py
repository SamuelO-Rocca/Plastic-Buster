"""
Módulo: logger.py
Descrição: Sistema de logging estruturado para o projeto Plastic Buster.
Autor: Samuel
Data: 2025
"""

import os
import logging
from datetime import datetime
from utils.constants import LOG_FILE

# =============================================================================
# 🔧 CONFIGURAÇÃO PADRÃO DO LOGGER
# =============================================================================

def configurar_logger(nome_modulo: str = "PlasticBuster"):
    """
    Cria e configura um logger com formato padrão para o projeto.
    Retorna o objeto logger configurado.
    """
    logger = logging.getLogger(nome_modulo)

    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)

        # Criação do diretório de logs, caso não exista
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

        # Formato das mensagens
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Saída para arquivo
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Saída para console (útil no modo Streamlit)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# =============================================================================
# 🧰 FUNÇÕES DE SUPORTE
# =============================================================================

def registrar_evento(mensagem: str, nivel: str = "info"):
    """
    Função simples para registrar logs de forma direta.
    Níveis: info, warning, error, critical, debug
    """
    logger = configurar_logger()

    niveis = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "critical": logger.critical,
        "debug": logger.debug
    }

    if nivel not in niveis:
        logger.warning(f"Nível de log inválido: {nivel}. Usando 'info' como padrão.")
        nivel = "info"

    niveis[nivel](mensagem)


def log_execucao(modulo: str, acao: str, status: str = "ok"):
    """
    Registra logs padronizados de execução entre módulos.
    Exemplo: log_execucao("IA_Model", "Treinamento", "sucesso")
    """
    logger = configurar_logger()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mensagem = f"[{timestamp}] | Módulo: {modulo} | Ação: {acao} | Status: {status}"
    logger.info(mensagem)


def registrar_erro(modulo: str, erro: Exception):
    """
    Registra erros críticos com contexto.
    """
    logger = configurar_logger()
    logger.error(f"[{modulo}] Erro detectado: {str(erro)}", exc_info=True)
