from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.recursosTarea import RecursosTarea
from models.recursos import Recursos

recursotarea_ns = Namespace('recursostarea', description="endpoint de recursos tarea")


@recursotarea_ns.route('/all')
class RecursosTareaResource(Resource):
    @jwt_required()
    def get(self):
        try:
            recursos = RecursosTarea.query.all()

            return jsonify([recurso.serialize() for recurso in recursos])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('id_recurso') or not data.get('id_tarea') or not data.get('cantidad'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        
        recurso = Recursos.query.filter(Recursos.id_recurso == data['id_recurso']).first()
        
        cantidad=data.get('cantidad')
        resta = recurso.cantidad_disponible - int(cantidad)

        if resta < 0:
            return {'msg':'No hay recursos suficientes'}, 401

        try:

            new_recurso = RecursosTarea(
                id_recurso=data['id_recurso'],
                id_tarea=data['id_tarea'],
                cantidad=data['cantidad']
            )
            
            new_recurso.save()

            recurso.updateStock(self, resta)

            return {'msg': 'recurso de tarea registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar recurso de tarea'}, 500
        

@recursotarea_ns.route('id_asignacion/<int:id_asignacion>')
class RecursoTarea(Resource):
    @jwt_required()
    def get(self, id_tarea):
        try:
            
            recurso = RecursosTarea.query.get(id_tarea)
            if recurso is None:
                return {'msg': 'Recurso de tarea no encontrado'}, 404

            return jsonify(recurso.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_asignacion):

        try:
            data = request.get_json()

            recursoTarea = RecursosTarea.query.get(id_asignacion)

            if recursoTarea is None:
                return {'msg': 'recurso no encontrado'}, 404
            
            if(not data  or not data.get('responsable') or not data.get('descripcion') or not data.get('estatus')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_id_tarea = data.get('id_tarea')
            new_estatus = data.get('estatus')

            RecursosTarea.update(self, new_id_tarea, new_estatus) 

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el recurso de tarea'}, 500
        

@recursotarea_ns.route('add/<int:id_asignacion>')
class RecursoTareaAdd(Resource):
    @jwt_required()
    def put(self, id_asignacion):
        try:
            data = request.get_json()

            recursoTarea = RecursosTarea.query.get(id_asignacion)

            if recursoTarea is None:
                return {'msg': 'recurso no encontrado'}, 404
            
            if(not data  or not data.get('cantidad')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            recurso = Recursos.query.filter(Recursos.id_recurso == data['id_recurso']).first()
            cantidad=data.get('cantidad')
            resta = recurso.cantidad_disponible - int(cantidad)

            if resta < 0:
                return {'msg':'No hay recursos suficientes'}, 401
            
            new_cantidad = int(data.get('cantidad')) + recursoTarea.cantidad

            RecursosTarea.updateStock(self, new_cantidad) 
            recurso.updateStock(self, resta)

            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el recurso de tarea'}, 500

@recursotarea_ns.route('quitar/<int:id_asignacion>')
class RecursoTareaQuitar(Resource):
    @jwt_required()
    def put(self, id_asignacion):
        try:
            data = request.get_json()

            recursoTarea = RecursosTarea.query.get(id_asignacion)

            if recursoTarea is None:
                return {'msg': 'recurso no encontrado'}, 404
            
            if(not data  or not data.get('cantidad')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            recurso = Recursos.query.filter(Recursos.id_recurso == data['id_recurso']).first()
            cantidad=data.get('cantidad')
            resta = recurso.cantidad_disponible + int(cantidad)

            if resta < 0:
                return {'msg':'No hay recursos suficientes'}, 401
            
            new_cantidad = recursoTarea.cantidad - int(data.get('cantidad'))
            
            if new_cantidad < 0:
                return {'msg':'No hay recursos suficientes'}, 401
            
            RecursosTarea.updateStock(self, new_cantidad) 
            recurso.updateStock(self, resta)

            return {'msg': 'Actualización de datos exitosamente'}, 200
        
        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el recurso de tarea'}, 500