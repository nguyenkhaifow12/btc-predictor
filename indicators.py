import pandas as pd
import ta

def calculate_indicators(df):
    df = df.copy()

    close = df['Close']
    if len(close.shape) > 1:
        close = close.squeeze()  # ép từ (N,1) thành (N,)

    # EMA
    df['EMA20'] = ta.trend.ema_indicator(close, window=20)
    df['EMA50'] = ta.trend.ema_indicator(close, window=50)
    df['EMA200'] = ta.trend.ema_indicator(close, window=200)

    # MACD
    macd = ta.trend.MACD(close)
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    # RSI
    df['RSI'] = ta.momentum.RSIIndicator(close).rsi()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(close)
    df['BB_upper'] = bb.bollinger_hband()
    df['BB_lower'] = bb.bollinger_lband()

    # ADX
    adx = ta.trend.ADXIndicator(df['High'], df['Low'], close)
    df['ADX'] = adx.adx()
    df['+DI'] = adx.adx_pos()
    df['-DI'] = adx.adx_neg()

    # Volume MA
    df['Volume_MA20'] = df['Volume'].rolling(20).mean()

    return df
