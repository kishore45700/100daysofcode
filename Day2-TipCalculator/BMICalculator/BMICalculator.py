#take the user's weight as an input
weight=input("Enter your weight in kg: \n")
#take the user's height as an input
height=input("Enter your height in m: \n")
#calculate and output the BMI
BMI=float(weight)/(float(height)**2)
result=int(BMI)
print("Your BMI is "+str(result))