import jwt
import jwt.exceptions

data = {'language': 'Python'}
secret = 'acelera'


def create_token(data, secret):
    return jwt.encode(data, key=secret, algorithm="HS256")


def verify_signature(token):
    try:
        return jwt.decode(token, key=secret, algorithm="HS256")

    except jwt.InvalidSignatureError:
        return {"error": 2}
