import os

folder = "files"

files = os.listdir(folder)

for i, file in enumerate(files):
    old_path = os.path.join(folder, file)
    new_name = f"product_{i+1}.jpg"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("Files renamed successfully!")
