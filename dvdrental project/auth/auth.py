from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt



ALGORITHM = "HS256"
SECRET_KEY = "NARESH_123456789"
ACCESS_EXPIRE_MINUTES = 60


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password: str) :
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) :
    return pwd_context.verify(plain_password, hashed_password)


def create_token(username: str, email: str):
    payload = {
        "sub": username,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    return username

    
        


