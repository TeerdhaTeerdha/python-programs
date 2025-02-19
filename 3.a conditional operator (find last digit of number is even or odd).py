# write a program to find last digit of number is even or odd
num=int(input("Enter integer value"))
l=num%10
r=l%2
res="Even" if r==0 else "Odd"
print("Last digit of", num,"is",res)
