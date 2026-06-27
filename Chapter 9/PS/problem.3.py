# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
#Place these files in a folder for a 13 – year old.


def generateTable(n):
    #first create string.
    table = ""

    for i in range(1, 11):
        #Keep adding lines
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        #Instead of calling write() 10 times, write the entire string in one go:
        f.write(table)

#Repeat for every number
for i in range(2, 21):
    generateTable(i)
