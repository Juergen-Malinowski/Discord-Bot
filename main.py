# Hauptprogramm vom Discord-Bot

# Thanks für Icon Discord "TestServerPyBot"
# <a href="https://www.flaticon.com/de/kostenlose-icons/gruppenchat" title="gruppenchat Icons">Gruppenchat Icons erstellt von Mehwish - Flaticon</a>

# Discord Funktionalitäten importieren ...
import discord

# nun op importieren, Windows-Befehlssatz für Dateioperationen
import os

# aus dotenv nun die Funktion "load_dotenv" importieren...
from dotenv import load_dotenv

# lädt die Variablen aus .env in die Umgebungsvariablen des Projekts
# zur späteren Nutzung ...
load_dotenv()  

# Den Discord-Token aus der .env laden ...
token = os.getenv("DISCORD_TOKEN")







"""
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
"""
