import uuid
import random
from ticketing_system.app import db, create_app
from ticketing_system.repository.postgres_repo.models import User, Ticket


app = create_app()
app.app_context().push()

db.create_all(app=app)

user1 = User(token=uuid.uuid4().hex, email='abfcd@gmail.com', name='John', user_type='customer')
user2 = User(token=uuid.uuid4().hex, email='xfyz@gmail.com', name='jane', user_type='customer')
user3 = User(token=uuid.uuid4().hex, email='deff@gmail.com', name='Mike', user_type='staff')

users = [user1, user2, user3]

for i in users:
    db.session.add(i)

db.session.commit()


for i in range(1, 20):
    ticket = Ticket(
        user=random.choice([user1, user2]),
        subject='SUBJECT {}'.format(i),
        priority=random.choice(['low', 'medium', 'high']),
        department=random.choice(['sale', 'technical', 'security']),
        message='Lorejfjhf...',
        code=uuid.uuid4().hex[:5]
    )
    db.session.add(ticket)

db.session.commit()

