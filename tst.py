from app import db
from api.models.relation_tables import SubjectTeacher


# db.create_all()

# db.session.commit()


# #     "Rajesh",
# st1=Student(name="Rajesh",email="Rajesh@gmail.com",mobile_no="1234567890",enroll_no="21C22001")

# db.session.add(st1)
# db.session.commit()

print(SubjectTeacher.query.filter_by(id=1).first())

