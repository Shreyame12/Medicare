
from flask import Blueprint, request, jsonify

medicine_bp = Blueprint(
    "medicine",
    __name__,
    url_prefix="/api/medicines"
)


def get_request_data():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return None

    return data


@medicine_bp.route("/", methods=["POST"])
def add_medicine():
    data = get_request_data()

    if data is None:
        return jsonify({
            "status": "error",
            "message": "A valid JSON object is required"
        }), 400

    name = data.get("name")
    instructions = data.get("instructions")

    if not isinstance(name, str) or not name.strip():
        return jsonify({
            "status": "error",
            "message": "Medicine name is required"
        }), 400

    if instructions is not None and not isinstance(instructions, str):
        return jsonify({
            "status": "error",
            "message": "Instructions must be text"
        }), 400

    name = name.strip()

    if instructions is not None:
        instructions = instructions.strip()

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
    if medicine_id <= 0:
        return jsonify({
            "status": "error",
            "message": "Medicine ID must be positive"
        }), 400

    return jsonify({
        "status": "success",
        "message": "Medicine deletion endpoint is working",
        "medicine_id": medicine_id
    }), 200
