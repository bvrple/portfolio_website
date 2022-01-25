from application import db

class Messages(db.Model):
    '''
    Model used to save contact information from the contact form in a MySQL database.
    '''
    id = db.Column(db.Integer, primary_key=True, nullable=False) # User ID
    name = db.Column(db.VARCHAR(50))
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    phone = db.Column(db.Integer)
    message = db.Column(db.VARCHAR(255))