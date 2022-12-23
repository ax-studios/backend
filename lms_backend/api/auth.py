from dataclasses import dataclass
from werkzeug.datastructures import EnvironHeaders
import graphql
import bcrypt
import os
from api import logger

# os.getenv("name", "default value")


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


# create decorator authenticate_user to use in resolvers
def authenticate_user(func):
    def wrapper(*args, **kwargs):
        logger.error("authenticate_user *****************************************")
        logger.error(args)
        logger.error(kwargs)
        logger.error("authenticate_user *****************************************")

        info: graphql.type.definition.GraphQLResolveInfo = args[1]

        request: EnvironHeaders = info.context.headers
        environment: dict = request.environ

        logger.error(environment)

        if environment.get("HTTP_JWT") is None:
            raise graphql.GraphQLError("User not logged in.")

        auth_token = environment.get("HTTP_JWT")
        tmp_token = environment.get("HTTP_AUTH")

        if tmp_token is None:
            raise graphql.GraphQLError("User not logged in.")

        if tmp_token != "kjsd09h^uiwe23hUwia*kaw9eqw%kja(nJaBGHawds":
            raise graphql.GraphQLError("User not logged in.")

        if auth_token:

            loggedInUser = LoggedInUser(
                username=auth_token,
                role="student",
            )

            # extra user info
            loggedInUser.tz_name = environment.get("tz_name")

            return func(*args, **kwargs)

        else:
            raise graphql.GraphQLError("User not logged in.")

    return wrapper


class LoggedInUser:
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role
