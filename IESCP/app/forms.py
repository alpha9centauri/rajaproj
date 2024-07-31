from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CampaignForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    budget = FloatField('Budget', validators=[DataRequired()])
    visibility = SelectField('Visibility', choices=[('public', 'Public'), ('private', 'Private')], validators=[DataRequired()])
    goals = TextAreaField('Goals', validators=[DataRequired()])
    submit = SubmitField('Create/Update Campaign')

class AdRequestForm(FlaskForm):
    campaign_id = SelectField('Campaign', coerce=int, validators=[DataRequired()])
    influencer_id = SelectField('Influencer', coerce=int, validators=[DataRequired()])
    messages = TextAreaField('Messages')
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    payment_amount = FloatField('Payment Amount', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], validators=[DataRequired()])
    submit = SubmitField('Create/Update Ad Request')from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('sponsor', 'Sponsor'), ('influencer', 'Influencer')], validators=[DataRequired()])
    submit = SubmitField('Register')
