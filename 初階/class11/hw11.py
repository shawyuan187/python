l = {}

while True:
    print("目前的成績" + str(l))
    print("1,新增分")
    print("2,移除分")
    print("3,提交並且顯示成績")
    option = input("歡迎使用，請輸入你的選項(1~3):")

    if option == "1":
        c = input("請輸入科目:")
        a = input("輸入該科目分數:")
        l[c] = a
    elif option == "2":
        b = input("你要移除甚麼:")
        if b in l:
            l.pop(b)
            print("已移除" + b)
        else:
            print("發生極大的錯誤，你腦袋有問題!")
    elif option == "3":
        print("已提交")
        if len(l) > 0:
            tot = sum([int(score) for score in l.values()])
            ave = tot / len(l)
            print("你的所有科目的平均是:" + ave)
        else:
            print("沒有科目成績可以顯示")
        break
    else:
        print("錯誤，我操你居然看不懂文字!")
        continue
