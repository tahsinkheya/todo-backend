from datetime import datetime, timedelta
from flask import current_app
import jwt
def encode_auth_token(username):
    try: 
        payload={'exp':datetime.utcnow()+timedelta(seconds=3600, days=0 ),
                 'iat': datetime.utcnow(),
                 'username':username
                 }
        token= jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token
    except Exception as e:
        return e
    
def decode_auth_token(token):
    current_app.logger.info(current_app.config['SECRET_KEY'])
    try:
        payload= jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError as e:
        return "expired"
    except jwt.InvalidTokenError as e:
        current_app.logger.info(e)
        return "invalid"

