from flask import Flask, request, render_template, redirect
from flask_mail import Mail, Message

app = Flask('__name__')

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'tedwaitforitmosby05@gmail.com',
    MAIL_PASSWORD = 'iloverobin'
))

mail = Mail(app)


@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message('Test', sender='tedwaitforitmosby05@gmail.com', recipients=['guruprasad2511@gmail.com'])
        msg.body = f'I am {name}, sending u mail from {email}, regarding the issue: {subject} and my message goes here : {message}'
        mail.send(msg)
        print(f'I am {name}, sending u mail from {email}, regarding the issue: {subject} and my message goes here : {message}')
        print('done !')

        
    return render_template('index.html')

if '__main__' == '__name__':
    app.run()