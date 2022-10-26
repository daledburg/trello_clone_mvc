from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.card import Card
from models.user import User


db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables dropped')

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Cleese',
            email='someone@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    cards = [
        Card(
            title = 'Start the project',
            description = ' Stage 1 - Creating the database',
            status = 'To do',
            priority = 'High',
            date = date.today(),
            user_id = users[0].id
        ),
        Card(
            title = 'SQLAlchemy',
            description = 'Stage 2 - Integrate ORM',
            status = 'Ongoing',
            priority = 'High',
            date = date.today(),
            user_id = users[0].id
        ),
        Card(
            title = 'ORM Queries',
            description = 'Stage 3 - Implement several queries',
            status = 'Ongoing',
            priority = 'Medium',
            date = date.today(),
            user_id = users[1].id
        ),
        Card(
            title = 'Marshmallow',
            description = 'Stage 4 - Implement Marshmallow to jsonify models',
            status = 'Ongoing',
            priority = 'Medium',
            date = date.today(),
            user_id = users[1].id
        )
    ]

    db.session.add_all(cards)
    db.session.commit()
    print('Tables seeded')