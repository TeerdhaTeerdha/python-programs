# write a program to find input number is amstrong number or not

num=int(input("Enter ant three digits value: "))
l=len(str(num))
num1=num

s=0
while num > 0:
    d=num%10
    s+=(d**l)
    num=num//10
if s==num1:
    print(f'{num1} is a amstrong number')
else:
    print(f'{num1} is not a amstrong number')
    
