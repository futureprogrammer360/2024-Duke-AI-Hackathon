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
    st.session_state.style_info = {
                "style": "Regular"
            }
    style = st.selectbox(label="Style of Advising", options = ["Regular", "Harsh","Humorous","Motivational","Philosophical", "Sympathetic"])
    if st.button("Save"):
            st.session_state.style_info = {
                "style": style
            }
            st.rerun()


st.title("💬 Diet Advisor")

st.subheader("Ask any diet questions!")    

if "style_info" not in st.session_state:
    st.sidebar.write("\n")
    st.sidebar.button("✏️ Select advising style", on_click= style_info)
    try:
        style_info()
    except st.errors.StreamlitAPIException:
        pass
else:
    cols = st.columns(2)
    st.sidebar.write("\n")
    with cols[0]:
        st.sidebar.button("✏️ Edit advising style", on_click= style_info)
    with cols[1]:
        #st.text(body = """Your current style: """+st.session_state.style_info["style"])
        name = st.session_state.style_info["style"]
        st.sidebar.markdown(f"<div style='text-align: center;display: flex; align-items: center; height: 30px;'>Your current style: {name}</div>", unsafe_allow_html=True)



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

    