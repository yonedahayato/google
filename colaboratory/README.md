# 目的
- Google ColaboratoryをAPIのようにして学習を行いたい
    - 参考 : [Google Colaboratoryを定期実行する方法について考える](https://qiita.com/Fortinbras/items/4cfa9269af2ab8d1d4d5)

# スクリプト
|スクリプト名|概要|
|---|---|
|schedule.py|セッションを切らさないよう「常時稼働させる」方向で90分のセッション切れを回避する。```colab上で起動想定```|
|exec_gcolab.py|ローカルPC上にてSelenumでGoogle Driveにログインして、Google Colabratoryのファイルを開いて一番上のセルの実行ボタンをクリックする|

# 環境準備
- Docker での環境を整えたかったが、エラーがでるためColbaの実行は外部APIにて実施する
