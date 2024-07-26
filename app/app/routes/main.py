from flask import redirect
from . import main_bp
from app.config import Config

@main_bp.route('/')
def root():
    return redirect(Config.API_PREFIX)

@main_bp.route('/<path:dummy>')
def fallback(dummy):
    # Redirect when the path is incorrect 
    return redirect(Config.API_PREFIX)