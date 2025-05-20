import pandas as pd
import ta

def calculate_indicators(df):
    df = df.copy()

    # EMA
    df['EMA20'] = ta.trend.ema_indicator(df['Close'], window=20)
    df['EMA50'] = ta.trend.ema_indicator(df['Close'], window=50)
    df['EMA200'] = ta.trend.ema_indicator(df['Close'], window=200)

    # MACD
    macd = ta.trend.macd(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    # RSI
    df['RSI'] = ta.momentum.RSIIndicator(df['Close']).rsi()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(df['Close'])
    df['BB_upper'] = bb.bollinger_hband()
    df['BB_lower'] = bb.bollinger_lband()

    # ADX
    adx = ta.trend.ADXIndicator(df['High'], df['Low'], df['Close'])
    df['ADX'] = adx.adx()
    df['+DI'] = adx.adx_pos()
    df['-DI'] = adx.adx_neg()

    # Volume MA
    df['Volume_MA20'] = df['Volume'].rolling(20).mean()

    return df
