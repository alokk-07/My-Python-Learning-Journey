def greet(name, ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)

greet("Alok", "Thanks")      # Since a value for ending was provided(Thanks), the default value is ignored.
greet("Rohan")       # No value is passed for ending, so Python uses the default: Thank You