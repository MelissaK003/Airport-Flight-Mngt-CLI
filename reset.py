from sqlalchemy import create_engine
from app.models import Base

# Replace with your actual database path
DATABASE_URL = 'sqlite:///your_database.db'

# Create an engine connected to your SQLite database
engine = create_engine(DATABASE_URL)

# Drop all existing tables (be careful as this will remove all data!)
Base.metadata.drop_all(engine)

# Recreate the tables according to your models.py
Base.metadata.create_all(engine)

print("Database has been reset.")
