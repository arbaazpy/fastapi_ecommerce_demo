from fastapi import APIRouter, BackgroundTasks
from app.tasks.email_tasks import send_order_confirmation

router = APIRouter()

@router.post("/orders")
def create_order(order_id: int, user_email: str, background_tasks: BackgroundTasks):
    # Add order creation logic here
    background_tasks.add_task(send_order_confirmation, order_id, user_email)
    return {"message": "Order created successfully"}
