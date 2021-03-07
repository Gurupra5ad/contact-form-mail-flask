from flask import Flask, request, render_template, redirect

app = Flask('__name__')

@app.route("/", methods = ['POST'])
def index():
    return render_template('index.html')

if '__main__' == '__name__':
    app.run()