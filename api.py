
from flask import Flask, jsonify, request
from db import db, init_db
from models import Patient, Medication, DoseRecord

app = Flask(__name__)
init_db(app)


@app.route("/")
def home():
    return jsonify({
        "message": "MediCare Database API is running!"
    })


# Get all patients
@app.route("/patients", methods=["GET"])
def get_patients():

    patients = Patient.query.all()

    return jsonify([
        {
            "patient_id": p.patient_id,
            "name": p.name,
            "email": p.email,
            "age": p.age
        }
        for p in patients
    ])


# Add a medicine
@app.route("/medications", methods=["POST"])
def add_medication():

    data = request.get_json()

    required = ["patient_id", "medicine_name"]

    if not data or any(key not in data for key in required):
        return jsonify({"error": "Missing required fields"}), 400

    patient = db.session.get(Patient, data["patient_id"])

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    medicine = Medication(
        patient_id=patient.patient_id,
        medicine_name=data["medicine_name"],
        dosage=data.get("dosage"),
        frequency=data.get("frequency")
    )

    db.session.add(medicine)
    db.session.commit()

    return jsonify({
        "message": "Medicine added successfully!",
        "medication_id": medicine.medication_id
    }), 201


# Get all medications for a patient
@app.route("/medications/<int:patient_id>", methods=["GET"])
def get_medications(patient_id):

    patient = db.session.get(Patient, patient_id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    medicines = Medication.query.filter_by(
        patient_id=patient_id
    ).all()

    return jsonify([
        {
            "medication_id": m.medication_id,
            "medicine_name": m.medicine_name,
            "dosage": m.dosage,
            "frequency": m.frequency
        }
        for m in medicines
    ])


# Get medication history
@app.route("/history/<int:patient_id>", methods=["GET"])
def get_history(patient_id):

    patient = db.session.get(Patient, patient_id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    medicines = Medication.query.filter_by(
        patient_id=patient_id
    ).all()

    result = []

    for medicine in medicines:

        doses = DoseRecord.query.filter_by(
            medication_id=medicine.medication_id
        ).all()

        result.append({
            "medicine_name": medicine.medicine_name,
            "dose_records": [
                {
                    "scheduled_datetime": d.scheduled_datetime.isoformat(),
                    "status": d.status,
                    "missed_reason": d.missed_reason
                }
                for d in doses
            ]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
