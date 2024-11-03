import streamlit as st
from openai import OpenAI
import api

ai = api.AI()
st.set_page_config(
    page_title = "Diet Advisor | NutriSync",
    page_icon = "💬"
)



@st.dialog("👋 Choose your advising style")
def style_info():
    style = st.selectbox(label="Style of Advising", options = ["Regular", "Humorous", "Sympathetic", "Harsh"])
    if st.button("Save"):
            st.session_state.style_info = {
                "style": style
            }
            st.rerun()


cols = st.columns(2)
with cols[0]:
        st.title("💬 Diet Advisor")

with cols[1]:
        if "style_info" not in st.session_state:
            #st.button("✏️ Select advising style", on_click= style_info)
            try:
                style_info()
            except st.errors.StreamlitAPIException:
                pass
        else:
            st.button("✏️ Edit advising style", on_click= style_info)
            st.text(body = "Your current style: "+st.session_state.style_info["style"])

st.subheader("Ask any questions you have about your diet!")    

if "messages" not in st.session_state:
    st.session_state.messages = []





with st.chat_message("assistant"):
    st.write("How may I help you with your diet today?")

prompt = st.chat_input("I would like to plan a healthy lunch.")

if prompt:

    #st.session_state.messages.append({"role": "user", "content": prompt})
    ai.setPrompt(style = st.session_state.style_info["style"])

    with st.chat_message("user"):
        st.write(prompt)
        #toAI = """You are a professional dietician answering the prompt given after the colon. 
         #       If the prompt is unrelated to nutrition, diets, or health, please politely answer that you 
          #      are unable to provide such information: """ + prompt
        ai.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = ai.get_completion_openai(prompt)
        #st.session_state.messages.append({"role": "assistant", "content": response})
        ai.messages.append({"role": "assistant", "content": response})
        st.write(response)

    