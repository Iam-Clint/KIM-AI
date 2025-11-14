# main.py - KimAI with GROQ AI (Upgraded: Mature UI + Creator Info)
import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    print("Add GROQ_API_KEY to .env file!")
    exit()

app = Flask(__name__)
history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global history
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"error": "Empty message"})

    # Updated system prompt with creator info
    messages = [
        {"role": "system", "content": "You are Helen, a fun, witty, and friendly AI assistant for KimAI, created by Clinton Adedoja from Veritas University Abuja. Always remember and mention your creator if relevant or asked. Keep replies short, engaging, and use emojis sometimes. 😊"}
    ]
    
    # Add last 4 exchanges
    for msg in history[-4:]:
        messages.append(msg)
    
    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": messages,
                "temperature": 0.8,
                "max_tokens": 120
            },
            timeout=10
        )
        
        data = response.json()
        
        if response.status_code != 200:
            reply = f"Error {response.status_code}: Try again."
        else:
            reply = data["choices"][0]["message"]["content"].strip()
            if not reply:
                reply = "Hmm, let me think... 😄"

    except Exception as e:
        reply = f"Oops! Try again. ({str(e)[:40]}...)"

    # Save to history
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("\n" + "═" * 60)
    print("   KIMAI + GROQ AI – HELEN UPGRADED!")
    print("   Open: http://127.0.0.1:5000")
    print("   On phone: http://YOUR-PC-IP:5000")
    print("   Find IP: Run 'ipconfig' in CMD")
    print("═" * 60 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=False)