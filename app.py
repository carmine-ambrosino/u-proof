from flask import Flask
from flask_cors import CORS
from routes import routes_bp
from error_handler import error_handler_bp


def create_app():
    application = Flask(__name__)

    # CORS(application)

    # Routes
    application.register_blueprint(routes_bp)
    application.register_blueprint(error_handler_bp)

    return application


# More setup for flask app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)