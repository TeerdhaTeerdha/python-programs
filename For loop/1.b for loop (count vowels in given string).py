# write a program to count vowels in given string
str1=input("Enter any string: ")
vc=0
for ch in str1:
    if ch in "aeiouAEIOU":
        vc+=1
print(f'Vowel Count {vc}')
