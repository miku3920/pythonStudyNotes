def printOnSale():
    firstProductPrice = 150  # 元
    secondProductPrice = 200  # 元

    # 打折
    if firstProductPrice > 100 and secondProductPrice > 100:
        firstProductPrice *= 0.8
        secondProductPrice *= 0.8
    elif firstProductPrice > 100:
        firstProductPrice *= 0.9
    elif secondProductPrice > 100:
        secondProductPrice *= 0.95

    totalPrice = firstProductPrice + secondProductPrice
    print(totalPrice)

    # 這是爛程式，這樣寫會改不動
    # 應將商品改成物件，並且使用「是否要打折」的函式

printOnSale()