import jwt
secretkey='poojasecretkey'
def encode(contact):
    token = jwt.encode({'contact': contact}, secretkey)
    print(token)
    return token

def decode(token):
    dec = jwt.decode(token, secretkey, 'HS256')
    print(dec)
    return dec

token=encode(9088554022)
decode(token)