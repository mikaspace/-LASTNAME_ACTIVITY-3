#promp user to enter the purchase amount
amount = float(input('Enter Purchase Amount: '))

#assign variable for the sales tax
tax = 0.06

#compute amount with tax
comp = amount * tax
comp = "{:.2f}".format(comp)

print('Purchase Amount: ', amount)
print('Sales tax is',comp)