import streamlit as st

def main():
    st.title("Final Page")

    st.success("Closed!")

    
    if st.button("Back to Home"):
        st.session_state.page = "home"  

if __name__ == "__main__":
    main()
