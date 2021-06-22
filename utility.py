import jwt
secretkey='poojasecretkey'
def jwtEncode(contact):
    token = jwt.encode({'contact': contact}, secretkey)
    print(token)
    return token

def jwtDecode(token):
    dec = jwt.decode(token, secretkey, 'HS256')
    print(dec)
    return dec

if __name__ == '__main__':
    token=jwtEncode(9088554022)
    jwtDecode(token)
