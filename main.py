# Hauptprogramm vom Discord-Bot

# Thanks für Icon Discord "TestServerPyBot"
# <a href="https://www.flaticon.com/de/kostenlose-icons/gruppenchat" title="gruppenchat Icons">Gruppenchat Icons erstellt von Mehwish - Flaticon</a>

# aus dotenv nun die Funktion "load_dotenv" importieren/loaden ...
from dotenv import load_dotenv
# nun op importieren, Windows-Befehlssatz für Dateioperationen
import os

# lädt die Variablen aus .env in die Umgebungsvariablen des Projekts
# zur späteren Nutzung ...
load_dotenv()  

# den persönlichen KEY aus Datei .env nun in die Variable "secretKey"
# einlesen und prüfen mit print() ...pi
secretKey = os.getenv("SECRET_KEY")
print(secretKey)
