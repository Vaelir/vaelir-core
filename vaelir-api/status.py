from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__, url_prefix="/vaelir")

@status_bp.route("/status")
def status():
    return jsonify({"status": "online", "fase": "Despertar"})
