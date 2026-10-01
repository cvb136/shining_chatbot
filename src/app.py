"""Streamlit layout for the Shining vehicle assistant.

Run with: streamlit run src/app.py
"""

import streamlit as st


st.set_page_config(
    page_title="Shining · 내 차 사용 가이드",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.html(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root { color-scheme: light; }
    html, body, [class*="css"], .stApp, button, input, textarea {
        font-family: 'Noto Sans KR', sans-serif;
    }
    .stApp { background: #fbfdff; color: #172b4d; }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] {
        background: #f0f5fc;
        border-right: 1px solid #dce6f3;
    }
    /* Keep the collapse control out of the content spacing calculation. */
    [data-testid="stSidebarContent"] { padding-top: 0; }
    [data-testid="stSidebarHeader"] {
        position: absolute; top: 12px; right: 12px; left: 12px;
        padding: 0; background: transparent;
    }
    [data-testid="stSidebarUserContent"] { padding-top: 70px; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] { color: #172b4d; }
    [data-testid="stSidebar"] hr { border-color: #dce6f3; }
    .brand { color: #172b4d; font-size: 25px; font-weight: 800; letter-spacing: -.8px; }
    .brand span { color: #3977ce; padding-right: 9px; }
    .brand-caption { color: #61748f; font-size: 12px; margin: 5px 0 42px; }
    .nav-item {
        background: #dfebfc; border-radius: 12px; padding: 15px 17px;
        color: #245da6; font-size: 14px; font-weight: 600;
    }
    .sidebar-note { color: #61748f; font-size: 12px; line-height: 1.9; margin-top: 22px; }
    .selection-label { color: #61748f; font-size: 11px; margin: 30px 0 8px; }
    .selection-value { font-size: 15px; font-weight: 600; color: #244a7c; }
    .stMainBlockContainer {
        max-width: 1120px; padding: 70px 3.5rem 8rem;
    }
    .stApp h1.welcome { color: #172b4d; padding: 0; font-size: clamp(26px, 3vw, 38px); font-weight: 700;
        line-height: 1.5; letter-spacing: -1.4px; margin: 0; }
    .intro { color: #61748f; font-size: 14px; line-height: 1.8; margin-top: 16px; }
    .section-label { color: #61748f; font-size: 12px; margin: 48px 0 14px; }
    .st-key-vehicle_cards [data-testid="stButton"] button {
        width: 100%; min-height: 174px; border-radius: 18px;
        border: 1px solid #dce6f3; background: #f1f6fd; color: #345780;
        box-shadow: 0 4px 14px #172b4d03; transition: all .18s ease;
        display: flex; flex-direction: column; gap: 18px;
    }
    .st-key-vehicle_cards [data-testid="stButton"] button p {
        font-size: 17px; font-weight: 600; letter-spacing: -.5px;
    }
    .st-key-vehicle_cards [data-testid="stButton"] button:hover {
        border-color: #7fa8e5; background: #e7f0ff; transform: translateY(-3px);
    }
    .st-key-vehicle_cards [data-testid="stButton"] button[kind="primary"] {
        background: #dfebff; border: 2px solid #3977ce; color: #245da6;
    }
    .st-key-vehicle_cards [data-testid="stButton"] button:focus-visible {
        outline: 3px solid #a9c7f4; outline-offset: 3px;
    }
    .hint { color: #61748f; font-size: 12px; margin: 16px 0 32px; }
    [data-testid="stBottom"], [data-testid="stBottom"] > div {
        background: #fbfdff;
    }
    [data-testid="stBottomBlockContainer"] {
        max-width: 1120px; padding: 1rem 3.5rem 2.5rem;
    }
    [data-testid="stChatInput"] {
        background: #fff; border: 1px solid #cbdcf2;
        border-radius: 24px; box-shadow: 0 6px 24px #172b4d06;
    }
    [data-testid="stChatInput"] > div { background: #fff !important; border-radius: inherit; }
    /* BaseWeb's inner textarea wrapper also inherits the active Streamlit theme. */
    [data-testid="stChatInput"] [data-baseweb="textarea"],
    [data-testid="stChatInput"] [data-baseweb="base-input"],
    [data-testid="stChatInput"] textarea {
        background-color: #fff !important;
        color: #172b4d !important;
        -webkit-text-fill-color: #172b4d;
        caret-color: #2563b9;
    }
    [data-testid="stChatInput"] textarea::placeholder {
        color: #61748f !important; -webkit-text-fill-color: #61748f; opacity: 1;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: #3977ce; box-shadow: 0 0 0 3px #3977ce1a;
    }
    [data-testid="stChatInput"] button {
        background: #3977ce !important; color: #fff !important; border-radius: 12px;
    }
    [data-testid="stChatInput"] button:hover { background: #245da6 !important; }
    [data-testid="stChatInput"] button:disabled {
        background: #e0eafa !important; color: #6c84a5 !important; opacity: 1;
    }
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] { color: #172b4d; }
    .stApp [data-testid="stCaptionContainer"] { color: #61748f; }
    [data-testid="stChatMessage"] { background: #eef5ff; border-radius: 16px; }
    @media (max-width: 760px) {
        .stMainBlockContainer { padding: 70px 1.3rem 7rem; }
        [data-testid="stBottomBlockContainer"] { padding: 1rem 1.3rem 1.5rem; }
        .section-label { margin-top: 30px; }
        .st-key-vehicle_cards [data-testid="stHorizontalBlock"] { flex-wrap: wrap; gap: 12px; }
        .st-key-vehicle_cards [data-testid="stColumn"] {
            flex: 1 1 calc(50% - 12px); min-width: calc(50% - 12px);
        }
        .st-key-vehicle_cards [data-testid="stButton"] button { min-height: 125px; }
    }
    </style>
    """,
)

VEHICLES = ("아이오닉", "싼타페", "쏘나타", "제네시스")
st.session_state.setdefault("selected_vehicle", None)
st.session_state.setdefault("messages", [])


def select_vehicle(vehicle: str) -> None:
    st.session_state.selected_vehicle = vehicle


with st.sidebar:
    st.markdown('<div class="brand"><span>✦</span>shining</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-caption">당신의 일상에 더 가까운 자동차 가이드</div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">제품 사용 문의하기 <span style="float:right">↗</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-note">내 차의 기능부터 사용 방법까지,<br>궁금했던 내용을 편하게 물어보세요.</div>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="selection-label">선택한 차량</div>', unsafe_allow_html=True)
    selected = st.session_state.selected_vehicle or "차량을 선택해주세요"
    st.markdown(f'<div class="selection-value">{selected}</div>', unsafe_allow_html=True)

st.markdown('<h1 class="welcome">안녕하세요!<br>보유하고 있는 자동차를 선택해주세요.</h1>', unsafe_allow_html=True)
st.markdown('<p class="intro">내 차에 꼭 맞는 안내, 작은 궁금증부터 함께 해결해요.</p>', unsafe_allow_html=True)
st.markdown('<div class="section-label">어떤 차량을 이용하고 계신가요?</div>', unsafe_allow_html=True)

with st.container(key="vehicle_cards"):
    for column, vehicle in zip(st.columns(4, gap="medium"), VEHICLES):
        with column:
            is_selected = st.session_state.selected_vehicle == vehicle
            st.button(
                vehicle,
                key=f"vehicle_{vehicle}",
                icon=":material/check_circle:" if is_selected else ":material/directions_car:",
                type="primary" if is_selected else "secondary",
                width="stretch",
                on_click=select_vehicle,
                args=(vehicle,),
            )

st.markdown('<p class="hint">차량은 언제든 다시 선택할 수 있어요.</p>', unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message("user"):
        st.caption(message["vehicle"])
        st.write(message["content"])

if st.session_state.messages:
    st.caption("현재는 화면 미리보기입니다. 답변 기능은 추후 연결될 예정이에요.")

prompt = st.chat_input(
    "궁금한 점을 말씀해주세요!" if st.session_state.selected_vehicle else "차량을 선택한 후 궁금한 점을 말씀해주세요!",
    disabled=st.session_state.selected_vehicle is None,
)
if prompt:
    st.session_state.messages.append(
        {"vehicle": st.session_state.selected_vehicle, "content": prompt}
    )
    st.rerun()
