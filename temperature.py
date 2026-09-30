def temprature():
    print("Temperature Conversion ")
    celsius = float(input("Enter Temperture in celsius : "))
    k = celsius + 273.15
    f = celsius * 1.80 + 32.00
    print(f"kelvin = {k}k\nFarenheit = {f}F")
    print()