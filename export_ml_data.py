
import pandas as pd
from flask import Flask
from db import db, init_db
from models import Patient, Medication, DoseRecord

app = Flask(__name__)
init_db(app)

with app.app_context():

    records = []

    patients = Patient.query.all()

    for patient in patients:

        medicines = Medication.query.filter_by(
            patient_id=patient.patient_id
        ).all()

        for medicine in medicines:

            doses = DoseRecord.query.filter_by(
                medication_id=medicine.medication_id
            ).all()

            for dose in doses:

                records.append({
                    "patient_id": patient.patient_id,
                    "medicine_name": medicine.medicine_name,
                    "scheduled_datetime": dose.scheduled_datetime,
                    "day_of_week": dose.scheduled_datetime.strftime("%A"),
                    "scheduled_hour": dose.scheduled_datetime.hour,
                    "status": dose.status,
                    "actual_taken_at": dose.actual_taken_at,
                    "missed_reason": dose.missed_reason
                })

    columns = [
        "patient_id",
        "medicine_name",
        "scheduled_datetime",
        "day_of_week",
        "scheduled_hour",
        "status",
        "actual_taken_at",
        "missed_reason"
    ]

    df = pd.DataFrame(records, columns=columns)

    # Remove duplicate records
    df = df.drop_duplicates()

    # Save data as CSV
    df.to_csv("medication_history.csv", index=False)

    print("ML dataset exported successfully!")
    print("Total records:", len(df))
    print(df.head())
