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
            "name": self.name,
            "mobile_no": self.mobile_no,
            "email": self.email
            # "username": self.username,
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

    def jsonify(self, parents):
        parent_json = super().jsonify()
        parent_json.update({
            "enroll_no": self.enroll_no,
            "class_": self.class_.jsonify(parents+[f'{self.__tablename__}']) if 'classes' not in parents else None

        })

        # update_if_not_in_parent(self,'class_',parents,json)

        # self.__getattribute__

        # if 'classses' not in parents:
        #     parent_json.update({
        #     })
        # else:
        #     'class_': None
        # print(parent_json)
        return parent_json


class Teacher(User):
    __tablename__ = 'teachers'

    id = db.Column(psql.UUID, db.ForeignKey('users.id'), primary_key=True)

    # subject_teacher = db.relationship('SubjectTeacher', secondary='subject_teacher', back_populates='teacher')

    __mapper_args__ = {
        'polymorphic_identity': 'teachers',
    }

    # @property
    # def subjects(self):
    #     return [i.jsonify() for i in ]

    def jsonify(self,parents):
        parent_dict = super().jsonify()
        parent_dict.update({
            'subjects': [i.subject.jsonify(parents+[self.__tablename__]) for i in SubjectTeacher.query.filter_by(teacher_id=self.id)] if 'teachers' not in parents else None,
            'subject_teacher': [i.jsonify(parents+[self.__tablename__]) for i in self.subject_teacher] if 'subject_teacher' not in parents else None,
        })
        return parent_dict
