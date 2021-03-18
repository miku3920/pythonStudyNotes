def defaultValue(num1=0, num2=0):
    print(num1, num2)


defaultValue()  # 0 0
defaultValue(12)  # 12 0
defaultValue(12, 34)  # 12 34
defaultValue(num1=12)  # 12 0
defaultValue(num2=34)  # 0 34
defaultValue(num1=12, num2=34)  # 12 34
defaultValue(num2=12, num1=34)  # 34 12
