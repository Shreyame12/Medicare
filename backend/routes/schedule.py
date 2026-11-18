
from flask import Blueprint, request, jsonify

schedule_bp = Blueprint(
    "schedule",
    __name__,
    url_prefix="/api/schedules"
)


@schedule_bp.route("/", methods=["POST"])
def create_schedule():
    data = request.get_json(silent=True) or {}

    medicine_id = data.get("medicine_id")
    scheduled_time = data.get("scheduled_time")

    if not medicine_id or not scheduled_time:
        return jsonify({
            "status": "error",
            "message": "Medicine ID and scheduled time are required"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Schedule details validated"
    }), 200


@schedule_bp.route("/", methods=["GET"])
def get_schedules():
    return jsonify({
        "status": "success",
        "message": "Schedule endpoint is working",
        "schedules": []
    }), 200
