#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
import os
import logging
from discord import app_commands
from discord.ext import commands
from config import TOKEN

# Konfiguracja logowania błędów do pliku
logging.basicConfig(
    level=logging.INFO,
    filename="logs/bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Ustawienie uprawnień bota (wymagane do poprawnego działania)
intents = discord.Intents.default()
# intents.messages = True  # Pozwala nasłuchiwać wiadomości
intents.guilds = True  # Dostęp do serwerów
intents.message_content = True  # Wymagane przez Discord API

# Tworzenie instancji bota dla `slash commands`
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


# Obsługa błędów komend
@bot.event
async def on_application_command_error(ctx, error):
    """Obsługa błędów dla komend aplikacyjnych (/)."""
    await ctx.respond(f"Wystąpił błąd: {error}")


# Zdarzenie uruchomienia bota
@bot.event
async def on_ready():
    """Funkcja wywoływana po uruchomieniu bota."""
    # Informacja o uruchomieniu bota
    print(f"Bot {bot.user} jest online!")
    logging.info(f"Bot {bot.user} jest online")

    # Automatyczne ładowanie wszystkich modułów (cogs)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                # filename[:-3] usuwa .py z nazwy pliku z ./cogs/
                await bot.load_extension(f"cogs.{filename[:-3]}")
                logging.info(f"Załadowano moduł: cogs.{filename[:-3]}")
            except Exception as e:
                logging.error(f"Błąd ładowania {filename}: {e}", exc_info=True)

    # Synchronizacja komend aplikacyjnych `slash commands`
    try:
        synced = await bot.tree.sync()
        logging.info(f"Zsynchronizowano {len(synced)} komend aplikacyjnych.")
    except Exception as e:
        logging.error(f"Błąd synchronizacji komend: {e}", exc_info=True)


# Uruchamianie bota
try:
    bot.run(TOKEN)
except Exception as e:
    logging.critical(f"Krytyczny błąd uruchamiania bota: {e}", exc_info=True)
