from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash





class RolePermissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __table_args__ = {'extend_existing': True}
    role = db.Column(db.String(20), nullable=True)  # Role-based permissions
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # User-specific permissions
    permission = db.Column(db.String(50), nullable=False)

class RolePermissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __table_args__ = {'extend_existing': True}
    role = db.Column(db.String(20), nullable=True)
    permission = db.Column(db.String(50), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='Pracownik', nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))   # "YYYY-MM-DD"
    gotowka = db.Column(db.Float, default=0.0)
    przelew = db.Column(db.Float, default=0.0)
    zaplacono = db.Column(db.Float, default=0.0)
    delivery = db.Column(db.Float, default=0.0)
    other = db.Column(db.Float, default=0.0)


class CostCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Cost(db.Model):
    payment_method = db.Column(db.String(20), nullable=False, default='Gotówka')
    __tablename__ = 'costs'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))   # "YYYY-MM-DD"
    category = db.Column(db.String(50))
    description = db.Column(db.String(200))
    amount = db.Column(db.Float, default=0.0)

from flask_sqlalchemy import SQLAlchemy



class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    location = db.Column(db.String(20), nullable=False)  # 'inside' lub 'outside'
    min_seats = db.Column(db.Integer, nullable=False)
    max_seats = db.Column(db.Integer, nullable=False)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # YYYY-MM-DD
    time = db.Column(db.String(5), nullable=False)  # HH:MM
    duration = db.Column(db.Integer, nullable=False)  # 75, 120, 180 minut
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=True)
    status = db.Column(db.String(20), default='Pending')  # 'Pending', 'Confirmed', 'Cancelled'

    table = db.relationship('Table', backref='reservations')

class OpeningHours(db.Model):
    __tablename__ = 'opening_hours'
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False)  # Monday-Sunday
    open_time = db.Column(db.String(5), nullable=False)  # HH:MM
    close_time = db.Column(db.String(5), nullable=False)  # HH:MM
