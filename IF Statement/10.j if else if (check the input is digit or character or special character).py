# write a program to input character and find
# character is alphabet
# character is digit
# character is special character

ch=input("Enter any character: ")
if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    print(f'{ch} is a alphabet')
elif (ch>='0' and ch<='9'):
    print(f'{ch} is a digit')
else:
    print(f'{ch} is a special character')
