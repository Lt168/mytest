import streamlit as st

# 1. 全局页面配置（强制展开侧边栏）
st.set_page_config(
    page_title="多功能应用",
    layout="wide",
    page_icon="✨",
    initial_sidebar_state="expanded"
)

# 2. 注册所有子页面（对应你的侧边栏选项）
pages = st.navigation([
    st.Page("pages/work11.py", title="数字档案", icon="🐱"),  # 注意文件名与实际一致
    st.Page("pages/video.py", title="视频网站", icon="🐷"),
    st.Page("pages/album.py", title="相册", icon="🍊"),
    st.Page("pages/music1.py", title="音乐播放器", icon="🎵"),
    st.Page("pages/food.py", title="南宁美食仪表盘", icon="🍜"),
    st.Page("pages/work7.py", title="简历生成器", icon="📄"),
])
# 执行导航（必须，侧边栏才会显示）
pages.run()

