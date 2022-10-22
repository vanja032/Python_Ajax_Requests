from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
#import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "A"

@app.route('/Hello', methods=['GET','POST'])
def Hello():
    data = "Hello, Hello, World!"
    data.headers['Access-Control-Allow-Origin'] = '*'
    return data

if __name__ == "__main__":
	app.run(debug=True)