# Пишем программу на Python по очистке компа от мусора

1.0

import os

directory_path = "C:/Users/Asus/Downloads"

directory_content = os.listdir(directory_path)
# print(directory_content)
for filename in directory_content:
    if filename.startswith("ex.img.file.name"):
        os.remove(os.path.join(directory_path, filename))
        print(filename, "is here")


2.0

import os

dirictory_path = "C:/Users/Asus/Pictures/Screenshots"

dirictory_img = os.listdir(dirictory_path)
print(dirictory_img)
os.remove(dirictory_path + "/" + "filename.jpg")
