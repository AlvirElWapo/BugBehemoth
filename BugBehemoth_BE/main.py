from flask import Flask
from flask import Flask, render_template, send_from_directory
from flask_jwt_extended import JWTManager
from flask_restx import Api
from endpoints.example_namespace import api as example_ns
from endpoints.time_namespace import api as time_ns
from endpoints.components_namespace import modals_bp
from models.exts import db
from auth.auth import auth_ns

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    JWTManager(app)

    @app.route('/')
    def home():
        return send_from_directory('../BugBehemoth_FE/src/pages', 'index.html')

    api=Api(app, doc='/docs')
    api.add_namespace(auth_ns)


    app.register_blueprint(modals_bp)
    return app

