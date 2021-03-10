membershipCard = True
invoiceSalesTax = True
price = 100
discount = 0.9
tax = 0.05
calculatedPrice = price

if membershipCard:
    calculatedPrice = discount * price
if invoiceSalesTax:
    calculatedPrice += tax * calculatedPrice

print(calculatedPrice)