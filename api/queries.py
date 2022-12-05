import traceback

import graphql
from ariadne import convert_kwargs_to_snake_case
import werkzeug
from api import auth
from api.constants import QUERY_NAME_TO_OBJECT
from api.models import Todo, User, Student, Teacher
import api.utilities as utils


@convert_kwargs_to_snake_case
def resolve_getQuery(obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs):
    try:
        conditions = ()

        for key, value in kwargs.items():
            if value is not None:
                conditions += (
                    getattr(QUERY_NAME_TO_OBJECT[info.field_name], key).ilike(value),
                )
                # conditions[key] = value.lower() if type(value) is str else value

        objects = [
            obj.jsonify([])
            for obj in QUERY_NAME_TO_OBJECT.get(info.field_name)
            .query.filter(*conditions)
            .all()
        ]

        return objects

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        return graphql.GraphQLError("Some error occured !!")


@convert_kwargs_to_snake_case
def resolveGetTodo(
    obj,
    info: graphql.type.definition.GraphQLResolveInfo,
    todo_id: str = None,
    username: str = None,
):
    try:
        if todo_id is not None:
            if utils.isValidUUID(todo_id):
                return [i.jsonify([]) for i in Todo.query.filter_by(id=todo_id).all()]
            else:
                return graphql.GraphQLError("Invalid todo id.")

        if username is not None:
            return [
                i.jsonify([])
                for i in Todo.query.join(User)
                .filter(User.username.ilike(username))
                .all()
            ]

        return [i.jsonify([]) for i in Todo.query.all()]

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        return graphql.GraphQLError("Some error occured !!")


@convert_kwargs_to_snake_case
def resolve_getStudent(
    obj,
    info: graphql.type.definition.GraphQLResolveInfo,
    username: str = None,
    enroll_no: str = None,
    email: str = None,
):
    try:
        if username is not None:
            return [
                i.jsonify([])
                for i in Student.query.join(User)
                .filter(User.username.ilike(username))
                .all()
            ]

        if enroll_no is not None:
            return [
                i.jsonify([])
                for i in Student.query.filter_by(enroll_no=enroll_no).all()
            ]

        if email is not None:
            return [
                i.jsonify([])
                for i in Student.query.join(User).filter(User.email.ilike(email)).all()
            ]

        return [i.jsonify([]) for i in Student.query.all()]

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        return graphql.GraphQLError("Some error occured !!")


@convert_kwargs_to_snake_case
def resolve_getTeacher(
    obj,
    info: graphql.type.definition.GraphQLResolveInfo,
    username: str = None,
    email: str = None,
):
    try:
        if username is not None:
            return [
                i.jsonify([])
                for i in Teacher.query.join(User)
                .filter(User.username.ilike(username))
                .all()
            ]

        if email is not None:
            return [
                i.jsonify([])
                for i in Teacher.query.join(User).filter(User.email.ilike(email)).all()
            ]

        return [i.jsonify([]) for i in Teacher.query.all()]

    except Exception as error:
        traceback.print_tb(error.__traceback__)
        return graphql.GraphQLError("Some error occured !!")

