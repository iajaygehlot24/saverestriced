import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8365878070:AAEJfOSGmSwRF2pPqalRzndebPDnmnh57ec")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "10634878"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2eab99b8459017fff27395cc52f3c860")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1168219996"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "saveaj_bot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
