# write a program for calculator application
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
opr=input("Enter Operator (+,-,*,/) :")
match(opr):
    case '+':
        print(f'sum of {n1} and {n2} is {n1+n2}')
    case '-':
        print(f'difference of {n1} and {n2} is {n1-n2}')
    case '*':
        print(f'product of {n1} and {n2} is {n1*n2}')
    case '/':
        print(f'division of {n1} and {n2} is {n1/n2}')
    case _:
        print("invalid operator and try again...")
