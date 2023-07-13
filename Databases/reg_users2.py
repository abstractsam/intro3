from studentreg_table import Student
try:
    jina = input("Enter Name\n")
    miaka = input("Enter Age\n")
    jinsia = input("Enter Gender\n")
    siri = input("Enter studentcode\n")
    nambariyasimu = input("Enter phonenumber\n")


    Student.create(name = jina,age = miaka,studentcode = siri,gender = jinsia,phonenumber = nambariyasimu)
    print("User created successfully")

except:
    print("Failed to create user")
