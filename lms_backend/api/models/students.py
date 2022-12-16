import sqlalchemy.dialects.postgresql as psql
from sqlalchemy.orm.attributes import flag_modified

from api.models.users import User
from app import db

from ..models import Class, SubjectTeacher


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(psql.UUID(as_uuid=True), db.ForeignKey("users.id"), primary_key=True)
    enroll_no = db.Column(db.String(10), unique=True, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"))

    class_ = db.relationship("Class", back_populates="students")

    def __init__(self, **kwargs):
        kwargs["enroll_no"] = kwargs["enroll_no"].lower()

        try:
            user = User.query.filter_by(id=kwargs["id"]).first()
            if user is None:
                raise Exception(f"Uset id {kwargs['id']} does not exist")

            if "student" in user.roles:
                raise Exception(f"User {user.username} is already a student")

            flag_modified(user, "roles")
            user.roles.append("student")

        except Exception as e:
            db.session.rollback()
            raise e

        super().__init__(**kwargs)

    def jsonify(self, parents):
        parent_json = User.query.filter_by(id=self.id).first().jsonify(parents)
        parent_json.update(
            {
                "enroll_no": self.enroll_no,
                "class_": self.class_.jsonify(parents + [f"{self.__tablename__}"])
                if "classes" not in parents and self.class_ is not None
                else None,
            }
        )
        return parent_json
