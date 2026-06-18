marks = {
    "Alok": 100,
    "shubham": 67,
    "Rohan": 38,
    "list": [100,67,38]
}

# dictioaries methods 
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Alok":99})
print(marks)



print(marks.get("Alok"))    
print(marks["Alok"])

print(marks.get("Alok2"))  # prints none
print(marks["Alok2"])    # returns an error