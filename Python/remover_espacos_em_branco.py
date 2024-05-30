# -*- coding: utf-8 -*-

"""
Objetivo: Remover linhas em branco de um arquivo de texto.
"""

import re
from pathlib import Path

def processar_arquivo(file_path, new_file_path=None):
    """
    Lê, processa e escreve o conteúdo de um arquivo removendo espaços em branco e
    quebras de linha repetidas.
    
    Args:
    file_path (str or Path): O caminho do arquivo a ser processado.
    new_file_path (str or Path, opcional): O caminho para o novo arquivo. Se não fornecido, o arquivo original será sobrescrito.
    """
    file_path = Path(file_path).resolve()
    
    # Lê o conteúdo do arquivo
    with open(file_path, encoding="utf-8", errors="ignore") as file:
        texto = file.read()
    
    # Remove espaços em branco no início e no final de cada linha
    texto = re.sub(r'^[ \t]+|[ \t]+$', '', texto, flags=re.MULTILINE)
    
    # Remove quebras de linha repetidas
    texto = re.sub(r'\n{2,}', '\n\n', texto)
    
    # Define o caminho para o novo arquivo
    if new_file_path:
        new_file_path = Path(new_file_path).resolve()
    else:
        new_file_path = file_path  # Sobrescreve o arquivo original se não for fornecido um novo caminho
    
    # Escreve o texto processado no novo arquivo
    with open(new_file_path, "w", encoding="utf-8", errors="ignore") as new_file:
        new_file.write(texto)

# Define o caminho do arquivo
file_path = "temp.txt"

# Chama a função para processar o arquivo, sobrescrevendo o original
processar_arquivo(file_path)

# Chama a função para processar o arquivo, salvando em um novo arquivo
# processar_arquivo(file_path, "temp_processed.txt")
