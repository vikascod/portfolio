from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/design')
def design():
    return render_template("design.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form.get('firstname')
        lname = request.form.get('lastname')
        schoolname = request.form.get('schoolname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        collagename = request.form.get('collagename')
        skill = request.form.get('skill')
        about = request.form.get('about')
    return "Uploaded"

if __name__ == '__main__':
    app.run(debug=True)