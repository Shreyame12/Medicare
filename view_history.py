
from flask import Flask
from db import db, init_db
from models import Patient, Medication, DoseRecord

app = Flask(__name__)
init_db(app)

with app.app_context():

    patient = Patient.query.filter_by(
        email="test@example.com"
    ).first()

    if patient is None:
        print("Patient not found!")

    else:
        medicines = Medication.query.filter_by(
            patient_id=patient.patient_id
        ).all()

        print("\nMEDICATION HISTORY")
        print("---------------------------")

        for medicine in medicines:

            print("\nMedicine:", medicine.medicine_name)

            records = DoseRecord.query.filter_by(
                medication_id=medicine.medication_id
            ).order_by(
                DoseRecord.scheduled_datetime.desc()
            ).all()

            if not records:
                print("No dose records available.")

            for record in records:
                print("Scheduled:", record.scheduled_datetime)
                print("Status:", record.status)
                print("Reason:", record.missed_reason)
                print("---------------------------")
