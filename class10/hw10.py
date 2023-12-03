l = []
one = "no1"
two = "no2"
three = "no3"
while True:
    print("no1,no2,no3")
    print("目前以點餐點" + str(l))
    print("1,新增物品")
    print("2,移除商品")
    print("3,提交")
    option = input("歡迎使用餐點，請打你要的選項:")
    if option == "1":
        a = input("type 1 or 2 or 3:")
        if a == "1":
            l.append(one)
        elif a == "2":
            l.append(two)
        elif a == "3":
            l.append(three)
    elif option == "2":
        b = input("你要移除甚麼:")
        if b in l:
            if b == "no1":
                while "no1" in l:
                    l.remove("no1")
            elif b == "no2":
                while "no1" in l:
                    l.remove("no1")
            elif b == "no3":
                while "no1" in l:
                    l.remove("no1")
            print("已移除")
        else:
            print("error")
    elif option == "3":
        print("已提交")
        print("no1=" + str(l.count("no1")))
        print("no2=" + str(l.count("no2")))
        print("no3=" + str(l.count("no3")))
        break
    else:
        print("操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操操")
        continue
