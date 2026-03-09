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

# Zwei weitere Funktionalitäten für den Bot auch HIER aktivieren ...
# (Diese müssen bei Dicord-Developer vorher beim Bot aktiviert werden!)
intents.message_content = True  # Bot kann nun auf Nachrichten reagieren
intents.members = True          # Bot kann den Members des Dicord-Servers direkt antworten

# Der "prefix", hier definiert als "/" (modernes Präfix, heute üblich in Discord / älter "!", "?", "$") 
# leitet später in Discord einen Befehl an den Bot ein, damit der Bot die Nachricht als Befehl (Funktions-Aufruf) 
# an ihn interpretiert.
# Mit intents=intents(command_prefix="/") weisen wir dem Bot die default()-Befehle zur Nutzung zu.
bot = commands.Bot(command_prefix="/", intents=intents)


# Terminal / cmd bestätigt, wenn der Bot im Dicord aktiviert wurde ...
@bot.event
async def on_ready():
    print(f"Ready !!! Ich bin {bot.user}")


# /hallo
# @bot.command() registriert die nachfolgende Funktion als Bot-Befehl (command).
# Ein User kann den Befehl mit "/hallo" aktivieren ...
@bot.command()
# "ctx" steht für Context (anstatt ctx könnte auch channel geschrieben werden / ctx ist eine Kurzform bei commands)
async def hallo(ctx):
    # mit .mention als "Anhang" wird zur normalen Nachricht des Bots zusätzlich der Benutzer "author" angepingt,
    # erhält also ein Info, dass er angesprochen wurde bzw. eine Antwort erhielt !!!
    await ctx.send(f"Grüße Dich {ctx.author.mention}")

# /message
# Schreibt ein User hinter /msg hallo, dann antwortet der Bot:
# "Deine Nachricht war hallo". Es wird nur das erste Wort zurückgegeben,
# es sei denn, der User setzt die Nachricht in "".
@bot.command()
async def message(ctx, arg):
    await ctx.send(f"Deine Nachricht war {arg}")

# assign
# Mit dem Bot einem User eine ROLLE (in Discord zuvor definiert worden
# über "Servereinstellungen/Rollen") ...
new_role = "HammerTyp"
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"Deine Rolle - {role} - wurde hinzugefügt.")
        return
    await ctx.send(f"Die Rolle wurde nicht gefunden !")

# remove
# Mit dem Bot eine Rolle entfernen ...
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Deine Rolle - {role} - wurde entfernt.")
        return
    await ctx.send(f"Die Rolle wurde nicht gefunden !")


# banana
# Bot-Event ... Bot soll auf die Nachricht "banana" reagieren ...
@bot.event
async def on_message(message):
    # Verhindert, dass Bot auf eigene Nachrichten reagiert ...
    if message.author == bot.user:
        return
    # Es wir auf "banana" reagiert, egal ob groß oder klein geschrieben ...
    if "banana" in message.content.lower():
        # Den Kanal der Nachricht in "channel" speichern
        channel = message.channel
        # In den gleichen Kanal nun die Reaktion des Bot ausgeben ...
        await channel.send(f"Hey, dieser Begriff ist nur für die Schüler der DA !")
    # Verhindert, dass der Bot nicht nocheinmal auf die gleiche Nachricht reagiert!
    # Muss ausserhalb der IF-Anweisung stehen!
    await bot.process_commands(message)


# BOT Start !!!
# Den bot starten und mit der Übergabe des token authentifizieren.
# log_handler aktiviert das Speichern der logs des Bots.
# log_level definiert, wie die logs gespeichert werden sollen (DEBUG umfangreich)
bot.run(token, log_handler=handler, log_level=logging.DEBUG)




"""
# Bot soll nun auf Nachrichten reagieren.
# Immer wenn auf dem Server eine Nachricht geschrieben wurde,
# wird für den Bot dieses Event ausgelöst.
# "message" ist ein Objekt und enthält folgende Informationen:
# Text der Nachricht, Author Nachricht, Kanal der Nachricht und Servername:
# message.content message.author  message.channel message.guild
@bot.event
async def on_message(message):
    # Die IF-Prüfung wird TRUE, wenn das Wort "/greet" als Nachricht eines
    # Users auftaucht. NUR dann !!!
    if message.content.startswith('/greet'):

        # Bot-Name ist "PyBot"

        # Verhindern, dass der Bot auf seine eigenen Nachrichten reagiert ...
        # (Dies würde sonst eine Endlosschleife auslösen !)
        if message.author == bot.user:
            return

        # Speichert den Kanal der Nachricht in "channel" ab.
        channel = message.channel
        # Der Bot antwortet und schreibt in den gespeicherten "channel"
        await channel.send('Say hello!')

        # Funktion, die auf eine bestimmte Antwort wartet, um dann entsprechend
        # zu reagieren ... ( ist die Nachricht "hello" UND ist es der richtige Kanal)
        def check(m):
            return m.content == 'hello' and m.channel == channel

        # Dies ist der wichtigste Teil ... Der "Bot" beobachtet den Kanal,
        # ob jemand in dem beobachteten Kanal ein "hello" schreibt und reagiert,
        # wenn beides auf TRUE geprüft wurde mit der Funktion "check". Die
        # Nachricht wird in "msg" gespeichert bei TRUE aus Funktion "check".
        msg = await bot.wait_for('message', check=check)
        # "msg" enthält den author der Nachricht. Nun kann der Bot im gespeicherten
        # Kanal "channel" dem Autor von "msg" eine Antwort senden und ihn direkt
        # ansprechen (msg.author) ...
        await channel.send(f'Hello {msg.author}!')

    # Wichtig, damit Bot keine erneute Nachrichten-Antworten erstellt.
    # Er wartet nun, bis die Message komplett abgearbeitet wurde.
    # Er reagiert also nicht nochmal auf die SELBE Nachricht!
    # Der Befehl darf nicht innerhalb der IF-Abfrage liegen !!!
    await bot.process_commands(message)
"""


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
