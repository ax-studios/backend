from api.models import Student, Class, Teacher, Subject

QUERY_NAME_TO_OBJECT = {
    # region get queries
    "getStudents": Student,
    "getClasses": Class,
    "getTeachers": Teacher,
    "getSubjects": Subject,
    # endregion
    # region create queries
    "createStudent": Student,
    "createTeacher": Teacher,
    "createClass": Class,
    "createSubject": Subject,
    # endregion
    # region update queries
    "updateStudent": Student,
    "updateTeacher": Teacher,
    # endregion
}
