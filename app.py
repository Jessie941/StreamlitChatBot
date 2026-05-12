import streamlit as st
import google.generativeai as genai

# 1. 從後台 Secrets 讀取金鑰
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-flash-lite-latest')

except Exception as e:
    st.error(f"金鑰設定錯誤: {e}")
    st.stop()

st.title(" Gemini API 連線測試")

st.info(
    "若能成功收到 AI 回覆, 表示你的 GitHub 與 Secrets 環境配置正確!"
)

# 2. 簡單輸入介面
user_input = st.text_input(
    "輸入一段話測試連線 (例如: 你好):"
)

if user_input:
    with st.spinner("AI 正在回應中..."):
        try:
            # 呼叫 API
            response = model.generate_content(user_input)

            # 3. 顯示結果
            st.subheader("AI 的回應:")
            st.write(response.text)

            st.success("連線成功!")

        except Exception as e:
            st.error(f"連線失敗: {e}")

# 頁面初始化設定
st.set_page_config(
page_title="中科 AI 客服 - Chillcc顧問",
page_icon="https://cdn-icons-png.flaticon.com/512/535/535239.png ",
layout="wide" # "wide" 可利用全螢幕寬度,適合放置儀表板
)

with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="中科顧問代表")
    st.title("系統控制台")
    # 建立下拉選單讓使用者切換服務
    service_type = st.selectbox(
    "請選擇服務類別:",
    ["一般諮詢","技術支援","投訴建議"]
    )
    # 增加 AI 創意度調整桿
    temp = st.slider("AI 靈活度(Temperature)", 0.0, 1.0, 0.7)
    
    st.divider() # 畫出一條美觀的分隔線
    st.info(f"當前連線:{service_type}")
