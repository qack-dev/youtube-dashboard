from janome.tokenizer import Tokenizer

t = Tokenizer()

# --- 感情辞書の定義 ---
positive_words = ['良い', '最高', '面白い', '楽しい', '好き', '感動', 'うまい', 'すごい', '素晴らしい', '素敵']
negative_words = ['悪い', '最悪', 'ひどい', 'つまらない', '嫌い', '悲しい', '下手', 'ダサい']

def analyze_sentiment(text: str) -> str:
    """
    与えられたテキストの感情を分析し、'ポジティブ', 'ネガティブ', 'ニュートラル'のいずれかを返す関数。
    """
    score = 0
    tokens = t.tokenize(text, wakati=True)
    
    for token in tokens:
        if token in positive_words:
            score += 1
        elif token in negative_words:
            score -= 1
            
    if score > 0:
        return 'ポジティブ'
    elif score < 0:
        return 'ネガティブ'
    else:
        return 'ニュートラル'

# --- 動作テスト用のコード ---
if __name__ == '__main__':
    test_comment1 = 'この動画は本当に最高で面白い！'
    test_comment2 = 'なんてひどい内容なんだ。つまらない。'
    test_comment3 = 'ふーん、なるほどね。'

    print(f'「{test_comment1}」-> {analyze_sentiment(test_comment1)}')
    print(f'「{test_comment2}」-> {analyze_sentiment(test_comment2)}')
    print(f'「{test_comment3}」-> {analyze_sentiment(test_comment3)}')
