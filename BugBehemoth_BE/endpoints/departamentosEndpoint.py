from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.departamento import Departamento

departamentos_ns = Namespace('departamentos', description="endpoint de departamentos")


@departamentos_ns.route('/all')
class DepartamentosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            departamentos = Departamento.query.all()

            return jsonify([departamento.serialize() for departamento in departamentos])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('nombre'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_departamento = Departamento(
                nombre=data['nombre']
            )
            
            new_departamento.save()

            return {'msg': 'Departamento registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar departamento'}, 500
        

@departamentos_ns.route('id_departamento/<int:id_departamento>')
class DepartamentoResource(Resource):
    @jwt_required()
    def get(self, id_departamento):
        try:
            
            departamento = Departamento.query.get(id_departamento)
            if departamento is None:
                return {'msg': 'Departamento no encontrado'}, 404

            return jsonify(departamento.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_departamento):

        try:
            data = request.get_json()

            departamento = Departamento.query.get(id_departamento)

            if departamento is None:
                return {'msg': 'Tarea no encontrado'}, 404
            
            if(not data or not data.get('nombre') or not data.get('estatus')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_nombre= data.get('nombre')
            new_estatus = data.get('estatus')

            departamento.update(self, new_nombre, new_estatus)
            
            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el departamento'}, 500