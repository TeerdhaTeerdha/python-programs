# write a program to calculate the electricity bill
''' unit                   price
  first 100 units         no charge
  next 100 units          rs.5 per unit
  after 200 units         rs.10 per unit
  (for example if input unit is 350 than total bill amount is rs.2000)
'''

units=int(input("Enter the units: "))
if units <=100:
    amount=0
elif units > 100 and units <=200:
    amount=(units-100)*5
else:
    amount=0+500+(units-200)*10
print(f'your total electricity bill is {amount}')
