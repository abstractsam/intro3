from studentreg_table import Student

students = Student.select()
#Use a forloop to display

for student in students:
    print(student.name,student.age,student.gender,student.studentcode,student.phonenumber)
