# ゲームAのサンプルコード
シンプルなシューティングゲーム。\
仕様書3章を参照。

## 担当者①
- 実装する機能
  - ゲームのメイン機構
  - 画面遷移
  - キャラクターなどの当たり判定
- 編集するファイル
  - [main.py](./main.py)(ゲームのメイン機構)

## 担当者②
- 実装する機能
  - プレイヤーの描画やキーボード操作
  - プレイヤーから発射される弾丸の描画
- 編集するファイル
  - [player.py](./player.py)(プレイヤー関連)
  - [bullet.py](./bullet.py)(弾丸関連)

## 担当者③
- 実装する機能
  -  敵キャラクターの描画や移動
  -  爆発エフェクトの描画
- 編集するファイル
  - [enemy.py](./enemy.py)(敵キャラクター関連)
  - [blast.py](./blast.py)(爆発エフェクト関連)

# 参考URL
- pyxelの公式ドキュメント
  - https://github.com/kitao/pyxel/blob/main/docs/README.ja.md
- キー定義一覧
  - https://github.com/kitao/pyxel/blob/main/python/pyxel/__init__.pyi
