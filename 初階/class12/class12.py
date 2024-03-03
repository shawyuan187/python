"""
def hello():
    print("hello")


hello()



def hello(name):
    print("hello " + str(name))


hello("you suck")



def my_min(a, b):
    if a < b:
        return a
    else:
        return b


x = my_min(1, 2)
print("my_min" + str(x))



def fun (a,b):
     (a,b)
fun(1,2)
print(a)#a 沒在外面


length =5
area=3.14*10**2

def cal():
    global area#gobal is 告訴python接下來的area是全域變數
    area=length**2
cal()
print('it is',area)

import random

l = []


def b():
    random.randint(1, 6)
    n = input("time:")
    for i in range(int(n)):
        a = random.randint(1, 6)
        l.append(a)


b()
print(l)



"""


def fun(a, b, c=0, d=0):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)


fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

fun(1, 2, d=4)
