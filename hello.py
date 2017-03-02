from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        return jsonify("ok")
        
    elif request.method == 'GET':
        return "GET"

if __name__ == "__main__":
    app.run()