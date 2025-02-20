# write a program for adding two numbers by using new style string formatting
n1=int(input("Enter the n1 value: "))
n2=int(input("Enter the n2 value: "))
n3=n1+n2
print("sum of {} and {} is {}".format(n1,n2,n3))
print("sum of {:d} and {:d} is {:d}".format(n1,n2,n3))
print("sum of {:o} and {:o} is {:o}".format(n1,n2,n3))
print("sum of {:x} and {:x} is {:x}".format(n1,n2,n3))
print("sum of {:b} and {:b} is {:b}".format(n1,n2,n3))
