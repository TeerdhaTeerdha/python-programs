# write a program to find input number is a palindrome or not
num=int(input("Enter the number: "))
num1=num
rev=0
while num > 0:
    d=num%10
    rev=(rev*10)+d
    num=num//10
if rev==num1:
    print(f'{num1} is a palindrome number')
else:
    print(f'{num1} is a not palindrome number')
