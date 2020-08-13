"""
Domain objects used by the accounts app.

These classes map to Django models, but have no dependency on an ORM. We use the attrs package to
construct simple, readable entity classes: "All attrs does is take your declaration, write dunder
methods based on that information, and attach them to your class."
"""

from datetime import date
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """User is the object identifying each person who has signed up for Topsy."""

    email: str
    name: str
    id: Optional[int] = None
    created_at: Optional[date] = None
    modified_at: Optional[date] = None
    is_active = True
    is_admin = False
    last_login: Optional[date] = None
    status = "active"
