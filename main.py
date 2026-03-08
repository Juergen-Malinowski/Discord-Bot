# Hauptprogramm vom Discord-Bot

# aus dotenv nun die Funktion "load_dotenv" importieren/loaden ...
from dotenv import load_dotenv
# nun op importieren, Windows-Befehlssatz für Dateioperationen
import os

# lädt die Variablen aus .env in die Umgebungsvariablen des Projekts
# zur späteren Nutzung ...
load_dotenv()  

secretKey = os.getenv("SECRET_KEY")
print(secretKey)
