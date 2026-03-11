import os
folders = ["0310test_A", "0310test_B"]
for f in folders:
    if not os.path.exists(f):
        os.mkdir(f)
print("Folders created!")