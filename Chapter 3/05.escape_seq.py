# escape sequences are special characters that are used to represent certain characters or actions in a string. They are denoted by a backslash (\) followed by a specific character.

a = " Alok is a good boy \n but not good in communication" 
# prints the string with a newline character
print(a)

a = " Alok is a good boy \t but not good in communication"
# prints the string with a tab character
print(a)

a = " Alok is a good boy \b but not good in communication"
# prints the string with a backspace character, which removes the previous character
print(a)        

a = " Alok is a good boy \r but not good in communication"
# prints the string with a carriage return character, which moves the cursor to the beginning of the line
print(a)    

a = " Alok is a good boy \ but not good in communication"
# prints the string with a backslash character, which is used to escape the next character
print(a)

