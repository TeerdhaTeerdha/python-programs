# write a orogram to find input number is (+ve) or (-ve) or zero
num=int(input("Enter any number"))
if num > 0:
    print(f'{num} is a positive number')
elif num < 0:
    print(f'{num} is a negative number')
else:
    print(f'{num} is zero')
