from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.tareas import Tareas

tareas_ns = Namespace('tareas', description="endpoint de tareas")

tareas_ns.route('/all')
class TareasResource(Resource):
    @jwt_required()
    def get(self):
        try:
            tareas = Tareas.query.all()

            return jsonify([tarea.serialize() for tarea in tareas])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('id_proyecto') or not data.get('responsable') or not data.get('descripcion'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_tarea = Tareas(
                email=data['email'],
                nombre=data['nombre'],
                username=data['username'],
                id_departamento=data['id_departamento'],
                id_rol=data['id_rol']
            )
            
            new_tarea.save()

            return {'msg': 'Tarea registrada exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar tarea'}, 500
        
@tareas_ns.route('/id_tarea/<int:id_tarea>')
class TareaResource(Resource):
    @jwt_required()
    def get(self, id_tarea):
        try:
            
            tarea = Tareas.query.get(id_tarea)
            if tarea is None:
                return {'message': 'Tarea no encontrado'}, 404

            return jsonify(tarea.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'message': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_tarea):

        try:
            data = request.get_json()

            tarea = Tareas.query.get(id_tarea)

            if tarea is None:
                return {'msg': 'Tarea no encontrado'}, 404
            
            if(not data or not data.get('id_proyecto') or not data.get('responsable') or not data.get('descripcion')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_id_proyecto = data.get('id_proyecto')
            new_responsable = data.get('responsable')
            new_descripcion = data.get('descripcion')

            tarea.update(self, new_id_proyecto, new_responsable, new_descripcion)

        except Exception as e:
            print(f"Error: {e}")
            return {'message': 'No se pudo actualizar la tarea'}, 500