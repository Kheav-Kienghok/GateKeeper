from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='pic.jpg')
    email = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"



@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")

@app.route('')
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created! Username: {form.username.data}!", "success")
        return redirect(url_for('home'))
    
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)