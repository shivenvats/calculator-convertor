def bmi():
    print("Calculate Your BMI ")
    A = int(input("Enter your Age : "))
    H = float(input("Enter your Height (in metres, e.g. 1.70) : "))
    W = float(input("Enter your Weight (in kg) : "))
    BMI = W/H**2
    if BMI < 18.5:
        print(f"Your BMI is : {BMI:.2f} , Underweight")
    elif BMI < 25:
        print(f"Your BMI is : {BMI:.2f} , Healthy Weight")
    elif BMI < 30:
        print(f"Your BMI is : {BMI:.2f} , Overweight")
    elif BMI < 35:
        print(f"Your BMI is : {BMI:.2f} , Obesity (Class 1)")
    elif BMI < 40:
        print(f"Your BMI is : {BMI:.2f} , Obesity (Class 2)")
    else:
        print(f"Your BMI is : {BMI:.2f} , Obesity (Class 3)")