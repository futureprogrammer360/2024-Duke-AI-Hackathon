import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Diet Advisor | NutriSync"
)

st.title("Diet Advisor")


if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("How may I help you with  your diet today?")

prompt = st.chat_input("I would like to plan a healthy lunch.")
if prompt: 
    st.write("Prompt: {prompt}")
    st.session_state.messages.append({"role": "user", "content": prompt})
    