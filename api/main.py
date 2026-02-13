from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from api.config import settings
from api.database import engine, Base, get_db
from api.models import User, Employee
from api.routes import auth
import uvicorn

app = FastAPI(
    title="Unbug ERP API",
    description="Modern Management System for Unbug Solutions TI",
    version="2.0.0"
)

# CORS configuration for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Adaptar para prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Unbug ERP API",
        "status": "online",
        "documentation": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
