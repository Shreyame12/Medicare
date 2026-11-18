
from flask import Blueprint, request, jsonify

dose_bp = Blueprint(
    "dose",
    __name__,
    url_prefix="/api/doses"
)


@dose_bp.route("/record", methods=["POST"])
def record_dose():
    data = request.get_json(silent=True) or {}

    medicine_id = data.get("medicine_id")
    status = data.get("status")

    allowed_statuses = ["taken", "skipped"]

    if not medicine_id or status not in allowed_statuses:
        return jsonify({
            "status": "error",
            "message": "Valid medicine ID and dose status are required"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Dose details validated",
        "dose_status": status
    }), 200


@dose_bp.route("/", methods=["GET"])
def get_doses():
    return jsonify({
        "status": "success",
        "message": "Dose endpoint is working",
        "doses": []
    }), 200
