from flask import Flask, jsonify, request
from src.config import Config

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Home endpoint: Provides a welcome message and application status.
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Welcome to the Portfolio CI/CD Application!",
            "status": "running"
        })

    # Health endpoint: Returns the health status of the application.
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "status": "healthy"
        })

    # Echo endpoint: Receives JSON data and echoes it back.
    @app.route("/echo", methods=["POST"])
    def echo():
        data = request.get_json()
        return jsonify({
            "echo": data,
            "status": "success"
        })

    return app

if __name__ == "__main__":
    # Create the app and run on the specified port from config.
    app = create_app()
    app.run(host="0.0.0.0", port=app.config.get("PORT", 5000))
