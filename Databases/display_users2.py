from database import User

users = User.select()
#Use a forloop to display

for student in users:
    print(student.name,student.age,student.gender,student.studentcode,student.phonenumber)
