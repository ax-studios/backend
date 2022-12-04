from dataclasses import dataclass
from werkzeug.datastructures import EnvironHeaders
import graphql


def authorize_user(info: graphql.type.definition.GraphQLResolveInfo):

    request: EnvironHeaders = info.context.headers
    environment: dict = request.environ

    if environment.get("HTTP_JWT") is None:
        raise graphql.GraphQLError("User not logged in.")

    auth_token: dict = environment.get("HTTP_JWT")

    if auth_token:
        loggedInUser = LoggedInUser(
            username=auth_token,
            role="student",
        )

        # extra user info
        loggedInUser.tz_name = environment.get("tz_name")

        return loggedInUser

    else:
        return None


class LoggedInUser:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role
