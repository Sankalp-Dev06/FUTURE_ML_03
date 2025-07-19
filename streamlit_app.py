import streamlit as st
from dialogflow_utils import detect_intent_texts
import uuid

st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬", layout="centered")

# --- CSS for Telegram-like look, vertical menu, and no white boxes ---
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100%;
        background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%) !important;
    }
    .tg-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #0088cc;
        margin-top: 32px;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    .vertical-menu {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        margin-bottom: 18px;
        margin-top: 0;
    }
    .vertical-chip-btn {
        background: #e5e5ea;
        color: #0088cc;
        border: none;
        border-radius: 12px;
        padding: 10px 0;
        font-size: 1rem;
        cursor: pointer;
        transition: background 0.2s;
        min-width: 220px;
        width: 100%;
        max-width: 320px;
        font-weight: 500;
        box-shadow: 0 1px 2px rgba(44,62,80,0.04);
        text-align: center;
    }
    .vertical-chip-btn:hover {
        background: #d0eaff;
        color: #005f8c;
    }
    .tg-bot-bubble, .tg-user-bubble {
        display: flex;
        align-items: flex-end;
        margin-bottom: 12px;
    }
    .tg-bot-bubble .bubble {
        background: #e5e5ea;
        color: #222;
        border-radius: 18px 18px 18px 0;
        padding: 12px 18px;
        box-shadow: 0 2px 8px rgba(44,62,80,0.06);
        max-width: 75%;
        font-size: 1.05rem;
        margin-left: 8px;
    }
    .tg-user-bubble {
        flex-direction: row-reverse;
    }
    .tg-user-bubble .bubble {
        background: #dcf8c6;
        color: #222;
        border-radius: 18px 18px 0 18px;
        padding: 12px 18px;
        box-shadow: 0 2px 8px rgba(44,62,80,0.06);
        max-width: 75%;
        font-size: 1.05rem;
        margin-right: 8px;
    }
    .tg-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #0088cc;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        font-weight: bold;
        font-size: 1.2rem;
        box-shadow: 0 2px 8px rgba(44,62,80,0.10);
    }
    .tg-input-bar {
        background: transparent !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
        margin-top: 18px;
        display: flex;
        justify-content: center;
        max-width: 420px;
        margin-left: auto;
        margin-right: auto;
    }
    .tg-input-inner {
        width: 100%;
        display: flex;
        gap: 8px;
    }
    @media (max-width: 600px) {
        .tg-input-bar {
            max-width: 100vw;
            border-radius: 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Persistent session ID for Dialogflow context ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- Title ---
st.markdown("""
    <div class='tg-title'>
        <span style="font-size:2.2rem;">💬</span> Customer Support Bot
    </div>
""", unsafe_allow_html=True)

# --- Vertical Menu of what the bot can do ---
MENU_OPTIONS = [
    "Track my order",
    "Return an item",
    "Shipping info",
    "Payment methods",
    "Contact support",
    "Refund status",
    "Product availability"
]

st.markdown("""
    <style>
    .vertical-menu {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        margin-bottom: 18px;
        margin-top: 0;
    }
    .vertical-chip-btn {
        background: #e5e5ea;
        color: #0088cc;
        border: none;
        border-radius: 12px;
        padding: 10px 0;
        font-size: 1rem;
        cursor: pointer;
        transition: background 0.2s;
        min-width: 220px;
        width: 100%;
        max-width: 320px;
        font-weight: 500;
        box-shadow: 0 1px 2px rgba(44,62,80,0.04);
        text-align: center;
    }
    .vertical-chip-btn:hover {
        background: #d0eaff;
        color: #005f8c;
    }
    </style>
""", unsafe_allow_html=True)

for option in MENU_OPTIONS:
    if st.button(option, key=f"menu_{option}", use_container_width=True):
        st.session_state.chat_history.append(("You", option))
        bot_response = detect_intent_texts(option, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", bot_response))

def submit():
    user_msg = st.session_state.get("user_input", "").strip()
    if user_msg:
        st.session_state.chat_history.append(("You", user_msg))
        bot_response = detect_intent_texts(user_msg, session_id=st.session_state.session_id)
        st.session_state.chat_history.append(("Bot", bot_response))
        st.session_state.user_input = ""

# --- Chat bubbles (no box) ---
if st.session_state.chat_history:
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(
                f"""<div class='tg-user-bubble'>
                    <div class='tg-avatar'>U</div>
                    <div class='bubble'>{message}</div>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown(
                f"""<div class='tg-bot-bubble'>
                    <div class='tg-avatar'>🤖</div>
                    <div class='bubble'>{message}</div>
                </div>""", unsafe_allow_html=True)
else:
    st.markdown(
        """
        <div style='text-align:center; color:#888; margin-top:32px;'>
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" width="70" style="opacity:0.7;"/><br>
            <span style='font-size:1.3rem; color:#0088cc; font-weight:700;'>Customer Support Bot</span><br>
            <span style='font-size:1.05rem;'>How can I help you today?</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Input bar always at the bottom, centered ---
st.markdown("""<div class='tg-input-bar'><div class='tg-input-inner'>""", unsafe_allow_html=True)
st.text_input(
    "Type your message and press Enter",
    key="user_input",
    label_visibility="collapsed",
    placeholder="Type your message...",
    on_change=submit
)
st.markdown("</div></div>", unsafe_allow_html=True) 