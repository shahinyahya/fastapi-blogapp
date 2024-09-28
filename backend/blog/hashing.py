from passlib.context import CryptContext

""" Create Hashed passwords by declaring password context from passlib """

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def password_hash(password: str):
        return pwd_context.hash(password)