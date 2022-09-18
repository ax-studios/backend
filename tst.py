import json
from app import db
from api.models.relation_tables import SubjectTeacher
from api.models.classes import Class
from api.models.users import Student


x=SubjectTeacher.query.all()[0].jsonify()

print(json.dumps(x,indent=2))

