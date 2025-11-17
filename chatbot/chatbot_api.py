
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    return jsonify({"reply": "Chatbot response placeholder."})

if __name__ == "__main__":
    app.run(port=5001)
