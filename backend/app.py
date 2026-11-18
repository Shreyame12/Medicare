
from flask import Flask, jsonify
from config import Config
from extensions import db, bcrypt, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialise extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Home route
    @app.route("/")
    def home():
        return jsonify({
            "message": "Welcome to MediCare Backend!",
            "status": "Running"
        })

    # Health check route
    @app.route("/api/health")
    def health():
        return jsonify({
            "status": "success",
            "message": "MediCare backend is working"
        })

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
