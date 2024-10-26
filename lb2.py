import os
import shutil

current_directory = os.getcwd()
print("Назва папки:", os.path.basename(current_directory))

print("Повний шлях до папки:", current_directory)

src = "start.txt"
dst = "fin.txt"

if os.path.exists(src):
    os.rename(src, dst)
    print(f"Файл {src} перейменовано на {dst}")

