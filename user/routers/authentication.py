from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session


router = APIRouter(tags=['Login'], prefix="/login")

@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials!')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password!')



    access_token = token.create_access_token(data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}