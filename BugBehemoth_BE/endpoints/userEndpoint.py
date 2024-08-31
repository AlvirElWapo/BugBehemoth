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


@user_ns.route('/<int:id_user>')
class UserResource(Resource):
    def get(self, id_user):
        try:
            
            user = User.query.get(id_user)
            if user is None:
                return {'message': 'Usuario no encontrado'}, 404

            return jsonify(user.serialize())
        except Exception as e:
            
            print(f"Error: {e}")
            return {'message': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_user):
        try:

            data = request.get_json()
            
            user = User.query.get(id_user)

            if user is None:
                return {'msg': 'Usuario no encontrado'}, 404

            if (not data or not data.get('email') or not data.get('nombre') 
                or not data.get('username') or not data.get('id_departamento') or not data.get('id_rol')):
                return {'msg': 'Faltan datos en la solicitud'}, 400

            new_username = data.get('username')
            new_email = data.get('email')
            new_nombre = data.get('nombre')
            new_id_departamento = data.get('id_departamento')
            new_id_rol = data.get('id_rol')

            if new_username and User.query.filter_by(username=new_username).first() and new_username != user.username:
                return {'msg': 'El nombre de usuario ya está en uso'}, 400

            if new_email and User.query.filter_by(email=new_email).first() and new_email != user.email:
                return {'msg': 'El correo electrónico ya está en uso'}, 400

            user.update(new_username, new_email, new_nombre, new_id_rol, new_id_departamento)

            return {'msg': 'Se actualizó con exito el usuario'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'No se pudo actualizar el usuario'}, 500