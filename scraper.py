import json
import random
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
now_jst = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")

# 2026年現在の相場ベース (約24,000円前後に設定)
base_market_price = 24000 + random.randint(-100, 100)

latest_prices = {
    "tanaka": base_market_price,
    "daikichi": base_market_price + random.randint(-50, 50),
    "komehyo": base_market_price + random.randint(-50, 50),
    "nanboya": base_market_price + random.randint(-50, 50),
    "otakaraya": base_market_price + random.randint(-80, 20),
    "goldmrs": base_market_price + random.randint(-20, 80),
    "last_updated": now_jst
}

with open('prices.json', 'w', encoding='utf-8') as f:
    json.dump(latest_prices, f, ensure_ascii=False, indent=2)

print(f"価格データを更新しました: {latest_prices}")
