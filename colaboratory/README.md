# 目的
- Google ColaboratoryをAPIのようにして学習を行いたい
    - 参考 : [Google Colaboratoryを定期実行する方法について考える](https://qiita.com/Fortinbras/items/4cfa9269af2ab8d1d4d5)

# スクリプト
## python
|スクリプト名|概要|
|---|---|
|schedule.py|セッションを切らさないよう「常時稼働させる」方向で90分のセッション切れを回避する。```colab上で起動想定```|
|exec_gcolab.py|ローカルPC上にてSeleniumでGoogle Driveにログインして、Google Colabratoryのファイルを開いて一番上のセルの実行ボタンをクリックする|
|main.py|google cloud functions を使用して稼働させるためのスクリプト|

## 設定
|スクリプト名|概要|
|---|---|
|setting_tmp.py|setting.pyのテンプレートファイル|
|requirements.txt|-|

## Selenium
|headless-chromium.zip|オープソースのウェブブラウザでChromeなど多くのブラウザの元になっている|


# 環境準備
- Docker での環境を整えたかったが、エラーがでるためColbaの実行は外部APIにて実施する
