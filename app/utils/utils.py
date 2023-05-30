from datetime import datetime, timedelta
from flask import current_app
import jwt
def encode_auth_token(username):
    try: 
        payload={'exp':datetime.utcnow()+timedelta(second=3600, days=0 ),
                 'iat': datetime.utcnow(),
                 'username':username
                 }
        token= jwt.encode(payload, current_app.config['SECRET_KEY'], algorith='HS256')
        return token
    except Exception as e:
        return e
    
def decode_auth_token(token):
    try:
        payload= jwt.decode(token, current_app.config['SECRET_KEY'], algorith='HS256', verify=True)
        return payload
    except jwt.ExpiredSignatureError as e:
        return "expired"
    except jwt.InvalidTokenError as e:
        return "invalid"

