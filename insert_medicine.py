
from flask import Flask
from datetime import date, time
from db import db, init_db
from models import Patient, Medication, MedicationSchedule

app = Flask(__name__)
init_db(app)

with app.app_context():

    # Find the existing test patient
    patient = Patient.query.filter_by(
        email="test@example.com"
    ).first()

    if patient is None:
        print("Patient not found. Run insert_data.py first.")

    else:
        # Add first medicine
        medicine = Medication(
            patient_id=patient.patient_id,
            medicine_name="Sample Medicine A",
            dosage="As prescribed",
            frequency="Twice daily",
            start_date=date.today()
        )

        db.session.add(medicine)
        db.session.commit()

        # Add morning schedule
        morning = MedicationSchedule(
            medication_id=medicine.medication_id,
            scheduled_time=time(8, 0),
            day_of_week="Every day"
        )

        # Add evening schedule
        evening = MedicationSchedule(
            medication_id=medicine.medication_id,
            scheduled_time=time(20, 0),
            day_of_week="Every day"
        )

        db.session.add_all([morning, evening])
        db.session.commit()

        print("Medicine added successfully!")
        print("Morning and evening schedules added!")
