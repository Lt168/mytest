import streamlit as st

# 页面配置：设置白色背景
st.set_page_config(page_title="我的音乐🍊", layout="wide", page_icon="🍊")
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    /* 美化按钮样式 */
    div.stButton > button {
        background-color: #f0f2f6;
        border: 1px solid #d0d7de;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 音乐数据
music_data = [
    {
        "cover_url": "http://p2.music.126.net/o4uXVUPBgh3utGX6LdmDLQ==/109951170434249438.jpg?param=130y130",
        "audio_url": "https://music.163.com/song/media/outer/url?id=2670364332.mp3",
        "name": "咏春",
        "singer": "7wiz",
        "duration": "4:02"
    },
    {
        "cover_url": "http://p2.music.126.net/yRcxq1NGWAJWa7Hd3AgR5w==/109951171445069498.jpg?param=130y130",
        "audio_url": "https://music.163.com/song/media/outer/url?id=5257138.mp3",
        "name": "爱情汛期",
        "singer": "yihuik苡慧",
        "duration": "5:19"
    },
    {
        "cover_url": "http://p1.music.126.net/m3223Pj4ZXrItuylsVL5hA==/18855524904843746.jpg?param=130y130",
        "audio_url": "https://music.163.com/song/media/outer/url?id=519913462.mp3",
        "name": "做我的猫",
        "singer": "满舒克",
        "duration": "4:01"
    }
]

# 初始化会话状态（当前歌曲索引）
if "ind" not in st.session_state:
    st.session_state["ind"] = 0

# 切换歌曲函数
def switch_song(step):
    st.session_state["ind"] = (st.session_state["ind"] + step) % len(music_data)

# 页面标题
st.title("我的音乐🍊")
st.caption("使用Streamlit制作的简单音乐播放器，支持切换和实际播放")

# 布局：封面 + 歌曲信息 + 按钮
col1, col2 = st.columns([1, 3])
current = music_data[st.session_state["ind"]]  # 当前播放的歌曲

with col1:
    # 专辑封面
    st.image(current["cover_url"], caption="专辑封面", width=200)

with col2:
    # 歌曲信息
    st.subheader(current["name"])
    st.write(f"歌手: {current['singer']}")
    st.write(f"时长: {current['duration']}")

    # 切换按钮
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.button("◀️ 上一首", on_click=switch_song, args=(-1,), use_container_width=True)
    with btn_col2:
        st.button("▶️ 下一首", on_click=switch_song, args=(1,), use_container_width=True)

# 核心：添加实际的音频播放组件（Streamlit原生）
st.subheader("播放区")
st.audio(
    data=current["audio_url"],  # 音频文件链接
    format="audio/ogg",         # 对应音频格式（mp3写audio/mp3，ogg写audio/ogg）
    start_time=0                # 起始播放时间
)



# 简化的播放控制说明
st.caption("🎧 提示：直接使用上方原生音频控件播放/暂停/调节音量")
