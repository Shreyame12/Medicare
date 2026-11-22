
from flask import Flask
from datetime import datetime
from db import db, init_db
from models import Patient, Medication, DoseRecord

app = Flask(__name__)
init_db(app)

with app.app_context():

    # Find the test patient
    patient = Patient.query.filter_by(
        email="test@example.com"
    ).first()

    if patient is None:
        print("Patient not found!")
    else:

        # Find the patient's medicine
        medicine = Medication.query.filter_by(
            patient_id=patient.patient_id
        ).first()

        if medicine is None:
            print("Medicine not found!")

        else:
            # Create a dose record
            dose = DoseRecord(
                medication_id=medicine.medication_id,
                scheduled_datetime=datetime.now(),
                status="missed",
                actual_taken_at=None,
                missed_reason="Forgot due to weekend routine"
            )

            db.session.add(dose)
            db.session.commit()

            print("Dose record saved successfully!")
            print("Status:", dose.status)
            print("Reason:", dose.missed_reason)
