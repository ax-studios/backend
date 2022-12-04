from api.models import Student, Class, Teacher, Subject, Todo

QUERY_NAME_TO_OBJECT = {
    # region get queries
    "getStudents": Student,
    "getClasses": Class,
    "getTeachers": Teacher,
    "getSubjects": Subject,
    "getTodos": Todo,
    # endregion
    # region create queries
    "createStudent": Student,
    "createTeacher": Teacher,
    "createClass": Class,
    "createSubject": Subject,
    "createTodo": Todo,
    # endregion
    # region update queries
    "updateStudent": Student,
    "updateTeacher": Teacher,
    "updateTodo": Todo,
    # endregion
}
