import random
from itertools import count
import json

import streamlit as st

import api
import images

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

    allergies = st.text_input(
        "Any allergies?", placeholder="None",
        value=st.session_state.bio_info["allergies"] if st.session_state.get("bio_info") else ""
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
                "act_lvl": act_lvl,
                "allergies": allergies
            }
            st.rerun()
    with cols[1]:
        if st.session_state.get("bio_info") and st.button("Reset"):
            del st.session_state.bio_info
            st.rerun()

st.title("⚖️ Diet Balancer")

if "bio_info" not in st.session_state:
    st.button("✏️ Add biometric profile", on_click=bio_info)
    try:
        bio_info()
    except st.errors.StreamlitAPIException:
        pass

else:
    st.sidebar.button("✏️ Edit biometric profile", on_click=bio_info)

    col_1, col_2 = st.columns([0.7, 0.3], vertical_alignment="center")
    with col_1:
        st.subheader("What have you eaten today?")
    with col_2:
        num_food_items = st.number_input("Number of food items", min_value=1, max_value=10)

    food_items = []

    for i in range(num_food_items):
        key = next(index)
        food = st.text_input(f"Food item {i + 1}", key=key)
        food_items.append(food)
        del st.session_state[key]

    if st.button("Get insights and recommendations"):
        response = ai.main(
            st.session_state["bio_info"]["age"],
            st.session_state["bio_info"]["gender"],
            st.session_state["bio_info"]["weight"],
            st.session_state["bio_info"]["height"],
            st.session_state["bio_info"]["act_lvl"],
            st.session_state["bio_info"]["allergies"],
            food_items
        )
        response = response[response.find("{"):response.rfind("}") + 1]

        try:
            response_dict = json.loads(response)
        except json.decoder.JSONDecodeError:
            pass
        else:
            st.markdown("""
            <style>
            .stExpander summary span div p {
              font-size: 20px;
            }
            </style>
            """, unsafe_allow_html=True)

            summary = response_dict["summary"]
            recipe = response_dict["recipe"]
            nutrients = response_dict["nutrients"]

            # Summary and recommended meal
            with st.expander("Summary and recommended meal", expanded=True):
                st.write(summary)
                st.write(f"Here's a recommended meal you should try: **{recipe['name']}**")

                cols = st.columns(2)
                with cols[0]:
                    st.write("**Ingredients**:")
                    markdown = ""
                    for i, ingredient in enumerate(recipe["ingredients"]):
                        markdown += f"{i + 1}. {ingredient}\n"
                    st.markdown(markdown)
                with cols[1]:
                    image_url = images.get_image(recipe["name"])
                    st.image(image_url, caption=recipe["name"])

                st.write("**Instructions**:")
                markdown = ""
                for i, instruction in enumerate(recipe["instructions"]):
                    markdown += f"{i + 1}. {instruction}\n"
                st.markdown(markdown)

            # Nutrients
            for nutrient in nutrients.keys():
                nutrient_info = nutrients[nutrient]
                is_sufficient = nutrient_info["sufficient"]
                nutrient = nutrient.replace("_", " ").title()

                with st.expander(f"{'✅' if is_sufficient else '❌'} {nutrient}", expanded=False):
                    if is_sufficient:
                        st.write(f"You are getting enough {nutrient}. Good job!")

                        cols = st.columns(2)
                        with cols[0]:
                            st.write("Contributing Foods:")
                            markdown = ""
                            for food in nutrient_info["food_contributors"]:
                                markdown += f"- {food}\n"
                            st.markdown(markdown)

                        with cols[1]:
                            image_url = images.get_image(nutrient_info["food_contributors"][0])
                            st.image(image_url, caption=nutrient_info["food_contributors"][0])

                    else:
                        st.write(f"You are not getting sufficient quantities of {nutrient}.")

                        cols = st.columns(2)
                        with cols[0]:
                            st.write("Recommendations:")
                            markdown = ""
                            for food in nutrient_info["recommendations"]:
                                markdown += f"- {food}\n"
                            st.markdown(markdown)

                        with cols[1]:
                            image_url = images.get_image(nutrient_info["recommendations"][0])
                            st.image(image_url, caption=nutrient_info["recommendations"][0])
