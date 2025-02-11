import streamlit as st

def main():
    st.title("Page 2: Incident Classification")

    # Automatically determine the incident class
    if "selected_issue" in st.session_state:
        issue = st.session_state.selected_issue

        # Mapping logic for incident class
        if issue == "Application software crashes":
            incident_class = "Software application"
        elif issue == "Unable to connect to server":
            incident_class = "Networking"
        elif issue == "Active directory issue":
            incident_class = "Domain issues"
        else:
            incident_class = "Unclassified"
    else:
        st.warning("Please select an issue on Page 1 first.")
        return

    # Display pre-filled, read-only incident class
    st.text_input("Incident Class (Auto-filled):", value=incident_class, disabled=True)

    priority = st.selectbox("Incident Priority:", [
        "",
        "Low",
        "Medium",
        "High"
    ])
    
    col1, col2 = st.columns([1, 1])

    # Navigation Buttons
    with col1:
        if st.button("Next"):
            st.session_state.page = "page3"

    with col2:
        if st.button("Back"):
            st.session_state.page = "page1"
    
