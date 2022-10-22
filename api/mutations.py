import graphql
from ariadne import convert_kwargs_to_snake_case
from api.error_handler import handle
from constants import QUERY_NAME_TO_OBJECT
from sqlalchemy.exc import IntegrityError
from api.models import Student, Teacher, Class, Subject

from api import db


@convert_kwargs_to_snake_case
def resolve_createMutation(
    obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs
):
    arg_name = tuple(kwargs.keys())[0]
    if info.field_name in QUERY_NAME_TO_OBJECT.keys():
        new_obj = QUERY_NAME_TO_OBJECT.get(info.field_name)(**kwargs[arg_name])
        db.session.add(new_obj)

    try:
        db.session.commit()

    except IntegrityError as e:
        handle(e)

    except Exception as e:
        raise graphql.GraphQLError(f"Unknown error {e.args}")

    return new_obj.jsonify([])


@convert_kwargs_to_snake_case
def resolve_updateMutation(
    obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs
):
    changes_dict: dict = kwargs.get("modifications")
    kwargs.pop("modifications")

    try:
        x = QUERY_NAME_TO_OBJECT.get(info.field_name).query.filter_by(**kwargs).all()[0]

    except IndexError:
        raise graphql.GraphQLError(f"{str(kwargs)} does not exist.")

    for key, value in changes_dict.items():
        setattr(x, key, value)

    try:
        db.session.commit()

    except IntegrityError as e:
        handle(e)

    except Exception as e:
        raise graphql.GraphQLError(f"Unknown error {e.args}")

    print(kwargs)
    return x.jsonify([])
