"""It's just example config file"""
import os

from dotenv import load_dotenv

load_dotenv()

LOGGER_BOT_TOKEN = os.getenv('LOGGER_BOT_TOKEN')
MY_TG_ID = os.getenv('MY_TG_ID')
