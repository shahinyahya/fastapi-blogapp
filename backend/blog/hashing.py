from passlib.context import CryptContext

""" Create Hashed passwords by declaring password context from passlib """

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    
    def password_hash(password: str):
        return pwd_context.hash(password)
    
    def verify_password(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)