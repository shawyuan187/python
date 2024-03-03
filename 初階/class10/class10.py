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
    elif option == "4":
        e = input("what do you want to search:")
        print(order_l.count(e))
    elif option == "5":
        order_l.pop()
    elif option == "6":
        f = int(input("which place you want to remove:"))
        order_l.pop(f)
    elif option == "7":
        order_l.sort()
    elif option == "8":
        order_l.sort(reverse=True)
    elif option == "9":
        order_l.reverse()
    elif option == "10":
        g = input("what do u want to search")
        print(l.indext(g))
    elif option == "11":
        print("thank you to use ordermachine")
        break

    else:
        print("type a number in 1-11")
        continue
    print("now orderlist is" + str(order_l))
"""
l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))

l.sort(reverse=True)

"""
