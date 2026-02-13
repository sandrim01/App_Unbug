from api.database import SessionLocal, engine, Base
from api import models, auth_utils
from datetime import datetime

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Create Admin
    admin = db.query(models.User).filter(models.User.username == "admin").first()
    if not admin:
        admin = models.User(
            username="admin",
            email="admin@unbug.com.br",
            hashed_password=auth_utils.get_password_hash("admin123"),
            role="admin"
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print("Admin user created: admin / admin123")

    # Create dummy stats/data for the "WOW" effect
    if not db.query(models.Client).first():
        client = models.Client(name="TechCorp Solutions", document="12.345.678/0001-90", email="contato@techcorp.com")
        db.add(client)
        db.commit()
    
    db.close()

if __name__ == "__main__":
    seed()
