from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.eventos import Eventos

eventos_ns = Namespace('eventos', description="endpoint de eventos")

@eventos_ns.route('/all')
class EventosResource(Resource):
    @jwt_required()
    def get(self):
        try:
            eventos = Eventos.query.all()

            return jsonify([evento.serialize() for evento in eventos])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('fecha') or not data.get('descripcion'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_evento = Eventos(
                fecha=data['fecha'],
                descripcion=data['descripcion']
            )
            
            new_evento.save()

            return {'msg': 'Evento registrado exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar evento'}, 500
        

@eventos_ns.route('id_evento/<int:id_evento>')
class EventoResource(Resource):
    @jwt_required()
    def get(self, id_evento):
        try:
            
            evento = Eventos.query.get(id_evento)
            if evento is None:
                return {'msg': 'Evento no encontrado'}, 404

            return jsonify(evento.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_evento):

        try:
            data = request.get_json()

            evento = Eventos.query.get(id_evento)

            if evento is None:
                return {'msg': 'Evento no encontrado'}, 404
            
            if(not data or not data.get('fecha') or not data.get('descripcion')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_fecha = data.get('fecha')
            new_descripcion = data.get('descripcion')

            evento.update(self, new_fecha, new_descripcion)
            
            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar el evento'}, 500