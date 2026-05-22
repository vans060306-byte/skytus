import os

path = "."

files = os.listdir(path)

print("Files and Folders:")
for file in files:
    print(file)