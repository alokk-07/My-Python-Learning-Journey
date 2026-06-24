def greet(name, ending):         # name, ending → parameters (inputs accepted by the function).
    print("Good Day, " + name)
    print(ending)                # print displays output only

greet("Alok",  "Thank You")
greet("Shreya", "Thanks")
greet("Rajat", "THANK YOU")

# ---------------------------------------------
def greet(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Done"           # return sends a value back to the place where the function was called.
                            # return returns the value so it can be stored and used later.
a = greet("Alok", "Thank You")
print(a)