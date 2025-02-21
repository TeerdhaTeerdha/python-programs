# write a program to find input number is a prime number or not

num=int(input("Enter any number: "))
c=0
i=1
while i <= num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
