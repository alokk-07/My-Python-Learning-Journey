# Write a program to find out whether a given post is talking about “Alok” or not.

post = input("Enter the post: ")

if("Alok".lower() in post.lower()):      
    #lower will convert any possibilities of alok , Alok , ALOK etc into lower case (alok)  and then search in the post
    print("This post is talking about Alok")

else:
    print("This post is not talking about Alok")
