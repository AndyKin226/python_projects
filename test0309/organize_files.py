import os
import shutil

folder = "test_folder"

for file in os.listdir(folder):

    if file.endswith(".jpg") or file.endswith(".png"):
        target = "images"

    elif file.lower().endswith(".pdf"):
        target = "pdf"

    elif file.endswith(".xlsx"):
        target = "excel"

    else:
        target = "others"

    os.makedirs(target, exist_ok=True)

    shutil.move(os.path.join(folder, file), os.path.join(target, file))
