from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoanForm(FlaskForm):
    principal_amount = FloatField('Principal Amount', validators=[DataRequired()])
    interest_rate = FloatField('Interest Rate (%)', validators=[DataRequired()])
    duration_years = IntegerField('Duration (Years)', validators=[DataRequired()])
    submit = SubmitField('Add Loan')

class RepaymentForm(FlaskForm):
    amount = FloatField('Repayment Amount', validators=[DataRequired()])
    submit = SubmitField('Repay Loan')
