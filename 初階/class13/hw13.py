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


def add_expense(date, amount):
    """添加新的支出"""
    if date not in expenses:
        expenses[date] = []
    expenses[date].append(amount)
    # expenses["2024-1-7"].append(120)
    # [200].append(120)
    # [200,120]


def query_expenses(date):
    """查詢特定日期的支出總和"""
    if date not in expenses:
        return 0

    return sum(expenses[date])  # sum([200, 120])


def total_expenses():
    """計算並返回所有記錄的總支出"""
    """
    {
    "2023-1-5":[180, 30],
    "2023-1-7":[200, 120]
    }
    """
    total = 0
    for value in expenses.values():
        total += sum(value)
    return total


expenses = {}

while True:
    print("1. 新增支出記錄")
    print("2. 查詢特定日期的支出總和")
    print("3. 輸出所有記錄的總和")
    print("4. 離開系統")
    select = input("請輸入功能編號:")
    if select == "1":
        date = input("請輸入日期:")
        amount = int(input("請輸入金額:"))
        add_expense(date, amount)
    elif select == "2":
        date = input("請輸入日期:")
        print(f"{date}的支出總和為{query_expenses(date)}")
    elif select == "3":
        print(f"所有記錄的總和為{total_expenses()}")
    elif select == "4":
        break
    else:
        print("查無此功能請重新輸入")
