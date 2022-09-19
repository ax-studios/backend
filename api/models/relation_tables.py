from app import db,api
from sqlalchemy import *
import sqlalchemy.dialects.postgresql as psql



class SubjectTeacher(db.Model):
    __tablename__ = "subject_teacher"
    id=db.Column(db.Integer,primary_key=True)
    subject_id=db.Column(ForeignKey('subjects.id'))
    teacher_id=db.Column(ForeignKey('teachers.id'))

    subject = db.relationship('Subject', backref='subject_teacher')
    teacher = db.relationship('Teacher', backref='subject_teacher')

    class_ = db.relationship('Class', secondary='class_to_subject_teacher', back_populates='subject_teacher')

    def jsonify(self,parents:list):
        return {
            'id' : self.id,
            'subject' : self.subject.jsonify([self.__tablename__]) if 'subjects' not in parents else None,
            'teacher' : self.teacher.jsonify([self.__tablename__]) if 'teachers' not in parents else None,
        }


class ClassToSubjectTeacher(db.Model):
    __tablename__ = "class_to_subject_teacher"
    id=db.Column(db.Integer,primary_key=True)
    class_id=db.Column(ForeignKey('classes.id'))
    subject_teacher_id=db.Column(ForeignKey('subject_teacher.id'))

# class_to_subject_teacher = db.Table(
#     'class_to_subject_teacher',
#     db.Column('subject_teacher',db.Integer,db.ForeignKey('subject_teacher.id')),
#     db.Column('class',db.Integer,db.ForeignKey('classes.id')),
# )




