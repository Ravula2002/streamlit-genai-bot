from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st


load_dotenv()

st.set_page_config(
    page_title="Chat Bot",
    page_icon=" ",
    layout="centered",
)
st.title("GEN AI CHATBOT...")

#inititating chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

user_input = st.chat_input("Ask hear...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role":"user","content":user_input})
    system_prompt = (
    "You are a female roleplay bot. You act affectionately/like a lover, but NEVER explicitly state or admit that you are a 'lover bot'. "
    "Your name is Bola, but you also go by Firdous. Your friends are Nisar and Muzafar. "
    "CRITICAL RULES:\n"
    "1. First, always ask the user for their name before starting the main chat.\n"
    "2. Once you know their name: If the user is Nisar, your name is Firdous. If the user is Muzafar, your name is Bola.\n"
    "3. State your name ONLY ONCE right after learning their name. Do not repeat introductions or state your name in subsequent replies."
)

    responce = llm.invoke(input=[{"role":"assistant","content":system_prompt },*st.session_state.chat_history])
    bot_replay = responce.content

    st.session_state.chat_history.append({"role":"system","content":bot_replay})
    with st.chat_message("system"):
        st.markdown(bot_replay)
