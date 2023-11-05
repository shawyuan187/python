"""
s = int(input("money:"))
t = s
while s != 0:
    s = int(input("money:"))
    t += s
    print(t)

import time

t = input("time:")
for i in range(int(t), 1, -1):
    print(i)
    time.sleep(1)
else:
    print("bruh")


while True:
    num = input("choose thing:")
    if num == "1":
        print("你選擇蘋果汁")
    elif num == "2":
        print("你選擇柳橙汁")
    elif num == "3":
        print("你選擇葡萄汁")
    elif num == "4":
        print("關機")
        break
    else:
        print("error")
"""
t = input("要跳繩的次數:")
for i in range(1, int(t) + 1):
    if i % 10 == 0:
        print("休息一下")
        continue

    print(str(i))
