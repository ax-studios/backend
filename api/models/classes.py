from app import db,api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid


class Class(db.Model):
    __tablename__ = "classes"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    subject_teacher = db.relationship('SubjectTeacher',secondary='class_to_subject_teacher',back_populates='classes')

    def jsonify(self):
        return {
            'id' : self.id,
            'name' : self.name,
        }




