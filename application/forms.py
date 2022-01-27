from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

class ContactForm(FlaskForm):
    '''
    Contact form for the contact me page.
    '''
    name = StringField("Name", validators=[InputRequired(), Length(max=40)])
    email = StringField("Email", validators=[InputRequired(), Length(max=50)])
    phone = StringField("Phone No.", validators=[Length(max=11, message="Please enter a valid phone number.")])
    message = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Send Message")