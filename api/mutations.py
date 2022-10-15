import traceback

import graphql
from ariadne import convert_kwargs_to_snake_case
from constants import QUERY_NAME_TO_OBJECT
from sqlalchemy.exc import IntegrityError
from api.models import Student, Teacher, Class, Subject


from api import db


@convert_kwargs_to_snake_case
def resolve_createMutation(
    obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs
):
    try:
        arg_name = tuple(kwargs.keys())[0]
        if info.field_name in QUERY_NAME_TO_OBJECT.keys():
            new_obj = QUERY_NAME_TO_OBJECT.get(info.field_name)(**kwargs[arg_name])
            db.session.add(new_obj)
            db.session.commit()
            return new_obj.jsonify([])

    except IntegrityError as e:
        err_details = str(e.orig).split("DETAIL:")[1]
        err_details = err_details.replace("Key", "")
        err_details = err_details.replace("=", " ")
        err_details = err_details.replace("(", "")
        err_details = err_details.replace(")", "")
        return graphql.GraphQLError(err_details.strip())

    # TODO add an "except" to catch other exceptions


@convert_kwargs_to_snake_case
def resolve_updateStudents(obj, info, **kwargs):
    print("###############################\nOK\n###############################")
    changes_dict = kwargs.get("modifications")

    x = Student.query.filter_by(enroll_no=kwargs["enroll_no"]).all()[0]

    for key, value in changes_dict.items():
        setattr(x, key, value)

    db.session.commit()
    print(kwargs)
    return x.jsonify([])
