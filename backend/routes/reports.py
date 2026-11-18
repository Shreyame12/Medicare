
from flask import Blueprint, jsonify

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/reports"
)


@reports_bp.route("/daily", methods=["GET"])
def daily_report():
    return jsonify({
        "status": "success",
        "message": "Daily report endpoint is working",
        "report": {
            "date": None,
            "taken": 0,
            "skipped": 0,
            "unconfirmed": 0
        }
    }), 200


@reports_bp.route("/weekly", methods=["GET"])
def weekly_report():
    return jsonify({
        "status": "success",
        "message": "Weekly report endpoint is working",
        "report": []
    }), 200
