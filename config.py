from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL")
