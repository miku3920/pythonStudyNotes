import time

def doSomething():
    print("每秒印一次這段文字")

while True:
    doSomething()
    time.sleep(1)