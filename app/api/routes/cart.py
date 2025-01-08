from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_to_cart(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    # Add logic to add product to cart (e.g., inserting into a cart table)
    return {"message": "Product added to cart", "user_id": user_id, "product_id": product_id, "quantity": quantity}
