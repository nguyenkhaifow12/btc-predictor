def detect_bullish_patterns(df):
    df = df.copy()
    signals = []
    
    if df.shape[0] < 3:
        return signals

    last = df.iloc[-1]
    prev = df.iloc[-2]
    pre_prev = df.iloc[-3]

    # Bullish Engulfing
    if prev['Close'] < prev['Open'] and last['Close'] > last['Open'] and last['Close'] > prev['Open'] and last['Open'] < prev['Close']:
        signals.append("Bullish Engulfing")

    # Morning Star
    if pre_prev['Close'] < pre_prev['Open'] and abs(prev['Close'] - prev['Open']) < (pre_prev['Open'] - pre_prev['Close']) * 0.5 and last['Close'] > last['Open'] and last['Close'] > pre_prev['Open']:
        signals.append("Morning Star")

    # Pin Bar
    if (last['High'] - last['Close']) > 2*(last['Open'] - last['Low']):
        signals.append("Bullish Pin Bar")

    return signals
