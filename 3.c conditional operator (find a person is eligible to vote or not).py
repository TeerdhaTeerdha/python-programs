# write a program to find a person is eligible to vote or not
name=input("Enter Name")
age=int(input("Enter age"))
print(name,"you are eligible to vote") if age>=18 else print(name,"you are not eligible to vote")
