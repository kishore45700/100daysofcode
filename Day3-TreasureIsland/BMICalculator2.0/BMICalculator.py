#take the user's weight as an input
weight=input("Enter your weight in kg: \n")
#take the user's height as an input
height=input("Enter your height in m: \n")
#calculate and output the BMI
BMI=float(weight)/(float(height)**2)
result=int(BMI)

if BMI<18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif BMI>=18.5 and BMI<25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif BMI>=25 and BMI<30:
    print(f"Your BMI is {result}, you are slightly over weight.")
elif BMI>=30 and BMI<35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")