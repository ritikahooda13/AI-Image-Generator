from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def get_bot_response(user_message):
    msg = user_message.lower().strip()
    
    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hello there! 👋 I am your advanced AI Assistant. How can I brighten your day today?"
    elif "how are you" in msg:
        return "I'm running at peak efficiency! 🚀 Ready to help you crack tasks or answer questions. How about you?"
    elif "name" in msg:
        return "I am a smart Neural Chatbot assistant designed with a modern Python & Flask backend."
    elif "internship" in msg:
        return "Internships are the ultimate launchpad for your career! You are doing amazing by building these projects. 💻✨"
    elif "python" in msg:
        return "Python is pure magic! 🐍 Perfect for Web Apps, Data Science, and Machine Learning. Excellent choice!"
    elif "clear" in msg or "bye" in msg:
        return "Goodbye! Clear skies ahead. Take care! 🌤️"
    else:
        return f"Interesting perspective! You mentioned: '{user_message}'. Let's dive deeper into this topic. Ask me anything else!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_data = request.get_json()
    user_message = user_data.get("message", "")
    
    # Chhota sa delay artificial intelligence typing feeling dene ke liye
    time.sleep(0.6) 
    
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5001)