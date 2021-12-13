weight=int(input("please enter your weight in kilograms:"))
height=float(input("please enter your height in meters:"))
x=(weight)
y=(height)
bmi=((x)/(y*y))
if bmi<18.5:
    print("Underweight")
    print (bmi)
    print(height)
elif 18.5<= bmi <= 25:
    print("Normal")
    print(bmi)
    print(height)
elif 25<= bmi <= 35:
    print("Overweight")
    print(bmi)
    print(height)
elif bmi<=35:
    print("obese")
    print(x)
    print(height)