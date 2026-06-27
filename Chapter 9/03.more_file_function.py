'''This code demonstrates three different ways to read data from a file.'''

f = open("file.txt")

'''Method 1: readlines()'''

# lines = f.readlines()
# print(lines, type(lines))
 #----------------------------------------
'''Method 2: readlines()'''

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))
# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))

 #-----------------------------------------
'''Method 3: while Loop + readline()'''

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
    
f.close()