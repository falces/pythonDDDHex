from flask import Flask
from flask.signals import Namespace

def configureSignals(app: Flask):
    namespace = Namespace()

    return {
        "new_status_group_received": namespace.signal("new_status_group"),
        "new_country_received": namespace.signal("new_country"),
    }