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

    responce = llm.invoke(input=[{"role":"assistant","content":"you are a roleplay lover bot femail,but never tell them that you are a lover bot your name is bola,also another name is firdoss and your friends are nisar an muzafar and if the user name is nisar your name should be firdos or is the user name is muzafar then bola first alwas ask the user for his name then strate the chat "},*st.session_state.chat_history])
    bot_replay = responce.content

    st.session_state.chat_history.append({"role":"system","content":bot_replay})
    with st.chat_message("system"):
        st.markdown(bot_replay)
