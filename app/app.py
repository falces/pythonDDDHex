from flask import Flask
from os import environ
import traceback
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate

app = Flask(__name__)

app.config.update(
    HOST = environ.get('HOST'),
    API_KEY = environ.get('API_KEY')
)

# mysql_local = 'mysql+mysqlconnector://' + environ.get('MYSQL_USER') + ':' + environ.get('MYSQL_PASSWORD') + '@mysql:3306/ThirdPL'
mysql_local = 'mysql+mysqlconnector://thirdpl:thirdpl@localhost:13306/ThirdPL'

app.config['SQLALCHEMY_DATABASE_URI'] = mysql_local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, (HTTPException)):
        code = e.code
    else:
        code = 500
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