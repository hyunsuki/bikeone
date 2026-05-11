import streamlit as st

from modules.loader import load_data
from modules.filters import render_filters
from modules.charts import plot_industry_distribution, plot_model_distribution
from modules.ui_components import render_cards

# ----------------------
# CONFIG
# ----------------------
st.set_page_config(
    page_title="ATV/UTV 레퍼런스 대시보드",
    layout="wide"
)

st.title("🚜 ATV / UTV 레퍼런스 분석 대시보드")

# ----------------------
# LOAD DATA
# ----------------------
df = load_data("data/atv_utv.parquet")

# ----------------------
# FILTERS
# ----------------------
filtered_df = render_filters(df)

# ----------------------
# KPI
# ----------------------
col1, col2, col3 = st.columns(3)

col1.metric("총 레퍼런스", len(df))
col2.metric("필터 결과", len(filtered_df))
col3.metric("고객 수", filtered_df["고객명"].nunique())

st.divider()

# ----------------------
# CHARTS
# ----------------------
col1, col2 = st.columns(2)

with col1:
    plot_industry_distribution(filtered_df)

with col2:
    plot_model_distribution(filtered_df)

st.divider()

# ----------------------
# CARDS
# ----------------------
render_cards(filtered_df)