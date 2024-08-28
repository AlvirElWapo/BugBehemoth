from flask import Flask, render_template, send_from_directory
from config import config
from flask_restx import Api
from endpoints.example_namespace import api as example_ns
from endpoints.time_namespace import api as time_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def home():
        return send_from_directory('../BugBehemoth_FE/src/pages', 'index.html')
    # Inicialización de Flask-RESTX
    api = Api(app, version='1.0', title='API Ejemplo', description='Una API sencilla')

    api.add_namespace(example_ns, path='/api')
    api.add_namespace(time_ns, path='/api')


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
