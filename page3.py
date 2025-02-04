import streamlit as st

def main():
    
    st.header("Diagnosis Activity")
    diagnosis_action = st.selectbox(
        "Select a diagnosis action:",
        [
            "Select an option",
            "Restart the software application",
            "Restart the system User’s session",
            "Restarting the printer",
            "Assigning IP Manually",
            "Restart network switches",
            "Installation of Microsoft Application",
            "Installation of JavaScript Plugins",
        ]
    )
    

    # Incident Escalation Section
    st.header("Incident Escalation")
    escalation_level = st.selectbox(
        "Select the escalation level:",
        ["",
         "2nd Level Support", 
         "3rd Level Support"],
    )

    st.header("Incident Resolution")
    st.write("Resolved with feedback sent to the following emails:")
    st.write("- **Amo@supportdesk**")
    st.write("- **Dcdata@supportdesk**")
    st.write("- **I-techsolution@supportdesk**")


    if st.button("Next"):
            if diagnosis_action == "Select an option" or escalation_level == "":
                st.error("Please fill all fields before proceeding.")
            else:
                st.success("Incident handling process completed successfully!")
                st.session_state.page = "home"

    