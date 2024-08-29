from flask import Flask
from flask import Flask, render_template, send_from_directory
from flask_jwt_extended import JWTManager
from flask_restx import Api
from models.exts import db
from auth.auth import auth_ns

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    JWTManager(app)

    api=Api(app, doc='/docs')
    api.add_namespace(auth_ns)

    return app

