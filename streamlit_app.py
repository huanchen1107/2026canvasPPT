import streamlit as st
import streamlit.components.v1 as components
import os

# 設定頁面為寬螢幕
st.set_page_config(layout="wide", page_title="Slide Pipeline Lab")

def load_index():
    # 讀取同目錄下的 index.html
    path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# 嵌入 HTML
# 注意：height 需設得夠高以容納您的整個管線儀表板
html_string = load_index()
components.html(html_string, height=1500, scrolling=True)
