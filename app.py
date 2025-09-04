from weather_service import getData
from flask import Flask, render_template, request
import json

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


    if request.method == "POST":
        try:
            data = getData(city)
            if isinstance(data, str):
                data = json.loads(data)
            temp = data.get("main", {}).get("temp")
            icon_code = data["weather"][0]["icon"]
            icon = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"



        except Exception as e:
            error = f"Fehlrer beim Laden: {e}"

    return render_template("result.html", error=error, temp=temp, city=city, icon=icon)

if __name__ == "__main__":
    app.run(debug=True)

