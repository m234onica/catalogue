from flask import Blueprint, render_template, jsonify, request, g, redirect, flash, url_for
from src.db import init_db, db_session
from src.models import Catalogs

api = Blueprint('api', __name__)
init_db()
