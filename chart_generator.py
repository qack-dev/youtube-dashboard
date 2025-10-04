import matplotlib.pyplot as plt
import matplotlib as mpl

def create_pie_chart(sentiment_counts: dict, output_path: str):
    """
    感情分析の集計結果から円グラフを生成し、指定されたパスに画像として保存する関数。
    """
    try:
        mpl.rcParams['font.family'] = 'Meiryo'  # 日本語フォントの設定
    except Exception as e:
        print(f"フォントの設定に失敗しました: {e}")
        mpl.rcParams['font.family'] = 'sans-serif'
    
    labels = sentiment_counts.keys()
    sizes = sentiment_counts.values()
    colors = ['#ff9999','#66b3ff','#99ff99'] # ネガティブ, ポジティブ, ニュートラル
    
    fig, ax = plt.subplots()
    ax.pie(
        sizes, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
    )
    ax.axis('equal')
    plt.title('YouTubeコメント感情分析結果')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"グラフを {output_path} に保存しました。")

# --- 動作テスト用のコード ---
if __name__ == '__main__':
    import os
    dummy_counts = {'ポジティブ': 55, 'ネガティブ': 25, 'ニュートラル': 20}
    
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    output_file = 'static/images/sentiment_chart_test.png'
    create_pie_chart(dummy_counts, output_file)
