from flask import Flask

def create_app():
    application = Flask(__name__)

    # Routes
    from .routes import api_v1_bp, main_bp, error_handler_bp
    application.register_blueprint(api_v1_bp)
    application.register_blueprint(main_bp)
    application.register_blueprint(error_handler_bp)

    return application


