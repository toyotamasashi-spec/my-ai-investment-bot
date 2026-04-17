import os
from google import genai

def main():
    # GitHubのSecretからキーを取得
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("APIキーが設定されていません。")
        return

    # 最新のClient方式で接続
    client = genai.Client(api_key=api_key)
    
    prompt = """
    シグマ光機(7713)とエヌエフHD(6864)について、量子コンピュータ関連の
    最新ニュースを踏まえた投資判断のポイントを3点にまとめてください。
    """
    
    try:
        # 404エラーを回避する最新の呼び出し方
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        print("--- AI投資分析レポート ---")
        print(response.text)
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
