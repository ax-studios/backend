import graphql
from ariadne import convert_kwargs_to_snake_case
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from api import auth, db
from api.auth import LoggedInUser
from api.error_handler import handle
from api.models import Class, Student, Subject, Teacher
from api.models.todos import Todo
from api.models.users import User
import api.utilities as utils
from constants import QUERY_NAME_TO_OBJECT


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
        db.session.rollback()
        handle(e)

    except Exception as e:
        db.session.rollback()
        raise graphql.GraphQLError(f"Unknown error {e.args}")

    return new_obj.jsonify([])


@convert_kwargs_to_snake_case
def resolve_createTodo(
    obj,
    info: graphql.type.definition.GraphQLResolveInfo,
    **kwargs,
):
    try:
        user: LoggedInUser = auth.authorize_user(info)

        if user is None:
            return graphql.GraphQLError("User not logged in.")

        todo = kwargs.get("todo")
        if todo is None:
            return graphql.GraphQLError("Todo not found.")

        try:
            date = datetime.strptime(todo.get("due_date"), r"%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError as ve:
            return graphql.GraphQLError(
                "Error: Date format must be YYYY-MM-DDTHH:MM:SS.MSZ"
            )

        new_todo = Todo(
            title=todo["title"],
            description=todo["description"],
            priority=todo["priority"],
            due_date=date,
            owner_id=User.query.filter_by(username=auth.authorize_user(info).username)
            .first()
            .id,
        )
        db.session.add(new_todo)
        db.session.commit()
        return new_todo.jsonify([])

    except Exception as e:
        db.session.rollback()
        raise graphql.GraphQLError(f"Unknown error {e.args}")


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
        db.session.rollback()
        handle(e)

    except Exception as e:
        db.session.rollback()
        raise graphql.GraphQLError(f"Unknown error {e.args}")

    print(kwargs)
    return x.jsonify([])


@convert_kwargs_to_snake_case
def resolve_updateTodo(obj, info: graphql.type.definition.GraphQLResolveInfo, **kwargs):

    print("**********")
    print(kwargs)
    todo_id = kwargs.get("id")
    changes_dict: dict = kwargs.get("modifications")
    kwargs.pop("modifications")

    if not utils.isValidUUID(todo_id):
        raise graphql.GraphQLError("Invalid todo id.")

    try:
        todo = Todo.query.filter_by(id=todo_id).all()[0]
    except IndexError:
        raise graphql.GraphQLError(f"{str(kwargs)} does not exist.")

    try:
        if changes_dict.get("due_date") is not None:
            date = datetime.strptime(
                changes_dict.get("due_date"), r"%Y-%m-%dT%H:%M:%S.%fZ"
            )
            changes_dict["due_date"] = date
    except ValueError as ve:
        return graphql.GraphQLError("Error: Date format must be YYYY-MM-DDTHH:MM:SS.MSZ")

    for key, value in changes_dict.items():
        setattr(todo, key, value)

    try:
        db.session.commit()

    except IntegrityError as e:
        db.session.rollback()
        handle(e)

    except Exception as e:
        db.session.rollback()
        raise graphql.GraphQLError(f"Unknown error {e.args}")

    return todo.jsonify([])
