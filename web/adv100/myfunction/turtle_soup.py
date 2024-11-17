import openai
import json
import random
import os
import sys


class TurtleSoupGame:
    def __init__(self, openai_client: openai):
        self.openai_client = openai_client
        self.games = {}
        self.questions = []

    def load_questions(self):
        try:
            os.chdir(sys.path[0])
            with open("turtle_soup.json", "r", encoding="utf-8") as f:
                self.questions = json.load(f)
        except Exception as e:
            self.questions = [
                {
                    "question": "一位女士每天早上都會去檢查家門口的郵箱，但郵箱裡從來沒有信。日復一日，她依然堅持這個習慣，從不間斷。某天，她終於在郵箱中發現了一封信。看完信後，她立刻決定搬離這個城市，甚至連夜離開，神情緊張而驚慌。",
                    "answer": "這位女士過去曾牽涉到一件敏感事件，並改名換姓遠走他鄉，希望徹底擺脫過去的陰影。這封信中揭露了她的真實身份，並暗示她的過去可能已被人發現。信的內容讓她意識到，無論她逃到哪裡，那段過去都始終在追隨著她。為了躲避未知的威脅，她不得不再次搬離。",
                    "solve": False,
                }
            ]

    def start_game(self, channel_id):
        if channel_id in self.games:
            return False, "這個頻道已經有一個遊戲了"
        self.load_questions()
        selected_question = random.choice(self.questions).copy()
        self.games[channel_id] = {
            "game_data": selected_question,
            "history": [],
        }
        return True, self.games[channel_id]["game_data"]["question"]

    def end_game(self, channel_id):
        if channel_id in self.games:
            self.games.pop(channel_id)
            return True
        return False

    async def process_answer(self, channel_id, user_input):
        if channel_id not in self.games:
            return None, "no game"
        game_data = self.games[channel_id]
        history = game_data.setdefault("history", [])
        history.append({"role": "user", "content": user_input})
        messages = (
            [
                {
                    "role": "system",
                    "content": f"""
你是一你是這個遊戲的主持人，你會回答我的問題。
請大家開始提問,輸入'結束遊戲'可結束遊戲
我的回應只會是[是]、[不是]或者[無可奉告]，不會回答其他內容
當玩家要求提示的時候，你可以提供'關鍵字'當作提示。
謎題:{game_data['question']}
解答:{game_data['answer']}""",
                }
            ]
            + history
        )
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.5,
            )
            answer = response.choices[0].message.content
            if answer == "恭喜答對!":
                game_data["game_data"]["solved"] = True
                self.games.pop(channel_id)
                return True, answer
            else:
                history.append({"role": "assistant", "content": answer})
                return False, answer
        except Exception as e:
            return None, f"eror: {str(e)}"

    def is_active_game(self, channel_id):
        return channel_id in self.games
