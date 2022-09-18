from app import db,api
from ..models import SubjectTeacher
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid


class Subject(db.Model):
    __tablename__ = "subjects"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    teachers = db.relationship('Teacher', secondary='subject_teacher', back_populates='subjects')

    def jsonify(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }

