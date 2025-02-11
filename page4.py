import streamlit as st

def main():
    st.title("Page 4: Incident Escalation and Closure")

    # Ensure we have the selected team from Page 3
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue

        # Team resolution mapping based on escalation levels
        if issue_class == "Software application":
            resolution_team = "@i.techsolutionuser"
            escalation_status_options = ["In Progress", "Order Software"]
        elif issue_class == "Networking":
            resolution_team = "@dcdatauser"
            escalation_status_options = ["In Progress", "Waiting Approval"]
        elif issue_class == "Domain issues":
            resolution_team = "@amouser"
            escalation_status_options = ["In Progress", "Order System"]
        else:
            resolution_team = "@generaluser"
            escalation_status_options = ["In Progress", "Waiting Approval", "Order System"]

    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Escalation Status
    escalation_status = st.selectbox("Escalation Status:", [""] + escalation_status_options)

    # Incident resolution status
    resolution_status = st.radio(
        "Was the incident resolved?",
        ["", "Yes - Resolve", "No - Escalate Further"],
        index=0
    )

    # Show resolved team
    if resolution_status == "Yes - Resolve":
        st.success(f"Incident resolved successfully by {resolution_team}")

    # Incident closure action
    incident_closure = st.checkbox("Mark incident as closed")

    # Navigation Buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Next"):
            if not escalation_status:
                st.error("Please select an escalation status.")
            elif not resolution_status:
                st.error("Please indicate whether the incident was resolved.")
            elif resolution_status == "Yes - Resolve" and not incident_closure:
                st.error("Please mark the incident as closed before proceeding.")
            else:
                st.success("Incident escalation and resolution process complete.")
                st.session_state.page = "final_page"

    with col2:
        if st.button("Back"):
            st.session_state.page = "page3"
