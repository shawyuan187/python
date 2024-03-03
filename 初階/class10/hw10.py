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
"""
juices = ["蘋果汁", "柳橙汁", "葡萄汁"]
my_list = []

while True:
    print("目前已點的餐:" + str(my_list))
    print("1. 新增餐點")
    print("2. 移除餐點")
    print("3. 提交菜單")
    s = input("請輸入功能選項:")
    print("==========================")
    if s == "1":
        while True:
            for j in range(len(juices)):
                print(str(j + 1) + ". " + str(juices[j]))

            try:
                ans = int(input("請輸入餐點編號:"))
            except:
                print("請輸入數字編號")
            else:
                if ans > len(juices):
                    print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                else:
                    print("您點的商品是:" + str(juices[ans - 1]))
                    my_list.append(juices[ans - 1])
                    break
    elif s == "2":
        ans = input("請輸入想移除的餐點完整名稱:")
        while ans in my_list:
            my_list.remove(ans)
        print("移除完成")
    elif s == "3":
        print("您點的餐點為")
        for j in juices:
            if j in my_list:
                print(str(j) + ":" + str(my_list.count(j)))
        print("菜單已提交囉!")
        break
    else:
        print("查無此功能請重新輸入!")
    print("==========================")
    """
