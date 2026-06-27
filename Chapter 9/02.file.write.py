st = "Hey Alok , You are amazing!"

f = open("myFile.txt", "w")   # "w"-- means Write Mode.

f.write(st)  # write()--Writes the contents of st into the file

f.close()