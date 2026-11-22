
from flask import Flask
from db import db, init_db
from models import Patient, EmergencyContact

app = Flask(__name__)

init_db(app)

with app.app_context():

    # Create a sample patient
    patient = Patient(
        name="Test Patient",
        email="test@example.com",
        password_hash="sample_hash",
        age=70
    )

    db.session.add(patient)
    db.session.commit()

    # Add emergency contact
    contact = EmergencyContact(
        patient_id=patient.patient_id,
        contact_name="Emergency Contact",
        phone="9876543210",
        email="contact@example.com"
    )

    db.session.add(contact)
    db.session.commit()

    print("Patient added successfully!")
    print("Emergency contact added successfully!")
