from dataclasses import dataclass
from werkzeug.datastructures import EnvironHeaders
import graphql


def authorize_user(
    info: graphql.type.definition.GraphQLResolveInfo,
    operation
    ):

    request: EnvironHeaders = info.context.headers

    if request.get("auth") is None:
        raise graphql.GraphQLError("User unauthorized")

    auth_token: dict = request.get("auth")

    if auth_token:
        return True
    else:
        return False
