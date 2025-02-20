# write a program for banking application
accno=input("Enter the Account number: ")
balance=float(input("Enter the balance amount: "))
totalamt=float(input("Enter the total amount to withdraw: "))
if totalamt >= 5000:
    print("With draw the amount")
if totalamt < balance:
    balance=balance-totalamt
print("Account number:", accno)
print("Total Balance:",balance)
