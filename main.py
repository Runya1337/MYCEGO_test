from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
import sys

def create_collage():

    # Диалог выбора папки
    root = tk.Tk()
    root.withdraw()  # Убираем главное окно Tkinter
    folder = filedialog.askdirectory()  # Диалог выбора директории

    if not folder:
        return

    filename = filedialog.asksaveasfilename(defaultextension=".tiff", filetypes=[("TIFF files", "*.tiff")])


    if not filename:
        return
    
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images = [Image.open(file) for file in files]

    # Определяем размер коллажа (здесь мы делаем сетку размером n x n)
    margin = 50  # отступ между изображениями
    # дополнительный отступ по краям
    if len(images) % 4 == 0:
        n = 4
        m = len(images) / n
    else:
        n = int(len(images)**0.5) + 1
        m = len(images) / n
    if int(m) < m:
        m = int(m) + 1
    m = int(m)
    width, height = images[0].size
    border = width // 3
    collage_width = width * n + margin * (n - 1) + border * 2
    collage_height = height * m + margin * (m - 1) + border * 2

    # Создаем новое изображение для коллажа с белым фоном
    collage = Image.new('RGB', (collage_width, collage_height), "white")

    # Размещаем изображения в коллаже
    x, y = border, border
    for i, img in enumerate(images):
        # Вычисляем позицию с учетом отступов
        collage.paste(img, (x, y))
        x += width + margin
        if (i + 1) % n == 0:  # Переход на новую строку
            x = border
            y += height + margin
    
    collage.save(filename, format='TIFF')
    print("Коллаж сохранен как", filename)

if __name__ == "__main__":
    create_collage()