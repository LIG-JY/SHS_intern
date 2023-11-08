from domain.telegram_bot import TelegramBot

if __name__ == '__main__':  
    bot = TelegramBot()
    msg = "안녕" ## 메세지 내용 put
    print(bot.getUpdates()) # 내 ID 확인하는 방법
    bot.sendMessage(msg)