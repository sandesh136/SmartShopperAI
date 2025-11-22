import streamlit as st
from ui.home import show_home
import logging

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting SmartShopperAI application")
    st.set_page_config(page_title="SmartShopperAI", layout="wide")
    show_home()

if __name__ == "__main__":
    main()
