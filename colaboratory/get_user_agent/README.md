# 目的
- docker 環境を作成
- chrome(selenium)で接続後、goole のサービスに自身の情報でログインをし、UserAgentを取得する

# script
## Docker
|name|description|
|---|---|
|Dockerfile| |
|Dockerfile_lib|ubuntu desktop 環境からimage を作成する。 |
|docker_exe.sh| |
|requirements.txt| |

## python
|name|description|
|---|---|
|colab_exe.py|Colaboratory の実行 |
|get_user_agent.py|UserAgent の取得 |
|server.py|CloudRun で使用するために web server|


# 参考
- ~~[Dockerを導入してGUI操作可能なLinux(Ubuntu)コンテナを作成する](https://qiita.com/ryoya-s/items/ee1daf9cab18c100c990)~~
