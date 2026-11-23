
# MediCare – Backend API Documentation

## 1. Project Overview

MediCare is an Elderly Medication Management application.

The backend is developed using Python Flask and provides REST API endpoints for authentication, medicines, schedules, dose tracking, analytics, notifications, history and reports.

## 2. Base URL

Local development:

http://127.0.0.1:5000

All endpoints are relative to this base URL.

## 3. Authentication APIs

### Register User

- Method: POST
- Endpoint: `/api/auth/register`

Request:
```json
{
  "name": "Test User",
  "email": "test@example.com",
  "password": "password123"
}
```

### Login User

- Method: POST
- Endpoint: `/api/auth/login`

Request:
```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

## 4. Medicine APIs

### Add Medicine

- Method: POST
- Endpoint: `/api/medicines/`

Request:
```json
{
  "name": "Vitamin D",
  "instructions": "Take after breakfast"
}
```

### Get Medicines

- Method: GET
- Endpoint: `/api/medicines/`

### Delete Medicine

- Method: DELETE
- Endpoint: `/api/medicines/<medicine_id>`

Example:
`/api/medicines/1`

## 5. Schedule APIs

### Create Schedule

- Method: POST
- Endpoint: `/api/schedules/`

Request:
```json
{
  "medicine_id": 1,
  "scheduled_time": "08:00"
}
```

Time format: HH:MM (24-hour format).

### Get Schedules

- Method: GET
- Endpoint: `/api/schedules/`

## 6. Dose APIs

### Record Dose

- Method: POST
- Endpoint: `/api/doses/record`

Request:
```json
{
  "medicine_id": 1,
  "status": "taken"
}
```

Allowed statuses:
- taken
- skipped

### Get Dose Records

- Method: GET
- Endpoint: `/api/doses/`

## 7. Analytics APIs

### Dose Summary

- Method: GET
- Endpoint: `/api/analytics/dose-summary`

### Missed Dose Patterns

- Method: GET
- Endpoint: `/api/analytics/missed-patterns`

## 8. Notification APIs

### Emergency Alert

- Method: POST
- Endpoint: `/api/notifications/emergency-alert`

Request:
```json
{
  "emergency_contact": "9876543210",
  "message": "Please contact me",
  "consent": true
}
```

Note: This endpoint currently validates the alert details. It does not send an actual notification.

## 9. History APIs

### Dose History

- Method: GET
- Endpoint: `/api/history/doses`

### Medicine History

- Method: GET
- Endpoint: `/api/history/medicines`

## 10. Report APIs

### Daily Report

- Method: GET
- Endpoint: `/api/reports/daily`

### Weekly Report

- Method: GET
- Endpoint: `/api/reports/weekly`

## 11. HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Request successful |
| 400 | Invalid request data |
| 403 | Permission or consent denied |
| 404 | Endpoint not found |
| 405 | Method not allowed |
| 500 | Internal server error |

## 12. Important Integration Notes

- Send JSON data with POST requests.
- Use the correct HTTP method for each endpoint.
- Scheduled times must use HH:MM format.
- Medicine IDs must be positive integers.
- Dose status must be taken or skipped.
- Some endpoints currently return placeholder data.
- Database integration is still pending.
- Authentication currently validates input but does not create or verify actual accounts.
- Frontend integration and actual notification delivery are pending.
