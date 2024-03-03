"""
weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
while True:
    c = int(input("what day will you want to change?  type 1-7 :"))
    w = input("what is it?:")
    if c == 1:
        weather[0] = w
        print(weather)
    elif c == 2:
        weather[1] = w
        print(weather)
    elif c == 3:
        weather[2] = w
        print(weather)
    elif c == 4:
        weather[3] = w
        print(weather)
    elif c == 5:
        weather[4] = w
        print(weather)
    elif c == 6:
        weather[5] = w
        print(weather)
    elif c == 7:
        weather[6] = w
        print(weather)
    else:
        print("type again")

weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
print(weather)
while True:
    try:
        ans = int(input("what day will you want to change?  type 1-7 :"))
    except:
        print("error")
        continue
    if ans > len(weather) or ans < 1:
        print("nothing type again")
    else:
        print("you are going to change " + str(ans))
        print("the old weather is " + weather[ans - 1])
        new_weather = input("type a new weather")
        weather[ans - 1] = new_weather
        print("the new weather is" + weather[ans - 1])
        print(weather)
        break
"""
l = ["a", "b", "c"]
a = l.copy()
a[0] = 1
print(a)
"""
a = ["apple", "banana"]
b = ["milk", "bread"]
print(a + b)
 
[1,2]*2

a = min(["火龍果", "哈密瓜", "百香果", "橘子", "蘋果", "香蕉", "梨", "李", "桃"])
b = max(["火龍果", "哈密瓜", "百香果", "橘子", "蘋果", "香蕉", "梨", "李", "桃"])
print(b)
print(a)

a = list("abc")
b = list([4, 5, 6])
c = list(range(3))
print(a)
print(b)
print(c)
"""
