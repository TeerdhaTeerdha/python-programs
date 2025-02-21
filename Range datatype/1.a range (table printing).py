# write a program to generate math table for given input
num=int(input("Enter a number: "))
for i in range(1,11):
    p=num*i
    print(f'{num}*{i}={p}')
