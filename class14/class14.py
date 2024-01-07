import datetime as dt

"""

print(datetime.datetime.now())

date = datetime.date.today()
print(date)
print(date.year)
print(date.month)d
print(date.day)


print(date.strftime("%d %b %B %Y %y %A %a"))

day = input("birthdayu:")
print(day)
birth = datetime.datetime.strptime(day, "%m/%d/%Y")
print(birth.date())


a = input("birthday:")
ne = dt.datetime.strptime(a, "%Y/%m/%d")
ne = ne.date()
now = dt.date.today()
diff = ne - now
print(diff)

t = dt.datetime.now()
print(t)
print(t.hour)
print(t.minute)
print(t.second)
"""

import math

math.fmod(x, y)
math.fabs(x)
math.floor(x)
math.ceil(x)
