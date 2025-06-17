from flask import Blueprint
from .CountryController import countryController

v1ControllerBase = Blueprint('v1', __name__)

v1ControllerBase.register_blueprint(countryController, url_prefix='/countries')