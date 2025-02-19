#write a program for random OTP number to login
import random
name=input("Enter Name:")
otp=random.randint(1000,9999)
print("This is your OTP number to login ----->",otp)
user=int(input("Enter OTP Number"))
print("Welcome") if otp==user else print("Invalid OTP Number")
