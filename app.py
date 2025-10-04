import os
import sys
from flask import Flask, render_template, request, url_for
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

# --- 他のファイルから必要な関数をインポート ---
from sentiment_analyzer import analyze_sentiment
from chart_generator import create_pie_chart

# Flaskアプリケーションの初期化
app = Flask(__name__)

def load_api_key():
    """api_key.txtファイルからAPIキーを読み込む関数"""
    try:
        with open('api_key.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        # サーバーログにエラーを出力し、アプリを終了させる
        app.logger.error("FATAL ERROR: 'api_key.txt'が見つかりません。")
        sys.exit(1)

# アプリケーション起動時にAPIキーを読み込む
API_KEY = load_api_key()

def get_video_id_from_url(url):
    """YouTubeのURLから動画IDを抽出する関数"""
    if 'youtu.be' in url:
        return urlparse(url).path[1:]
    if 'youtube.com' in url:
        query = urlparse(url).query
        params = parse_qs(query)
        return params.get('v', [None])[0]
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form['video_url']
    video_id = get_video_id_from_url(video_url)

    if not video_id:
        return "無効なYouTube URLです。もう一度お試しください。"

    # 1. コメント取得
    comments = []
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        req = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=100)
        res = req.execute()
        for item in res['items']:
            comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    except Exception as e:
        return f"APIエラー: コメントの取得に失敗しました。APIキーや動画IDが正しいか確認してください。詳細: {e}"

    # 2. 感情分析
    sentiment_results = {'ポジティブ': 0, 'ネガティブ': 0, 'ニュートラル': 0}
    for comment in comments:
        sentiment = analyze_sentiment(comment)
        sentiment_results[sentiment] += 1
    
    # 3. グラフ生成
    chart_image_path = 'images/chart.png'
    output_path = os.path.join('static', chart_image_path)
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    create_pie_chart(sentiment_results, output_path)

    # 4. 結果ページ表示
    return render_template(
        'result.html',
        video_url=video_url,
        total_comments=len(comments),
        results=sentiment_results,
        chart_image=chart_image_path
    )

if __name__ == '__main__':
    app.run(debug=True)
