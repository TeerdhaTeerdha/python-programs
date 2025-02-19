# write a program to input name, 2 subject marks and calculate total, average, and result
name=input("Enter name of the subject: ")
s1=int(input("Enter the subject1 Marks: "))
s2=int(input("Enter the subject2 Marks: "))
total=s1+s2
average=total/2
result="Fail" if s1>40 or s2<40 else "Pass"
print("Name: ",name)
print("Subject1 Marks: ",s1)
print("Subject2 Marks: ",s2)
print("Total Marks: ",total)
print("Average Marks: ",average)
print(f'Result= ',result)
