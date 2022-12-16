import pytz
from api.models.users import User
from app import db
from sqlalchemy import ForeignKey
import sqlalchemy.dialects.postgresql as psql
import uuid


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(
        psql.UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    title = db.Column(db.String)
    description = db.Column(db.String)
    priority = db.Column(db.Integer)
    due_date = db.Column(psql.TIMESTAMP)
    owner_id = db.Column(psql.UUID(as_uuid=True), ForeignKey("users.id"))

    owner: User = db.relationship("User", back_populates="todos")

    def jsonify(self, parents):
        result = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": str(self.due_date.isoformat()),
            "owner": self.owner.jsonify(parents + [self.__tablename__])
            if "users" not in parents
            else None,
        }
        return result
