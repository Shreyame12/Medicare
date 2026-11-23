
from flask import Flask, jsonify

from routes.auth import auth_bp
from routes.medicine import medicine_bp
from routes.schedule import schedule_bp
from routes.dose import dose_bp
from routes.analytics import analytics_bp
from routes.notifications import notifications_bp
from routes.history import history_bp
from routes.reports import reports_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(medicine_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(dose_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(reports_bp)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Welcome to MediCare Backend!",
            "status": "Running"
        })

    @app.route("/api/health")
    def health():
        return jsonify({
            "status": "success",
            "message": "MediCare backend is working"
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": "error",
            "message": "The requested resource was not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "status": "error",
            "message": "An internal server error occurred"
        }), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
