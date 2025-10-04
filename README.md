# YouTube Comment Sentiment Analysis Dashboard

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

特定のYouTube動画のコメントを取得し、日本語の感情分析（ポジティブ/ネガティブ）を行い、結果を円グラフで可視化するシンプルなWebアプリケーションです。

データ分析やWebアプリケーション開発の初学者向けのサンプルプロジェクトとして作成しました。

![Dashboard Screenshot](https://user-images.githubusercontent.com/10/222333444-c689304a-4428-4f27-8e6d-9c3f46f22200.png)
*(ここに完成したアプリケーションのスクリーンショットを挿入してください)*

---

## ✨ 主な機能

-   **コメント自動取得:** 指定したYouTube動画のURLからコメントを100件まで自動で取得します。
-   **感情分析:** 各コメントを「ポジティブ」「ネガティブ」「ニュートラル」の3種類に分類します。
-   **結果の可視化:** 分析結果の全体的な割合を円グラフで分かりやすく表示します。
-   **シンプルなWeb UI:** 直感的に操作できるWebインターフェースを提供します。

## 🛠️ 使用技術

-   **Webフレームワーク:** Flask
-   **API連携:** Google API Client Library for Python
-   **日本語形態素解析:** Janome
-   **データ可視化:** Matplotlib
-   **日本語文字化け対策:** japanize-matplotlib

---

## 🚀 Getting Started

このアプリケーションをあなたのローカル環境で動かすための手順です。

### 1. 前提条件

-   Python 3.8 以上
-   pip
-   Git

### 2. インストール手順

1.  **リポジトリをクローン**
    ```sh
    git clone https://github.com/あなたのユーザー名/youtube-dashboard.git
    cd youtube-dashboard
    ```

2.  **Python仮想環境の作成と有効化**
    -   Windowsの場合:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    -   macOS / Linuxの場合:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **必要なライブラリをインストール**
    ```sh
    pip install -r requirements.txt
    ```
    > **💡 `requirements.txt`について**
    > このプロジェクトで使われているPythonライブラリの一覧です。上記のコマンドで、必要なライブラリがすべて一括でインストールされます。

### 3. APIキーの設定

このアプリケーションは **YouTube Data API v3** を利用します。以下の手順でAPIキーを取得し、設定してください。

1.  [Google Cloud Console](https://console.cloud.google.com/)にアクセスし、新しいプロジェクトを作成します。
2.  「APIとサービス」 > 「ライブラリ」から **"YouTube Data API v3"** を検索し、有効化します。
3.  「APIとサービス」 > 「認証情報」から「+ 認証情報を作成」をクリックし、「APIキー」を選択します。
4.  発行されたAPIキーをコピーします。
5.  プロジェクトのルートディレクトリ（`app.py`と同じ階層）に `api_key.txt` という名前のファイルを作成します。
6.  `api_key.txt` の中に、コピーしたAPIキーの文字列**だけ**を貼り付けて保存します。

    **`api_key.txt` の中身の例:**
    ```txt
    AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ```

    > **⚠️ セキュリティ上の注意**
    > `api_key.txt` は、絶対にGitの管理に含めないでください。プロジェクトのルートディレクトリにある`.gitignore`ファイルに `api_key.txt` と記載することで、誤ってAPIキーを公開してしまう事故を防げます。
    > ```.gitignore
    > # ... other settings ...
    >
    > # API Key
    > api_key.txt
    > ```

### 4. アプリケーションの実行

すべての設定が完了したら、以下のコマンドでWebサーバーを起動します。

```sh
flask run
```

ターミナルに `* Running on http://127.0.0.1:5000` と表示されたら、お使いのWebブラウザでこのアドレスにアクセスしてください。

## 📜 ライセンス

このプロジェクトはMITライセンスです。詳細は [LICENSE](LICENSE) ファイルをご覧ください。
