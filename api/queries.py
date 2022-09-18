from .models import Student
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def resolve_students(obj, info, enroll_no):
    try:
        if enroll_no is not None:
            students = [student.jsonify() for student in Student.query.filter_by(enroll_no=enroll_no)]
        else:
            students = [student.jsonify() for student in Student.query.all()]

        print(students)
        return students

    except Exception as error:
        payload = None
    return payload


