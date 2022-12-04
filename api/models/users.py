from app import db

from ..models import SubjectTeacher, Class
from sqlalchemy import *

import sqlalchemy.dialects.postgresql as psql

import uuid


class User(db.Model):
    __tablename__ = "users"

    # Basic user info
    id = db.Column(
        psql.UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_no = db.Column(db.String(15), unique=True, nullable=False)
    roles = db.Column(psql.ARRAY(db.String(10)), default=[])

    todos = db.relationship("Todo", back_populates="owner")

    # Login info
    username = db.Column(String(80), unique=True, nullable=False)
    # password = db.Column(String(120), nullable=False)

    def __init__(self, **kwargs):
        kwargs["email"] = kwargs["email"].lower()
        kwargs["mobile_no"] = kwargs["mobile_no"].lower()
        super().__init__(**kwargs)

    def jsonify(self, parents):
        return {
            "name": self.name,
            "mobile_no": self.mobile_no,
            "email": self.email,
            "username": self.username,
            "todos": [todo.jsonify(["users"]) for todo in self.todos]
            if "todos" not in parents
            else None,
        }
