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