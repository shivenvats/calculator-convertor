def cal():
    print("You Have Chose to Calculate. ")

    print("What Operation do you want to Operate : ")

    print("a) '+'\nb) '-'\nc)'*'\nd)'/' ")

    O = input("Enter your Operator : ")
    match O :
        case "a" : 
            print("You have selected ADDITION ")
        case "b" :
            print("You have selected SUBSTRACTION ")
        case "c" :
            print("You have selected MULTIPLICATION ")
        case "d" :
            print("You have selected DIVISION ")
        case _ :
            print("Invalid Operator ")
            return

    x = float(input("Enter the value of x : "))
    y = float(input('Enter the value of y : '))

    if O == "a" :
        print(" x + y = ",x+y)
        
    if O == "b" :
        print(" x - y = ",x-y)
        
    if O == "c" :
        print(" x * y = ",x*y)
        
    if O == "d" :
        if y == 0 :
            print("Cannot divide by zero ")
        else :
            print(" x / y = ",x/y)