from datetime import datetime
from ticketing_system.app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(50))
    user_type = db.Column(db.String(10))

    def __repr__(self):
        return self.email


class TimestampMixin:
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


class Ticket(TimestampMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(250), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    message = db.Column(db.String(5000), nullable=False)
    code = db.Column(db.String(5), unique=True, nullable=False)
    closed = db.Column(db.Boolean, default=False)
    user = db.relationship('User', backref=db.backref('tickets', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '{}-{}'.format(self.subject, self.code)


class Reply(TimestampMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ticket = db.relationship('Ticket', backref=db.backref('tickets', lazy=True))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    message = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return self.ticket
