import streamlit as st

def main():
    st.title("Page 3: Incident Log \status")

    # Ensure we have the selected issue class from Page 2
    if "selected_issue" in st.session_state:
        issue_class = st.session_state.selected_issue

        # Mapping logic for team assignment and diagnosis action
        if issue_class == "Software application":
            assigned_team = "Software Support Team"
            diagnosis_action = "Reinstall the software and check for updates"
            resolution_email = "resolved@i.techsolutionuser"
        elif issue_class == "Networking":
            assigned_team = "Network Support Team"
            diagnosis_action = "Check router configurations and reset network"
            resolution_email = "resolved@dcdatauser"
        elif issue_class == "Domain issues":
            assigned_team = "Domain Support Team"
            diagnosis_action = "Verify domain settings and rejoin the network"
            resolution_email = "resolved@amouser"
        else:
            assigned_team = "General Support Team"
            diagnosis_action = "Perform general diagnostics and system checks"
            resolution_email = "resolved@generaluser"
    else:
        st.warning("Please complete the previous steps before proceeding.")
        return

    # Display pre-filled, read-only fields for assigned team and diagnosis action
    st.text_input("Assigned Team (Auto-filled):", value=assigned_team, disabled=True)
    st.text_area("Diagnosis Action (Auto-filled):", value=diagnosis_action, disabled=True)

    # Incident resolution status
    resolution_status = st.radio(
        "Was the incident resolved?",
        ["", "Resolved", "Escalate"],
        index=0
    )

    col1, col2 = st.columns([1, 1])

    # Navigation Buttons with Resolution Handling
    with col1:
        if st.button("Next"):
            if not resolution_status:
                st.error("Please indicate whether the incident was resolved before proceeding.")
            else:
                if resolution_status == "Resolved":
                    st.success(f"Incident resolved successfully. Resolution sent to {resolution_email}")
                    st.session_state.page = "page4"
                else:
                    st.warning("Incident escalated. Moving to escalation details.")
                    st.session_state.page = "page4"

    with col2:
        if st.button("Back"):
            st.session_state.page = "page2"
