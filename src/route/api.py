from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for
from uuid import uuid1
from src.db import init_db, db_session
from src.models import Catalogs

api = Blueprint('api', __name__)
init_db()

@api.context_processor
def utility_processor():
  def setuuid(static):
    return static + "?v=" + g.uuid
  return {"setuuid": setuuid}


@api.before_request
def before_req():
  g.uuid = str(uuid1())

