from flask_sqlalchemy import SQLAlchemy

#creating the database
db = SQLAlchemy()


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return self.username
