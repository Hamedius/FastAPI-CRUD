from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash



def create(request: schemas.User, db: Session):
    new_user = models.User(username = request.username, first_name = request.first_name,
                           last_name = request.last_name, email = request.email,
                           password = Hash.bcrypt(request.password), national_id = request.national_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return 'user created'


def destroy(id: int, db: Session):
    deleted_user = db.query(models.User).filter(models.User.id == id)
    if not deleted_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user Not Found!')
    
    deleted_user.delete(synchronize_session=False)
    db.commit()
    return 'user Deleted'



def show(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return user



def update(id: int, request: schemas.User, db: Session):
    updated_user = db.query(models.User).filter(models.User.id == id)
    if not updated_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user Not Found!')
    updated_user.update(request.dict())
    db.commit()
    return 'Updated succesfully!'


