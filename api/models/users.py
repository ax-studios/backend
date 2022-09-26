from email.policy import default
from api.models.relation_tables import ClassToSubjectTeacher
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
    role = db.Column(db.String(15), nullable=False)

    # Login info
    # username = db.Column(String(80), unique=True, nullable=False)
    # password = db.Column(String(120), nullable=False)

    # Connect child tables
    __mapper_args__ = {"polymorphic_identity": "users", "polymorphic_on": role}

    def jsonify(self):
        return {
            "name": self.name,
            "mobile_no": self.mobile_no,
            "email": self.email
            # "username": self.username,
        }


class Student(User):
    __tablename__ = "students"

    id = db.Column(psql.UUID, db.ForeignKey("users.id"), primary_key=True)
    enroll_no = db.Column(db.String(10), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    class_ = db.relationship("Class", back_populates="students")

    __mapper_args__ = {
        "polymorphic_identity": "students",
    }

    def jsonify(self, parents):
        parent_json = super().jsonify()
        parent_json.update(
            {
                "enroll_no": self.enroll_no,
                "class_": self.class_.jsonify(parents + [f"{self.__tablename__}"])
                if "classes" not in parents
                else None,
            }
        )
        return parent_json


class Teacher(User):
    __tablename__ = "teachers"

    id = db.Column(psql.UUID, db.ForeignKey("users.id"), primary_key=True)

    # subject_teacher = db.relationship('SubjectTeacher', secondary='subject_teacher', back_populates='teacher')

    __mapper_args__ = {
        "polymorphic_identity": "teachers",
    }

    def class_subject(self, parents=[]):
        x = (
            db.session.query(SubjectTeacher, Class)
            .select_from(SubjectTeacher)
            .join(Class.subject_teacher)
            .filter_by(teacher_id=self.id)
            .all()
        )

        lst = []
        for subject_teacher, class_ in x:

            lst.append(
                {
                    "subject": subject_teacher.subject.jsonify(
                        parents + [self.__tablename__, "classes","subjects"]
                    ),
                    "class_": class_.jsonify(
                        parents + [self.__tablename__, "classes","subjects"]
                    ),
                }
            )

        return lst

    def jsonify(self, parents):
        parent_dict = super().jsonify()
        parent_dict.update(
            {
                "class_subject": self.class_subject(parents)
                if "classes" not in parents and "subjects" not in parents
                else None
            }
        )
        return parent_dict
