import streamlit as st

st.set_page_config(
    page_title="Home | NutriSync"
)

st.title("Welcome to NutriSync!")


st.write("Use the Diet Balancer to supplement your diet with the help of LLMs!")

st.write("Use the Diet Advisor for general advice on your diet!")

st.subheader("About")
st.markdown(
     """Nutritional deficiency is one of America's greatest public health challenges.
     [According to the CDC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8735562/), 
     Only 12.3 and 10.0 percent of Americans are meeting recommended intake values for 
      fruits and vegetables respectivly. While people can get nutritional advice from 
      professionals, that can be unaffordable and inconvienient. NutriSync uses the 
      power of AI to provide free and personalized nutritional advice to the public."""
    )
st.write("Created by Logan Chu, Ethan Fazal, Ian Le, and Anric Ngan for the 2024 Duke AI Hackathon.")
