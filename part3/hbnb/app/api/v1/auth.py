from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade
from flask_bcrypt import check_password_hash
from flask import request

api = Namespace('auth', description='Opérations d\'authentification')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='Email de l\'utilisateur'),
    'password': fields.String(required=True, description='Mot de passe de l\'utilisateur')
})

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_model)
    def post(self):
        """Authentifie un utilisateur et retourne un token JWT"""
        data = api.payload
        
        user = facade.get_user_by_email(data.get('email'))

        if user:
            print(f"DEBUG: Utilisateur trouvé -> {user.email}")
            is_valid = check_password_hash(user.password, data.get('password'))
            print(f"DEBUG: Mot de passe valide ? -> {is_valid}")
            
            if is_valid:
                access_token = create_access_token(
                    identity=str(user.id), 
                    additional_claims={'is_admin': getattr(user, 'is_admin', False)}
                )
                
                return {'access_token': access_token}, 200
        else:
            print("DEBUG: Utilisateur non trouvé ou mot de passe incorrect")

        return {'message': 'Invalid email or password'}, 401

    def options(self):
        """Gère la requête de pré-vérification CORS (Preflight)"""
        return {'message': 'OK'}, 200