import streamlit as st

# 全局CSS样式（核心：固定侧边栏+防位移+内容完整显示）
# 全局CSS样式（替换原样式）
st.markdown("""
    <style>
    /* 全局基础样式 */
    .stApp {
        background-color: white;
        margin: 0 !important;
        padding: 0 !important;
    }
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* 侧边栏固定样式 */
    [data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 260px !important;
        max-width: 260px !important;
        visibility: visible !important;
    }
    [data-testid="stSidebarHeader"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
        padding-top: 1rem !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        height: 100vh !important;
        width: 260px !important;
        z-index: 9999 !important;
        border-right: 1px solid #eee;
    }

    /* ========== 核心修复：主内容区完全隔离 ========== */
    /* 主内容区容器：彻底与侧边栏分离 */
    [data-testid="stAppViewContainer"] {
        margin-left: 260px !important;  /* 与侧边栏宽度一致 */
        width: calc(100% - 260px) !important;
    }
    /* 页面内容块：约束在容器内，避免溢出 */
    [data-testid="stMainContainer"] {
        padding: 2rem !important;
        min-height: 100vh !important;
        box-sizing: border-box !important;
        overflow: hidden auto !important;  /* 纵向溢出滚动 */
    }
    /* 单个页面的内容容器：避免跨页面内容重叠 */
    .st-emotion-cache-12fmjuu {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* 侧边栏按钮样式 */
    [data-testid="stSidebar"] .stButton button {
        width: 100% !important;
        margin-bottom: 0.5rem !important;
        border-radius: 6px !important;
        border: 1px solid #eee !important;
        background-color: white !important;
        color: #333 !important;
        font-size: 0.9rem !important;
    }
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #f0f8ff !important;
        border-color: #4682B4 !important;
    }

    /* 通用组件适配 */
    .stVideo, .stImage {
        max-width: 100% !important;
        height: auto !important;
    }
    .stButton > button {
        white-space: normal !important;
    }

    /* 模块专用样式 */
    .section-underline {
        border-bottom: 2px solid #4682B4;
        padding-bottom: 4px;
        margin-bottom: 15px;
    }
    .title {
        color: #e86b9c;
        text-shadow: 0 0 3px #fcc8d1;
        font-family: "Comic Sans MS", cursive;
        font-size: 1.2rem !important;
    }
    .header {
        color: #8b5cf6;
        text-shadow: 0 0 3px #d8b4fe;
        font-family: "Comic Sans MS", cursive;
        font-size: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化全局会话状态（跨页面共享）
if "img_ind" not in st.session_state:
    st.session_state.img_ind = 0    # 相册图片索引
if "peppa_ind" not in st.session_state:
    st.session_state.peppa_ind = 0  # 小猪佩奇集数索引
if "music_ind" not in st.session_state:
    st.session_state.music_ind = 0  # 音乐播放器索引

# ========== 多页面导航配置（侧边栏功能入口） ==========
pages = st.navigation([
    # 注册pages文件夹下的功能页面（需确保文件存在）
    st.Page("pages/work11.py", title="数字档案", icon="🐱"),
    st.Page("pages/video.py", title="视频网站", icon="🐷"),
    st.Page("pages/album.py", title="相册", icon="🍊"),
    st.Page("pages/music1.py", title="音乐播放器", icon="🎵"),
    st.Page("pages/food.py", title=" 南宁美食仪表盘", icon="🍜"),
    st.Page("pages/work7.py", title="简历生成器", icon="📄"),
])
pages.run()  # 启动导航（必须加，否则侧边栏不显示功能）



