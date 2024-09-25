from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schema import ProductListValidate
from typing import List
from models import Product

app = FastAPI(title='Mysite')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/create/', response_model=ProductListValidate)
def create_product(product: ProductListValidate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get('/products/', response_model=List[ProductListValidate])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@app.get('/products/{product_id}', response_model=ProductListValidate)
def read_car(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail='product not found')
    else:
        return product


@app.put('/product/update/{product_id}', response_model=ProductListValidate)
def update_car(product_id: int, product: ProductListValidate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail='product not found')

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete('/cars/delete/{car_id}', response_model=ProductListValidate)
def delete_car(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()

    if db_product is None:
        raise HTTPException(status_code=404, detail='product not found')

    db.delete(db_product)
    db.commit()
    return db_product
