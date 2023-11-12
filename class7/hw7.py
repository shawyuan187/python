import random

ran = random.randrange(0, 101)
s = 1
b = 100
while True:
    num = int(input("type a number in " + str(s) + "~" + str(b) + "---->"))
    if num > ran:
        if num < b:
            b = num
            print("smaller")

    elif num < ran:
        if num > s:
            s = num
            print("big")

    elif num == ran:
        print("u are correct")
        break
