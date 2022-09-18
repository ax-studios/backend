from app import db,api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid


class Class(db.Model):
    __tablename__ = "classes"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    subject_teacher = db.relationship('SubjectTeacher',secondary='class_to_subject_teacher',back_populates='class_')

    students = db.relationship('Student', back_populates='class_')

    def jsonify(self):
        return {
            'id' : self.id,
            'name' : self.name,
            # 'students' : self.students,
            # 'subject_teacher' : [i.jsonify() for i in self.subject_teacher]
        }




