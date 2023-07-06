from database import User

try:
    jina = input("Enter name\n")
    arafa = input("Enter Email\n")
    siri = input("Enter Password\n")


    User.create(name = jina,email = arafa,password = siri)
    print("User created successfully")

except:
    print("Failed to create user")







