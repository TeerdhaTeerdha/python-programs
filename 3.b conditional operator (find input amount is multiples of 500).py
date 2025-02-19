# write a program to find input amount is multiples of 500
amt=int(input("please enter amount in multiple of 500: "))
print("Allow to withdraw") if amt%500==0 else print("Not allowed to withdraw")
