# SmartShopperAI

🛍️ AI-powered multi-agent e-commerce recommendation system using LangGraph and Streamlit, delivering personalized product suggestions with live web search and direct buy links.

## Setup

1. Clone the repo
2. Create and activate a Python virtual environment
3. Install dependencies:

pip install -r requirements.txt

text
4. Set environment variable `GEMINI_API_KEY` with your Google API key
5. Run the app:
streamlit run app.py

text

## Features

- Live web search powered by Google Gemini API with grounding tool
- Multi-agent orchestration (via LangGraph possible integration)
- Streamlit-based interactive UI for seamless shopping experience

## Project Structure

- `app.py`: Main Streamlit app entry
- `gemini_client`: Google Gemini API integration for search
- `ui`: Streamlit UI components
- `utils`: Helper utilities
