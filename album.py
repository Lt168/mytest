import streamlit as st
#修改标签页的文字和图标
st.set_page_config(page_title="相册",page_icon="🍊")
st.title("我的相🍊册")
if 'ind' not in st.session_state:
    st.session_state['ind']=0
images = [
    {
        'url': "https://joy.online.sh.cn/images_quote/attachement/jpg/site1/20221024/IMG0025116ac9cf61658066857.jpg",
        'text': '第一张'
    },  # 第一个字典（第一张图），结尾加逗号分隔
    {
        'url': "https://ts1.tc.mm.bing.net/th/id/OIP-C.sr6DZG_gwbdxCB4ERTW24QHaJ4?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
        'text': '第二张'
    },  # 第二个字典（第二张图）
    {
        'url': "https://n.sinaimg.cn/sinakd10112/120/w1080h1440/20220407/9f10-83195c1b0ea0529c3fc0c77182c763e3.jpg",
        'text': '第三张'
    }  # 第三个字典（第三张图），最后一个元素末尾逗号可加可不加
]

# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)

# 分列容器 课本110页
cl1, cl2 = st.columns(2)
#cl1, cl2 = st.columns((1, 21))
with cl1:
    st.button("上一张", on_click=nextImg, use_container_width=True)
with cl2:
    # 按钮 课本73页
    st.button("下一张", on_click=nextImg, use_container_width=True)
    
