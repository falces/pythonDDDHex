from flask import Blueprint
from modules.Countries.controller import countryController
from Infrastructure.Controller.StatusController import statusController
from Infrastructure.Controller.HarmonisedCodesController import harmonisedCodesController
# from Infrastructure.Controller.SignalListener.CountrySignalListener import countrySignalListener
from Infrastructure.Controller.SignalListener.StatusSignalListener import statusSignalListener
from Infrastructure.Controller.SignalListener.RabbitMQListener import rabbitMQSignalListener
from modules.Currencies.controller import currenciesController




v1ControllerBase = Blueprint('v1', __name__)

v1ControllerBase.register_blueprint(countryController, url_prefix='/countries')
v1ControllerBase.register_blueprint(statusController, url_prefix='/status')
v1ControllerBase.register_blueprint(harmonisedCodesController, url_prefix='/harmonisedCodes')
v1ControllerBase.register_blueprint(currenciesController, url_prefix='/currencies')

# v1ControllerBase.register_blueprint(countrySignalListener)
v1ControllerBase.register_blueprint(statusSignalListener)
v1ControllerBase.register_blueprint(rabbitMQSignalListener)