"""import random


print(random.randint(1, 3))
print(random.randint(0, 10))

print(random.randrange(1, 3))
print(random.randrange(0, 10, 2))


import random

ran = random.randrange(0, 101)
while True:
    num = int(input("type number:"))
    if num > ran:
        print("small")
    elif num < ran:
        print("big")
    elif num == ran:
        print("u are correct")
        break


l = [1, 2, 3]
print(l)

l = [1, 2, 3, "hello", "world"]
print(l)

l = [1, 2, 3, "hello", "world", [4, 5, 6]]
print(l)


l = ["a", "b", "c"]
print(l[0])
print(l[1])
print(l[2])

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(l)
print(l[0])
print(l[2])
print(l[-1])
print(l[-3])
print(l[0:3])
print(l[0:6])
print(l[0:10:2])
print(l[::2])
print(len(l))
for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)



juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "可樂", "系統關閉"]  # 可以直接加上註解
while True:
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + juices_list[i])  # 選擇商品
    try:
        ans = int(input("請輸入編號:"))  # 看是不是數字
    except:
        print("輸入錯誤查無此果汁，請重新輸入")
        continue
    if ans == len(juices_list):
        print("~~系統關閉~~")
        break
    elif ans > len(juices_list) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print("您點的商品是" + juices_list[ans - 1])  # 商品選擇
"""
