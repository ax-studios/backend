from app import app, db, logger
from flask.cli import FlaskGroup

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    with app.app_context():
        db.create_all()
        logger.error("Database created")
    logger.error("Database populated with sample data!")


if __name__ == "__main__":
    cli()
