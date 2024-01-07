'''from datetime import datetime


def standardize_date(input_date):
    input_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y/%m/%d"]
    output_format = "%Y-%m-%d"

    for format_str in input_formats:
        try:
            # 嘗試將輸入日期按照各種格式進行轉換
            date_obj = datetime.strptime(input_date, format_str)

            # 如果轉換成功，將日期轉換為標準格式並返回
            standardized_date = date_obj.strftime(output_format)
            return standardized_date
        except ValueError:
            pass  # 忽略轉換失敗的格式

    # 如果所有格式都無法轉換，則拋出例外或返回None，視需求而定
    raise ValueError("Invalid date format: {}".format(input_date))


# 測試函數
input_date = input("請輸入日期: ")
try:
    standardized_date = standardize_date(input_date)
    print("標準格式日期: {}".format(standardized_date))
except ValueError as e:
    print(e)


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
'''


def add_expense(date, amount):
    """添加新的支出"""
    if date not in expenses:
        expenses[date] = []
    expenses[date].append(amount)
    safe_file(date, amount)


def safe_file(date, amount):
    """將每一筆支出寫入檔案"""
    with open("memory.txt", "a") as file:
        file.write(f"{date},{amount}\n")


def query_expenses(date):
    """查詢特定日期的支出總和"""
    if date not in expenses:
        return 0

    return sum(expenses[date])


def total_expenses():
    """計算並返回所有記錄的總支出"""
    total = 0
    for value in expenses.values():
        total += sum(value)
    return total


expenses = {}

while True:
    print("1. 新增支出記錄")
    print("2. 查詢特定日期的支出總和")
    print("3. 輸出所有記錄的總和")
    print("4. 將每一筆料寫入memory.txt")
    print("5. 離開系統")
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
        with open("memory.txt", "r") as file:
            content = file.read()
            print("memory.txt 內容:")
            print(content)
    elif select == "5":
        break
    else:
        print("查無此功能請重新輸入")
