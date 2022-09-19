from app import db, api
from ..models import SubjectTeacher
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # teachers = db.relationship('Teacher', secondary='subject_teacher', back_populates='subjects')
    # subject_teacher = db.relationship('SubjectTeacher', back_populates='subject')

    @property
    def teachers(self):
        return [i.teacher.jsonify([self.__tablename__]) for i in SubjectTeacher.query.filter_by(subject_id=self.id)]

    def jsonify(self, parents):
        return {
            'id': self.id,
            'name': self.name,
            'teachers': [i.teacher.jsonify(parents+[self.__tablename__]) for i in SubjectTeacher.query.filter_by(subject_id=self.id)] if 'teachers' not in parents else None,
            'subject_teacher': [i.jsonify(parents+[self.__tablename__]) for i in self.subject_teacher] if 'subject_teacher' not in parents else None
        }
