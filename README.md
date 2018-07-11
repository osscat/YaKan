YaKan
===============

# バックエンド

# Python のインストール
★バージョン : 3.6.5
インストーラをダウンロードしてインストール
https://www.python.org/downloads/
バージョン確認
```
python --version
```
# Django のインストール
★バージョン : 2.0.6
pip でインストール
プロキシを通す場合は proxy オプションを付ける
```
pip install Django==2.0.6 --proxy=http://userid:password@proxyhost:port
```
# Django REST frameworkのインストール
```
pip install djangorestframework
```
# PostgreSQL 接続ドライバのインストール
```
pip install psycopg2
```
# CORS に対応する
ライブラリをインストールする
```
pip install django-cors-headers
```
# django-filter のインストール
```
pip install django-filter
```


# 開発環境
Pycharm
https://www.jetbrains.com/pycharm/
とか
Eclipse (PyDev)
とか


# その他
・プロジェクト作成
```
django-admin startproject XXXX
```
・アプリケーション作成
```
python manage.py startapp XXXX
```
・サーバー起動
```
python manage.py runserver
```
・スーパーユーザ作成
```
python manage.py createsuperuser
```
・マイグレーション
```
python manage.py makemigrations
python manage.py migrate
```

# フロントエンド

# Node.js のインストール
適宜インストーラで。

# vue-cli のインストール
```
npm install -g vue-cli
```

# 開発環境

# その他
・プロジェクト作成
```
vue init webpack XXX
```
・プロジェクトをチェックアウトした場合は下記を実施
```
npm install
```
・開発ビルドと起動
```
npm run dev
```
・製品版ビルド
```
???
```


# WebSocket の設定
・参考サイト
　https://poyo.hatenablog.jp/entry/2018/05/17/224247

・必要なもの
　channels
　VisualC++ Build Tool (channels のインストールに必要）
　pywin32
　redis (インメモリDB)

・インストール
　■ VisualC++ Build Tool
　　https://download.microsoft.com/download/5/F/7/5F7ACAEB-8363-451F-9425-68A90F98B238/visualcppbuildtools_full.exe

　■ channels
　　pip install -U channels

　■ settings.py の設定
　　Yakan/settings.py に以下の記述を追加

　　ASGI_APPLICATION = "YaKan.routing.application"

　　CHANNEL_LAYERS = {
　　    'default': {
　　        'BACKEND': 'channels_redis.core.RedisChannelLayer',
　　        'CONFIG': {
　　            "hosts": [('127.0.0.1', 6379)],
　　        },
　　    },
　　}

　ここまで設定した後、runserver して　「ModuleNotFoundError: No module named 'win32api'」のエラーが
　出た場合、pywin32 をインストールしてください。

　■ pywin32　
　　https://github.com/mhammond/pywin32/releases
　　　python3.6.5 なら pywin32-223.win-amd64-py3.6.exe

　■ redis
　　channels で複数ブラウザに対して値を返却する仕組みのバックエンドとして redis という
　　インメモリーデータベースを使います。

　　本体（更新とまってますが仕方ない）
　　https://github.com/MicrosoftArchive/redis/releases

　　連携用のモジュール
　　pip install channels_redis
　　pip install asgi_redis
　　pip install asgiref==2.2.0

　　