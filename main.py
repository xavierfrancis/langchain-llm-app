import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("", "cat", "dog", "rabbit", "squirrel", "peacock"))
pet_color = st.sidebar.text_input(label="What is the color of your pet?", max_chars=15)

if animal_type and pet_color:
    response = lch.generate_pet_name(animal_type=animal_type, pet_color=pet_color)
    st.subheader("Suggested Names:")
    st.text(response)
else:
    st.info("Please select a pet and enter its color to get name suggestions.")

