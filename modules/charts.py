import plotly.express as px
import streamlit as st

def plot_industry_distribution(df):
    fig = px.bar(
        df["대분류"].value_counts().reset_index(),
        x="count",
        y="대분류",
        orientation="h",
        title="대분류별 납품 분포"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_model_distribution(df):
    fig = px.bar(
        df["모델명"].value_counts().reset_index(),
        x="count",
        y="모델명",
        orientation="h",
        title="모델별 납품 현황"
    )
    st.plotly_chart(fig, use_container_width=True)