from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas




def create(request: schemas.Product, db: Session):
    new_product = models.Product(product_id = request.product_id, name = request.name, price = request.price, description = request.description)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def show(id: int, db: Session):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


def destroy(id: int, db: Session):
    deleted_product = db.query(models.Product).filter(models.Product.id == id)
    if not deleted_product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Product Not Found!')
    
    deleted_product.delete(synchronize_session=False)
    db.commit()
    return 'Product Deleted'


def update(id: int, request: schemas.Product, db: Session):
    updated_product = db.query(models.Product).filter(models.Product.id == id)
    if not updated_product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='product Not Found!')
    updated_product.update(request.dict())
    db.commit()
    return 'Updated succesfully!'


