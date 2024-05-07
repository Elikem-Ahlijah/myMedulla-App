# app.py
from flask import Flask, jsonify, request, flash, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to myMedulla App!'

@app.route('/send_request', methods=['POST'])
def send_request():
    data = request.get_json()
    url = data.get('url')
    
    print(url)
    
    if url:
        # response = requests.get(url)
        return jsonify({'status': 'success', 'data': url}), 200
    else:
        return jsonify({'status': 'error', 'message': 'URL not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
