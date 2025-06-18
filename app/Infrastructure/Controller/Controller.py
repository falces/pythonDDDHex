from flask import Blueprint
from Infrastructure.Controller.CountryController import countryController
from Infrastructure.Controller.StatusController import statusController

v1ControllerBase = Blueprint('v1', __name__)

v1ControllerBase.register_blueprint(countryController, url_prefix='/countries')
v1ControllerBase.register_blueprint(statusController, url_prefix='/status')