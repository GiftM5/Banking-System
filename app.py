from flask import Flask, render_template, request, url_for, redirect, session
from database import db, User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking_system.db'


db.init_app(app)


app.secret_key = "bngngjewdfwij@#$%^&*"

@app.before_first_request
def create_tables():
    
    db.create_all()

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user'] = username
            print("Login Successful.")
            return redirect(url_for('homepage'))
        else:
            print("Username or password incorrect")
            return render_template("login.html")
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        user = User.query.filter_by(username=username).first()
        if user:
            print("Username already exists.")
            return render_template("register.html")
        else:
            password = request.form["password"]
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            print("Account created.")
            return redirect(url_for('homepage'))
    
    return render_template("register.html")

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/update")
def update():
    return render_template("UpdateAccount.html")

@app.route("/withdraw")
def withdraw():
    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)
