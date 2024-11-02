import streamlit as st
from openai import OpenAI
import api

ai = api.AI()
st.set_page_config(
    page_title = "Diet Advisor | NutriSync",
    page_icon = "💬"
)

st.title("💬 Diet Advisor")
st.subheader("Ask any questions you have about your diet!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

with st.chat_message("assistant"):
    st.write("How may I help you with your diet today?")

prompt = st.chat_input("I would like to plan a healthy lunch.")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)
        toAI = """You are a professional dietician answering the prompt given after the colon. 
                If the prompt is unrelated to nutrition, diets, or health, please politely answer that you 
                are unable to provide such information: """ + prompt
        ai.messages.append({"role": "user", "content": toAI})

    with st.chat_message("assistant"):
        response = ai.get_completion_openai(toAI)
        st.session_state.messages.append({"role": "assistant", "content": response})
        ai.messages.append({"role": "assistant", "content": response})
        st.write(response)

    