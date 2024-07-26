from flask import Blueprint
from app.config import Config

main_bp = Blueprint('main', __name__)

error_handler_bp = Blueprint('error_handler', __name__, template_folder='templates/errors/',
                             static_folder='static')

api_v1_bp = Blueprint('api_v1', __name__, url_prefix=Config.API_PREFIX)

from . import api_v1, main, error_handler
