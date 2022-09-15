from .models import Student,Class
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def resolve_students(obj, info, id):
    try:
        status_code = 200
        if id is not None:
            students = [student.to_dict()
                        for student in Student.query.filter_by(id=id)]
        else:
            students = [student.to_dict() for student in Student.query.all()]

        print("************", type(obj), type(info))
        payload = students
        if len(payload) == 0:
            status_code = 404
        else:
            status_code = 200

    except Exception as error:
        print("#########################", error)
        payload = None
        status_code = 400

    return payload

@convert_kwargs_to_snake_case
def resolve_classes(obj, info, id):
    try:
        if id is not None:
            classes = [class_.to_dict()
                       for class_ in Class.query.filter_by(id=id)]
            
        else:
            print("^^^^^^^^^")
            classes = [class_.to_dict() for class_ in Class.query.all()]
            print(classes[0]["teachers"])

        payload = classes
    
    except Exception as error:
        print("#########################", error)
        payload = None

    return payload

