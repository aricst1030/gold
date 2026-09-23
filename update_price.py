import json
import re
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

URL = "https://gold.tanaka.co.jp/commodity/souba/index.php"
OUT = "prices.json"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (compatible; GoldRateUpdater/1.0)"})
with urllib.request.urlopen(req, timeout=30) as r:
    html = r.read().decode("utf-8", errors="ignore")

# HTMLタグ等を除去して検索しやすくする
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)

# 「金」の地金価格ブロック内にある店頭買取価格を取得
m = re.search(r"地金価格.*?金.*?店頭小売価格.*?店頭買取価格.*?([0-9,]+)\s*円", text)
if not m:
    raise RuntimeError("田中貴金属公式ページから金の買取価格を取得できませんでした。ページ構成が変更された可能性があります。")

buy = int(m.group(1).replace(",", ""))

now = datetime.now(ZoneInfo("Asia/Tokyo"))
data = {
    "tanaka_buy": buy,
    "last_updated_jst": now.strftime("%Y-%m-%d %H:%M"),
    "source_label": "田中貴金属公式・金 店頭買取価格（税込）",
    "source_url": URL
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Updated Tanaka gold buy price: {buy:,} yen/g")
