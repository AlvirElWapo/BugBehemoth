from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.alertas import Alertas

alerlas_ns = Namespace('alertas', description="endpoint de alertas")


@alerlas_ns.route('/all')
class AlertasResource(Resource):
    @jwt_required()
    def get(self):
        try:
            alertas = Alertas.query.all()

            return jsonify([alerta.serialize() for alerta in alertas])
        
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('destinatario') or not data.get('fecha_alerta') or not data.get('tipo'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_alerta = Alertas(
                destinatario=data['destinatario'],
                fecha_alerta=data['fecha_alerta'],
                tipo=data['tipo'],
            )
            
            new_alerta.save()

            return {'msg': 'Alerta registrada exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar tarea'}, 500
        

@alerlas_ns.route('id_alerta/<int:id_alerta>')
class AlertaResource(Resource):
    @jwt_required()
    def get(self, id_alerta):
        try:
            
            alerta = Alertas.query.get(id_alerta)
            if alerta is None:
                return {'msg': 'Alerta no encontrado'}, 404

            return jsonify(alerta.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def put(self, id_alerta):

        try:
            data = request.get_json()

            alerta = Alertas.query.get(id_alerta)

            if alerta is None:
                return {'msg': 'Alerta no encontrada'}, 404
            
            if(not data or not data.get('estatus')):
                return {'msg': 'Faltan datos en la solicitud'}, 400
            
            new_estatus = data.get('estatus')

            alerta.update(self, new_estatus)
            
            return {'msg': 'Actualización de datos exitosamente'}, 200

        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo actualizar la alerta'}, 500