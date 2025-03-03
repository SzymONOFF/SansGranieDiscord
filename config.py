import os
from dotenv import load_dotenv

load_dotenv()  # Wczytuje zmienne z .env

TOKEN = os.getenv("DISCORD_TOKEN")
