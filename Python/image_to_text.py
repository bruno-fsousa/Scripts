# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image
import pytesseract

dir_path = Path(__file__).parent

images_list = []
extensions = [".png", ".jpg", ".jpeg"]
for ext in extensions:
  try:
    images_list.extend(dir_path.glob(f"*{ext.lower()}"))
  except:
    images_list.extend(dir_path.glob(f"*{ext.upper()}"))

extracted_text = ""
for i, image_path in enumerate(images_list, start=1):
  image = Image.open(image_path)
  extracted_text += "\n\n"
  extracted_text += pytesseract.image_to_string(image)
  print(f"Imagem {i} extraída com sucesso.")

text_file_path = Path.joinpath(dir_path, "extracted_text.txt")
with open(text_file_path, 'w', encoding="utf-8") as text_file:
  text_file.write(extracted_text)

# Mensagem final de sucesso
print(f"Arquivo {str(text_file_path)} criado com sucesso")


