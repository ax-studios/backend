from app import db,api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql
# from ..models.users import Teacher
# from ..models.subjects import Subject



class SubjectTeacher(db.Model):
    __tablename__ = "subject_teacher"
    id=db.Column(db.Integer,primary_key=True)
    subject_id=db.Column(ForeignKey('subjects.id'))
    teacher_id=db.Column(ForeignKey('teachers.id'))

    # subject = db.relationship('Subject', back_populates='subject_teacher')
    classes = db.relationship('Class', secondary='class_to_subject_teacher', back_populates='subject_teacher')

    # @property
    # def teacher(self):
    #     return Teacher.query.filter_by(id=self.teacher_id).first()

    # @property
    # def subject(self):
    #     return Subject.query.filter_by(id=self.subject_id).first()

    def jsonify(self):
        return {
            'id' : self.id,
            'subject' : self.subject,
            'teacher' : self.teacher,
        }


class_to_subject_teacher = db.Table(
    'class_to_subject_teacher',
    db.Column('subject_teacher',db.Integer,db.ForeignKey('subject_teacher.id')),
    db.Column('class',db.Integer,db.ForeignKey('classes.id')),
)




