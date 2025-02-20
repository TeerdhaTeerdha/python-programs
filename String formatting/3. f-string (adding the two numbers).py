# write a program for adding two numbers using f-string
n1=int(input("Enter n1 value: "))
n2=int(input("Enter n2 value: "))
n3=n1+n2
print("sum of %d and %d is %d"%(n1,n2,n3))
print("sum of {} and {} is {}".format(n1,n2,n3))
print(f'sum of {n1} and {n2} is {n3}')
print(f'sum of {n1:d} and {n2:d} is {n3:d}')
print(f'sum of {n1:o} and {n2:o} is {n3:o}')
print(f'sum of {n1:x} and {n2:x} is {n3:x}')
print(f'sum of {n1:b} and {n2:b} is {n3:b}')
