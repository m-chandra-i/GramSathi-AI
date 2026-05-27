import streamlit as st

st.title("🌾 GramSathi AI")

crop = st.text_input("Enter crop name")
district = st.text_input("Enter district")
issue = st.text_input("What is your issue?")

if st.button("Get Suggestions"):

    crop = crop.lower()
    issue = issue.lower()

    st.write("Crop:", crop)
    st.write("District:", district)

    if crop == "cotton":
        st.success("Season: Kharif")
        st.success("Water requirement: Medium")
        st.info("Cotton may be affected by bollworm pests")

    elif crop == "wheat":
        st.success("Season: Rabi")
        st.success("Water requirement: Medium")

    elif crop == "rice":
        st.success("Season: Kharif")
        st.success("Water requirement: High")

    else:
        st.warning("Crop data unavailable")

    if "pest" in issue:
        st.warning("Suggestion: Inspect crop leaves and use appropriate pest control methods")

    if "flood" in issue or "waterlogging" in issue:
        st.warning("Suggestion: Improve drainage and avoid standing water")

    if "weather" in issue:
        st.warning("Suggestion: Monitor weather alerts and irrigation schedule")
