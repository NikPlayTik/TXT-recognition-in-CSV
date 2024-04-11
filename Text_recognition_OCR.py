import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Создание экземпляра Tkinter
root = tk.Tk()
root.withdraw()  # Скрытие окна Tkinter

# Открытие диалога выбора файлов
file_path = filedialog.askopenfilename()

# Загрузка изображения
img = Image.open(file_path)

pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'

# Установите параметр языка
tessdata_dir_config = r'--tessdata-dir ".\Tesseract-OCR\tessdata" --oem 3 --psm 6 -l eng+rus'
# Распознавание текста на изображении
text = pytesseract.image_to_string(img, config=tessdata_dir_config)

print(text)