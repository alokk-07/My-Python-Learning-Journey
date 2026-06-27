''' 
a = "a very long string with emails"

emails = []
3 seconds

'''

f = open("file.txt", "r")     # "r" → read mode.
# file.txt  ─────► open() ─────► f (file object)
data = f.read()   # read()-Reads the entire contents of the file.Returns it as a string.
print(data)  # Prints the contents of the file.
f.close()
# Closes the file after you're done using it.
#Why? Frees system resources.Ensures all operations on the file are completed.It's considered good programming practice.
