from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.proyectos import Proyecto

proyectos_ns = Namespace('proyectos', description="endpoint de proyectos")


@proyectos_ns.route('/all')
class ProyectosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            proyectos = Proyecto.query.all()

            return jsonify([proyecto.serialize() for proyecto in proyectos])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if (not data or not data.get('nombre') or not data.get(' id_user_director') or not data.get('fecha_expira')
            or not data.get('descripcion')):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_proyecto = Proyecto(
                nombre=data['nombre'],
                id_user_director=data[' id_user_director'],
                username=data['fecha_expira'],
                id_departamento=data['descripcion']
            )
            
            new_proyecto.save()

            return {'msg': 'Proyecto registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar proyecto'}, 500
        

@proyectos_ns.route('id_proyecto/<int:id_proyecto>')
class ProyectoResource(Resource):
    @jwt_required()
    def get(self, id_proyecto):
        try:
            
            proyecto = Proyecto.query.get(id_proyecto)
            if proyecto is None:
                return {'msg': 'Proyecto no encontrado'}, 404

            return jsonify(proyecto.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_proyecto):

        try:
            data = request.get_json()

            proyecto = Proyecto.query.get(id_proyecto)

            if proyecto is None:
                return {'msg': 'Proyecto no encontrado'}, 404
            
            if(not data or not data.get('nombre') or not data.get('fecha_expira') or not data.get('descripcion')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_nombre = data.get('nombre')
            new_fecha_expira = data.get('fecha_expira')
            new_descripcion = data.get('descripcion')

            proyecto.update(self, new_nombre, new_fecha_expira, new_descripcion)

            return {'msg': 'Actualización de datos exitosamente'}, 200
        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar la tarea'}, 500