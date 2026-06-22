from math import trunc

from passlib.context import CryptContext

passwd_context = CryptContext(
    schemes=['bcrypt']
)

def generate_passwd_hash(password : str) -> str:
    passwd_hash = passwd_context.hash(password)
    return passwd_hash

def verify_passwd(password : str, hash : str) -> str:
    return passwd_context.verify(password,hash)