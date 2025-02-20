# write a program for course fee details
''' menu --> python , java , .net , exit '''

opt=int(input("Enter Your Option: "))
match(opt):
    case 1:
        print("Python Course Fee : 5000")
    case 2:
        print("Java Course Fee : 2000")
    case 3:
        print(".Net Course Fee : 1000")
    case 4:
        print("Exit...")
    case _:
        print("Wrong input try again...")
