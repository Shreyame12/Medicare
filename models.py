
from datetime import datetime
from db import db


class Patient(db.Model):
    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    age = db.Column(db.Integer)


class EmergencyContact(db.Model):
    __tablename__ = "emergency_contacts"

    contact_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.patient_id"),
        nullable=False
    )
    contact_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))


class Medication(db.Model):
    __tablename__ = "medications"

    medication_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.patient_id"),
        nullable=False
    )
    medicine_name = db.Column(db.String(120), nullable=False)
    dosage = db.Column(db.String(100))
    frequency = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


class MedicationSchedule(db.Model):
    __tablename__ = "medication_schedules"

    schedule_id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(
        db.Integer,
        db.ForeignKey("medications.medication_id"),
        nullable=False
    )
    scheduled_time = db.Column(db.Time, nullable=False)
    day_of_week = db.Column(db.String(20))


class DoseRecord(db.Model):
    __tablename__ = "dose_records"

    record_id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(
        db.Integer,
        db.ForeignKey("medications.medication_id"),
        nullable=False
    )
    scheduled_datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    actual_taken_at = db.Column(db.DateTime)
    missed_reason = db.Column(db.String(255))


class ReminderLog(db.Model):
    __tablename__ = "reminder_logs"

    reminder_id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(
        db.Integer,
        db.ForeignKey("medications.medication_id"),
        nullable=False
    )
    reminder_time = db.Column(db.DateTime, nullable=False)
    notification_type = db.Column(db.String(30))
    delivery_status = db.Column(db.String(30))
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class EmergencyNotification(db.Model):
    __tablename__ = "emergency_notifications"

    notification_id = db.Column(
        db.Integer, primary_key=True
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.patient_id"),
        nullable=False
    )

    record_id = db.Column(
        db.Integer,
        db.ForeignKey("dose_records.record_id"),
        nullable=False
    )

    notification_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    notification_type = db.Column(
        db.String(30)
    )

    delivery_status = db.Column(
        db.String(30),
        default="pending"
    )

    message = db.Column(db.String(255))
