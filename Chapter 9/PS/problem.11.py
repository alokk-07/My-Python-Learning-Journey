# Write a python program to rename a file to “renamed_by_ python.txt.

with open("old.txt") as f:
    content = f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(content)


# or
''' 

import os

# Open the file (optional)
with open("old.txt", "r") as f:
    print(f.read())

# Rename the file
os.rename("old.txt", "renamed_by_python.txt")

print("File renamed successfully.")


''' 
# or 
'''

import shutil

shutil.move("old.txt", "renamed_by_python.txt")

print("File renamed successfully.")


'''