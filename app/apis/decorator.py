from functools import wraps
from flask import abort, request, current_app as app

from app.utils.utils import decode_auth_token, encode_auth_token


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = request.headers.get("Authorization")
        if auth_token:
            token = auth_token.split(" ")[1]
        payload = decode_auth_token(token)
        if payload == "expired":
            abort(401, "Expired Token")
        elif payload == "invalid" or payload == "blacklisted":
            abort(401, "Invalid Token")
        setattr(decorated, "username", payload["username"])
        return f(*args, **kwargs)
    return decorated
