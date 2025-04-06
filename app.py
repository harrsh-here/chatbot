from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "AIzaSyCSUE8sAG_ZcRJQOstMDEeXrFdjfDiNsjI")  # Gemini API Key

if not api_key:
    raise ValueError("Error: Gemini API key is missing.")

# Initialize Gemini API
genai.configure(api_key=api_key)

app = Flask(__name__, template_folder="templates")

# ✅ Serve the Chatbot Webpage
@app.route("/")
def home():
    return render_template("chat.html")

# ✅ Chatbot API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_message)
        
        # Ensure response is valid before accessing attributes
        reply = getattr(response, 'text', "I'm sorry, but I couldn't generate a response at the moment.")
        
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
