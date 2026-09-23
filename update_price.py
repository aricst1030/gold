import json, re, urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

# 各社の公開ページを取得し、価格表を更新します。
# ページ構成が変わった場合は抽出部分の修正が必要です。
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 GoldRateComparison/1.0"})
    with urllib.request.urlopen(req,timeout=30) as r:
        return re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",r.read().decode("utf-8","ignore")))

def num(x): return int(x.replace(",",""))

# 田中：最新のK24地金買取価格を取得。その他純度はK24比で概算せず、
# 既存価格を残す設計にして、誤った自動推定を避けます。
tanaka = get("https://gold.tanaka.co.jp/commodity/souba/index.php")
m = re.search(r"金\s+([0-9,]+)円\s*\([^\)]*\)\s+([0-9,]+)円",tanaka)
if m:
    k24=num(m.group(2))
else:
    # ページ表記の変更に備え、別パターン
    m=re.search(r"金.*?店頭買取価格.*?([0-9,]+)",tanaka)
    if not m: raise RuntimeError("田中貴金属の価格を取得できませんでした")
    k24=num(m.group(1))

with open("prices.json","r",encoding="utf-8") as f: data=json.load(f)
data["updated_jst"]=datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M")
data["shops"][0]["prices"]["K24"]=k24
# K24以外は各社の公表値を安全側に残す。K24の自動取得確認後に拡張可能。

with open("prices.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2); f.write("\n")
print("Tanaka K24:",k24)
