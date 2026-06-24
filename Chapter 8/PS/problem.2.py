# Write a python program using function to convert Celsius to Fahrenheit.

# Formula: c/5 = (f-32)/9


'''f = int(input("Enter temperature in F: "))
c = 5*(f-32)/9

print(c)'''      #Output- Enter temperature in F: 34 
                 # 1.1111111111111112

# ------------------------------------------------------
def f_to_c(f):      # (f) :Parameter.Receives the Fahrenheit value when the function is called.
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c,2)}°C")      # Rounds the number to 2 decimal places.