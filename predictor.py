from indicators import calculate_indicators
from pattern_recognition import detect_bullish_patterns
from onchain import analyze_onchain_data

def generate_signal(df, funding_rate, open_interest, exchange_flow):
    df = calculate_indicators(df)
    last = df.iloc[-1]
    
    # Kỹ thuật
    conditions = {
        "trend_strong": last['EMA20'] > last['EMA50'] > last['EMA200'],
        "macd_bullish": last['MACD'] > last['MACD_signal'],
        "rsi_ok": 55 < last['RSI'] < 70,
        "adx_strong": last['ADX'] > 25 and last['+DI'] > last['-DI'],
        "volume_high": last['Volume'] > last['Volume_MA20'],
    }

    pattern_signals = detect_bullish_patterns(df)

    # On-chain
    onchain_result = analyze_onchain_data(funding_rate, open_interest, exchange_flow)

    score = sum(conditions.values()) + onchain_result['onchain_score'] + (1 if pattern_signals else 0)

    if score >= 6:
        decision = "STRONG BUY / LONG"
    elif score >= 4:
        decision = "BUY / Watch for LONG"
    elif score <= 2:
        decision = "SELL / Possible SHORT"
    else:
        decision = "HOLD"

    return {
        "decision": decision,
        "score": score,
        "conditions": conditions,
        "onchain_notes": onchain_result['onchain_notes'],
        "patterns": pattern_signals,
        "price_now": last['Close']
    }
