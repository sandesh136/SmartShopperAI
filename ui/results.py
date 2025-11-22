import streamlit as st

def display_recommendations(results_text: str):
    st.header("Recommended Products and Info")
    # Directly display the output text from Gemini, which can include clickable links and citations
    st.markdown(results_text, unsafe_allow_html=True)
