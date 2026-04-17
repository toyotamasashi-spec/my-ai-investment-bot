import os
from google import genai

def main():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("APIキーがありません。Settingsを確認してください。")
        return

    # 最新のClient方式を使用。これで404エラーを回避します。
    client = genai.Client(api_key=api_key)
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="シグマ光機(7713)とエヌエフHD(6864)の将来性を分析して。"
        )
        print("--- 分析結果 ---")
        print(response.text)
    except Exception as e:
        print(f"実行エラー: {e}")

if __name__ == "__main__":
    main()
