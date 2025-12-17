import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------- 1. 数据读取函数 --------------------------
def get_dataframe_from_excel():
    file_path = "C:\\Users\\712\\Desktop\\（商场销售数据）supermarket_sales.xlsx"
    try:
        df = pd.read_excel(
            file_path,
            sheet_name="销售数据",
            skiprows=1,
            index_col="订单号"
        )
        df["小时数"] = pd.to_datetime(df["时间"], format="%H:%M:%S", errors="coerce").dt.hour
        df = df.dropna(subset=["小时数", "总价", "评分"])
        return df
    except Exception as e:
        st.error(f"数据读取失败：{str(e)}")
        st.stop()

# -------------------------- 2. 侧边栏筛选函数（核心修改：无选择时匹配全部） --------------------------
def add_sidebar_func(df):
    with st.sidebar:
        st.header("请筛选数据:")
        
        # 城市筛选：无选择时默认全部，选择后仅展示选中项
        city_options = df["城市"].unique()
        selected_city = st.multiselect("请选择城市:", city_options)
        # 若未选择城市，自动匹配全部城市
        if not selected_city:
            selected_city = city_options
        
        # 顾客类型筛选：无选择时默认全部
        cust_options = df["顾客类型"].unique()
        selected_cust = st.multiselect("请选择顾客类型:", cust_options)
        if not selected_cust:
            selected_cust = cust_options
        
        # 性别筛选：无选择时默认全部
        gender_options = df["性别"].unique()
        selected_gender = st.multiselect("请选择性别", gender_options)
        if not selected_gender:
            selected_gender = gender_options
        
        # 应用筛选（无选择时自动取全部）
        df_filtered = df[
            (df["城市"].isin(selected_city)) &
            (df["顾客类型"].isin(selected_cust)) &
            (df["性别"].isin(selected_gender))
        ]
    return df_filtered

# -------------------------- 3. 图表生成函数（匹配原样式） --------------------------
def create_hour_chart(df):
    hour_sales = df.groupby("小时数")["总价"].sum().reset_index()
    fig = px.bar(
        hour_sales,
        x="小时数",
        y="总价",
        title="<b>按小时数划分的销售额</b>",
        color_discrete_sequence=["#1f77b4"],
        labels={"总价": "总价", "小时数": "小时数"}
    )
    fig.update_layout(showlegend=False, font_family="SimHei", height=400)
    return fig

def create_product_chart(df):
    product_sales = df.groupby("产品类型")["总价"].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(
        product_sales,
        x="总价",
        y="产品类型",
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
        color_discrete_sequence=["#1f77b4"],
        labels={"总价": "总价", "产品类型": "产品类型"}
    )
    fig.update_layout(showlegend=False, font_family="SimHei", height=400)
    return fig

# -------------------------- 4. 主界面渲染 --------------------------
def render_main_dashboard(df):
    # 核心指标计算
    total_sales = int(df["总价"].sum())
    avg_rating = round(df["评分"].mean(), 1)
    total_orders = df.index.nunique()
    avg_per_order = round(total_sales / total_orders, 2) if total_orders > 0 else 0

    # 页面标题
    st.title("销售仪表板")
    st.divider()

    # 核心指标展示
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.subheader("总销售额:")
        st.markdown(f"<h2>RMB ¥{total_sales:,}</h2>", unsafe_allow_html=True)
    with col2:
        st.subheader("顾客评分的平均值:")
        star_display = "⭐" * int(round(avg_rating, 0))
        st.markdown(f"<h2>{avg_rating} {star_display}</h2>", unsafe_allow_html=True)
    with col3:
        st.subheader("每单的平均销售额:")
        st.markdown(f"<h2>RMB ¥{avg_per_order}</h2>", unsafe_allow_html=True)

    st.divider()

    # 图表展示
    chart_col1, chart_col2 = st.columns(2, gap="large")
    with chart_col1:
        st.plotly_chart(create_hour_chart(df), use_container_width=True)
    with chart_col2:
        st.plotly_chart(create_product_chart(df), use_container_width=True)

# -------------------------- 5. 应用入口 --------------------------
def run_sales_dashboard():
    st.set_page_config(page_title="销售仪表板", layout="wide")
    sales_df = get_dataframe_from_excel()
    filtered_df = add_sidebar_func(sales_df)
    render_main_dashboard(filtered_df)

if __name__ == "__main__":
    run_sales_dashboard()
