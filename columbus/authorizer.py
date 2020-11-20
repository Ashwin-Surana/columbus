import jwt
import datetime


class Authorizer:
    def __init__(self, secret, bearer, exp=1):
        self.secret = secret
        self.bearer = bearer
        self.expiry = exp

    def encode_auth(self, params):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=self.expiry),
            'iat': datetime.datetime.utcnow(),
            'sub': params
        }
        token = jwt.encode(payload, self.secret, algorithm='HS256')
        return token

    def decode_auth(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Login please'
        except jwt.InvalidTokenError:
            return 'Invalid token. Login please'
