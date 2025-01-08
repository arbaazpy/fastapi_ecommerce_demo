from fastapi import BackgroundTasks

def send_order_confirmation(order_id: int, user_email: str):
    # Simulate sending email
    print(f"Sending order confirmation for order {order_id} to {user_email}")
