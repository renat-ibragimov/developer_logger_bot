import requests

import config


class TGLoggerBot:
    """This bot will rcv msg and send it to developer.
    Config file is just example.
    You can use Your own BOT_TOKEN and CHAT_ID.
    Pls read README"""
    def __init__(self, message: str):
        self.message = message
        self.send_msg()

    def send_msg(self):
        requests.post(
            f"https://api.telegram.org/bot{config.LOGGER_BOT_TOKEN}/"
            f"sendMessage",
            data={"chat_id": config.MY_TG_ID,
                  "text": self.message})
