import streamlit as st
from app.generator import generate_listing
st.set_page_config(page_title="Global Seller Copilot", layout="wide")

# --- 헤더 --- 
st.title("아마존/쇼피 판매왕")
st.caption("한국어 설명만 대충 적으세요. 미국/일본 쇼핑몰에 바로 올릴 수 있는 영어/일본어로 바꿔드립니다.")
st.divider()
 
col1, col2 = st.columns([1,1])

# --- 입력 섹션 (좌측) ---
with col1:
    st.subheader("상품 정보 입력")
    
    # 타겟 국가 선택
    market =st.selectbox(
        "어디에 파실 건가요?",
        ["Amazon US (미국) us", "Rakuten Japan (일본) jp"]
    )

    # 상품명
    p_name = st.text_input("상품명 (한글)", placeholder="예: 국산 들기름 300ml")

    # 특징
    p_features = st.text_area(
        "상품 특징 및 장점 (한국어)",
        height=200,
        placeholder="- 100% 국산 깨 사용\n- 저온 압착 방식이라 고소함\n- 선물용 패키지 있음\n- 오메가3 풍부"
    )

    generate_btn = st.button("글로벌 리스팅 생성", type="primary", width="stretch")

# --- 결과 섹션 (우측) ---
with col2:
    st.subheader("번역 및 최적화 결과")

    if generate_btn:
        if not p_name or not p_features:
            st.warning("상품명과 특징을 모두 입력해주세요!")
        else:
            with st.spinner(f"{market} 현지 마케터가 글을 쓰는 중입니다..."):
                result = generate_listing(p_name, p_features, market)

                if "error" in result:
                    st.error(result["error"])
                else:
                    # 결과 파싱
                    title = result.get("title", "")
                    bullets = result.get("bullets", [])
                    desc = result.get("description", "")
                    keywords = result.get("keywords", "")

                    # 상품 제목
                    st.success("**상품 제목 (Title)**")
                    st.code(title, language=None)

                    # 핵심 포인트
                    st.info("**핵심 포인트**")
                    for b in bullets:
                        st.markdown(f"- {b}")

                    # 상세 설명
                    with st.expander("상세 설명 보기", expanded=True):
                        st.write(desc)

                    # 검색 키워드
                    st.warning("**검색 키워드**")
                    st.code(keywords, language=None)

                    st.success("팁: 위 내용을 복사해서 셀러 센터에 바로 붙여넣으세요!")
    elif not generate_btn:
        st.info("👈 왼쪽에서 정보를 입력하고 버튼을 눌러보세요.")