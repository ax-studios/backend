import random
from secrets import choice
import names
import csv

# from app import db
# from api.models.relation_tables import ClassToSubjectTeacher
# from api.models import Student, Class, Subject, SubjectTeacher, Teacher
# from datetime import time, date, datetime
# import names

# db.drop_all()
# db.create_all()

# Generate 100 random names & save them to sample_data.csv
with open("./tests/sample_data.csv", "w") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(["name", "email", "mobile_no", "enroll_no", "username", "password"])
    for i in range(20):
        name = names.get_full_name()
        email = name.replace(" ", "_") + str(i) + "@itmbu.ac.in"
        mobile_no = random.randint(1000000000, 9999999999)
        enroll_no = "C" + ("0" * (3 - len(str(i)))) + str(i)
        username = name.replace(" ", "_") + str(i)
        password = "password"
        writer.writerow([name, email, mobile_no, enroll_no, username, password])
