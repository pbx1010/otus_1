from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime
from markupsafe import escape

db = SQLAlchemy()

app = Flask(__name__)
app.config.update(
    ENV="development",
    SECRET_KEY="qwertytrewsupersecret",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://username:passwd!@pg:5432/blog",
)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    pr = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    info = []
    try:
        info = Users.query.all()
    except:
        print("Ошибка чтения из БД")

    return render_template("index.html", title="Главная", list=info)


@app.route("/register", methods=("POST", "GET"))
def register():
    if request.method == "POST":

        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                         city=request.form['city'], user_id=u.id)
            print(p)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")
            return redirect(url_for('index'))

    return render_template("register.html", title="Регистрация")


if __name__ == "__main__":
    app.run(port=5000)