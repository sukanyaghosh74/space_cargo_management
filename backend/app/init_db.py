from app.database import engine, Base
from app.models import Item, Container, Log

print("Creating Database Tables...")
Base.metadata.create_all(bind=engine)
print("Tables Created Successfully!")
