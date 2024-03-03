"""
1,2,3".split(",")
"2020/1".split("/")  # cut


img = ["1", "2", "3"]
"-".join(img)  # 把他家進逗號的位置

img = "2023/10/20".split("/")
a = "-".join(img)
print(a)
l=[1,2,3]
l.append(4)
print(l)

l=['a,'b','c','d']
l.remove('a')
print(l)

l=[1,2,3]
l.insert(0,'A')
print(l)
"""
import random

order_l = []
while True:
    print("welcome to use 點餐機")
    print("1,add new thing in list ")
    print("2,remove things in list")
    print("3,add things in 特定位置")
    print("4,count how many things in list")
    print("5,cancel last things in list")
    print("6, cancel thing in 特定位置")
    print("7,list them in small to big")
    print("8,list them in big to small")
    print("9,反轉短餐清單順序")
    print("10,search where is the food in list")
    print("11,exit")
    option = input("welcome to use order machine type what you want(number)")
    if option == "1":
        a = input("type thing name")
        order_l.append(a)
    elif option == "2":
        b = input("what do you want to remove?:")
        if b in order_l:
            order_l.remove(b)
            print("you remove it")
        else:
            print("error")
    elif option == "3":
        c = int(input("which place will this new thing put:"))
        d = input("what is it:")
        order_l.insert(c, d)
    elif option == "11":
        print("thank you to use ordermachine")
        break

    else:
        print("type a number in 1-11")
        continue
    print("now orderlist is" + str(order_l))
