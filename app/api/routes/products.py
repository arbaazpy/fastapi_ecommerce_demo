from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.services.dependencies import get_db, require_admin

router = APIRouter()


@router.post("/create", dependencies=[Depends(require_admin)])
def create_product(name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price, stock=stock)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"id": product.id, "name": product.name, "price": product.price}

@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
