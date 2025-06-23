from flask import Flask
from os import environ
import traceback
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    HOST=environ.get('HOST'),
    API_KEY=environ.get('API_KEY')
)

dockerURI = 'postgresql://' + environ.get('POSTGRES_USER') + ':' + environ.get('POSTGRES_PASSWORD') + '@' + environ.get('SERVICE_NAME') + '_db:' + environ.get('POSTGRES_PRIVATE_PORT') + '/' + '/' + environ.get('POSTGRES_DATABASE')
localURI = 'postgresql://' + environ.get('POSTGRES_USER') + ':' + environ.get('POSTGRES_PASSWORD') + '@localhost:' + environ.get('POSTGRES_PUBLIC_PORT') + '/' + '/' + environ.get('POSTGRES_DATABASE')


app.config['SQLALCHEMY_DATABASE_URI'] = localURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, (TypeError, AttributeError)):
        code = 500
    else:
        code = e.code
    response = {
                "error": str(e),
                "code": code,
                "traceback": traceback.format_exc()
            }
    return response, code

from Infrastructure.Controller.Controller import v1ControllerBase
from Infrastructure.Controller.ToolsController import toolsController

app.register_blueprint(v1ControllerBase, url_prefix='/api/v1')
app.register_blueprint(toolsController, url_prefix='/tools')

@app.route('/', methods=['GET'])
def index():
    return {'status': 'API is running'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)