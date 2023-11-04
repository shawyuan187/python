"""
import turtle

turtle.speed(10000000)
turtle.penup()
for i in range(10):
    turtle.forward(80)
    turtle.stamp()
    turtle.home()
    turtle.right(45 * i)
turtle.done()
----------------------------------------
import turtle

import time  # 匯入time模組

turtle.speed(10)
for i in range(60):
    turtle.clear()
    turtle.right(6 * i)
    turtle.forward(100)
    turtle.home()

    time.sleep(1)


輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18

請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
 * 
*** 
*****
 * 
 * 
 * 


n = int(input("請輸入正整數: "))

for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)

size = int(input("請輸入要印出的箭頭大小: "))


for i in range(1, size + 1):
    stars = "*" * (i * 2 - 1)
    print(stars.center(size * 2 - 1))


for i in range(size):
    print("*".center(size * 2 - 1))
"""
