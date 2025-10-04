import sys
from googleapiclient.discovery import build

def load_api_key():
    """api_key.txtファイルからAPIキーを読み込む関数"""
    try:
        with open('api_key.txt', 'r') as f:
            # strip()で前後の余計な改行や空白を削除
            return f.read().strip()
    except FileNotFoundError:
        print("エラー: 'api_key.txt' ファイルが見つかりません。")
        print("プロジェクトフォルダにAPIキーを記載したファイルを作成してください。")
        # プログラムを終了させる
        sys.exit(1)

# -----------------------------------------------------
# ここから下を、あなた自身の情報に書き換えてください
# -----------------------------------------------------
# 1. コメントを取得したいYouTube動画のIDを設定
# 例: 動画URLが https://www.youtube.com/watch?v=XXXXXXXXXXX の場合
# XXXXXXXXXXX の部分が動画IDです。
VIDEO_ID = '8e3jHjJc9nk'
# -----------------------------------------------------

# api_key.txtからAPIキーを読み込む
API_KEY = load_api_key()

# YouTube APIとの接続を確立
youtube = build('youtube', 'v3', developerKey=API_KEY)

# APIリクエストを作成
request = youtube.commentThreads().list(
    part='snippet',
    videoId=VIDEO_ID,
    maxResults=100,
    order='relevance'
)

# APIリクエストを実行
try:
    response = request.execute()
    for item in response['items']:
        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        print(f'投稿者: {author_name}')
        print(f'コメント: {comment_text}')
        print('---')
except Exception as e:
    print(f'エラーが発生しました: {e}')
