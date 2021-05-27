from dotenv import load_dotenv, find_dotenv
import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
