import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "YAIzaSyCSUE8sAG_ZcRJQOstMDEeXrFdjfDiNsjI")

if not api_key:
    raise ValueError("Error: Gemini API key is missing.")

# Initialize Gemini API
genai.configure(api_key=api_key)

# List available models
models = genai.list_models()

for model in models:
    print(model.name)
