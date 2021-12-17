from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import users


router = APIRouter(tags=['Users'], prefix="/user")
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.destroy(id, db)



@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show(id:int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.show(id, db)




@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.update(id, request, db)