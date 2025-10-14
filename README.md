# 🌤️ WeatherWebsite

Eine einfache Web-App, die aktuelle Wetterdaten über eine API anzeigt.

## 🚀 Installation

```bash
git clone https://github.com/carnevio/WeatherWebsite.git
cd WeatherWebsite
pip install -r requirements.txt

```
Erstelle eine .env Datei (aus .env.example) mit deinem API-Key:

```ini
WEATHER_API_KEY=dein_api_key

```
Dann starten:
```bash
python app.py

```
→ Öffne http://127.0.0.1:5000

🧩 Aufbau

app.py – Hauptprogramm / Server

weather_service.py – Kommunikation mit der Wetter-API

templates/ – HTML-Dateien

static/ – CSS, Icons usw.

✨ Features

Aktuelle Wetterdaten per API

Einfaches responsives Design

Erweiterbar (Vorhersage, Dark Mode, Standort, usw.)

📄 Lizenz

MIT License © 2025 Nevio

