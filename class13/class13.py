"""
l = {}


def add():
    c = input("請輸入科目:")
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


ans = eval("1+2")
print(ans)

ans = eval("a+b")
print(ans)


a = input("type number:")

print(eval(a))



import os

fp = "C:/Users/R2/Desktop/all foders/python/class12/class12.py"
#class12/class12.py
if os.path.isfile(fp):
    print("yes")
else:
    print("you suck")

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

fn = "example.txt"
m = "w"
mf = open(fn, m)
mf.write("hi\n")
mf.write("how old are you?")
mf.close()
"""
p = "course/class13/example.txt"
f = open(p, "r")
t = f.read()
print(t)
f.close()


p = "course/class13/example.txt"
f = open(p, "r")
l1 = f.readline()
l2 = f.readline()
print(t)
f.close()


p = "course/class13/example.txt"
f = open(p, "r")
l = f.readlines()
for line in l:
    print(l)
f.close()
