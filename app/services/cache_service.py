import aioredis

redis = aioredis.from_url("redis://localhost:6380")

async def get_cached_product(product_id: int):
    cached_product = await redis.get(f"product:{product_id}")
    if cached_product:
        return cached_product
    return None

async def set_cached_product(product_id: int, product_data: dict):
    await redis.set(f"product:{product_id}", product_data, ex=3600)  # Cache for 1 hour
