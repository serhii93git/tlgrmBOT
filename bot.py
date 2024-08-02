import os
from dotenv import load_dotenv

#  load and get the environment variables from the .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
print(BOT_TOKEN)