from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/get": {"origins": "*"}})  # Enable CORS for /get route

chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@app.route("/get", methods=["POST"])
def get_bot_response():
    data = request.get_json()
    user_message = data.get('msg')
    response = str(chatbot.get_response(user_message))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
