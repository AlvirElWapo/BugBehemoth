from flask import Flask
from flask import Flask, render_template, send_from_directory
from flask_jwt_extended import JWTManager
from flask_restx import Api
from endpoints.time_namespace import api as time_ns
from endpoints.components_namespace import modals_bp
from models.exts import db
from auth.auth import auth_ns
from endpoints.userEndpoint import user_ns
from endpoints.tareasEndpoint import tareas_ns
from endpoints.rolesEndpoint import roles_ns
from endpoints.recursosTareaEndpoint import recursotarea_ns
from endpoints.RecursosEndpoint import recursos_ns
from endpoints.proyectosEndpoint import proyectos_ns
from endpoints.invitacionesEndpoint import invitaciones_ns
from endpoints.eventosEndpoint import eventos_ns
from endpoints.departamentosEndpoint import departamentos_ns
from endpoints.asignacionProyectosEndpoint import asignacionproyecto_ns
from endpoints.alertasEndpoint import alerlas_ns


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
    api.add_namespace(user_ns)
    api.add_namespace(tareas_ns)
    api.add_namespace(roles_ns)
    api.add_namespace(recursotarea_ns)
    api.add_namespace(recursos_ns)
    api.add_namespace(proyectos_ns)
    api.add_namespace(invitaciones_ns)
    api.add_namespace(eventos_ns)
    api.add_namespace(departamentos_ns)
    api.add_namespace(asignacionproyecto_ns)
    api.add_namespace(alerlas_ns)

    
    app.register_blueprint(modals_bp)
    return app

