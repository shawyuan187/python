import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo")
from langchain_core.messages import HumanMessage

print(model.invoke([HumanMessage(content="你好")]).content)
while True:
    ans = input("請輸入想跟AI說的話: ")
    print(
        model.invoke(
            [
                HumanMessage(
                    content="""
    你是一個負責開燈跟關燈負責開關車庫的門的管理員
    你只能根據使用者的回應來決定要回答'ON'或'OFF'或'close'或'open'
    
    回答的格式是'ON'或'OFF'或'close'或'open'
    on 代表開燈
    off 代表關燈
    close 代表關閉車庫
    open 代表開啟車庫

                """
                ),
                HumanMessage(content=ans),
            ]
        ).content
    )
