import email
import json
from turtle import st
from app import db
from api.models.relation_tables import ClassToSubjectTeacher, SubjectTeacher
from api.models.classes import Class
from api.models.users import Student, Teacher
from api.models.subjects import Subject
import pprint


# db.drop_all()
# db.create_all()
# c1=Class(name="class1")
# db.session.add(c1)

# s1=Student(name="Kamal",mobile_no="1234567890",email="Kamal@gmain.com",enroll_no="21C22001",class_id=1)
# db.session.add(s1)

# t1=Teacher(name="Raj",mobile_no="9934567890",email="Raj@gmail.com")
# db.session.add(t1)

# sub1=Subject(name="Maths")
# db.session.add(sub1)

# st1=SubjectTeacher(subject_id=1,teacher_id=Teacher.query.all()[0].id)
# db.session.add(st1)

# db.session.commit()

# print(Class.query.all()[0].jsonify())
# print(Student.query.all()[0].jsonify())
# print(Teacher.query.all()[0].jsonify())
# print(Subject.query.all()[0].jsonify())
# print()

# print(Class.query.all()[0].students)
# print(Student.query.all()[0].class_)

# print(Teacher.query.all()[1].subject_teacher)
# print(Subject.query.all()[0].subject_teacher)

# print(Class.query.all()[0].students)

# x=SubjectTeacher.query.all()[0].jsonify()

pp=pprint.PrettyPrinter(indent=2)

# x = Class.query.all()[0].jsonify([])
# x = Student.query.all()[0].jsonify([])
x = Teacher.query.all()[1].jsonify([])
# x = SubjectTeacher.query.all()[0].jsonify([])
# x = Subject.query.all()[1].jsonify([])


pp.pprint(x)

# print(json.dumps(x, indent=2))
# print(x)
