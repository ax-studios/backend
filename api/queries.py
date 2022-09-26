import traceback

import graphql
from ariadne import convert_kwargs_to_snake_case
from constants import QUERY_NAME_TO_OBJECT


@convert_kwargs_to_snake_case
def resolve_getQueryResolver(
    obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs
):
    try:
        conditions = {}

        for key, value in kwargs.items():
            if value is not None:
                conditions[key] = value.lower() if type(value) is str else value

        students = [
            student.jsonify([])
            for student in QUERY_NAME_TO_OBJECT.get(info.field_name)
            .query.filter_by(**conditions)
            .all()
        ]

        return students

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        payload = None

    return payload

