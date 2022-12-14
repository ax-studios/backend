from api.models import User, Student, Class, Teacher, Subject, Todo

QUERY_NAME_TO_OBJECT = {
    # region get queries
    "getUsers": User,
    "getStudents": Student,
    "getClasses": Class,
    "getTeachers": Teacher,
    "getSubjects": Subject,
    "getTodos": Todo,
    # endregion
    # region create queries
    "createUser": User,
    "createStudent": Student,
    "createTeacher": Teacher,
    "createClass": Class,
    "createSubject": Subject,
    "createTodo": Todo,
    # endregion
    # region update queries
    "updateUser": User,
    "updateStudent": Student,
    "updateTeacher": Teacher,
    "updateTodo": Todo,
    # endregion
}
