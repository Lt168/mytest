# 导入streamlit库，用于快速构建交互式Web应用
import streamlit as st

# 页面配置：设置页面基础属性，打造猫咪主题的窄布局页面
st.set_page_config(
    page_title="小猫咪的数字档案",  # 浏览器标签页标题
    layout="centered",  # 页面布局：居中布局
    initial_sidebar_state="collapsed",  # 初始侧边栏状态：折叠
    page_icon="🐱"  # 页面图标：猫咪表情
)

# 自定义CSS样式：通过markdown注入CSS，实现50%宽度+猫咪风格美化
st.markdown("""
    <style>
    /* 核心样式：设置页面整体宽度为50%，居中显示，配置猫咪主题背景色和文字色 */
    .stApp {
        width: 50% !important;  /* 强制设置页面宽度为50% */
        margin: 0 auto !important; /* 上下边距0，左右自动（实现居中） */
        background-color: #fef7fb; /* 浅粉色背景，营造温馨感 */
        color: #5a4b60; /* 深紫色文字，柔和不刺眼 */
        overflow: hidden !important; /* 隐藏溢出内容，避免滚动条 */
    }
    /* 内容容器适配：填满50%宽度的父容器，压缩内边距 */
    .main .block-container {
        max-width: 100% !important;  /* 内容宽度填满父容器 */
        width: 100% !important;
        padding-top: 1rem !important; /* 顶部内边距1rem，紧凑布局 */
        padding-bottom: 1rem !important; /* 底部内边距1rem */
        padding-left: 0.5rem !important; /* 左侧内边距0.5rem */
        padding-right: 0.5rem !important; /* 右侧内边距0.5rem */
    }
    /* 压缩标题和段落的间距，减少空白 */
    h1, h2, h3, p {
        margin-top: 0.3rem !important; /* 上边距0.3rem */
        margin-bottom: 0.3rem !important; /* 下边距0.3rem */
    }
    /* 自定义title类样式：粉色系标题，卡通字体，文字阴影 */
    .title {
        color: #e86b9c; /* 玫粉色文字 */
        text-shadow: 0 0 3px #fcc8d1; /* 浅粉色文字阴影，增加层次感 */
        font-family: "Comic Sans MS", cursive; /* 卡通字体，适配猫咪主题 */
        font-size: 1.2rem !important; /* 字体大小1.2rem */
    }
    /* 自定义header类样式：紫色系子标题，卡通字体 */
    .header {
        color: #8b5cf6; /* 紫蓝色文字 */
        text-shadow: 0 0 3px #d8b4fe; /* 浅紫色文字阴影 */
        font-family: "Comic Sans MS", cursive; /* 卡通字体 */
        font-size: 1rem !important; /* 字体大小1rem */
    }
    /* 缩小Metric组件尺寸，适配紧凑布局 */
    .stMetric {
        padding: 0.2rem !important; /* 内边距0.2rem */
        font-size: 0.8rem !important; /* 整体字体大小0.8rem */
    }
    /* Metric组件标签样式：玫红色，加粗，小字号 */
    .metric-label {
        color: #d946ef !important; /* 玫紫色文字 */
        font-weight: bold; /* 加粗 */
        font-size: 0.7rem !important; /* 字体大小0.7rem */
    }
    /* Metric组件数值样式：绿色，文字阴影，略大字号 */
    .metric-value {
        color: #10b981 !important; /* 青绿色文字 */
        text-shadow: 0 0 2px #a7f3d0; /* 浅绿色阴影 */
        font-size: 0.9rem !important; /* 字体大小0.9rem */
    }
    /* Metric组件变化值样式：橙色，小字号 */
    .stMetricDelta {
        color: #f59e0b !important; /* 橙黄色文字 */
        font-size: 0.6rem !important; /* 字体大小0.6rem */
    }
    /* 表格样式：白色背景，粉色边框，圆角，小字号 */
    .stTable {
        background-color: #ffffff; /* 白色背景 */
        border: 1px solid #f9a8d4; /* 浅粉色边框 */
        border-radius: 8px; /* 8px圆角，柔和边角 */
        font-size: 0.75rem !important; /* 字体大小0.75rem */
    }
    /* 代码块样式：浅紫色背景，紫蓝色边框，圆角，小字号 */
    .stCode {
        background-color: #faf5ff; /* 浅紫粉色背景 */
        border: 1px solid #c4b5fd; /* 紫蓝色边框 */
        border-radius: 6px; /* 6px圆角 */
        font-size: 0.7rem !important; /* 字体大小0.7rem */
        padding: 0.5rem !important; /* 内边距0.5rem */
    }
    /* 进度条样式：缩小高度，粉色进度条 */
    .stProgress > div {
        height: 8px !important; /* 进度条高度8px */
    }
    .stProgress > div > div {
        background-color: #f472b6 !important; /* 粉色进度条颜色 */
    }
    /* 列布局样式：缩小列之间的间距 */
    .stColumns {
        gap: 0.2rem !important; /* 列间距0.2rem */
    }
    /* 说明文字样式：小字号，压缩上下边距 */
    .stCaption {
        font-size: 0.7rem !important; /* 字体大小0.7rem */
        margin-top: 0.2rem !important; /* 上边距0.2rem */
        margin-bottom: 0.2rem !important; /* 下边距0.2rem */
    }
    </style>
""", unsafe_allow_html=True)  # 允许使用不安全的HTML（自定义样式需要）


# ---------- 标题区域 ----------
# 设置页面主标题，anchor=False禁用锚点链接（避免标题出现跳转图标）
st.title("🐱 小猫咪的数字档案", anchor=False)
# 插入自定义样式的子标题（基础信息），使用unsafe_allow_html启用HTML样式
st.markdown('<p class="title">🐾 基础信息</p>', unsafe_allow_html=True)

# 基础信息展示：使用HTML格式化文字，不同状态用不同颜色标注
st.markdown("""
    猫咪ID: CAT-2025-001<br>  <!-- 换行符 -->
    领养时间: 2025-09-01 | 状态: <span style="color:#10b981">活力满满</span><br>  <!-- 绿色状态文字 -->
    当前徽章: <span style="color:#f59e0b">干饭·小能手</span>  <!-- 橙色徽章文字 -->
""", unsafe_allow_html=True)  # 允许HTML渲染


# ---------- 技能矩阵 ----------
# 插入自定义样式的子标题（技能矩阵）
st.markdown('<p class="header">🐱 技能矩阵</p>', unsafe_allow_html=True)
# 创建3列布局，用于并排展示Metric组件
col1, col2, col3 = st.columns(3)

# 第一列：展示抓老鼠技能的Metric组件
with col1:
    st.metric(label="抓老鼠", value="95%", delta="+3%")  # label=标签，value=数值，delta=变化值
# 第二列：展示撒娇技能的Metric组件
with col2:
    st.metric(label="撒娇", value="87%", delta="-2%")
# 第三列：展示拆家技能的Metric组件
with col3:
    st.metric(label="拆家", value="68%", delta="-10%")

# 添加进度条说明文字（caption）
st.caption("🐟 干饭进度条")
# 展示进度条，80%进度（取值范围0-1，80%即0.8）
st.progress(80)


# ---------- 任务日志 ----------
# 插入自定义样式的子标题（猫咪日常）
st.markdown('<p class="header">📋 猫咪日常</p>', unsafe_allow_html=True)
# 定义任务日志数据：列表嵌套字典，每行为一条日志
task_data = [
    {"日期": "2025-10-01", "任务": "巡视房间", "状态": "✅", "难度": "★"},
    {"日期": "2025-10-12", "任务": "打翻水杯", "状态": "✅", "难度": "★★★"},
    {"日期": "2025-10-15", "任务": "陪睡", "状态": "❌", "难度": "★"}
]
# 展示表格，自动将字典列表转换为表格形式
st.table(task_data)


# ---------- 最新代码成果 ----------
# 插入自定义样式的子标题（猫咪代码）
st.markdown('<p class="header">🐱 猫咪代码</p>', unsafe_allow_html=True)
# 定义Python代码字符串，模拟猫咪抓老鼠的逻辑
code = '''def catch_mouse(pos):
    if pos == "沙发下":
        meow()
        return "🐭 抓到啦！"
    else:
        nap()
        return "😴 先睡~"

def meow(): print("喵呜~")
def nap(): print("呼噜~")
'''
# 展示代码块，指定语言为Python，实现语法高亮
st.code(code, language="python")


# ---------- 系统日志 ----------
# 插入猫咪日记/总结/目标/状态信息，使用不同颜色区分不同类型的信息
st.markdown("""
    <br>  <!-- 换行符，增加空白行 -->
    <p style="font-size:0.8rem; color:#e86b9c">【日记】2025年的小鱼干超好吃！</p>  <!-- 玫粉色日记文字 -->
    <p style="font-size:0.8rem; color:#8b5cf6">【总结】拆家3次 | 撒娇8次</p>  <!-- 紫蓝色总结文字 -->
    <p style="font-size:0.8rem; color:#f59e0b">【目标】2025年偷喝更多牛奶🥛</p>  <!-- 橙黄色目标文字 -->
    <p style="font-size:0.8rem; color:#10b981">状态: 吃饱喝足 | 心情: 超开心😺</p>  <!-- 青绿色状态文字 -->
""", unsafe_allow_html=True)  # 允许HTML渲染
