import datetime
import random

import pytz
from app import db
from api.models.relation_tables import ClassToSubjectTeacher
from api.models import Student, Class, Subject, SubjectTeacher, Teacher, User, Todo

db.drop_all()
db.create_all()

# List of 20 random indian names
s_names = [
    "Kamal",
    "Rahul",
    "Raj",
    "Rajesh",
    "Ramesh",
    "Ravi",
    "Ravindra",
    "Rohan",
    "Ronak",
    "Sachin",
    "Sagar",
    "Sahil",
    "Sajid",
    "Sandeep",
    "Santosh",
    "Sarfaraz",
    "Sarvesh",
    "Saurabh",
    "Saurav",
    "Savita",
]

# List of 20 random phone numbers
contact_numbers = [
    "1234567890",
    "1234567891",
    "1234567892",
    "1234567893",
    "1234567894",
    "1234567895",
    "1234567896",
    "1234567897",
    "1234567898",
    "1234567899",
    "1234567800",
    "1234567801",
    "1234567802",
    "1234567803",
    "1234567804",
    "1234567805",
    "1234567806",
    "1234567807",
    "1234567808",
    "1234567809",
]

# List of 10 random indian names
t_names = [
    "Kamal Sir",
    "Rahul Sir",
    "Raj Sir",
    "Rajesh Sir",
    "Ramesh Sir",
    "Ravi Sir",
    "Ravindra Sir",
    "Rohan Sir",
    "Ronak Sir",
    "Sachin Sir",
]

# List of 10 random contact numbers
t_contact_numbers = [
    "9934567890",
    "9987654321",
    "9934567891",
    "9934567892",
    "9934567893",
    "9934567894",
    "9934567895",
    "9934567896",
    "9934567897",
    "9934567898",
]

# List of 10 programming languages
languages = [
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "HTML",
    "CSS",
    "PHP",
    "Ruby",
]

email_addresses = [i + "@gmail.com" for i in s_names]
enroll_numbers = ["21C220" + ("0" if i < 10 else "") + str(i) for i in range(1, 21)]

t_email_addresses = [i + "@itmbu.ac.in" for i in s_names]

# Create 2 classes
class_1 = Class(name="AI")
# class_1.students = []
db.session.add(class_1)
db.session.commit()
class_2 = Class(name="CS")
# class_2.students = []
db.session.add(class_2)
db.session.commit()


# Create 20 students
for i in range(20):
    student = Student(
        name=s_names[i],
        mobile_no=contact_numbers[i],
        email=email_addresses[i],
        enroll_no=enroll_numbers[i],
        class_id=random.choice([1, 2]),
        username=s_names[i].lower().replace(" ", "_") + "_" + str(i),
    )
    db.session.add(student)
    db.session.commit()

# Create 10 subjects
for i in range(10):
    subject = Subject(name=languages[i])
    db.session.add(subject)
    db.session.commit()
    languages[i] = subject


# Create 10 teachers
for i in range(10):
    teacher = Teacher(
        name=t_names[i],
        mobile_no=t_contact_numbers[i],
        email=t_email_addresses[i],
        username=t_names[i].lower().replace(" ", "_") + "_" + str(i),
    )
    db.session.add(teacher)
    db.session.commit()

# Create 20 subject_teacher relations
for i in range(10):
    subject_teacher = SubjectTeacher(
        subject_id=languages[i].id, teacher_id=random.choice(Teacher.query.all()).id
    )
    db.session.add(subject_teacher)
    db.session.commit()

# Create 8 class_to_subject_teacher relations
for i in range(6):
    class_to_subject_teacher1 = ClassToSubjectTeacher(
        class_id=class_1.id,
        subject_teacher_id=random.choice(SubjectTeacher.query.all()).id,
    )
    class_to_subject_teacher2 = ClassToSubjectTeacher(
        class_id=class_2.id,
        subject_teacher_id=random.choice(SubjectTeacher.query.all()).id,
    )
    db.session.add_all([class_to_subject_teacher1, class_to_subject_teacher2])
    try:
        db.session.commit()
    except:
        db.session.rollback()

# Create 50 todos
for i in range(50):
    todo = Todo(
        title="Todo " + str(i + 1),
        description="This is a description for todo " + str(i + 1),
        priority=random.choice([1, 2, 3]),
        due_date=pytz.UTC.normalize(
            datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata"))
            + datetime.timedelta(days=random.randint(1, 20))
        ),
        owner_id=random.choice(User.query.all()).id,
    )
    db.session.add(todo)
    db.session.commit()

# st1 = SubjectTeacher.query.all()[0].id

# db.session.add(
#     ClassToSubjectTeacher(
#         class_id=class_1.id,
#         subject_teacher_id=st1,
#     )
# )
# db.session.commit()

# db.session.add(
#     ClassToSubjectTeacher(
#         class_id=class_1.id,
#         subject_teacher_id=st1,
#     )
# )
# db.session.commit()

# db.session.add(
#     ClassToSubjectTeacher(
#         class_id=class_1.id,
#         subject_teacher_id=st1,
#     )
# )
# db.session.commit()


# for i in range(4):
#     # print("+++",type(class_1.subject_teacher))
#     # print("+++",type(class_2.subject_teacher))

#     class_1.subject_teacher.append(SubjectTeacher.query.filter_by(id=random.randint(1, 20)).first())
#     class_2.subject_teacher.append(SubjectTeacher.query.filter_by(id=random.randint(1, 20)).first())
#     db.session.add_all([class_2, class_1])
#     db.session.commit()
