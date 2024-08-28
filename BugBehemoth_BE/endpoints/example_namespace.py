from flask_restx import Namespace, Resource

# Creación del namespace
api = Namespace('example', description='Operaciones relacionadas con el ejemplo')

@api.route('/example')
class ExampleResource(Resource):
    def get(self):
        return {'message': 'Este es un endpoint de ejemplo.'}
