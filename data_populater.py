import pprint
import random
from app import db
from api.models import Student, Class, Subject, SubjectTeacher, Teacher, users

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
]

# List of 10 random contact numbers
t_contact_numbers = ["9934567890",
                     "9987654321",
                     "9934567891",
                     "9934567892",
                     "9934567893",
                     "9934567894",
                     "9934567895",
                     "9934567896",
                     "9934567897",
                     "9934567898",]

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

email_addresses = [i+"@gmail.com" for i in s_names]
enroll_numbers = ["21C220" + ("0" if i < 10 else "") + str(i)
                  for i in range(1, 21)]

t_email_addresses = [i+"@itmbu.ac.in" for i in s_names]

# Create 2 classes
class_1 = Class(name="AI")
db.session.add(class_1)
db.session.commit()
class_2 = Class(name="CS")
db.session.add(class_2)
db.session.commit()


# Create 20 students
for i in range(20):
    student = Student(
        name=s_names[i],
        mobile_no=contact_numbers[i],
        email=email_addresses[i],
        enroll_no=enroll_numbers[i],
        class_id=random.choice([class_1.id, class_2.id])
    )
    # student.class_.append()
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
        subjects=[random.choice(languages), random.choice(languages)]
    )
    # teacher.contact_nos.append(t_contact_numbers[i])
    db.session.add(teacher)
    db.session.commit()

for i in range(4):
    class_1.subject_teacher.append(SubjectTeacher.query.filter_by(id=random.randint(1, 20)).first())
    class_2.subject_teacher.append(SubjectTeacher.query.filter_by(id=random.randint(1, 20)).first())
    db.session.add_all([class_2, class_1])
    db.session.commit()



# class_1.subject_teacher = [



# print("--------",class_1.subject_teacher)
# class_1.subject_teacher = [(users.query.all())]
# print("--------", class_1.subject_teacher[0].to_dict())
# db.session.commit()
# print(SubjectTeacher.query.all())
# print("------------------", languages[0].teachers)
