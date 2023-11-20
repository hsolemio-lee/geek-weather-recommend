from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from weather_recommendation import recommend_weather


app = Flask(__name__, static_url_path="", static_folder="static")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend-weather", methods=["GET"])
def process():
    region = request.args.get("region")
    weather_fashion, image_url = recommend_weather(region=region)
    return jsonify(
        {
            "temperature": weather_fashion.temperature,
            "weather": weather_fashion.weather,
            "fashion": weather_fashion.fashion,
            "image": image_url.url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
