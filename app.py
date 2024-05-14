
from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import re



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/courses')
def courses():
    return render_template('courses.html', title='Курсы')

@app.route('/news')
def news():
    return render_template('news.html', title='Новости')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not email or not re.match(r"[^@]+@[^@]+.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400
    if not name:
        return jsonify({"error": "Name is required"}), 400
    if not message:
        return jsonify({"error": "Message is required"}), 400

    data = f'Name: {name}\nEmail: {email}\nMessage: {message}'

    try:
        file_path = os.path.join(app.root_path, 'userdata.txt')
        with open(file_path, 'a') as file:
            file.write(data + '\n')
    except Exception as e:
        return jsonify({"error": "Unable to save data"}), 500

    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
