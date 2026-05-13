import plotly.express as px
import streamlit as st
import pandas as pd


def plot_industry_distribution(df):

    chart_df = (
        df["대분류"]
        .value_counts()
        .rename_axis("대분류")
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    fig = px.bar(
        chart_df,
        x="count",
        y="대분류",
        orientation="h",
        title="대분류별 납품 분포"
    )

    # 많은 건수가 위로 오도록
    fig.update_yaxes(categoryorder="total ascending")

    st.plotly_chart(fig, use_container_width=True)


def plot_model_distribution(df):

    chart_df = (
        df["모델명"]
        .fillna("UNKNOWN")
        .value_counts()
        .rename_axis("모델명")
        .reset_index(name="count")
    )

    # UNKNOWN 여부
    chart_df["is_unknown"] = chart_df["모델명"].eq("UNKNOWN")

    # UNKNOWN은 마지막
    chart_df = chart_df.sort_values(
        ["is_unknown", "count"],
        ascending=[True, False]
    )

    fig = px.bar(
        chart_df,
        x="count",
        y="모델명",
        orientation="h",
        title="모델별 납품 현황"
    )

    # 순서 강제 지정
    fig.update_yaxes(
        categoryorder="array",
        categoryarray=chart_df["모델명"][::-1].tolist()
    )

    st.plotly_chart(fig, use_container_width=True)
