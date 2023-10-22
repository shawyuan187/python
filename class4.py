"""
password = input("請輸入密碼:")
if password == "1487":
    print("歡迎光臨")
elif password == "1234":
    print("hi ethan")
else:
    print("密碼錯誤")

score = input("type your score here:")
if int(score) >= 90:
    print("a")
elif int(score) >= 80 and int(score) <= 89:
    print("b")
elif int(score) >= 70 and int(score) <= 79:
    print("c")
elif int(score) >= 60 and int(score) <= 69:
    print("d")
else:
    print("e")

number = int(input("type a number here:"))
if number % 2 == 0:
    print("你打的數字是偶數")
else:
    print("你打的數字是奇數")

turtle.stamp()
turtle.penup()
import turtle

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()

turtle.stamp()
turtle.penup()
"""
import turtle

turtle.speed(10)
turtle.shape("circle")
for i in range(100):
    turtle.penup()
    turtle.forward(1 + i)
    turtle.right(30)
    turtle.stamp()
