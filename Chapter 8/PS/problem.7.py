# Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word):
    n = []          # empty list : This list will store the final result
    for item in l:
        if not(item == word):
            n.append(item.strip(word))   # strip() does not remove a word. It removes the characters present in the argument from the beginning and end of the string.
    return n 
    
l = ["Alok", "Rohan", "Shubham", "an"]

print(rem(l, "an"))