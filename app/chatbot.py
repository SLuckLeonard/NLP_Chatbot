import nltk
from flask import request, jsonify, render_template
from app import app
from app.model import predict_intent

nltk.download('punkt')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = predict_intent(user_input)
    return jsonify({"response": response})

@app.route('/')
def index():
    return render_template('index.html')
