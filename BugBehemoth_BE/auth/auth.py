from flask import jsonify, request, make_response
from flask_restx import Resource, Namespace
from flask_jwt_extended import (
    create_access_token, create_refresh_token, 
    set_refresh_cookies, unset_jwt_cookies,
    get_jwt_identity, jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User

auth_ns = Namespace('auth', description="Atenticación de usaurio")

@auth_ns.route('/login')
class LoginUser(Resource):
    def post(self):
        data = request.get_json()
        print(data);

        if not data or not data.get('email') or not data.get('password'):
            return {'msg':'Faltan datos en la solicitud'}, 401
        
        email = data['email']
        db_user = User.query.filter(User.email==email).first()
        
        if not db_user:
            return {'msg':'Credenciales incorrectas'}, 401
        print()
        
        try:
            if check_password_hash(db_user.password, data['password']):
                acces_tkn = create_access_token(identity=db_user.username)
                refresh_tkn = create_refresh_token(identity=db_user.username)
                
                response = jsonify({
                    "acces_tkn": acces_tkn,
                    "rol":db_user.role.serialize() if db_user.role else None
                })
                set_refresh_cookies(response,refresh_tkn)
                
                return response
            else:
                return {'msg':'Credenciales incorrectas'}, 401
        except Exception as e:
            return {'msg': 'Error al inciar sesión'}, 500

@auth_ns.route('/refresh')
class RefreshUser(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        db_user = User.query.filter(User.username == current_user).first()

        if not db_user:
            return {'msg':'Credenciales incorrectas'}, 401
        
        try:
            new_acces_tkn = create_access_token(identity=current_user)
            response = jsonify({
                    "acces_tkn": new_acces_tkn,
                    "rol":db_user.rol.rol
                })
            return make_response(response,200)
        except Exception as e:
            return{'msg':'Error en iniciar'}, 500
        
@auth_ns.route('/exit')
class ExitUser(Resource):
    @jwt_required(refresh=True)
    def delete(self):
        response= jsonify({"msg":"Sessión cerrada"})
        unset_jwt_cookies(response)

        return make_response(response,200)
