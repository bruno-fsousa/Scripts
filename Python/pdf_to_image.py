# -*- coding: utf-8 -*-

# Intalação das bibliotecas
"""
Para Importar fitz (versão PyMuPDF==1.24.4 no dia da instalação)
pip install PyMuPDF 
Para importar Image from PIL:
pip install Pillow
"""

from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_images(pdf_path, start=1, end=5):

    with fitz.open(pdf_path) as pdf_document:

        # Pasta de saída para as imagens
        output_folder = Path.joinpath(pdf_path.parent, "Imagens")

        # Verificar se a pasta de saída existe e criar se não existir
        output_folder.mkdir(exist_ok=True)

        # Fazendo alguns ajustes no intervalo de páginas.
        if end < start:
            raise ValueError("ERRO. start > end.\nAjuste o intervalo de páginas.")
        if start < 1:
            raise ValueError("ERRO. A página inicial (start) deve ser maior ou igual a 1, assim como no arquivo pdf.\n")

        # Iterar sobre as páginas do PDF
        for page_number in range((start - 1), (end - 1) + 1):

            # Caminho da imagem
            image_path = Path.joinpath(output_folder, f"page_{page_number + 1}.png")

            # Verifica se a imagem já existe
            if not image_path.exists():

                # Obter a página atual
                page = pdf_document[page_number]

                # Renderizar a página como uma imagem (resolução de 300 DPI)
                image = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))

                # Converter a imagem para o formato PIL
                pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)

                # Salvar a imagem
                pil_image.save(image_path)
                print(f"Salvo: {image_path}")

# Caminho para o arquivo PDF de entrada
pdf_path = Path("2022_Soeharto_Csapo_Exploring_Indonesian_student_misconcepti.pdf")

# Converter o PDF para imagens
convert_pdf_to_images(pdf_path, start=1, end=8)
