from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'start'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = '0ef30302a82342'
app.config['MAIL_PASSWORD'] = '2226e01fbc5541'

mail = Mail(app)
from app import views
