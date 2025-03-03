import discord
import os
from discord.ext import commands
from config import TOKEN
import logging

# Konfiguracja logowania błędów do pliku
logging.basicConfig(level=logging.INFO, filename="bot.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Ustawienie uprawnień bota (wymagane do poprawnego działania)
intents = discord.Intents.default()
intents.messages = True  # Pozwala nasłuchiwać wiadomości
intents.guilds = True  # Dostęp do serwerów
intents.message_content = True  # Wymagane przez Discord API

# Tworzenie instancji bota z prefiksem komend
bot = commands.Bot(command_prefix="!", intents=intents)

# Obsługa błędów komend
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Nie znaleziono takiej komendy. Użyj `!help`.")
    else:
        await ctx.send(f"Wystąpił błąd: {error}")

# Zdarzenie informujące, że bot jest online + ładowanie cogs (modułów)
@bot.event
async def on_ready():
    print(f'Bot {bot.user} jest online!')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # Automatycznie ładuje moduły (cogs)
            # filename[:-3] usuwa .py z nazwy pliku z ./cogs/
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f'Załadowano: cogs.{filename[:-3]}')

# Uruchamianie bota
bot.run(TOKEN)
