import os
from typing import List

from ariadne import (
    ObjectType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request

import api
from api import app, db
from api.mutations import (
    resolve_assignRole,
    resolve_createMutation,
    resolve_createTodo,
    resolve_updateMutation,
    resolve_updateTodo,
)
from api.queries import (
    resolve_getQuery,
    resolve_getStudent,
    resolve_getTeacher,
    resolveGetTodo,
)

query = ObjectType("Query")

query.set_field("getUsers", resolve_getQuery)
query.set_field("getStudents", resolve_getStudent)
query.set_field("getTeachers", resolve_getTeacher)
query.set_field("getClasses", resolve_getQuery)
query.set_field("getSubjects", resolve_getQuery)
query.set_field("getTodos", resolveGetTodo)

mutation = ObjectType("Mutation")
mutation.set_field("createUser", resolve_createMutation)
mutation.set_field("createStudent", resolve_createMutation)
mutation.set_field("createTeacher", resolve_createMutation)
mutation.set_field("createClass", resolve_createMutation)
mutation.set_field("createSubject", resolve_createMutation)
mutation.set_field("createTodo", resolve_createTodo)

mutation.set_field("updateUser", resolve_updateMutation)
mutation.set_field("updateStudent", resolve_updateMutation)
mutation.set_field("updateTeacher", resolve_updateMutation)
mutation.set_field("updateTodo", resolve_updateTodo)

mutation.set_field("assignRole", resolve_assignRole)


def generate_schema() -> str:
    schema_str: str = ""
    base_folder: str = "./api/schema"
    schema_files: List[str] = [
        "Enums",
        "User",
        "Student",
        "Teacher",
        "Class",
        "Subject",
        "Todo",
        "typedefs",
        "schema",
    ]

    for file in schema_files:
        with open(os.path.join(base_folder, file + ".gql")) as f:
            schema_str += f.read() + "\n"

    return schema_str


type_defs: str = generate_schema()

schema = make_executable_schema(
    type_defs, [query, mutation], snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
