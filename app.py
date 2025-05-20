from flask import Flask, jsonify, render_template
from utils import fetch_btc_data
from predictor import generate_signal

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    df = fetch_btc_data(days=90)
    # Dữ liệu on-chain giả lập (bạn có thể thay bằng API thật)
    funding_rate = -0.01
    open_interest = {"change": 1.5, "volume_change": 2.0}
    exchange_flow = {"inflow": 1000, "outflow": 1500}

    result = generate_signal(df, funding_rate, open_interest, exchange_flow)
    return jsonify(result)

if __name__ == "__main__":
    # Chạy app ở chế độ debug khi phát triển, port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
