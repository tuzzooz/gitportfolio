from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seuemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'suasenha'

mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)
