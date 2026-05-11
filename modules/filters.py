import streamlit as st

def render_filters(df):
    st.sidebar.header("🔎 필터")

    category = st.sidebar.multiselect(
        "카테고리",
        df["카테고리"].unique()
    )

    industry = st.sidebar.multiselect(
        "대분류",
        df["대분류"].unique()
    )

    model = st.sidebar.multiselect(
        "모델명",
        df["모델명"].unique()
    )

    keyword = st.sidebar.text_input("고객명 검색")

    filtered = df.copy()

    if category:
        filtered = filtered[filtered["카테고리"].isin(category)]

    if industry:
        filtered = filtered[filtered["대분류"].isin(industry)]

    if model:
        filtered = filtered[filtered["모델명"].isin(model)]

    if keyword:
        filtered = filtered[filtered["고객명"].str.contains(keyword)]

    return filtered