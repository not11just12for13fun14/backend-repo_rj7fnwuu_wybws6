"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Literal

# Example schemas (kept for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Moroccan Cybersecurity community schemas

class Breach(BaseModel):
    """Security breach record"""
    id: Optional[str] = Field(None, description="Document id (optional)")
    target: str = Field(..., description="Target organization or system")
    description: str = Field(..., description="Short description of the breach")
    usefulness: Optional[bool] = Field(False, description="Whether the intel was useful")
    date: Optional[str] = Field(None, description="ISO date string of the breach")

class Stream(BaseModel):
    id: str
    title: str
    description: str
    videoId: str
    date: str
    duration: str
    host: str
    tags: List[str] = []
    type: Literal['upcoming','past'] = 'past'

class Article(BaseModel):
    title: str
    slug: str
    excerpt: str
    author: str
    authorAvatar: str
    publishedAt: str
    categories: List[str] = []
    tags: List[str] = []
    content: str

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
