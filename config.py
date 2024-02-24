import os

from environs import Env

env = Env()
env.read_env()


class Settings:
    STMP_USERNAME = env.str("STMP_USERNAME")
    STMP_PASSWORD = env.str("STMP_PASSWORD")
    BOT_TOKEN = env.str("BOT_TOKEN")


settings = Settings()
os.makedirs("logs", exist_ok=True)