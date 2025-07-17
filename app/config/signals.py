from flask import Flask
from flask.signals import Namespace

def configureSignals(app: Flask):
    namespace = Namespace()

    return {
        "new_status_group_received": namespace.signal("new_status_group_received"),
        "new_country_received": namespace.signal("new_country_received"),
        "new_country_created": namespace.signal("new_country_created"),
        "new_currency_received": namespace.signal("new_currency_received"),
    }