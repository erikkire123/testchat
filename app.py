# app.py

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connect to MongoDB using your provided connection string
client = MongoClient("mongodb+srv://procar69690:qQDzlwWvdzsapjU9@cluster0.dskdtyr.mongodb.net/?retryWrites=true&w=majority")
db = client.chat_app
messages = db.messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form['sender']
    content = request.form['content']
    timestamp = datetime.now()

    messages.insert_one({
        'sender': sender,
        'content': content,
        'timestamp': timestamp
    })

    return 'Message sent successfully'

@app.route('/get_messages', methods=['GET'])
def get_messages():
    user_messages = messages.find({}).sort('timestamp')
    messages_list = [{'sender': msg['sender'], 'content': msg['content']} for msg in user_messages]
    return jsonify({'messages': messages_list})

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
