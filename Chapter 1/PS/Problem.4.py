# Write a Python program to print the contents of a directory using the os module. Search online for the function that does that.

import os
# specify the path of the directory you want to list
directory_path = '/'


# list the contents of the directory in the specified path
contents = os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)