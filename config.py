# Configurações do bot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_IDS = set(
    int(value.strip())
    for value in os.getenv("ADMIN_IDS", "").split(",")
    if value.strip()
)
GATEWAY_URL = os.getenv(
    "GATEWAY_URL",
    "https://t.me/VortexBank_bot?start=8819482547",
)

APP_NAME = "Vortex Digital Stock"
