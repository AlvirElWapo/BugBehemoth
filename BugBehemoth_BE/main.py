from flask import Flask
from config import Config
from flask_restx import Api
from endpoints.example_namespace import api as example_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialización de Flask-RESTX
    api = Api(app, version='1.0', title='API Ejemplo', description='Una API sencilla')

    api.add_namespace(example_ns, path='/api')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
