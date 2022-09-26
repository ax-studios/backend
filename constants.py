from api.models import Student, Class, Teacher, Subject

QUERY_NAME_TO_OBJECT = {
    "getStudents": Student,
    "getClasses": Class,
    "getTeachers": Teacher,
    "getSubjects": Subject,
}
