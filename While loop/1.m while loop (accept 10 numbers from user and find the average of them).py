# Accept the 10 numbers from user and find out the average of those numbers
s=0
i=1
while i <= 10:
    num=int(input("Enter the number: "))
    s=s+num
    i=i+1
a=s/10
print(f'Average of 10 numbers is {a:.2f}')
