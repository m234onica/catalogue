from flask import Blueprint, request, flash, abort, redirect, render_template, url_for
from flask_login import LoginManager, login_user, current_user, logout_user

from src import login_manager, bcrypt
from src.models import Users
from src.login.form import LoginForm, RegisterForm
from src.db import init_db, db_session

init_db()


@login_manager.user_loader
def user_loader(id):
    user = db_session.query(Users).get(id)
    return user


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET'])
def register_page():
    form = RegisterForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('blog.home'))
    return render_template('register.html', form=form)


@auth.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        db_session.add(Users(fullname=form.fullname.data, username=form.username.data,
                             email=form.email.data, password=hashed_password))
        db_session.commit()
        flash('Your account has been created! You are now able to log in', 'success')

        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('blog.home'))

    form = LoginForm(request.form)
    return render_template('login.html', form=form)


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db_session.query(Users).filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('blog.home'))

        else:
            flash('Logged in successful.')

    return render_template('login.html', form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('blog.home'))
