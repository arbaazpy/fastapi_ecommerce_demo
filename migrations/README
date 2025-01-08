### Project Setup

#### **Step 1: Initializing the Project**

```bash
# Create project directory and navigate into it
mkdir fastapi-ecommerce
cd fastapi-ecommerce

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # For Windows use `env\Scripts\activate`

# Install FastAPI, Uvicorn, and other dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-multipart passlib bcrypt python-dotenv aioredis alembic

# Create project directories
mkdir app app/api app/models app/services app/core app/tasks

# Add __init__.py files to make directories Python packages
for dir in app app/api app/models app/services app/core app/tasks; do
  touch "$dir/__init__.py"
done
```

---

### Database Setup

#### **Step 1: Creating the Database**

1. Open PostgreSQL shell or a GUI tool (e.g., pgAdmin).
2. Run the following command to create a new database:

   ```sql
   CREATE DATABASE ecommerce_db;
   ```

3. Update the `.env` file with the database URL:

   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ecommerce_db
   SECRET_KEY=your_secret_key_here
   ```

---

### Alembic Setup

#### **Step 1: Initialize Alembic**

```bash
alembic init migrations
```

This creates a `migrations/` folder and an `alembic.ini` file.

#### **Step 2: Configure `alembic.ini`**

Open `alembic.ini` and replace the `sqlalchemy.url` line with:

```ini
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/ecommerce_db
```

Alternatively, modify `migrations/env.py` to dynamically load the URL from the `.env` file:

```python
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.config import settings
from app.core.database import Base  # Import your Base
from app.models.user import User  # Import all models
from app.models.product import Product

from dotenv import load_dotenv
load_dotenv(".env")

config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

#### **Step 3: Create and Apply the Initial Migration**

1. Generate the initial migration:

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. Apply the migration:

   ```bash
   alembic upgrade head
   ```

This creates the tables in your PostgreSQL database.

#### **Step 4: Verify Tables**

Connect to your PostgreSQL database and list the tables to verify:

```bash
psql -U postgres -d ecommerce_db
```

```sql
\d
```

You should see `users` and `products` tables listed.

---

### Running the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

---

### Example API Endpoints

1. **Signup**
   - **Endpoint**: `POST /auth/signup`
   - **Request Body**:
     ```json
     {
       "username": "example_user",
       "email": "user@example.com",
       "password": "password123"
     }
     ```

2. **Login**
   - **Endpoint**: `POST /auth/login`
   - **Request Body**:
     ```json
     {
       "username": "example_user",
       "password": "password123"
     }
     ```
   - **Response**:
     ```json
     {
       "access_token": "<JWT_TOKEN>",
       "token_type": "bearer"
     }
     ```

3. **Create Product**
   - **Endpoint**: `POST /products/create`
   - **Request Body**:
     ```json
     {
       "name": "Product 1",
       "description": "This is a sample product",
       "price": 100.0,
       "stock": 10
     }
     ```

4. **Get Product**
   - **Endpoint**: `GET /products/{product_id}`

---

### Environment Configuration

#### **.env File Example**

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ecommerce_db
SECRET_KEY=your_secret_key_here
```
