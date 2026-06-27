f = open("file.txt", "r")     # "r" → read mode.
# file.txt  ─────► open() ─────► f (file object)
data = f.read()   # read()-Reads the entire contents of the file.Returns it as a string.
print(data)  # Prints the contents of the file.
f.close()