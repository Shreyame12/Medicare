
from flask import Blueprint, request, jsonify

notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/api/notifications"
)


@notifications_bp.route("/emergency-alert", methods=["POST"])
def emergency_alert():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    contact = data.get("emergency_contact")
    message = data.get("message")
    consent = data.get("consent")

    if (
        not isinstance(contact, str)
        or not contact.strip()
        or not isinstance(message, str)
        or not message.strip()
    ):
        return jsonify({
            "status": "error",
            "message": "Emergency contact and message are required"
        }), 400

    if consent is not True:
        return jsonify({
            "status": "error",
            "message": "Emergency contact consent is required"
        }), 403

    return jsonify({
        "status": "success",
        "message": "Alert details validated. No notification has been sent."
    }), 200
