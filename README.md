# SansGranieDiscord



### Środowisko

(https://mareknowak.pl/python-wirtualne-srodowisko-venv/)

$`python3 -m venv venv`

$`source venv/bin/activate`

$`deactivate`

(venv) $`pip install discord python-dotenv`


Plik .env (zawiera token)

```
DISCORD_TOKEN=...token...
```

`chmod 600 .env`

 - Tylko właściciel może czytać i modyfikować plik
 - Inni użytkownicy nie mogą go zobaczyć

Pliki kodu (bot.py, config.py, itp.)

`chmod 644 bot.py config.py`

 - Właściciel może czytać i edytować
 - Inni mogą czytać (ale nie zmieniać)

Foldery (cogs/, venv/) 

`chmod 700 discord-bot`

 - Właściciel może wszystko
 - Inni użytkownicy nie mają dostępu

Plik .gitignore :

```
.env
venv/
__pycache__/
```

