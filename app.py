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
from api.queries import resolve_getQueryResolver
from api.mutations import resolve_createStudent

query = ObjectType("Query")

query.set_field("getStudents", resolve_getQueryResolver)
query.set_field("getTeachers", resolve_getQueryResolver)
query.set_field("getClasses", resolve_getQueryResolver)
query.set_field("getSubjects", resolve_getQueryResolver)

mutation = ObjectType("Mutation")
mutation.set_field("createStudent", resolve_createStudent)
mutation.set_field("createTeacher", resolve_createStudent)
mutation.set_field("createClass", resolve_createStudent)
mutation.set_field("createSubject", resolve_createStudent)

type_defs = load_schema_from_path("./schema")
schema = make_executable_schema(type_defs, [query, mutation], snake_case_fallback_resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
