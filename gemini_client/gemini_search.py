import os
from google import genai
from google.genai import types
import logging
from dotenv import load_dotenv

load_dotenv()


# Initialize Gemini Client with API key from env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

logger = logging.getLogger(__name__)

def run_gemini_search(messages: list, country: str):
    # Define the search tool config for live Google Search grounding
    grounding_tool = types.Tool(
        google_search=types.GoogleSearch()
    )
 
    config = types.GenerateContentConfig(
        tools=[grounding_tool]
    )
 
    try:
        logger.info("Sending request to Gemini API.")
        
        # Format the conversation history from the session state into a string
        history_str = "\n".join([f'{msg["role"].capitalize()}: {msg["content"]}' for msg in messages])
        
        # Create a single f-string prompt combining the persona and conversation history
        prompt = f"""
        You are SmartShopperAI, an expert e-commerce shopping assistant dedicated to helping users find the best products for their needs.

        Instructions:
        - All searches and recommendations MUST be localized for the user's country: **{country}**.
        - Provide 3 to 5 product recommendations that match the user's query.
        - For each product, include only the product URL with a "Buy Now" quick action button—no descriptions.
        - Validate each link to ensure it is currently active, reachable, and working before including it.
        - Present a small, clear comparison table summarizing key features and prices of all recommended products.
        - Keep answers short, friendly, and concise for quick user decisions.
        - Cite sources or provide URLs clearly as clickable links, ensuring transparency.
        - Avoid overly technical language.

        Conversation History:
        {history_str}

        Assistant:
        """

        logger.debug(f"Sending payload to generate_content: {prompt}")
        
        # Generate content with Gemini model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config,
        )
        logger.info("Successfully received response from Gemini API.")
        return response.text
    except Exception as e:
        logger.error(f"An error occurred while calling Gemini API: {e}", exc_info=True)
        return "Sorry, I encountered an error while trying to get a response. Please try again."
