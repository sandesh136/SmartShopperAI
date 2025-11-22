import streamlit as st
from gemini_client.gemini_search import run_gemini_search
import logging

logger = logging.getLogger(__name__)

COUNTRIES = ["United States", "Canada", "United Kingdom", "Germany", "France", "Australia", "India", "Japan"]
 
def show_home():
    st.title("🛍️ SmartShopperAI")
    st.subheader("Your AI-powered E-commerce Assistant")
    st.markdown("Tell me what you're looking for, and I'll find the best products, compare them, and provide you with purchase links tailored to your country.")
    
    st.sidebar.title("Chat Controls")
    # Add a button to the sidebar to start a new chat
    if st.sidebar.button("New Chat"):
        st.session_state.messages = []
        logger.info("Chat session reset by user.")
        st.rerun()
 
    # Add country selector to sidebar
    if 'country' not in st.session_state:
        st.session_state.country = "United States" # Default country

    st.session_state.country = st.sidebar.selectbox(
        "Select your country for localized search:",
        COUNTRIES,
        index=COUNTRIES.index(st.session_state.country)
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        logger.info("New chat session initialized.")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What are you shopping for today?"):
        logger.info(f"User input received: {prompt}")
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("Finding the best products for you..."):
            logger.info("Sending conversation history to Gemini agent.")
            # Pass the whole conversation history to the agent
            response = run_gemini_search(st.session_state.messages, st.session_state.country)
            logger.info("Received response from Gemini agent.")
            
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response, unsafe_allow_html=True)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
