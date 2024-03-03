"""
food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
food_list["冰淇淋"] = 10
food_list["熱狗"] = 20
food_list["果汁"] = 25
items = food_list.items()
for key, value in items:
    if key == "果汁":
        print(key, str(value) + "杯")
    else:
        print(key, str(value) + "分")


food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
food_list["冰淇淋"] = 10
food_list["熱狗"] = 20
food_list["果汁"] = 25

w = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}

for key, value in food_list.items():
    if key in w:
        if value > w[key]:
            print(key + ":" + str(value - w[key]))

    else:
        print(key + ":" + str(value))



d = food_list
v = d.pop(0, "刪除資料失敗")
for key, value in food_list.items():
    if value == 0:
        food_list.pop(key, "error")
        print(key + "you eat it all")
    else:
        continue
        




gifts = {
    "小明": "樂高積木",
    "小花": "畫筆",
    "小強": "足球",
    "小美": "書",
    "小偉": "遙控車",
}
# 顯示一共收到了多少個禮物
print("一共收到了" + str(len(gifts)) + "個禮物")
for name, gift in gifts.items():
    print(name + "送了你一個" + gift)



food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
food_list["蛋糕"] = 0
food_list["三明治"] = 5
food_list["果汁"] = 8
food_list["薯條"] = 10
food_list["披薩"] = 1
food_list["冰淇淋"] = 3
food_list["熱狗"] = 0
d = []
for key, value in food_list.items():
    if value == 0:
        d.append(key)
for i in d:
    food_list.pop(i)
print(food_list)
print(d)
"""
