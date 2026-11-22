
from flask import Flask
from db import db, init_db
from models import Patient, DoseRecord, EmergencyNotification

app = Flask(__name__)
init_db(app)

with app.app_context():

    # Find test patient
    patient = Patient.query.filter_by(
        email="test@example.com"
    ).first()

    if patient is None:
        print("Patient not found!")

    else:
        # Find the latest missed dose
        dose = DoseRecord.query.filter_by(
            status="missed"
        ).order_by(
            DoseRecord.scheduled_datetime.desc()
        ).first()

        if dose is None:
            print("No missed doses found!")

        else:
            # Create emergency notification record
            alert = EmergencyNotification(
                patient_id=patient.patient_id,
                record_id=dose.record_id,
                notification_type="Emergency",
                delivery_status="pending",
                message="A scheduled medicine dose was reported as missed."
            )

            db.session.add(alert)
            db.session.commit()

            print("Emergency notification recorded!")
            print("Patient:", patient.name)
            print("Delivery status:", alert.delivery_status)
