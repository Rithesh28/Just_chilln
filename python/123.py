w=int(input("Enter your weight in Kg:"))
h=float(input("Enter your height in meters:"))
bmi=w/(h*h)
print('BMI is:',bmi)
if bmi<18:
    print("underweight")
elif 18<=bmi<25:
    print("Normal")
else:
    print("Obesity")
