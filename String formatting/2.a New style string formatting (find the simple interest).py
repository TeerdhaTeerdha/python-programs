# Write a program to find simple interest

amt=float(input("Enter Amount "))
rate=float(input("Enter Rate "))
time=int(input("Enter Time "))

si=amt*rate*time/100

print('''Simple Interest with
Amount={:.2f}
Rate={:.2f}
Time={:d} is {:.2f}'''.format(amt,rate,time,si))
