def analyze_onchain_data(funding_rate, open_interest, exchange_flow):
    score = 0
    notes = []

    if funding_rate < 0:
        score += 1
        notes.append("Funding rate < 0: tâm lý tiêu cực -> dễ đảo chiều tăng")

    if open_interest['change'] > 0 and open_interest['volume_change'] > 0:
        score += 1
        notes.append("OI và Volume tăng đồng thời: xác nhận trend")

    if exchange_flow['inflow'] < exchange_flow['outflow']:
        score += 1
        notes.append("BTC rút khỏi sàn > nạp vào: tín hiệu tích trữ")

    return {"onchain_score": score, "onchain_notes": notes}
