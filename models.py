from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

class Disk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disk_id = db.Column(db.Integer, db.ForeignKey('disk.id'))
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(64), nullable=False)

def init_db():
    db.create_all()
    if not User.query.first():
        user1 = User(username='user1', email='user1@example.com', password_hash=generate_password_hash('password1'))
        user2 = User(username='user2', email='user2@example.com', password_hash=generate_password_hash('password2'))
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        disk1 = Disk(title='Dark Side of the Moon', artist='Pink Floyd', year=1973, owner_id=user1.id)
        disk2 = Disk(title='The Wall', artist='Pink Floyd', year=1979, owner_id=user1.id)
        disk3 = Disk(title='Thriller', artist='Michael Jackson', year=1982, owner_id=user2.id)
        disk4 = Disk(title='Back in Black', artist='AC/DC', year=1980, owner_id=user2.id)
        db.session.add(disk1)
        db.session.add(disk2)
        db.session.add(disk3)
        db.session.add(disk4)
        db.session.commit()
