from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Text, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user") # admin, management, tech, financial
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    employee = relationship("Employee", back_populates="user", uselist=False)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    department = Column(String)
    phone = Column(String)
    hire_date = Column(Date)
    is_active = Column(Boolean, default=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="employee")

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(String, unique=True) # CPF/CNPJ
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    service_orders = relationship("ServiceOrder", back_populates="client")
    projects = relationship("Project", back_populates="client")

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(String, unique=True)
    contact_name = Column(String)
    email = Column(String)
    phone = Column(String)
    category = Column(String)
    active = Column(Boolean, default=True)

class ServiceOrder(Base):
    __tablename__ = "service_orders"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="pending") # pending, in_progress, completed, cancelled
    priority = Column(String, default="medium") # low, medium, high, urgent
    
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="service_orders")
    
    tech_id = Column(Integer, ForeignKey("employees.id"))
    # tech = relationship("Employee")
    
    created_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="planning") # planning, active, on_hold, completed
    
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="projects")

class StockItem(Base):
    __tablename__ = "stock_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, unique=True)
    category = Column(String)
    quantity = Column(Float, default=0)
    min_quantity = Column(Float, default=0)
    unit_price = Column(Numeric(10, 2))
    location = Column(String)

class FinancialEntry(Base):
    __tablename__ = "financial_entries"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False) # income, expense
    category = Column(String)
    amount = Column(Numeric(10, 2), nullable=False)
    description = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)
    
    # Optional relationships
    client_id = Column(Integer, ForeignKey("clients.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="open") # open, pending, resolved, closed
    priority = Column(String, default="medium")
    
    client_id = Column(Integer, ForeignKey("clients.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    created_at = Column(DateTime, default=datetime.utcnow)
