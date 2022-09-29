import traceback

import graphql
from ariadne import convert_kwargs_to_snake_case
from constants import QUERY_NAME_TO_OBJECT


@convert_kwargs_to_snake_case
def resolve_getQuery(obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs):
    try:
        conditions = {}

        for key, value in kwargs.items():
            if value is not None:
                conditions[key] = value.lower() if type(value) is str else value

        objects = [
            object.jsonify([])
            for object in QUERY_NAME_TO_OBJECT.get(info.field_name)
            .query.filter_by(**conditions)
            .all()
        ]

        return objects

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        return graphql.GraphQLError("Some error oddured !!")
