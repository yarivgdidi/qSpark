from flask import Flask, request, jsonify
from flask_cors import CORS
from decrypt import guess_key

app = Flask(__name__)
CORS(app)

@app.route("/bruteforce/", methods=['POST'])
def bruteforce():
    if request.method == 'POST':
        content = request.json
        text = content['text']
        arr = list(map(toInt, text.split(',')))
        size = content['size']
        res = guess_key(arr, size)
        return jsonify(res)

def toInt(x):
    return int(x.strip())