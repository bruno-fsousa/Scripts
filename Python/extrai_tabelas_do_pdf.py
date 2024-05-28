# -*- coding: utf-8 -*-

# Instale as dependências
# pip install tabula-py==2.9.3

# Instale o java

import os
import tabula
from pathlib import Path

# Definir o caminho para o Java
# IMPORTANTE: Adicionar a variável JAVA_HOME (com esse mesmo nome) e esse mesmo caminho nas variáveis de ambiente do Windows

# Definir a variável de ambiente JAVA_HOME
os.environ["JAVA_HOME"] = r'C:\Program Files\Common Files\Oracle\Java\javapath'

# Pasta deste script
dir_path = Path(__file__).parent

# Caminho para o arquivo PDF
pdf_path = dir_path.joinpath("2022_Soeharto_Csapo_Exploring_Indonesian_student_misconcepti.pdf")

# Função para extrair tabelas do PDF
def extract_tables(pdf_path):
    # Extrair tabelas usando a função read_pdf
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

# Extrair tabelas do PDF
tables = extract_tables(pdf_path)

# Mostrar o número de tabelas extraídas
print(f'Number of tables extracted: {len(tables)}')

# Salvar cada tabela em um arquivo CSV
for i, table in enumerate(tables):
    output_path = f'table_{i + 1}.csv'
    table.to_csv(output_path, index=False)  # Salva a tabela em um arquivo CSV sem índice
    print(f'Table {i + 1} saved to {output_path}')

