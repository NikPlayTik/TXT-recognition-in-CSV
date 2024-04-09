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

# Распознавание текста на изображении
text = pytesseract.image_to_string(img)

print(text)