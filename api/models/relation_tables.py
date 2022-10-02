from app import db, api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql


class SubjectTeacher(db.Model):
    __tablename__ = "subject_teacher"
    __table_args__ = (db.UniqueConstraint("subject_id", "teacher_id"),)

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(ForeignKey("subjects.id"))
    teacher_id = db.Column(ForeignKey("teachers.id"))

    subject = db.relationship("Subject", backref="subject_teacher")
    teacher = db.relationship("Teacher", backref="subject_teacher")

    class_ = db.relationship(
        "Class", secondary="class_to_subject_teacher", back_populates="subject_teacher"
    )

    def jsonify(self, parents: list):
        return {
            "id": self.id,
            "subject": self.subject.jsonify(parents + [self.__tablename__])
            if "subjects" not in parents
            else None,
            "teacher": self.teacher.jsonify(parents + [self.__tablename__])
            if "teachers" not in parents
            else None,
        }


class ClassToSubjectTeacher(db.Model):
    __tablename__ = "class_to_subject_teacher"
    __table_args__ = (UniqueConstraint("class_id", "subject_teacher_id"),)

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(ForeignKey("classes.id"))
    subject_teacher_id = db.Column(ForeignKey("subject_teacher.id"))
