import streamlit as st

def render_cards(df):
    st.subheader("📦 레퍼런스 리스트")

    for _, row in df.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])

            with col1:
                if row.get("썸네일URL"):
                    st.image(row["썸네일URL"], width=120)
                else:
                    st.image("assets/placeholder.png", width=120)

            with col2:
                st.markdown(f"### {row['고객명']}")
                st.write(f"🏷 산업: {row['대분류']} / {row['중분류']}")
                st.write(f"🚗 모델: {row['모델명']}")

            with col3:
                if row.get("출처URL"):
                    st.link_button("🔗 상세보기", row["출처URL"])

            st.divider()