import os
import google.generativeai as genai

def main():
    # GitHubのSecretから読み込み
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "シグマ光機(7713)とエヌエフHD(6864)の最新の技術動向を分析して。"
    response = model.generate_content(prompt)
    
    print("--- 投資分析レポート ---")
    print(response.text)

if __name__ == "__main__":
    main()
