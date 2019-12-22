# 参考
- [Dockerを導入してGUI操作可能なLinux(Ubuntu)コンテナを作成する](https://qiita.com/ryoya-s/items/ee1daf9cab18c100c990)

```
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```
