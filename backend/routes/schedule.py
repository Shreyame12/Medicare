
import re

from flask import Blueprint, request, jsonify

schedule_bp = Blueprint(
    "schedule",
    __name__,
    url_prefix="/api/schedules"
)


def get_request_data():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return None

    return data


@schedule_bp.route("/", methods=["POST"])
def create_schedule():
    data = get_request_data()

    if data is None:
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    medicine_id = data.get("medicine_id")
    scheduled_time = data.get("scheduled_time")

    if (
        isinstance(medicine_id, bool)
        or not isinstance(medicine_id, int)
        or medicine_id <= 0
    ):
        return jsonify({
            "status": "error",
            "message": "Medicine ID must be a positive integer"
        }), 400

    if not isinstance(scheduled_time, str):
        return jsonify({
            "status": "error",
            "message": "Scheduled time must be in HH:MM format"
        }), 400

    if not re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", scheduled_time):
        return jsonify({
            "status": "error",
            "message": "Scheduled time must be a valid 24-hour time (HH:MM)"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Schedule details validated",
        "schedule": {
            "medicine_id": medicine_id,
            "scheduled_time": scheduled_time
        }
    }), 200


@schedule_bp.route("/", methods=["GET"])
def get_schedules():
    return jsonify({
        "status": "success",
        "message": "Schedule endpoint is working",
        "schedules": []
    }), 200
