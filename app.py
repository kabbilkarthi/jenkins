from flask import Flask, render_template, request, redirect, url_for
from database import insert_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/handle_choice', methods=['POST'])
def handle_choice():
    choice = request.form.get('choice')
    if choice == 'yes':
        return redirect(url_for('user_details'))
    else:
        return redirect(url_for('bye'))

@app.route('/user_details')
def user_details():
    return render_template('user_details.html')

@app.route('/submit_user_details', methods=['POST'])
def submit_user_details():
    name = request.form.get('name')
    email = request.form.get('email')

    # Save to database
    insert_user(name, email)

    return render_template('result.html', name=name, email=email)

@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
