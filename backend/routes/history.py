
from flask import Blueprint, jsonify

history_bp = Blueprint(
    "history",
    __name__,
    url_prefix="/api/history"
)


@history_bp.route("/doses", methods=["GET"])
def dose_history():
    return jsonify({
        "status": "success",
        "message": "Medication history endpoint is working",
        "history": []
    }), 200


@history_bp.route("/medicines", methods=["GET"])
def medicine_history():
    return jsonify({
        "status": "success",
        "message": "Medicine history endpoint is working",
        "history": []
    }), 200
