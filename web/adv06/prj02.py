def greet():  # 定義函數
    print("hello")  # 印出訊息


def welcome(func):  # 定義函數
    print("welcome")  # 印出訊息
    func()  # 呼叫函數


welcome(greet)  # 呼叫函數


def decorator_with_args(greeting):  # 定義函數
    def decorator(func):  # 定義函數
        def wrapper(*args, **kwargs):  # 定義函數
            print(f"{greeting}!before")  # 印出訊息
            func(*args, **kwargs)  # 呼叫函數
            print(f"{greeting}!after")  # 印出訊息

        return wrapper  # 回傳函數

    return decorator  # 回傳裝飾器


@decorator_with_args("welcome")  # 呼叫裝飾器
def greet(name=None):  # 定義函數
    if name:  # 判斷參數
        print(f"hello, {name}!")
    else:
        print("hello!")


greet()  # 呼叫函數
greet("alice")
