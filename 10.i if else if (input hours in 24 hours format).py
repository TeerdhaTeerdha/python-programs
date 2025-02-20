# write a program to input hours in 24 hours format
h=int(input("Enter hours in 24 hours format"))
if h<=12:
    print("Good morning")
elif h>12 and h<=17:
    print("Good Afternoon")
elif h>17 and h<=20:
    print("Good Evening")
else:
    print("Good night")
