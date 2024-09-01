from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.asignacionProyecto import AsignacionProyecto

asignacionproyecto_ns = Namespace('asignacionproyecto', description="endpoint de asignación de proyectos")



asignacionproyecto_ns.route('/all')
class AsignacionProyectosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            asignaciones = AsignacionProyecto.query.all()

            return jsonify([asignacion.serialize() for asignacion in asignaciones])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('id_user') or not data.get('id_proyecto'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_asignacion = AsignacionProyecto(
                id_user=data['id_user'],
                id_proyecto=data['id_proyecto']
            )
            
            new_asignacion.save()
            #codigo para enviar correo

            return {'msg': 'Asignacion de proyecto registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar Asignación'}, 500
        

@asignacionproyecto_ns.route('id_asignacion/<int:id_asignacion>')
class AsignacionProyectoResource(Resource):
    @jwt_required()
    def get(self, id_asignacion):
        try:
            
            asignacion = AsignacionProyecto.query.get(id_asignacion)
            if asignacion is None:
                return {'msg': 'Asignacion no encontrado'}, 404

            return jsonify(asignacion.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_asignacion):

        try:
            data = request.get_json()

            asignacion = AsignacionProyecto.query.get(id_asignacion)

            if asignacion is None:
                return {'msg': 'Asginación no encontrado'}, 404
            
            if(not data or not data.get('id_user') or not data.get('id_proyecto') or not data.get('estatus')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_id_user = data.get('id_user')
            new_id_proyecto = data.get('id_proyecto')
            new_estatus = data.get('estatus')

            asignacion.update(self, new_id_user, new_id_proyecto, new_estatus)
            
            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar la asignación'}, 500