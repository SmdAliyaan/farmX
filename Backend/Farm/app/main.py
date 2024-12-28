from flask import Flask, render_template, request, jsonify
from scraper import get_crop_prices_from_csv, predict_prices

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_prices", methods=["POST"])
def get_prices():
    crop = request.json["crop"]
    prices = get_crop_prices_from_csv(crop)
    if not prices:
        return jsonify({"error": f"No data found for crop: {crop}"})
    
    predictions = predict_prices(prices)
    return jsonify({"prices": prices, "predictions": predictions})

if __name__ == "__main__":
    app.run(debug=True)
