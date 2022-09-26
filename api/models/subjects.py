from api.models.classes import Class
from app import db, api
from ..models import SubjectTeacher
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
import uuid


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    @property
    def teachers(self):
        return [
            i.teacher.jsonify([self.__tablename__])
            for i in SubjectTeacher.query.filter_by(subject_id=self.id)
        ]

    def class_teacher(self, parents=[]):
        x = (
            db.session.query(SubjectTeacher, Class)
            .select_from(SubjectTeacher)
            .join(Class.subject_teacher)
            .filter_by(subject_id=self.id)
            .all()
        )

        lst = []
        for subject_teacher, class_ in x:
            lst.append(
                {
                    "teacher": subject_teacher.teacher.jsonify(
                        parents + [self.__tablename__, "classes", "teachers"]
                    ),
                    "class_": class_.jsonify(
                        parents + [self.__tablename__, "classes", "teachers"]
                    ),
                }
            )

        return lst

    def jsonify(self, parents):
        return {
            "id": self.id,
            "name": self.name,
            "class_teacher": self.class_teacher(parents)
            if "classes" not in parents and "teachers" not in parents
            else None,
        }
