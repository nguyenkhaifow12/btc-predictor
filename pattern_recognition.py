def detect_bullish_patterns(df):
    """
    Phát hiện các mô hình nến đảo chiều tăng:
    - Bullish Engulfing
    - Morning Star
    - Bullish Pin Bar
    
    df: DataFrame có ít nhất các cột ['Open', 'High', 'Low', 'Close']
    Trả về list các mô hình tìm được trong cây nến cuối cùng
    """
    df = df.copy()
    signals = []
    
    if df.shape[0] < 3:
        return signals

    last = df.iloc[-1]
    prev = df.iloc[-2]
    pre_prev = df.iloc[-3]

    # Bullish Engulfing
    if (prev['Close'] < prev['Open'] and           # nến trước giảm
        last['Close'] > last['Open'] and           # nến sau tăng
        last['Close'] > prev['Open'] and
        last['Open'] < prev['Close']):
        signals.append("Bullish Engulfing")

    # Morning Star
    # Nến 3: tăng, nến 2 nhỏ, nến 1 giảm mạnh
    if (pre_prev['Close'] < pre_prev['Open'] and
        abs(prev['Close'] - prev['Open']) < abs(pre_prev['Open'] - pre_prev['Close']) * 0.5 and
        last['Close'] > last['Open'] and
        last['Close'] > pre_prev['Open']):
        signals.append("Morning Star")

    # Bullish Pin Bar
    # Bóng trên dài, thân nhỏ, đóng cửa gần đáy
    if (last['High'] - last['Close']) > 2 * (last['Open'] - last['Low']):
        signals.append("Bullish Pin Bar")

    return signals
