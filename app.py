from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
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



if __name__ =="__main__":
    app.run(debug=True)