from weather_service import getData
from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():

    data = None
    error = None
    temp = None
    city = request.form.get("city")
    now = datetime.now()
    now = now.strftime("%H:%M")


    if request.method == "POST":
        try:
            data = getData(city)
            if isinstance(data, str):
                data = json.loads(data)

            sunrise = data.get("sys", {}).get("sunrise")
            sunset = data.get("sys", {}).get("sunset")

            sunrise = datetime.fromtimestamp(sunrise).strftime("%H:%M")
            sunset = datetime.fromtimestamp(sunset).strftime("%H:%M")





        except Exception as e:
            error = f"Fehlrer beim Laden: {e}"

    return render_template("result.html", error=error, data=data, now=now, sunrise=sunrise, sunset=sunset)

if __name__ == "__main__":
    app.run(debug=True)

