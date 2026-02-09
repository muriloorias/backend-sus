#import
from flask import jsonify, Blueprint, request

login_bp = Blueprint("login", __name__)

emailtest = "email.teste@teste.com"
passwordtest = "tesetest" 

#requisição
@login_bp.route('/login', methods=['GET'])
def verifyLoged(): 
    return jsonify({"email" : f"{emailtest}",
                    "password" : f"{passwordtest}"}), 200

@login_bp.route('/login', methods=['POST'])
def makeLogin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email == emailtest and password == passwordtest:
        return jsonify({"sucess": True})
    else:
        return jsonify({"sucess": False,
                        "cause": "email and password is wrong"})