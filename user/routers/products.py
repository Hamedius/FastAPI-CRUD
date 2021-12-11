from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import products


router = APIRouter(tags=['Products'], prefix="/product")
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Product, db: Session = Depends(get_db)):
    return products.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowProduct)
def show(id:int, db: Session = Depends(get_db)):
    return products.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return products.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Product, db: Session = Depends(get_db)):
    return products.update(id, request, db)