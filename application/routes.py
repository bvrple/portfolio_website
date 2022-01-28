from flask import render_template, request, redirect, url_for
from application import app, db
from application.forms import ContactForm
from application.models import Messages
import pymysql


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    form = ContactForm()
    
    if request.method == 'POST':
        new_message = Messages(name=form.name.data,email=form.email.data, phone=form.phone.data, message=form.message.data)
        db.session.add(new_message)
        db.session.commit()
        return redirect('/thank_you')
    return render_template('contact.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')