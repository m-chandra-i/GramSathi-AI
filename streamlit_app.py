import streamlit as st

st.title("🌾 GramSathi AI")

crop = st.text_input("Enter crop name")
district = st.text_input("Enter district")
issue = st.text_input("What is your issue?")

if st.button("Get Suggestions"):

    st.write("Crop:", crop)
    st.write("District:", district)
    st.write("Issue:", issue)

    crop = crop.lower()

    if crop == "wheat":
        st.success("Season: Rabi")
        st.success("Water requirement: Medium")

    elif crop == "rice":
        st.success("Season: Kharif")
        st.success("Water requirement: High")

    else:
        st.warning("Crop information not available yet")

    st.info("Weather integration coming soon")
    st.info("Government schemes coming soon")
