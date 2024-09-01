from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.recursos import Recursos

recursos_ns = Namespace('recursos', description="endpoint de recursos")

@recursos_ns.route('/all')
class RecursosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            recursos = Recursos.query.all()

            return jsonify([recurso.serialize() for recurso in recursos])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('nombre') or not data.get('cantidad_total') or not data.get('cantidad_disponible'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_recurso = Recursos(
                nombre=data['nombre'],
                cantidad_total=data['cantidad_total'],
                cantidad_disponible=data['cantidad_disponible']
            )
            
            new_recurso.save()

            return {'msg': 'Recurso registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar recurso'}, 500
        

@recursos_ns.route('id_recurso/<int:id_recurso>')
class RecursoResource(Resource):
    @jwt_required()
    def get(self, id_recurso):
        try:
            
            recurso = Recursos.query.get(id_recurso)
            if recurso is None:
                return {'msg': 'recurso no encontrado'}, 404

            return jsonify(recurso.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_recurso):

        try:
            data = request.get_json()

            recurso = Recursos.query.get(id_recurso)

            if recurso is None:
                return {'msg': 'Recurso no encontrado'}, 404
            
            if(not data or not data.get('nombre') or not data.get('cantidad_total') or not data.get(' cantidad_disponible')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_nombre= data.get('nombre')
            new_cantidad_total = data.get('cantidad_total')
            new_cantidad_disponible = data.get(' cantidad_disponible')

            recurso.update(self, new_nombre, new_cantidad_total, new_cantidad_disponible)

            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el recurso'}, 500