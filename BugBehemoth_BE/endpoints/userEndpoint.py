from flask_restx import Namespace, Resource
from flask import jsonify, request
from models.user import User
from flask_jwt_extended import jwt_required
from werkzeug.security import  generate_password_hash

user_ns = Namespace('users', description="endpoint para users")

@user_ns.route('/all')
class usersResourse(Resource):
    @jwt_required()
    def get(self):
        try:
            users = User.query.all()

            return jsonify([user.serialize() for user in users])
        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        

    def post(self):
        data = request.get_json()
        if (not data or not data.get('email') or not data.get('password') or not data.get('nombre') 
            or not data.get('username') or not data.get('id_departamento') or not data.get('id_rol')):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:
            if User.query.filter_by(email=data['email']).first():
                return {'msg': 'El correo electrónico ya existe'}, 400
            
            if User.query.filter_by(username=data['username']).first():
                return {'msg': 'El nombre de usuario ya existe'}, 400
            
            hashed_password = generate_password_hash(data['password'])
            new_user = User(
                email=data['email'],
                password=hashed_password,
                nombre=data['nombre'],
                username=data['username'],
                id_departamento=data['id_departamento'],
                id_rol=data['id_rol']
            )
            
            new_user.save()

            return {'msg': 'Usuario registrado exitosamente'}, 201

        except Exception as e:
            return {'msg': 'Error al registrar usuario'}, 500
    