# write a program to find input number is prime or not
num=int(input("Enter any number: "))
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not prime number')
