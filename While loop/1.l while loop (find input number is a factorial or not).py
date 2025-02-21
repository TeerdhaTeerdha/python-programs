# write a program to find input number is a factorial or not

num=int(input("Enter any number: "))
fact=1
i=1
while i <= num:
    fact=fact*i
    i+=1
print(f'{fact} is a factorial number')

