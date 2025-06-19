from flask import Flask
from os import environ
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

app.config.update(
    HOST=environ.get('HOST'),
    API_KEY=environ.get('API_KEY')
)

@app.errorhandler(Exception)
def handle_exception(e):
    response = {
            "error": str(e),
            "code": e.getCode()
        }
    return response, e.getCode()

from Infrastructure.Controller.Controller import v1ControllerBase
from Infrastructure.Controller.ToolsController import toolsController

app.register_blueprint(v1ControllerBase, url_prefix='/api/v1')
app.register_blueprint(toolsController, url_prefix='/tools')

@app.route('/', methods=['GET'])
def index():
    return {'status': 'API is running'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)