from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for
from flask_login import login_required, current_user

from src.db import init_db, db_session
from src.models import Catalogs, Comments, Tags, Users

blog = Blueprint('blog', __name__)
init_db()

@blog.route('/')
@blog.route('/home', methods=['Get'])
@login_required
def home():
  catalogs = db_session.query(Catalogs).all()
  result = []
  for catalog in catalogs:
    content = catalog.introduction
    content = content.replace('\n', '<br>')
    data = {
      "id": catalog.id,
      "fullname": catalog.username,
      'author': catalog.author,
      "book": catalog.book,
      "intro": content
    }
    result.append(data)
  return render_template('home.html', result=result)

@blog.route('/card', methods=['GET'])
def card():
  return render_template('card.html')

@blog.route('/profile', methods=['GET'])
@login_required
def profile_page():
    
    return render_template('profile.html')
