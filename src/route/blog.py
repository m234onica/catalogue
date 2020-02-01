from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for
from uuid import uuid1

from src.db import init_db, db_session
from src.models import Catalogs, Comments, Tags

blog = Blueprint('blog', __name__)
init_db()

@blog.context_processor
def utility_processor():
  def setuuid(static):
    return static + "?v=" + g.uuid
  return {"setuuid": setuuid}


@blog.before_request
def before_req():
  g.uuid = str(uuid1())


@blog.route('/home', methods=['Get'])
def index():
  catalogs = db_session.query(Catalogs).all()
  result = []
  for catalog in catalogs:
    content = catalog.introduction
    content = content.replace('\n', '<br>')
    data = {
      "id": catalog.id,
      "fullname": catalog.fullname,
      'author': catalog.author,
      "book": catalog.book,
      "intro": content
    }
    result.append(data)
  return render_template('home.html', result=result)
