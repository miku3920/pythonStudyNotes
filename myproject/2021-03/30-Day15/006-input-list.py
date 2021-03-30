list1=[]
i=0
while True:
    try:
        x = int(input("輸入數字: "))
        list1.append(x)
        i+=1
    except:
        print("  輸入錯誤!!")

    if i>=3:
        break

print(list1)