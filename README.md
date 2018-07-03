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
