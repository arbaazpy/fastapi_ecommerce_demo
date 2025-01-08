from fastapi import FastAPI
from app.api.routes import auth, orders, products, cart
from app.core.database import Base, engine
from app.models.user import User
from app.models.product import Product


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include API routers
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)
