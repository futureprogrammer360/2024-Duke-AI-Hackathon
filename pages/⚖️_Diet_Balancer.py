import random
from itertools import count

import streamlit as st

import api

index = count()

ai = api.AI()

st.set_page_config(
    page_title="Diet Balancer | NutriSync"
)

@st.dialog("👋 Tell us about yourself")
def bio_info():
    cols = st.columns(2)

    with cols[0]:
        name = st.text_input(
            "Name", value=st.session_state.bio_info["name"] if st.session_state.get("bio_info") else ""
        )
        weight = st.number_input(
            "Weight (pounds)", min_value=0, max_value=500,
            value=st.session_state.bio_info["weight"] if st.session_state.get("bio_info") else 150, step=5
        )

    with cols[1]:
        age = st.number_input(
            "Age", min_value=0, max_value=100, step=1,
            value=st.session_state.bio_info["age"] if st.session_state.get("bio_info") else 18
        )
        cols = st.columns(2)
        with cols[0]:
            height_ft = st.number_input(
                "Height (ft)", min_value=0, max_value=10, step=1,
                value=st.session_state.bio_info["height"] // 12 if st.session_state.get("bio_info") else 5
            )
        with cols[1]:
            height_in = st.number_input(
                "(in)", min_value=0, max_value=12, step=1,
                value=st.session_state.bio_info["height"] % 12 if st.session_state.get("bio_info") else 0
            )

    gender_options = ["Male", "Female", "Other"]
    gender = st.radio("Gender", gender_options, horizontal=True,
        index=gender_options.index(st.session_state.bio_info["gender"]) if st.session_state.get("bio_info") else 0
    )

    act_lvl_options = ["Low", "Medium", "High"]
    act_lvl = st.radio(
        "Activity level", act_lvl_options, horizontal=True,
        index=act_lvl_options.index(st.session_state.bio_info["act_lvl"]) if st.session_state.get("bio_info") else 0
    )

    cols = st.columns(2)
    with cols[0]:
        if st.button("Save"):
            st.session_state.bio_info = {
                "name": name,
                "age": age,
                "gender": gender,
                "height": height_ft * 12 + height_in,
                "weight": weight,
                "act_lvl": act_lvl
            }
            st.rerun()
    with cols[1]:
        if st.session_state.get("bio_info") and st.button("Reset"):
            del st.session_state.bio_info
            st.rerun()

st.header("⚖️ Diet Balancer")

if "bio_info" not in st.session_state:
    st.button("✏️ Add biometric profile", on_click=bio_info)
    try:
        bio_info()
    except st.errors.StreamlitAPIException:
        pass

else:
    st.sidebar.button("✏️ Edit biometric profile", on_click=bio_info)

    st.subheader("What have you eaten today?")

    num_food_items = st.sidebar.number_input("Number of food items", min_value=1, max_value=10)

    example_food_items = [
        "Ice cream",
        "Cheeseburger",
        "Pasta",
        "Omelette",
        "Mac and cheese",
        "Boiled potatoes"
    ]
    food_items = []

    for i in range(num_food_items):
        key = next(index)
        food = st.text_input(f"Food item {i + 1}", key=key)
        food_items.append(food)
        del st.session_state[key]

    if st.button("Get recommendations"):
        response = ai.main(
            st.session_state["bio_info"]["age"],
            st.session_state["bio_info"]["gender"],
            st.session_state["bio_info"]["weight"],
            st.session_state["bio_info"]["height"],
            st.session_state["bio_info"]["act_lvl"],
            food_items
        )
        st.write(response)
