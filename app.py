from weather_service import getData
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    data = None
    error = None
    temp = None

    if request.method == "POST":
        try:
            data = getData()
            if isinstance(data, str):
                data = json.loads(data)
            temp = data.get("main", {}).get("temp")


        except Exception as e:
            error = f"Fehlrer beim Laden: {e}"

    return render_template("index.html", error=error, temp=temp)

if __name__ == "__main__":
    app.run(debug=True)