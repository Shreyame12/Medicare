
from flask import Blueprint, request, jsonify

medicine_bp = Blueprint(
    "medicine",
    __name__,
    url_prefix="/api/medicines"
)


@medicine_bp.route("/", methods=["POST"])
def add_medicine():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    instructions = data.get("instructions")

    if not name:
        return jsonify({
            "status": "error",
            "message": "Medicine name is required"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Medicine details validated",
        "medicine": {
            "name": name,
            "instructions": instructions
        }
    }), 200


@medicine_bp.route("/", methods=["GET"])
def get_medicines():
    return jsonify({
        "status": "success",
        "message": "Medicine endpoint is working",
        "medicines": []
    }), 200


@medicine_bp.route("/<int:medicine_id>", methods=["DELETE"])
def delete_medicine(medicine_id):
    return jsonify({
        "status": "success",
        "message": "Medicine deletion endpoint is working",
        "medicine_id": medicine_id
    }), 200
