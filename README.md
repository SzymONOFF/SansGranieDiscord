# SansGranieDiscord

Opis kiedyś będize


## ⚙️ Wymagania

Przed uruchomieniem bota upewnij się, że masz:

- Python 3.12+ (na takim pracuje)
- Zainstalowane zależności `requirements.txt` (patrz niżej)
- Token bota wygenerowany na [Discord Developer Portal](https://discord.com/developers/applications)
- zaznaczone w OAuth2 URL Generator `applications.commands` oraz `bot`

## 🔧 Instalacja

### 1. Sklonuj repozytorium

```
git clone https://github.com/SzymONOFF/SansGranieDiscord.git
```

```
cd SansGranieDiscord
```

### 2. Stwórz środowisko `venv`

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
deactivate
```

### 3. Zainstaluj wymagane biblioteki

```
pip install -r requirements.txt
```

### 4. Dodaj token bota

Edytuj plik `.env` i wprowadź swój token:

```
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

### 5. Uprawnienia

**DO_ZROBIENIA**

Mam nadzieje że to dobre ustawienie

```
chmod 600 .env
chmod 644 bot.py config.py
chmod 700 SansGranieDiscord/
chmod 700 cogs/ venv/
```

### 6. Uruchom bota

#### ⚡ Uruchamianie bota jako program

```
python3 bot.py
```

#### ⚡ Uruchamianie bota w tle

```
nohup python3 bot.py

# lub

nohup python3 bot.py > bot.log 2>&1 &
```

## 📂 Struktura programu

```
discord-bot/
│── cogs/              # Folder z modułami (cogs)
│   ├── basic.py       # Przykładowy moduł
│── logs/              # Folder z logami (cogs)
│   ├── *.log          # generowany automatyczne
│── .env               # Plik z tokenem bota
│── config.py          #
│── bot.py             # Główny plik bota
│── requirements.txt   # Lista wymaganych pakietów
```
