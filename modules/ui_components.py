import streamlit as st
import pandas as pd
import re

def clean_image_url(url):
    if pd.isna(url):
        return None

    url = str(url).strip()

    # url(https://...) 형태 제거
    match = re.search(r"https?://[^\s)]+", url)
    if match:
        return match.group(0)

    # 그냥 http로 시작하면 그대로 사용
    if url.startswith("http"):
        return url

    return None


def render_cards(df):
    #st.subheader("📦 레퍼런스 리스트")
    st.markdown("#### 판매 리스트")

    for _, row in df.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])

            with col1:
                img_url = clean_image_url(row.get("썸네일URL"))

                if img_url:
                    st.image(img_url, width=120)
                else:
                    st.image("assets/placeholder.png", width=120)

            with col2:
                st.markdown(f"### {row['고객명']}")
                st.write(f"🏷 산업: {row['대분류']} / {row['중분류']}")
                st.write(f" 모델: {row['모델명']}")

            with col3:
                if pd.notna(row.get("출처URL")):
                    st.link_button("🔗 상세보기", row["출처URL"])

            st.divider()
