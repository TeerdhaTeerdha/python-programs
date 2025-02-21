# write a program to input string and count the alphabets, digits, and special characters
ac=0
dc=0
sc=0
str1=input("Enter the string: ")
for ch in str1:
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1
print(f'Total alphabets are:{ac}')
print(f'Total digits are: {dc}')
print(f'Total special characters are: {sc}')
