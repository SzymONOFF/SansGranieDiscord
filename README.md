# SansGranieDiscord

Discordowy bot napisany w Pythonie z użyciem [discord.py](https://github.com/Rapptz/discord.py), bazujący na systemie modułów [cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html). Moduły można poprostu dodawać do katalogu `cogs/`, a bot je załaduje. Głównym pomysłem było używanie `slash commands` aby łatwiej go obsługiwać, a od komend prefixowych odejść.


## Wymagania

Przed uruchomieniem bota upewnij się, że masz:

- Python 3.8 lub wyższe
- Zainstalowane zależności `requirements.txt` (patrz niżej)
- Token bota wygenerowany na [Discord Developer Portal](https://discord.com/developers/applications)
- zaznaczone w OAuth2 URL Generator `applications.commands` oraz `bot`

## Instalacja

### 1. Sklonuj repozytorium

```
git clone https://github.com/SzymONOFF/SansGranieDiscord.git
```

```
cd SansGranieDiscord
```

### 2. Stwórz wirtualne środowisko [venv](https://docs.python.org/3/library/venv.html)

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
# Gdy chcesz wyjść z venv
deactivate
```

### 3. Zainstaluj wymagane biblioteki

```
pip install -r requirements.txt
```

### 4. Dodaj token bota

Stwórz plik `.env` i wprowadź swój token:

```
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

### 5. Uprawnienia

***Mam nadzieje że to dobre ustawienie***

```
chmod 600 .env && chmod 644 bot.py config.py && chmod 700 ../SansGranieDiscord/ && chmod 700 cogs/ venv/
```


### 6. Uruchom bota

#### Uruchamianie bota jako program

```
python3 bot.py
```

#### Uruchamianie bota w tle

```
nohup python3 bot.py > logs/nohup.log 2>&1 &
```

## Dodawanie nowych modułów

Aby dodać nową funkcjonalność, wystarczy stworzyć plik `.py` w katalogu `cogs/`.
Przykładowy moduł (`cogs/example.py`):

```
import discord
from discord.ext import commands

class Example(commands.Cog):
    """Przykładowy moduł"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Cześć! Jestem botem Discorda.")

async def setup(bot):
    await bot.add_cog(Example(bot))
```

## Struktura programu

```
SansGranieDiscord/
│── cogs/              # Folder z modułami (cogs)
│   ├── basic.py       # Przykładowy moduł
│── logs/              # Folder z logami (cogs)
│   ├── *.log          # generowany automatyczne
│── .env               # Plik z tokenem bota
│── config.py          # Moduł ładujący token
│── bot.py             # Główny plik bota
│── requirements.txt   # Lista wymaganych pakietów
```

## Licencja

Projekt jest udostępniony na licencji MIT – możesz go używać, modyfikować i rozwijać.
