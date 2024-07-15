from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, Label, Button
import sys
import subprocess


def main_work():
    folder = filedialog.askdirectory()

    if not folder:
        return

    filename = filedialog.asksaveasfilename(defaultextension=".tiff", filetypes=[("TIFF files", "*.tiff")])


    if not filename:
        return
    
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images = [Image.open(file) for file in files]

    margin = 50
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

    collage = Image.new('RGB', (collage_width, collage_height), "white")

    x, y = border, border
    for i, img in enumerate(images):
        collage.paste(img, (x, y))
        x += width + margin
        if (i + 1) % n == 0:
            x = border
            y += height + margin
    
    collage.save(filename, format='TIFF')
    print("Коллаж сохранен как", filename)
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        subprocess.run(['open', filename])

def create_collage():
    root = tk.Tk()
    root.title("Тестовое приложение")
    root.geometry('400x300')
    
    label = Label(root, text="Тестовое задание в компанию MYCEGO. \nИсполнитель: Нуртдинов Айнур", font=('Helvetica', 16), fg='blue')
    label.pack(expand=True)
    
    btn_choose_directory = Button(root, text="Выбрать папку", command=main_work)
    btn_choose_directory.pack(side=tk.BOTTOM, pady=10)
    root.mainloop()

if __name__ == "__main__":
    create_collage()