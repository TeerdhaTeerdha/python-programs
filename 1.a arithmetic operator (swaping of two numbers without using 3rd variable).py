# write a program to swap two numbers without using 3rd variable
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))


# Method-1 using third variable
num3=num1
num1=num2
num2=num3

print(num1,num2)

# Method-2 without using third variable

num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1,num2)

# Method-3 without using arithmetic operators
num1,num2=num2,num1
print(num1,num2)

