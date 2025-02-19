# write a program to find largest number
num1=int(input("Enter the first value"))
num2=int(input("Enter the second value"))
num3=int(input("Enter the third value"))
if(num1>=num2) and (num1>=num3):
    print(f'{num1}')
elif (num2>=num1) and (num2>=num3):
    print(f'{num2}')
else:
    print(f'{num3}')
