from flask import Flask, render_template, request, url_for, redirect, session
from database import db, User

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking_system.db'
app.secret_key = "bngngjewdfwij@#$%^&*"

db.init_app(app)

with app.app_context():
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
            session['user'] = user.username
            session['balance'] = user.balance
            return redirect(url_for('homepage'))
        else:
            return "Invalid login credentials!"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        amount = float(request.form["amount"])
        user = User.query.filter_by(username=session['user']).first()
        user.balance += amount
        db.session.commit()
        session['balance'] = user.balance
        return redirect(url_for('homepage'))
    return render_template("deposit.html")

@app.route("/balance")
def balance():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    return render_template("balance.html", username=user.username, balance=user.balance)

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        amount = float(request.form["amount"])
        user = User.query.filter_by(username=session['user']).first()
        if user.balance >= amount:
            user.balance -= amount
            db.session.commit()
            session['balance'] = user.balance
            return redirect(url_for('homepage'))
        else:
            return "Insufficient balance!"
    return render_template("withdraw.html")


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        new_password = request.form["new_password"]
        user = User.query.filter_by(username=session['user']).first()
        user.password = new_password
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("update_account.html")


@app.route("/delete_account", methods=["POST"])
def delete_account():
    user = User.query.filter_by(username=session['user']).first()
    db.session.delete(user)
    db.session.commit()
    session.pop('user', None)
    session.pop('balance', None)
    return redirect(url_for('homepage'))

@app.route("/logout")
def logout():
    session.pop('user', None)
    session.pop('balance', None)
    return redirect(url_for('homepage'))

if __name__ == "__main__":
    app.run(debug=True)
