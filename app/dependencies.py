from fastapi import Header, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from jose import jwt
from .models import User
from sqlalchemy.future import select

# Security settings
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "YOUR_SECRET_KEY_HERE"
ALGORITHM = "HS256"

# Dependency for getting the current user from the token
async def get_current_user(security_scopes: SecurityScopes, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except JWTError:
        raise credentials_exception

    user = await db.execute(select(User).filter(User.username == token_data.username))
    user = user.scalars().first()
    if user is None:
        raise credentials_exception
    
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=403,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": "Bearer"},
            )
    return user

# Dependency for getting a database session
async def get_db_session():
    async with get_db() as session:
        yield session
