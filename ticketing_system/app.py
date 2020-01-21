from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ticketing_system.flask_settings import DevConfig


db = SQLAlchemy()


from ticketing_system.rest import user, ticket, reply
from ticketing_system.repository.postgres_repo.models import User, Ticket, Reply


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(ticket.blueprint)
    app.register_blueprint(reply.blueprint)
    db.init_app(app)
    db.create_all(app=app)
    return app
