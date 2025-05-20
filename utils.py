import yfinance as yf

def fetch_btc_data(days=90):
    df = yf.download("BTC-USD", period=f"{days}d", interval="1d")
    df = df.dropna()
    return df


### File: app.py (Flask tích hợp)
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
    # Giả lập dữ liệu on-chain tạm thời (có thể cập nhật từ API thật)
    funding_rate = -0.01
    open_interest = {"change": 1.5, "volume_change": 2.0}
    exchange_flow = {"inflow": 1000, "outflow": 1500}

    result = generate_signal(df, funding_rate, open_interest, exchange_flow)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
