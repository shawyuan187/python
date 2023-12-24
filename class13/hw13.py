"""
執行結果:
1. 新增支出記錄
2. 查詢特定日期的支出總和
3. 輸出所有記錄的總和
4. 離開系統
請輸入功能編號:1
請輸入日期:2024-01-01
請輸入金額:100
1. 新增支出記錄
2. 查詢特定日期的支出總和
3. 輸出所有記錄的總和
4. 離開系統
請輸入功能編號:1
請輸入日期:2024-01-01
請輸入金額:200
1. 新增支出記錄
2. 查詢特定日期的支出總和
3. 輸出所有記錄的總和
4. 離開系統
請輸入功能編號:2
請輸入日期:2024-01-01
2024-01-01的支出總和為300
1. 新增支出記錄
2. 查詢特定日期的支出總和
3. 輸出所有記錄的總和
4. 離開系統
請輸入功能編號:3
所有記錄的總和為300


1. 新增支出記錄
2. 查詢特定日期的支出總和
3. 輸出所有記錄的總和
4. 離開系統
請輸入功能編號:4
"""
l = {}


def add():
    c = input("請輸入日期:")
    a = input("輸入該科目分數:")
    l[c] = a


def de():
    b = input("你要移除甚麼:")
    if b in l:
        l.pop(b)
        print("已移除" + b)
    else:
        print("發生極大的錯誤，你腦袋有問題!")


def done():
    print("已提交")
    if len(l) > 0:
        tot = sum([int(score) for score in l.values()])
        ave = tot / len(l)
        print("你的所有科目的平均是:" + ave)
    else:
        print("沒有科目成績可以顯示")


def el():
    print("錯誤，我操你居然看不懂文字!")


op = [add, de, done]

while True:
    print("目前的成績" + str(l))
    print("1,新增分")
    print("2,移除分")
    print("3,提交並且顯示成績")
    try:
        select = int(input("type what you want"))
    except:
        print("you suck")
    else:
        if select > len(op) or select < 1:
            print("you suck")

        elif select == len(op):
            done()
            break
        else:
            op[select - 1]()
