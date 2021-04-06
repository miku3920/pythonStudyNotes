import aiml

kernel = aiml.Kernel()
kernel.learn("AIML-all.xml")
while True:
    str1 = input("Enter your message: ")
    res = kernel.respond(str1)
    print(res)
