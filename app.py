#import
from flask import Flask, jsonify

app = Flask(__name__)

#requisição
@app.route('/', methods=['GET'])
def home():
    return jsonify({"mensagem" : "olá"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)