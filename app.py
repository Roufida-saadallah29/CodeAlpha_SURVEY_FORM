from flask import Flask, render_template, request, Response, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

app = Flask(__name__)

# Connect to the SQLite database
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/')
def index():
    return render_template('page1.html')

@app.route('/page1', methods=['POST'])
def page1():
    name = request.form.get('name')
    email = request.form.get('email')
    course = request.form.get('course')

    if request.method == 'POST' and 'previous' in request.form:
        return render_template('page1.html', name=name, email=email)
    elif request.method == 'POST':
        return render_template('page2.html', name=name, email=email, course=course)

    return redirect('/')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    data = request.form.to_dict()
    print(data)
    # Save the form data to a JSON file
    json_filename = f"{name}_{email}_data.json"
    with open("data/"+json_filename, 'w') as json_file:
        json.dump(data, json_file)

    return "Account created successfully!"
if __name__ == '__main__':
    app.run()