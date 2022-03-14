from http import HTTPStatus
import re
from sqlalchemy.exc import IntegrityError
from flask import current_app, jsonify, request
from app.exceptions import EmailError, PhoneError
from app.models.user_model import UserModel
from app.configs.database import db 

def get_all():
    try:
        all_users: UserModel = UserModel().query.all()
        if len(all_users == 0):
            raise

        return jsonify({'data': all_users}), HTTPStatus.OK

    except:
        return {'msg': 'There is no user registered'}, HTTPStatus.OK

def create_user():
    try:
        session = current_app.db.session
        data = request.get_json()
        data['name'] = data['name'].title()
        data['phone'] = re.sub('\D', '', data['phone'])
        user = UserModel(**data)
        session.add(user)
        session.commit()

        result = {'name': user.name, 'email': user.email, 'phone': user.phone}
        
        return result, HTTPStatus.CREATED
    
    except IntegrityError as err:
        if 'psycopg2.errors.UniqueViolation' in str(err):
            return {'error': 'Email already registered'}, HTTPStatus.CONFLICT
    
    except EmailError as error:
        return error.message, error.code

    except PhoneError as error:
        return error.message, error.code
