from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # admin, officer, borrower

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    borrower = db.relationship('User', backref='loans')
    principal_amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    duration_years = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_total_repayment(self):
        total_interest = (self.principal_amount * self.interest_rate * self.duration_years) / 100
        return self.principal_amount + total_interest

    def make_payment(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance = 0

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)
    loan = db.relationship('Loan', backref='transactions')
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
