from flask import Flask

from Infrastructure.Controller.Controller import v1ControllerBase
from Infrastructure.Controller.ToolsController import toolsController

app = Flask(__name__)
app.register_blueprint(v1ControllerBase, url_prefix='/api/v1')
app.register_blueprint(toolsController, url_prefix='/tools')

@app.route('/', methods=['GET'])
def index():
    return {'status': 'API is running'}

if __name__ == "__main__":
    
    app.run(debug=True)
