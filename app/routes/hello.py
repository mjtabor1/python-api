
from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/main', methods=['GET'])
def main():
    return jsonify(message="This is our main route")