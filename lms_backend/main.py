from app import app, db
from flask.cli import FlaskGroup

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    print("Database created!")

    # populate_db()
    print("Database populated with sample data!")


if __name__ == "__main__":
    cli()
