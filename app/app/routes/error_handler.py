from flask import Blueprint, render_template
from . import error_handler_bp

@error_handler_bp.app_errorhandler(404)
def page_not_found(_e):
    return render_template('errors/error_404.html'), 404


@error_handler_bp.app_errorhandler(500)
def internal_server_error(_e):
    return render_template('errors/error_500.html'), 500


@error_handler_bp.app_errorhandler(400)
def bad_request_error(_e):
    return render_template('errors/error_400.html'), 400

@error_handler_bp.app_errorhandler(401)
def unauthorized_error(_e):
    return render_template('errors/error_401.html'), 401

@error_handler_bp.app_errorhandler(403)
def forbidden_error(_e):
    return render_template('errors/error_403.html'), 403


@error_handler_bp.app_errorhandler(405)
def method_not_allowed_error(_e):
    return render_template('errors/error_405.html'), 405


@error_handler_bp.app_errorhandler(503)
def service_unavailable_error(_):
    return render_template('errors/error_503.html'), 503