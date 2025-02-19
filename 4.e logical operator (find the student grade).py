# write a program to input name, 2 subject marks and calculate total, average, and grade
# A ---> >=80
# B ---> >=60 and <=80
# C ---> >=50 and <=60
# D ---> <50

name=input("Enter name of the subject: ")
s1=int(input("Enter the subject1 Marks: "))
s2=int(input("Enter the subject2 Marks: "))
total=s1+s2
average=total/2
grade="A" if average>=80 else "B" if average>=60 and average<=80 else "C" if average>=50 and average<60 else "D"
print("Name: ",name)
print("Subject1 Marks: ",s1)
print("Subject2 Marks: ",s2)
print("Total Marks: ",total)
print("Average Marks: ",average)
print(f'Grade= ',grade)
