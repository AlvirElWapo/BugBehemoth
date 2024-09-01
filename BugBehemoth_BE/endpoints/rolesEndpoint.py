from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.roles import Role

roles_ns = Namespace('roles', description="endpoint de roles")

@roles_ns.route('/all')
class RolesResource(Resource):
    @jwt_required()
    def get(self):
        try:
            roles = Role.query.all()

            return jsonify([rol.serialize() for rol in roles])
        
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('rol'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_rol = Role(
                rol=data['rol']
            )
            
            new_rol.save()

            return {'msg': 'Rol registrada exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar Rol'}, 500
        

@roles_ns.route('/id_rol/<int:id_rol>')
class roleResource(Resource):
    @jwt_required()
    def get(self, id_rol):
        try:
            
            role = Role.query.get(id_rol)
            if role is None:
                return {'message': 'Tarea no encontrado'}, 404

            return jsonify(role.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_rol):

        try:
            data = request.get_json()

            role = Role.query.get(id_rol)

            if role is None:
                return {'msg': 'rol no encontrado'}, 404
            
            if(not data or not data.get('rol') or not data.get('estatus')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_rol = data.get('rol')
            new_estatus = data.get('estatus')

            role.update(self, new_rol, new_estatus)

            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'No se pudo actualizar el rol'}, 500