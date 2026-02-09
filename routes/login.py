#import
from flask import jsonify, Blueprint

login_bp = Blueprint("login", __name__)

#requisição
@login_bp.route('/login', methods=['GET'])
def home():
    return jsonify({"mensagem" : "olá"}), 200
