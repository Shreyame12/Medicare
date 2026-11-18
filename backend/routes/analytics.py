
from flask import Blueprint, jsonify

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/api/analytics"
)


@analytics_bp.route("/dose-summary", methods=["GET"])
def dose_summary():
    return jsonify({
        "status": "success",
        "message": "Dose analytics endpoint is working",
        "summary": {
            "taken": 0,
            "skipped": 0,
            "unconfirmed": 0
        }
    }), 200


@analytics_bp.route("/missed-patterns", methods=["GET"])
def missed_patterns():
    return jsonify({
        "status": "success",
        "message": "Missed-dose analysis endpoint is working",
        "patterns": []
    }), 200
