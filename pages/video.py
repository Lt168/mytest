# 导入streamlit库，用于快速构建Web应用
import streamlit as st

# 配置页面基础信息：设置浏览器标签页的标题和图标
st.set_page_config(page_title="小猪佩奇", page_icon="🐷")

# 页面顶部：渲染剧集核心信息栏（使用HTML自定义样式）
st.markdown("""
    <div style='padding: 12px; border-bottom: 1px solid #eee; margin-bottom: 15px;'>
        <!-- 主标题：设置36px大号字体+加粗，视觉上突出显示 -->
        <h2 style='margin: 0; font-size: 36px; font-weight: bold;'>小猪佩奇 第一季</h2>
        <!-- 基础信息行：字号16px，灰色字体，包含中英文/地区/年份/总集数 -->
        <p style='margin: 5px 0; color: #666; font-size: 16px;'>
            <span>英文名称：Peppa Pig Season 1</span> · 
            <span>地区：英国</span> · 
            <span>年份：2025</span> · 
            <span>总集数：52集</span>
        </p>
        <!-- 配音演员行：字号16px，灰色字体，列出主要配音演员及对应角色 -->
        <p style='margin: 5px 0; color: #666; font-size: 16px;'>
            <span>主要配音：</span>
            海莉·伯德（Peppa）、莫温娜·班克斯（Mummy Pig）、理查德·赖丁斯（Daddy Pig）、奥利维娅·科尔曼（Mummy Rabbit）
        </p>
    </div>
""", unsafe_allow_html=True)  # 允许渲染HTML代码，实现自定义样式

# 定义视频列表：包含每集的播放链接、标题、剧情介绍
video_arr = [
    {
        # 第1集视频播放链接
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/36/87/1418068736/1418068736_u1-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=hw&uipk=5&oi=771356656&platform=html5&mid=0&trid=9d1215f173454230a80fca0c0cba63ch&deadline=1765766356&gen=playurlv3&nbs=1&upsig=a773432444e5878d0c299f5429cbcea0&uparams=e,os,og,uipk,oi,platform,mid,trid,deadline,gen,nbs&bvc=vod&nettype=0&bw=498073&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        # 第1集标题
        'title': '第1集：泥坑',
        # 第1集剧情介绍
        'intro': '佩奇和乔治最喜欢在泥坑里跳来跳去，猪妈妈提醒他们要穿上雨靴才能玩。佩奇带着乔治一起开心地跳泥坑，猪爸爸也忍不住加入了孩子们的行列，一家人都玩得不亦乐乎。'
    },{
        # 第2集视频播放链接
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/00/74/32531547400/32531547400-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=19c59b1df6394f028a0aedd16e52ee1h&mid=0&deadline=1765766636&nbs=1&platform=html5&gen=playurlv3&os=cosovbv&og=hw&oi=771356656&uipk=5&upsig=9424b470597aaf6e94e2a2f93492046b&uparams=e,trid,mid,deadline,nbs,platform,gen,os,og,oi,uipk&bvc=vod&nettype=0&bw=722510&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
        # 第2集标题
        'title': '第2集：恐龙先生弄丢了',
        # 第2集剧情介绍
        'intro': '乔治最喜欢的玩具是恐龙先生，可是他不小心把恐龙先生弄丢了。佩奇帮乔治一起找，找遍了花园、客厅都没找到，最后猪爸爸在自己的报纸下面发现了恐龙先生，乔治开心极了。'
    },{
        # 第3集视频播放链接
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/49/54/34340405449/34340405449-1-192.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&trid=83c30b8ce5104fe6892780ba2d76345h&deadline=1765766678&platform=html5&mid=0&os=cosovbv&og=ali&uipk=5&oi=771356656&gen=playurlv3&upsig=c3bb0d7e4810093d5517ba2df752ca55&uparams=e,nbs,trid,deadline,platform,mid,os,og,uipk,oi,gen&bvc=vod&nettype=0&bw=853915&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        # 第3集标题
        'title': '第3集：最好的朋友',
        # 第3集剧情介绍
        'intro': '佩奇的好朋友小羊苏西来家里玩，她们一起玩过家家，佩奇扮演妈妈，苏西扮演爸爸，还一起喝茶、跳泥坑。乔治想加入她们的游戏，一开始被拒绝了，最后佩奇和苏西还是带着乔治一起开心玩耍。'
    }
]

# 初始化会话状态：判断是否存在播放索引，不存在则设为0（默认播放第1集）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 获取当前播放集的信息：根据会话状态的索引，从视频列表中取出对应集的数据
current_video = video_arr[st.session_state['ind']]

# 显示当前播放集的标题：使用subheader组件，样式为二级标题
st.subheader(current_video['title'])

# 显示当前播放集的剧情介绍：添加图标前缀，提升视觉效果
st.write(f"📝 剧情介绍：{current_video['intro']}")

# 播放当前选中的视频：自动播放，加载对应集的视频链接
st.video(current_video['url'], autoplay=True)

# 定义切换集数的函数：接收集数索引，更新会话状态中的播放索引
def play(i):
    st.session_state['ind'] = int(i)

# 创建列布局：根据视频列表长度创建等宽列，列间隙设为small（紧凑排列）
cols = st.columns(len(video_arr), gap="small")  

# 遍历列布局，为每一列添加集数切换按钮
for idx, col in enumerate(cols):
    # 进入当前列的上下文（Streamlit列布局必须通过with使用）
    with col:
        # 创建集数按钮
        st.button(
            f'第{idx + 1}集',  # 按钮显示文本（第1集/第2集/第3集）
            on_click=play,     # 点击按钮触发的函数
            args=(idx,),       # 传递给play函数的参数（集数索引）
            use_container_width=True,  # 按钮宽度占满列宽
            help=video_arr[idx]['title']  # 鼠标悬浮提示：显示该集完整标题
        )
