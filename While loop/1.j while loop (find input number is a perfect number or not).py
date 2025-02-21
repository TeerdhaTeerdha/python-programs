# write a program to find input number is a perfect number or not
# perfect number, a positive integer that is equal to the sun of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1,2 and 3
# other perfect numbers are 28, 496, and 8,128

num=int(input("Enter any number: "))
s=0
i=1
while i<num:
    if num%i==0:
        s+=i
    i+=1
if s==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')
