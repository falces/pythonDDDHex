from flask import Flask
from dotenv import load_dotenv
from os import environ
import os

app = Flask(__name__)

# load_dotenv()
# app.config.update(
#     HOST=os.getenv('HOST'),
#     API_KEY=os.getenv('API_KEY'),
# )
# app.config['HOST'] = os.getenv('HOST')
# app.config['API_KEY'] = os.getenv('API_KEY')
app.config.update(
    HOST=environ.get('HOST'),
    API_KEY=environ.get('API_KEY')
)

from Infrastructure.Controller.Controller import v1ControllerBase
from Infrastructure.Controller.ToolsController import toolsController

app.register_blueprint(v1ControllerBase, url_prefix='/api/v1')
app.register_blueprint(toolsController, url_prefix='/tools')

@app.route('/', methods=['GET'])
def index():
    return {'status': 'API is running'}



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)