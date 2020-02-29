from flask import Blueprint, request, flash, abort, redirect, render_template, url_for
from flask_login import LoginManager, login_user, current_user

from src import login_manager, bcrypt
from src.models import User
from src.login.form import LoginForm
from src.db import init_db, db_session

init_db()


@login_manager.user_loader
def user_loader(id):
    user = db_session.query(User).get(id)
    return user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.home'))
    
    form = LoginForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = db_session.query(User).filter_by(username=username).first()
        print("user.password:", user.password)
        print("password:", password)
        if user:
            login_user(user)

            next = request.args.get('next')
            return redirect(next) if next else redirect(url_for('blog.home'))

        else:
            flash('Logged in successful.')
    return render_template('login.html', form=form)
    
    return render_template('login.html', form=form)
