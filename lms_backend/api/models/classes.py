from app import db
from sqlalchemy import *


class Class(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    subject_teacher = db.relationship(
        "SubjectTeacher", secondary="class_to_subject_teacher", back_populates="class_"
    )

    students = db.relationship("Student", back_populates="class_")

    def jsonify(self, parents):
        result = {
            "id": self.id,
            "name": self.name,
            "subject_teacher": [
                i.jsonify(
                    parents + [self.__tablename__, "students", "subject", "teacher"]
                )
                for i in self.subject_teacher
            ]
            if "subjects" not in parents and "teachers" not in parents
            else None,
            "students": [
                i.jsonify(parents + [self.__tablename__]) for i in self.students
            ]
            if "students" not in parents
            else None,
        }
        return result
