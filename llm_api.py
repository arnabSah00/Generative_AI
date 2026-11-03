import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load variables from the .env file into the environment
load_dotenv()

# 2. Read the API key and stop early with a clear message if it's missing
## Gemini config.....
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME=os.getenv("GEMINI_MODEL_NAME")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Check that your .env file exists and has the key.")


# # 3. Create the Gemini 3.5 Flash model
# llm = ChatGoogleGenerativeAI(
#     model=MODEL_NAME,
#     api_key=API_KEY,
#     temperature=0.7,
# )

def get_llm():
    # 3. Create the Gemini 3.5 Flash model
    return ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        api_key=API_KEY,
        temperature=0.7,
    )