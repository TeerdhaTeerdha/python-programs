# Write a program to display factorials of numbers from 1-5

for num in range(1,6):  
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f'{num} --> {fact}')
