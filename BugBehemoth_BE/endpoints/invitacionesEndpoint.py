from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, request
from models.invitaciones import Invitaciones

invitaciones_ns = Namespace('invitaciones', description="endpoint de invitaciones")


@invitaciones_ns.route('/all')
class InvitacionesResource(Resource):
    @jwt_required()
    def get(self):
        try:
            invitaciones = Invitaciones.query.all()

            return jsonify([invitacion.serialize() for invitacion in invitaciones])
        except Exception as e:
            return {'msg': 'No se pudo hacer la consulta'}, 500
        
    def post(self):
        data = request.get_json()

        if not data or not data.get('id_evento') or not data.get('id_invitado'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        try:

            new_invitacion = Invitaciones(
                id_evento=data['id_evento'],
                id_invitado=data['id_invitado'],
            )
            
            new_invitacion.save()

            #colocar codigo de envio a email

            return {'msg': 'Tarea registrada exitosamente'}, 200

        except Exception as e:
            return {'msg': 'Error al registrar tarea'}, 500
        

@invitaciones_ns.route('id_invitacion/<int:id>')
class InvitacionResource(Resource):
    @jwt_required()
    def get(self, id):
        try:
            
            invitacion = Invitaciones.query.get(id)
            if invitacion is None:
                return {'msg': 'Invitación no encontrado'}, 404

            return jsonify(invitacion.serialize())
        
        except Exception as e:
            
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500