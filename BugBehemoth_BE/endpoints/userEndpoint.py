from flask_restx import Namespace, Resource
from flask import Flask, jsonify
from models.user import User

user_ns = Namespace('users', description="endpoint para users")

@user_ns.route('/all')
class usersResourse(Resource):
    def get(self):
        try:
            users = User.query.all()

            return jsonify([user.serialize() for user in users])
        except Exception as e:
            print(f"Error: {e}")
            return {'msg': 'No se pudo hacer la consulta'}, 500