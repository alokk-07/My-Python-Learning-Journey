a = int(input("Enter your age: "))

#condition.1
if(a>=18):      
    print("You are above the age of consent")
    print("Good for you")

#condition.2
elif(a<0):
    print("You are entering an invalid negative age")

#condition.3
elif(a==0):
    print("You are entering 0 which is not a valid age")

#otherwise
else:
    print("you are below the age of cosent")

 

print("End of Program")
