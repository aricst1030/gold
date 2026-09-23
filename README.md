# GOLD RATE 金買取相場シミュレーター

田中貴金属公式の「金 店頭買取価格（税込）」を定期取得し、K24〜K9の概算買取額を計算するGitHub Pages用サイトです。

## 自動更新
GitHub Actionsで平日 9:40 / 14:10（日本時間）に価格を取得します。
手動更新も Actions → Update Gold Price → Run workflow から実行できます。

※GitHub Actionsのスケジュールは混雑時などに遅延する場合があります。
※田中貴金属側のページ構成が変更された場合、取得処理の修正が必要になる可能性があります。
