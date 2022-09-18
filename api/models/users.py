from email.policy import default
from app import db

from ..models import SubjectTeacher
from sqlalchemy import *

import sqlalchemy.dialects.postgresql as psql

import uuid


class User(db.Model):
    __tablename__ = 'users'

    # Basic user info
    id = db.Column(psql.UUID(as_uuid=True), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_no = db.Column(db.String(15), unique=True, nullable=False)
    role = db.Column(db.String(15), nullable=False)

    # Login info
    # username = db.Column(String(80), unique=True, nullable=False)
    # password = db.Column(String(120), nullable=False)

    # Connect child tables
    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'polymorphic_on': role
    }

    def jsonify(self):
        return {
            "username": self.username,
            "email": self.email
        }


class Student(User):
    __tablename__ = 'students'

    id = db.Column(psql.UUID, db.ForeignKey('users.id'), primary_key=True)
    enroll_no = db.Column(db.String(10), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    class_ = db.relationship('Class', back_populates='students')



    __mapper_args__ = {
        'polymorphic_identity': 'students',
    }

    def jsonify(self):
        return {
            "name": self.name,
            "mobile_no": self.mobile_no,
            "email": self.email,
            "enroll_no": self.enroll_no
        }


class Teacher(User):
    __tablename__ = 'teachers'

    id = db.Column(psql.UUID, db.ForeignKey('users.id'), primary_key=True)

    subjects = db.relationship(
        'Subject', secondary='subject_teacher', back_populates='teachers')

    __mapper_args__ = {
        'polymorphic_identity': 'teachers',
    }

    def jsonify(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "class_id": self.class_id
        }
