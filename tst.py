# import api
# from api import db
# from api.models.relation_tables import ClassToSubjectTeacher, SubjectTeacher
# from api.models.classes import Class
# from api.models.users import User
# from api.models.teachers import Teacher
# from api.models.students import Student
# from api.models.subjects import Subject
# from api.models.todos import Todo
import pprint

import datetime
import random

import pytz
from sqlalchemy.orm.attributes import flag_modified

from app import db
from api.models import Class, Student, Subject, SubjectTeacher, Teacher, Todo, User
from api.models.relation_tables import ClassToSubjectTeacher


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

pp = pprint.PrettyPrinter(indent=2)

# x = Class.query.all()[0].jsonify([])
# x = Student.query.all()[0].jsonify([])
# x = Teacher.query.all()[5].jsonify([])
# x = SubjectTeacher.query.all()[0].jsonify([])
# x = Subject.query.all()[1].jsonify([])
# x = SubjectTeacher.query.all()[2].class_


# x = db.session.query(SubjectTeacher, Class).select_from(SubjectTeacher).join(Class.subject_teacher).filter_by(teacher_id='302eb2a6-a3ec-482a-b98d-98d6698aa68a').all()
# x = db.session.query(SubjectTeacher, Class).select_from(SubjectTeacher).join(Class.subject_teacher).filter_by(subject_id=1).all()
# x = SubjectTeacher.query.select_from(SubjectTeacher).join(Class.subject_teacher).add_columns(Class).filter_by(teacher_id='302eb2a6-a3ec-482a-b98d-98d6698aa68a').all()
# x = db.session.query(Student, Class).select_from(Student).join(Class).all()


# create teacher, class association

# lst=[]

# for subject_teacher,class_ in x:
#     d={}
#     d.update({"subject":subject_teacher.subject.jsonify([])})
#     d.update({"class_":class_.jsonify([])})
#     lst.append(d.copy())
# pp.pprint(k.jsonify([]))
# tch=Teacher.query.filter_by(id='302eb2a6-a3ec-482a-b98d-98d6698aa68a').first()
# x= tch.class_subject(['teacher'])
# for i in range(10):
# t = (Student.name.ilike("R%"), Student.enroll_no.like("21c22%"))
# cls = Student.query.filter(*t).all()
# # pp.pprint(cls)
# pp.pprint([i.jsonify([]) for i in cls])

# # subj= Subject.query.all()[0]
# print('a="Subject"')

# # print(json.dumps(x, indent=2))
# # print(x)


# pp.pprint(Todos.query.all()[0].jsonify([]))
# pp.pprint(Student.query.all()[0].jsonify([]))

# x = Todo.query.filter(Todo.title.like('Todo 512%')).all()
# x= Todo.query.join(User).filter(User.name.ilike('saNdeep%')).all()

# for i in x:
#     print(i.jsonify([]))

# u1 = User(
#     name="Sandeep ext",
#     email="sandeep_ext@gmail.com",
#     mobile_no="8999899834",
#     role="Student",
#     username="sandeep_89",
#     enroll_no="21C22001"
# )

# # add user u1 to db
# db.session.add(u1)
# db.session.commit()


# pp.pprint(x.jsonify([]))

# pp.pprint(db.session.query(SubjectTeacher, Class)
#             .select_from(SubjectTeacher)
#             .join(Class.subject_teacher)
#             .filter_by(teacher_id='0169c7a1-a559-4b69-9ea4-18957cf22a01')
#             .all())

# .filter_by(teacher_id='abe5ead6-0378-44c7-96be-1553e3692d69')

x = User.query.all()[0]
pp.pprint(x.__dict__)
print(User.user_only_attrs)
# pp.pprint(x.jsonify([]))
