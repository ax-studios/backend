from psycopg2.errors import *
import psycopg2
import graphql


def handle(error: psycopg2.Error):
    if isinstance(error.__cause__, UniqueViolation):
        error: UniqueViolation = error.__cause__
        err_details = str(error.args).split("DETAIL:")[1]
        err_details = err_details.replace("Key", "")
        err_details = err_details.replace("=", " ")
        err_details = err_details.replace("(", "")
        err_details = err_details.replace(")", "")

        raise graphql.GraphQLError(err_details.strip())

    else:
        raise graphql.GraphQLError(f"Unknown integrity error {error.args}")
