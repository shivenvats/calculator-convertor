# CALCULATOR FOR VITYARTHI PROJECT
from speed_01 import s
from temperature import temprature
from bmi import bmi
from calculator import cal

def main_menu():
    print("Choose Want you Want to do : ")
    print("1)CALCULATE\n2)CONVERTOR\n3)EXIT")
    try:
        choice = int(input("Enter your Choice : "))
    except ValueError:
        print("Invalid Response")
        main_menu()
        return
    if choice < 1 or choice > 3 :
        print("Invalid Response")
        main_menu()
        return

    match choice :
        case 1 :
            cal()
            main_menu() 

        case 2 :
            print("You have Chose Convertor : ")
            print("a)BMI\nb)Temperature\nc)Speed")
            select_converter = input("Enter your Conversion : ")
            match select_converter :
                case "a" :
                    bmi()
                case "b" :
                    temprature()
                case "c" :
                    s()
                case _ :
                    print("Invalid Response")
            main_menu()


        case 3 :
            print("Have a Nice Day!!!")

print("=============================")
print(" Welcome to the Calculator")
print("=============================")

main_menu()
# END OF CODE
