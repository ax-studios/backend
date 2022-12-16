import sqlalchemy.dialects.postgresql as psql
from sqlalchemy.orm.attributes import flag_modified

from api.models.users import User
from app import db

from ..models import Class, SubjectTeacher


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(psql.UUID(as_uuid=True), db.ForeignKey("users.id"), primary_key=True)
    employee_id = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, **kwargs):
        try:
            user = User.query.filter_by(id=kwargs["id"]).first()
            if user is None:
                raise Exception(f"Uset id {kwargs['id']} does not exist")

            if "teacher" in user.roles:
                raise Exception(f"User {user.username} is already a teacher")

            flag_modified(user, "roles")
            user.roles.append("teacher")

        except Exception as e:
            db.session.rollback()
            raise e

        super().__init__(**kwargs)

    def class_subject(self, parents=[]):
        x = (
            db.session.query(SubjectTeacher, Class)
            .select_from(SubjectTeacher)
            .join(Class.subject_teacher)
            .filter_by(teacher_id=self.id)
            .all()
        )

        lst = []
        for subject_teacher, class_ in x:

            lst.append(
                {
                    "subject": subject_teacher.subject.jsonify(
                        parents + [self.__tablename__, "classes", "subjects"]
                    ),
                    "class_": class_.jsonify(
                        parents + [self.__tablename__, "classes", "subjects"]
                    ),
                }
            )

        return lst

    def jsonify(self, parents):
        parent_dict = User.query.filter_by(id=self.id).first().jsonify(parents)
        parent_dict.update(
            {
                "employee_id": self.employee_id,
                "class_subject": self.class_subject(parents)
                if "classes" not in parents and "subjects" not in parents
                else None,
            }
        )
        return parent_dict
