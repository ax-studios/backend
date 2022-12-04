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
from api.queries import resolve_getQuery, resolveGetTodo
from api.mutations import (
    resolve_createMutation,
    resolve_createTodo,
    resolve_updateMutation,
    resolve_updateTodo,
)

query = ObjectType("Query")

query.set_field("getStudents", resolve_getQuery)
query.set_field("getTeachers", resolve_getQuery)
query.set_field("getClasses", resolve_getQuery)
query.set_field("getSubjects", resolve_getQuery)
query.set_field("getTodos", resolveGetTodo)

mutation = ObjectType("Mutation")
mutation.set_field("createStudent", resolve_createMutation)
mutation.set_field("createTeacher", resolve_createMutation)
mutation.set_field("createClass", resolve_createMutation)
mutation.set_field("createSubject", resolve_createMutation)
mutation.set_field("createTodo", resolve_createTodo)

mutation.set_field("updateStudent", resolve_updateMutation)
mutation.set_field("updateTeacher", resolve_updateMutation)
mutation.set_field("updateTodo", resolve_updateTodo)

type_defs = load_schema_from_path("./schema")
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
