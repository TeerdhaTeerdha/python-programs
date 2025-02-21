# write a program to find length of a number

num=int(input("Enter any number: "))
count=0
while num > 0:
    count+=1
    num=num//10
print(f'Length of the number is {count}')
