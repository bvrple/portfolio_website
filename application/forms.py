from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired, Length

class ContactForm(FlaskForm):
    '''
    Contact form for the contact me page.
    '''
    name = StringField("Name", validators=[InputRequired(), Length(max=40)])
    email = StringField("Email", validators=[InputRequired(), Length(max=50)])
    phone = StringField("Phone No.", validators=[Length(max=11, message="Please enter a valid phone number.")])
    message = StringField("Message", validators=[InputRequired(), Length(min=11)])
    submit = SubmitField("Send Message")