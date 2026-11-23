from app import create_app


def setup_app():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home():
    client = setup_app()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "Running"


def test_health():
    client = setup_app()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "success"


def test_register_valid_details():
    client = setup_app()
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200


def test_register_short_password():
    client = setup_app()
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "password": "123"
        }
    )
    assert response.status_code == 400


def test_add_medicine():
    client = setup_app()
    response = client.post(
        "/api/medicines/",
        json={
            "name": "Vitamin D",
            "instructions": "Take after breakfast"
        }
    )
    assert response.status_code == 200


def test_create_schedule():
    client = setup_app()
    response = client.post(
        "/api/schedules/",
        json={
            "medicine_id": 1,
            "scheduled_time": "08:00"
        }
    )
    assert response.status_code == 200


def test_record_dose():
    client = setup_app()
    response = client.post(
        "/api/doses/record",
        json={
            "medicine_id": 1,
            "status": "taken"
        }
    )
    assert response.status_code == 200


def test_emergency_alert_without_consent():
    client = setup_app()
    response = client.post(
        "/api/notifications/emergency-alert",
        json={
            "emergency_contact": "9876543210",
            "message": "Please contact me",
            "consent": False
        }
    )
    assert response.status_code == 403

def test_add_medicine_without_name():
    client = setup_app()
    response = client.post(
        "/api/medicines/",
        json={
            "name": "   ",
            "instructions": "Take after breakfast"
        }
    )
    assert response.status_code == 400
def test_invalid_schedule_time():
    client = setup_app()
    response = client.post(
        "/api/schedules/",
        json={
            "medicine_id": 1,
            "scheduled_time": "25:90"
        }
    )
    assert response.status_code == 400
def test_invalid_dose_status():
    client = setup_app()
    response = client.post(
        "/api/doses/record",
        json={
            "medicine_id": 1,
            "status": "unknown"
        }
    )
    assert response.status_code == 400
def test_register_invalid_email():
    client = setup_app()
    response = client.post(
        "/api/auth/register",
        json={
            "name": "Test User",
            "email": "invalid-email",
            "password": "password123"
        }
    )
    assert response.status_code == 400
def test_invalid_medicine_id_for_dose():
    client = setup_app()
    response = client.post(
        "/api/doses/record",
        json={
            "medicine_id": 0,
            "status": "taken"
        }
    )
    assert response.status_code == 400
def test_invalid_medicine_id_for_schedule():
    client = setup_app()
    response = client.post(
        "/api/schedules/",
        json={
            "medicine_id": 0,
            "scheduled_time": "08:00"
        }
    )
    assert response.status_code == 400

def test_login_invalid_email():
    client = setup_app()
    response = client.post(
        "/api/auth/login",
        json={
            "email": "wrong-email",
            "password": "password123"
        }
    )
    assert response.status_code == 400


def test_login_missing_password():
    client = setup_app()
    response = client.post(
        "/api/auth/login",
        json={"email": "test@example.com"}
    )
    assert response.status_code == 400


def test_medicine_invalid_instructions():
    client = setup_app()
    response = client.post(
        "/api/medicines/",
        json={
            "name": "Vitamin D",
            "instructions": 123
        }
    )
    assert response.status_code == 400


def test_schedule_missing_time():
    client = setup_app()
    response = client.post(
        "/api/schedules/",
        json={"medicine_id": 1}
    )
    assert response.status_code == 400


def test_dose_missing_status():
    client = setup_app()
    response = client.post(
        "/api/doses/record",
        json={"medicine_id": 1}
    )
    assert response.status_code == 400


def test_emergency_alert_without_contact():
    client = setup_app()
    response = client.post(
        "/api/notifications/emergency-alert",
        json={
            "message": "Please contact me",
            "consent": True
        }
    )
    assert response.status_code == 400
