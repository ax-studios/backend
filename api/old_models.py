from app import db
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import ARRAY, JSONB


class_to_SubjectTeacher = db.Table(   
        'class_to_subject_teacher',
        db.Column('subject_teacher',db.Integer,db.ForeignKey('subject_teacher.id')),
        db.Column('class',db.Integer,db.ForeignKey('classes.id')),
    )

# class PhoneNumbers(db.Model):
#     __tablename__ = "phone_numbers"
#     id = db.Column(db.Integer, primary_key=True)
#     phone_number = db.Column(db.String(10), nullable=False)
#     associated_teacher = db.Column(db.Integer, db.ForeignKey('teachers.id'))
#     associated_student = db.Column(db.String, db.ForeignKey('students.id'))
    

class SubjectTeacher(db.Model):
    __tablename__ = 'subject_teacher'
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "subject_id": self.subject_id,
            "teacher_id": self.teacher_id
        }


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(String, primary_key=True)
    name = db.Column(String, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    contact_num = db.Column(ARRAY(String), unique=True, nullable=False)
    # contact_nos = db.relationship('PhoneNumbers')
    class_id = db.Column(ForeignKey('classes.id'))
    

    def to_dict(self):
        return {
            "enroll_num": self.id,
            "email": self.email,
            "name": self.name,
            "contact_num": self.contact_num,
            "class": self.class_id
        }


class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String, nullable=False)
    subject_teacher = db.relationship('SubjectTeacher',secondary=class_to_SubjectTeacher,backref='classes')
    students = db.relationship('Student')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "teachers": [i.to_dict() for i in self.subject_teacher],
            "students": [i.to_dict() for i in self.students]
        }

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String)
    # trachers = db.relationship('Teacher',secondary='subject_teacher',back='subjects')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String,nullable=False)
    email = db.Column(String,nullable=False,unique=True)
    contact_num = db.Column(ARRAY(String),nullable=False,unique=True)
    subjects = db.relationship('Subject',secondary='subject_teacher',backref='teachers')

    # @property
    # def contacts(self):
    #     return [i.contact_num for i in self.contacts]

    # @contacts.setter
    # def contacts(self,contacts):
    #     for i in contacts:
    #         self.contacts.append(i)
    #     self.contact_num = contacts



    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "contact_num": self.contact_num,
            "subjects": self.subjects
        }



