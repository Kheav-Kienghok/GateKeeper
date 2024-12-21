from flask import Flask, render_template, url_for, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Home page route
@app.route("/", methods=['GET', 'POST'])
def home_page():
    message = None  

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'register':  # Handle Registration
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            # Validate and register user
            if User.query.filter_by(email=email).first():
                message = 'Email is already registered.'
            elif User.query.filter_by(username=username).first():
                message = 'Username is already taken.'
            else:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                user = User(username=username, email=email, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('home_page'))

        elif action == 'login':
            email = request.form.get('email')
            password = request.form.get('password')

            # Authenticate user
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
            # if user and user.password == password:
                message = f'Welcome back, {user.username}!'
                session['user_id'] = user.id
                return redirect(url_for('login_page'))
            else:
                message = 'Login unsuccessful. Please check your email and password.'

    return render_template('index.html', message=message)

# Helper function to check login status
def is_logged_in():
    return 'user_id' in session

@app.route("/home")
def login_page():
    if not is_logged_in():  # Check if the user is logged in
        return redirect(url_for('home_page'))
    return render_template('logout.html')

# Logout route
@app.route("/logout", methods=["POST"])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    message = "You have been logged out."
    return redirect(url_for('home_page'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure the database and tables exist
    app.run(debug=True)