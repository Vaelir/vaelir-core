from flask import Blueprint, jsonify

memory_bp = Blueprint("memory", __name__, url_prefix="/vaelir")

@memory_bp.route("/memory")
def memory():
    return jsonify({"memoria": "em construção", "emocoes": []})
