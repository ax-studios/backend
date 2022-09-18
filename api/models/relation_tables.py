from app import db,api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid



class SubjectTeacher(db.Model):
    __tablename__ = "subject_teacher"
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(ForeignKey('subjects.id'))
    teacher=db.Column(ForeignKey('teachers.id'))

    classes = db.relationship('Class', secondary='class_to_subject_teacher', back_populates='subject_teacher')


class_to_subject_teacher = db.Table(
    'class_to_subject_teacher',
    db.Column('subject_teacher',db.Integer,db.ForeignKey('subject_teacher.id')),
    db.Column('class',db.Integer,db.ForeignKey('classes.id')),
)




