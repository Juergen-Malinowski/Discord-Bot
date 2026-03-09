# Hauptprogramm vom Discord-Bot

# Discord Funktionalitäten importieren ...
import discord
# Import der Discord-commands zur Nutzung ...
from discord.ext import commands

# nun op importieren, Windows-Befehlssatz für Dateioperationen
import os

# aus dotenv nun die Funktion "load_dotenv" importieren...
from dotenv import load_dotenv

# FileHandler ... fängt die logs des Discord-Bots ab und speichert
# diese in der Datei "discordBot.log" ab, damit diese später auslesbar sind.
# Der "handler" wird beim bot.run als Parameter mitgegeben.
import logging
handler = logging.FileHandler(filename="discordBot.log", mode='w', encoding="utf-8")

# lädt die Variablen aus .env in die Umgebungsvariablen des Projekts
# zur späteren Nutzung ...
load_dotenv()  

# Den Discord-Token aus der .env laden ...
token = os.getenv("DISCORD_TOKEN")

# Dem Bot die Erlaubnis / Regeln aus Dicord übergeben, die default().
# Diese habe ich in Discord bei Erstellung des Bots festgelegt, sind also änderbar ...
intents = discord.Intents.default()

# Der "prefix", hier definiert als "!" leitet später in Discord einen Befehl an den Bot
# ein, damit der Bot die Nachricht als Befehl (Funktions-Aufruf) an ihn interpretiert.
# Mit intents=intents(Variable oben) weisen wir dem Bot die default()-Befehle zur Nutzung zu.
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Ready !!! Ich bin {bot.user}")

# Den bot starten und mit der Übergabe des token authentifizieren.
# log_handler aktiviert das Speichern der logs des Bots.
# log_level definiert, wie die logs gespeichert werden sollen (DEBUG umfangreich)
bot.run(token, log_handler=handler, log_level=logging.DEBUG)


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
