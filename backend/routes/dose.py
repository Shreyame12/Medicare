
from flask import Blueprint, request, jsonify

dose_bp = Blueprint(
    "dose",
    __name__,
    url_prefix="/api/doses"
)


@dose_bp.route("/record", methods=["POST"])
def record_dose():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    medicine_id = data.get("medicine_id")
    status = data.get("status")

    allowed_statuses = ["taken", "skipped"]

    if (
        isinstance(medicine_id, bool)
        or not isinstance(medicine_id, int)
        or medicine_id <= 0
    ):
        return jsonify({
            "status": "error",
            "message": "Medicine ID must be a positive integer"
        }), 400

    if status not in allowed_statuses:
        return jsonify({
            "status": "error",
            "message": "Dose status must be taken or skipped"
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
