from flask_restx import Namespace, Resource
from datetime import datetime

api = Namespace('example', description='Example operations')

@api.route('/time')
class TimeResource(Resource):
    def get(self):
        # Get the current server time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Return the time as a JSON response
        return {'server_time': current_time}
