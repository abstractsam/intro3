#calculating ones bmi

#weight = w
#height = h

weight = float(input("Enter w in kgs"))
height = float(input("Enter h in meters"))


BMI = weight/(height*height)

print("Your bmi is", BMI)
if BMI <= 18:
    print("You are underweight")
elif 18.1 <= BMI <= 29:
    print("You are normalweight")
elif 29.1 <= BMI <= 34:
     print("You are overweight")
else:
     print("You are obese")







