import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path: str):
    df = pd.read_parquet(path)

    # 컬럼 정리
    df.columns = [c.strip() for c in df.columns]

    # 모델명 정리 (공백/특수문자 정리용)
    df["모델명"] = df["모델명"].fillna("UNKNOWN").astype(str)

    return df