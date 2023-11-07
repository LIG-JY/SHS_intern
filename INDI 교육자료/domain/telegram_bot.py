import telepot
from datetime import datetime

class TelegramBot():
    def __init__(self):
        self.my_id = "5684099702"  # id
        my_token = "6836280679:AAHqTH-tFBhilDlodg69mKraZHhEh2gC6dU"
        self.bot = telepot.Bot(token=my_token)

    def sendMessage(self, message):
        self.bot.sendMessage(self.my_id, message, parse_mode="Markdown")

    def send_message_with_time(self, message):
         # 현재 시간을 가져옵니다.
         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

         # 메시지에 현재 시간을 포함시킵니다.
         message_with_time = f"[{current_time}] {message}"

         # 메시지를 보냅니다.
         self.bot.sendMessage(self.my_id, message_with_time, parse_mode="Markdown")

    def getUpdates(self):
        return self.bot.getUpdates()
