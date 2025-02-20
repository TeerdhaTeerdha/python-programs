# Write a program to input rollno,name,course,fee and display/output
rollno=int(input("Enter the Rollno "))
name=input("Enter the name ")
course=input("Enter the course ")
fee=float(input("Enter the fee "))


print('''Rollno\t%d
Name\t%s
Course\t%s
Fee\t%.2f'''%(rollno,name,course,fee))
