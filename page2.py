import streamlit as st

def main():
    st.title("Incident Classification")

    incident_class = st.selectbox("Incident Class:", [
        "Domain issues",
        "Printing issues",
        "Operating system",
        "Networking",
        "Domain issues",
        "Software application"
    ])

    priority = st.selectbox("Incident Priority:", [
        "",
        "Low",
        "Medium",
        "High"
    ])

    next_button_clicked = st.button("Next")

    if next_button_clicked:
        if incident_class == "" or priority == "":
            st.error("Please select both Incident Class and Priority before proceeding.")
        else:
            st.session_state.page = "page3"  
