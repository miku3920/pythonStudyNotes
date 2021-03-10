def memberCard(price, membershipCard, invoiceSalesTax):
    discount = 0.9
    tax = 0.05
    calculatedPrice = price

    if membershipCard:
        calculatedPrice = discount * price
    if invoiceSalesTax:
        calculatedPrice += tax * calculatedPrice

    return calculatedPrice


print(memberCard(100, True, True))
